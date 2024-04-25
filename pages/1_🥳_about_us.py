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
main_bg('./img/back.png')
st.sidebar.image('./img/ico0.png')
# 页面标题美化
st.title("【🌟中国大运河博物馆游客评价数据分析项目🌟】")

# 一、数据采集与清洗
with st.expander("🎈 1. 数据采集与清洗"):
    st.markdown("""
    👩‍💻 我们灵活运用开源的 **Scrapy** 框架，特制并部署了一套面向各大主流旅游网站及社交媒体平台的网络爬虫系统，专程搜集有关扬州中国大运河博物馆的游客评价数据。通过集成 **Scrapy-Redis** 技术，我们实现了高效的分布式爬取战略，极大地增强了数据收集的效率与稳定性。

    🧹 获取初始数据之后，我们倚仗强大的数据清洗工具 **Pandas** 对数据进行了精细打磨。这包括但不限于消除重复项、填充或剔除缺失值，并对文本内容执行了标准化预处理步骤，例如清除特殊符号、过滤掉无意义的停用词等，力求确保后续分析的精度和可信度。
    """)

# 二、文本特征提取与情感分析
with st.expander("🕵️‍♂️ 2. 文本特征提取与情感分析"):
    st.markdown("""
    💻 我们的技能树涵盖了 **PyTorch** 深度学习架构和 **Hugging Face Transformers** 库。我们借助其中预训练的中文 **BERT** 模型，深掘游客评价文本中的深层语义特征，并在此基础之上建立了精准的情感分析模型，能准确定位每条评价所蕴含的情感倾向（积极、消极还是中立）。
    """)

# 三、关键词提取与主题分析
with st.expander("🔍 3. 关键词提取与主题分析"):
    st.markdown("""
    📊 结合法则悠久的 **TF-IDF** 算法以及尖端的基于 **BERT** 的关键词抽取技术，我们从浩瀚的游客评价海洋中捞取出高频率关键词和热点主题。同时，我们运用 **LDA** 或 **BERTopic** 等主题建模方法，抽丝剥茧，揭开隐藏在评价背后的潜在话题以及游客们最关注的核心议题。
    """)

# 四、可视化与数据展示
with st.expander("🎨 4. 可视化与数据展示"):
    st.markdown("""
    📈 为了生动形象地展示分析成果，我们巧妙应用 **Python** 中的 **Matplotlib**、**Seaborn** 以及 **Plotly** 等可视化库，绘制出丰富多彩的数据图表和热度图。更为精彩的是，我们借助 **Dash**/**Streamlit** 互动式数据可视化框架，匠心打造了一款既简单易用又极具观赏性的应用程序，赋予用户一个亲切友好的界面，让他们能够轻松自如地探索和操控各项分析结果。

    """)

with st.expander("💫 5. 项目团队成员"):
    st.markdown("""

      --- 
      - 🌟 **负责人**：李博文
      - 👥 **组员**：柴子豪、刘延博、邓浩翔
      """)