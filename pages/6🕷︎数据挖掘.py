import base64

import streamlit as st
from streamlit.components.v1 import html
import os
from tempfile import NamedTemporaryFile
from spider.qunaer import fetch_and_store_comments
from spider.xiecheng import scrape_comments as fetch_xiecheng_comments
import pandas as pd



def main_bg(main_bg):
    main_bg_ext = "png"
    with open(main_bg, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url(data:image/{main_bg_ext};base64,{encoded_string});
            background-size: cover;
            background-position: center;
            background-color: #F5F5F5; /* 融入新的背景颜色 */
        }}
        .stButton > button {{
            color: white;
            background-color: #0072B1;
            border-radius: 5px;
        }}
        .tab {{
            border: 1px solid #DDDDDD;
            padding: 10px;
            border-radius: 5px;
            background-color: #FFFFFF;
        }}
        .tab-selected {{
            background-color: #F5F5F5; /* 融入选中标签的背景颜色 */
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
main_bg('./img/back2.png')
def download_excel_file(df):
    """
    将DataFrame保存为临时Excel文件，并返回可供下载的文件名。
    """
    with NamedTemporaryFile(delete=False, suffix=".xlsx") as tmp:
        df.to_excel(tmp.name, index=False)
        return tmp.name

def fetch_and_process_comments(website, start_page, end_page):
    """
    根据选择的网站调用相应的抓取函数。
    """
    if website == "去哪儿网":
        fetch_and_store_comments(start_page, end_page)
        file_path = 'comments.xlsx'  # 假设Qunar的评论存储在此文件
    elif website == "携程":
        comments_df = fetch_xiecheng_comments(start_page, end_page)
        # 假设fetch_xiecheng_comments直接返回一个DataFrame
        file_path = 'ctrip_comments.xlsx'
        comments_df.to_excel(file_path, index=False)
    else:
        raise ValueError("未支持的网站类型")
    return file_path

def main():
    st.title("多平台景点评价抓取工具")

    # 选项卡式导航
    website_options = ["去哪儿网", "携程","大众点评","微博","小红书"]
    selected_website = st.selectbox("选择网站", website_options, index=0, key="website_selector")

    st.write(f"当前选择: {selected_website} 评价抓取")

    # 用户输入
    col1, col2 = st.columns(2)
    with col1:
        start_page = st.number_input("起始页", min_value=1, value=1, step=1)
    with col2:
        end_page = st.number_input("结束页", min_value=start_page, value=start_page + 1, step=1)

    if st.button("开始抓取"):
        with st.spinner("正在抓取数据..."):
            file_path = fetch_and_process_comments(selected_website, start_page, end_page)
            st.success("抓取完成！")



        # 下载链接
        st.markdown("### 下载评论数据")
        temp_file_path = download_excel_file(pd.read_excel(file_path))
        st.download_button(
            label="点击下载评论数据",
            data=open(temp_file_path, "rb").read(),
            file_name=f"{selected_website}_comments.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
        os.unlink(temp_file_path)

if __name__ == "__main__":
    main()



