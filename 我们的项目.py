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
            background-size: cover;
            background-position: center;  # 新增：使背景图像居中
        }}
        .welcome-box {{
            background-color: rgba(255, 255, 255, 0.85); /* 调整背景色为白色，轻微透明 */
            padding: 20px 40px; /* 增加内边距，使内容不那么拥挤 */
            border-radius: 10px; /* 调整边角圆滑度 */
            text-align: center;
            margin-bottom: 30px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* 调整阴影效果 */
        }}
        .info-box {{
            background-color: rgba(255, 255, 255, 0.75); /* 调整背景色为白色，透明度降低 */
            padding: 20px; /* 均匀内边距 */
            border-radius: 25px; /* 更大的边角圆弧 */
            margin-bottom: 30px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }}
        .grayed-text {{
            color: rgba(0, 0, 0, 0.6); /* 调整文字颜色为深灰色 */
            font-style: normal; /* 去除斜体，使文字更清晰 */
        }}
        h1, p {{
            color: #333; /* 调整文字颜色为深灰色 */
            font-family: 'Arial', sans-serif; /* 使用 Arial 字体 */
            line-height: 1.6; /* 调整行高，提高可读性 */
        }}
        a {{
            color: #0066cc; /* 超链接颜色 */
            text-decoration: none; /* 去除下划线 */
            transition: color 0.3s; /* 鼠标悬停时颜色变化的过渡效果 */
        }}
        a:hover {{
            color: #004c99; /* 鼠标悬停时的超链接颜色 */
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

main_bg('./img/img.png')  # 确保'./img/img.png'是正确的路径

# 将欢迎标题放入一个具有特定样式的文本框中
st.markdown(
    f"""
    <div class="welcome-box">
    <h1>欢迎使用 *文本分析采集器*!👋</h1>
    <p class="grayed-text">一款专注于解析旅游评价文本价值的专业工具。</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.sidebar.success("请在上方侧边栏选择一个操作。")
st.sidebar.image('./img/ico0.png')

st.markdown(
    """
    <div class="info-box">
        <p>通过我们的工具，您可以深入了解旅游者的真实反馈和体验。</p>
        <p><strong>👈 从侧边栏选取功能模块</strong>，开始分析旅游文本吧！</p>
        <div style="height: 2px; background: black; margin: 1em 0;"></div>
        <h2>想要深入了解我们？</h2>
        <ul>
            <li><a href="https://github.com/answer0412/dayunhe">访问我们的项目官网</a>，获取更多官方信息</li>
            <li><a href="https://docs.streamlit.io">阅读使用文档</a>，学习如何使用本工具</li>
            <li><a href="https://discuss.streamlit.io">加入社区讨论区</a>，发表疑问，交流心得</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True
)
