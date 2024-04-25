import base64

import streamlit as st

def main_bg(main_bg):
    main_bg_ext = "png"
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
            background-size: cover
        }}
        .welcome-box {{
            background-color: grey;
            padding: 15px;
            border-radius: 5px;
            text-align: center;
            margin-bottom: 20px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }}
        .info-box {{
        background-color: grey; /* 更改此处以设置文本框的背景颜色 */
        padding: 10px 20px;
        border-radius: 5px;
        margin-bottom: 20px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }}
        .grayed-text {{ /* 定义灰色文本样式 */
        color: white;
        font-style: italic;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# 调用背景图片设置函数
main_bg('./img/img.png')

# 包裹在 welcome-box 类中的文本
st.markdown(
    f"""
    <div class="welcome-box">
    <h1>仅供学习参考</h1>
    <ul>
        <li><a href="https://huggingface.co/hfl/chinese-roberta-wwm-ext/tree/main">情感分析</a></li>
        <li><a href="https://canalmuseum.net/">中运博</a></li>
        <li><a href="https://canalmuseum.net/">dayunhe</a></li>
    </ul>
    <p>目前处于测试阶段</p>
    </div>
    """,
    unsafe_allow_html=True
)
