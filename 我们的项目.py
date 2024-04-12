import base64

import streamlit as st

# 设置页面配置
st.set_page_config(
    page_title="中运博文本分析器在线版",
    page_icon="👋",  # 使用手势图标作为页面标签图标
)
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
main_bg('./img/img.png')
# 设置背景图片及样式


# 将欢迎标题放入一个具有特定样式的文本框中
st.markdown(
    f"""
    <div class="welcome-box">
    <h1>欢迎使用 **中运博文本分析器**! 👋</h1>
    </div>
    """,
    unsafe_allow_html=True
)

st.sidebar.success("请在上方侧边栏选择一个操作。")

st.markdown(
    """
    <div class="info-box">
    中运博文本分析器 是一款专注于解析旅游评价文本价值的专业工具。
    **👈 别忘了从侧边栏选取一个功能模块**，来体验它的强大之处！

    <br/>

    ### 想要深入了解？

    - 访问 [大运河博物馆官网](https://canalmuseum.net/) 获取更多官方信息
    - 阅读详细的 [使用文档](https://docs.streamlit.io) 学习如何使用本工具
    - 在 [社区讨论区](https://discuss.streamlit.io) 发表疑问，交流心得
    
    
    
     <br/>

    ### 这里有一张可爱的照片跟您打招呼 😊

    </div>
    </div>

   
    """,
    unsafe_allow_html=True
)

# 注意：同样请注意确认背景图片URL的有效性以正确展示背景图片。

# 以下为示例代码，假设接下来会根据侧边栏的选择展示具体功能...