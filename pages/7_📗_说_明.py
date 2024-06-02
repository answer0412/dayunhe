import base64
import streamlit as st


def main_bg(main_bg_path):
    with open(main_bg_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url(data:image/png;base64,{encoded_string});
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        .welcome-container {{
            position: relative;
            height: 100vh;
        }}
        .welcome-box {{
            background-color: rgba(0, 0, 0, 0.6); /* Slightly more transparent for better readability */
            padding: 40px;
            border-radius: 20px; /* Increased radius for softer edges */
            text-align: center;
            position: absolute;
            left: 50%;
            top: 40%; /* Lowered slightly for visual balance */
            transform: translate(-50%, -50%);
            width: 80%;
            max-width: 800px; /* Widened for larger screens */
            color: white;
            font-family: 'Roboto', sans-serif; /* Changed to a more modern font */
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2); /* Enhanced shadow for depth */
        }}
        .welcome-box h1 {{
             font-size: 2.5em;
             margin-bottom: 20px;
             font-weight: 300;
             color: rgba(255, 255, 255, 0.9); /* 使用偏白色的不透明度调整 */
        }}
        .welcome-box ul {{
            list-style: none;
            padding: 0;
            display: flex;
            justify-content: center;
            flex-wrap: wrap; /* Allows links to wrap on smaller screens */
            gap: 10px; /* Consistent spacing between items */
            margin-bottom: 20px;
        }}
        .welcome-box li {{
            margin: 5px 20px; /* Reduced margin for tighter list */
        }}
        .welcome-box a {{
            color: white;
            text-decoration: none;
            border-bottom: 2px solid white; /* Thicker underline for emphasis */
            padding-bottom: 4px;
            transition: border-color 0.3s; /* Smooth transition effect */
        }}
        .welcome-box a:hover {{
            border-color: #ccc; /* Light gray on hover for contrast */
        }}
        .welcome-box p {{
            font-size: 1em;
            margin: 0 0 30px;
            line-height: 1.6; /* Improved line spacing */
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
    <div class="welcome-container">
        <div class="welcome-box">
            <h1>仅供学习参考</h1>
            <ul>
                <li><a href="https://huggingface.co/hfl/chinese-roberta-wwm-ext/tree/main">情感分析</a></li>
                <li><a href="https://canalmuseum.net/">中运博</a></li>
                <li><a href="https://canalmuseum.net/">大运河</a></li>
            </ul>
            <p>我们正在不断努力，为您带来更好的体验！</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)