import base64

import jieba
import streamlit as st
import pandas as pd
from cnsenti import Emotion, Sentiment
import re

# st.title("中运博网络情感分析")
# st.markdown("""
# *这是中文情感分析**中运博 **对应的测试网站，可以提供简单中文文本的情绪及情感计算。*
# """)
#
# st.title('准备数据')
# uploaded_file = st.file_uploader(label='可以对自有的CSV文件进行上传、分析情感、制作词云图', type=['csv'])
# st.markdown("""
# **注意: **上传前请参考[**CSV示例**](https://raw.githubusercontent.com/thunderhit/cnsenti/master/test/cnsenti_example.csv)，将数据文件改为字段名为 **text**, 编码方式为 **UTF-8** 的 CSV
#     """)


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

# 设置页面标题
st.markdown("""
## <center>中运博网络情感分析</center>

一款针对中运博评价文本的情感及情绪分析工具。

---

"""
, unsafe_allow_html=True)


# 页面描述
st.markdown("""
本工具可以对中文文本进行情感和情绪分析，并生成词频统计与可视化结果。
请按照以下步骤操作：
1. 上传您的CSV文件。
2. 点击“情感计算”以获取结果。
3. 上传前请参考[**CSV示例**](https://raw.githubusercontent.com/thunderhit/cnsenti/master/test/cnsenti_example.csv)
""")

# 文件上传区域
st.subheader("上传CSV文件")
uploaded_file = st.file_uploader("请上传包含文本数据的CSV文件", type=['csv'])
st.caption("注意：请确保CSV文件中的文本字段名为 'text'，并且使用UTF-8编码。")


@st.cache_data
def wordfreqs_count(uploaded_file='cnsenti_example.csv'):
    df = pd.read_csv(uploaded_file)
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)
    text = ''.join(re.findall('[\u4e00-\u9fa5]+', ''.join(df['text'])))
    wordfreqs = dict()
    # for idx, text in enumerate(df['text']):
    words = jieba.lcut(text)
    wordset = set(words)
    for word in wordset:
        wordfreqs.setdefault(word, 0)
        wordfreqs[word] = wordfreqs[word] + words.count(word)
    res = [(k, v) for k, v in wordfreqs.items() if v > 1 and len(k) > 1]
    return res
@st.cache_data
def measure(uploaded_file='cnsenti_example.csv'):
    df = pd.read_csv(uploaded_file)
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)
    sentiment = Sentiment()
    emotion = Emotion()
    sensentiment_res = df['text'].apply(sentiment.sentiment_count).apply(pd.Series)
    emotion_res = df['text'].apply(emotion.emotion_count).apply(pd.Series)
    sentiment_result = pd.concat([df, sensentiment_res], axis=1)
    emotion_result = pd.concat([df, emotion_res], axis=1)
    return sentiment_result, emotion_result


senti = st.button(label='情感计算')
try:
    sentiment_result, emotion_result = measure(uploaded_file=uploaded_file)
except ValueError as e:
    sentiment_result, emotion_result = measure()
if senti == True:
    st.balloons()
    st.markdown('**Sentiment Result**')
    st.write(sentiment_result)
    st.markdown('**Emoion Result**')
    st.write(emotion_result)


