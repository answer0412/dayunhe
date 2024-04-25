import base64
import time
from http import HTTPStatus
import dashscope
import docx
import streamlit as st
import pandas as pd
from dashscope import Generation

# 设置API密钥
dashscope.api_key = "sk-3c11cb7ee814447d8868cbbecd968541"


def generate_report(df):
    # 将DataFrame转换为字符串形式，并取前9000个字符
    df_str = df.to_string()
    first_9000_chars = df_str[:9000]

    # 定义用于生成报告的消息
    messages = [{'role': 'user',
                 'content': f'{first_9000_chars} 根据这个大运河博物馆文本部分的高频词提取的内容，生成定制化报告，要求专业具体详细，对大运河博物馆的旅游形象有具体帮助'}]

    # 调用dashscope API并合并响应
    full_content = ''
    for response in Generation.call(
            Generation.Models.qwen_max,
            messages=messages,
            result_format='message',
            stream=True,
            incremental_output=True
    ):
        if response.status_code == HTTPStatus.OK:
            full_content += response.output.choices[0]['message']['content']
        else:
            print(
                f'Request id: {response.request_id}, Status code: {response.status_code}, error code: {response.code}, error message: {response.message}')

    return full_content


def save_report_to_word(content):
    doc = docx.Document()
    doc.add_paragraph(content)
    doc.save('output.docx')

def main_bg(main_bg):
    main_bg_ext = "png"
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
# 调用背景图片设置函数
main_bg('./img/back.png')
def main():
    # 设置页面样式
    # st.set_page_config(layout="centered", page_title="大运河博物馆定制化报告生成器", initial_sidebar_state="expanded")

    # 提供详细的上传说明
    st.sidebar.image('./img/ico0.png')
    st.markdown("""
    **上传您的Excel文件**

    请上传包含大运河博物馆文本分析数据的Excel文件（.xlsx格式）。我们将使用其中的高频词信息，为您生成一份专业、详尽的大运河博物馆旅游形象定制化报告。

    **注意：** 确保文件内容符合预期，以便程序正确生成报告。
    """)

    # 读取上传的Excel文件
    uploaded_file = st.file_uploader("选择文件", type="xlsx")

    if uploaded_file is not None:
        try:
            df = pd.read_excel(uploaded_file)

            # 显示加载进度条
            with st.progress(0):
                for i in range(100):
                    time.sleep(0.01)
                    st.progress(i + 1)

            report_content = generate_report(df)

            # 显示生成的报告内容
            st.subheader("定制化报告")
            st.text_area("报告内容预览:", value=report_content, height=300)

            # 提供下载按钮
            download_button = st.download_button(
                label="下载为Word文档",
                data=report_content,
                file_name="custom_report.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )

            # 在用户点击下载按钮时，将报告内容保存到本地Word文档
            if download_button:
                save_report_to_word(report_content)

        except Exception as e:
            st.error(f"发生错误：{str(e)}\n请检查文件格式或内容是否正确，如有疑问，请联系技术支持。")
    else:
        st.warning("请上传Excel文件以生成报告。")


main()
