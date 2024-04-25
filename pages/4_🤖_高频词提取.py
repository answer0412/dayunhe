import base64
import time
import openpyxl
import pandas as pd
import streamlit as st
import jieba
import jieba.analyse
import jieba.posseg as pseg
# 创建词性映射表
flag_en2cn = {
    'a': '形容词', 'ad': '副形词', 'ag': '形语素', 'an': '名形词', 'b': '区别词',
    'c': '连词', 'd': '副词', 'df': '不要', 'dg': '副语素',
    'e': '叹词', 'f': '方位词', 'g': '语素', 'h': '前接成分',
    'i': '成语', 'j': '简称略语', 'k': '后接成分', 'l': '习用语',
    'm': '数词', 'mg': '数语素', 'mq': '数量词',
    'n': '名词', 'ng': '名语素', 'nr': '人名', 'nrfg': '古代人名', 'nrt': '音译人名',
    'ns': '地名', 'nt': '机构团体', 'nz': '其他专名',
    'o': '拟声词', 'p': '介词', 'q': '量词',
    'r': '代词', 'rg': '代语素', 'rr': '代词', 'rz': '代词',
    's': '处所词', 't': '时间词', 'tg': '时间语素',
    'u': '助词', 'ud': '得', 'ug': '过', 'uj': '的', 'ul': '了', 'uv': '地', 'uz': '着',
    'v': '动词', 'vd': '副动词', 'vg': '动语素', 'vi': '动词', 'vn': '名动词', 'vq': '动词',
    'x': '非语素字', 'y': '语气词', 'z': '状态词', 'zg': '状态语素','eng':'英文','xn':'其他专名'
}

jieba.load_userdict(r"C:/Users/李博文/Desktop/chat/dayun/dayunhe/add0.txt")
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
def analyze_keywords(text):
    # 进行精确分词
    words_with_pos = pseg.cut(text)
    # 将分词结果中的单词部分连接成字符串
    seg_text = ' '.join(word for word, flag in words_with_pos)
    # 提取关键词和权值
    keywords = jieba.analyse.extract_tags(seg_text, withWeight=True, topK=10000)
    # 创建一个DataFrame来存储关键词分析结果
    data = []
    for word, weight in keywords:
        words = pseg.cut(word)
        for w, flag in words:
            count = text.count(w)
            flag_cn = flag_en2cn.get(flag, '未知')
            data.append([w, count, flag_cn, weight])
    return pd.DataFrame(data, columns=["关键词", "词频数", "词性", "TF-IDF值"])

def main():
    # 设置页面样式
    # st.set_page_config(layout="centered", page_title="关键词分析工具")

    # 提供上传说明
    st.markdown("""
    **上传您的文本文件**

    请上传您想要分析的文本文件。我们将使用 TF-IDF 算法提取关键词，并提供词频数和词性分析。
    """)

    # 读取上传的文本文件
    uploaded_file = st.file_uploader("选择文件", type=["txt"])

    if uploaded_file is not None:
        try:
            # 读取文件内容
            text = uploaded_file.read().decode('utf-8')

            # 使用容器居中展示内容
            with st.container():
                st.markdown("""
                   <style>
                   .centered-table {
                       display: table;
                       margin-left: auto;
                       margin-right: auto;
                   }
                   </style>
                   """, unsafe_allow_html=True)

                # 显示加载进度条
                with st.spinner('正在分析关键词...'):
                    keywords_df = analyze_keywords(text)

                # 展示分析结果
                st.subheader("关键词分析结果")

                st.dataframe(keywords_df, width=2800)

                    # 提供下载按钮
                st.download_button(
                    label="下载为Excel文件",
                    data=keywords_df.to_csv(index=False),
                    file_name="keywords_analysis.csv",
                    mime="text/csv"
                )
        except Exception as e:
            st.error(f"发生错误：{str(e)}\n请检查文件格式或内容是否正确，如有疑问，请联系技术支持。")
    else:
        st.warning("请上传文本文件以进行分析。")

if __name__ == "__main__":
    main()