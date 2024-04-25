import base64

import streamlit as st
import pandas as pd
import re
import jieba
from pyecharts import options as opts
from pyecharts.charts import WordCloud
from streamlit_echarts import st_pyecharts

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
# 使用Markdown来自定义标题样式
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
st.markdown("""
### <center>词云图生成</center>

在这里，您可以生成一个基于您上传的CSV文件内容的词云图。这将帮助您可视化文本中的关键词和它们的出现频率。

---

请点击下面的按钮来生成您的词云图。

"""
, unsafe_allow_html=True)

st.markdown("""
<div class="card mb-3">
  <div class="card-body">
    <h5 class="card-title">准备数据</h5>
    <p class="card-text">
      本工具支持对自有的CSV文件进行上传、分析情感，并生成精美的词云图以直观展示文本词汇分布。
    </p>
    <ul>
      <li><strong>上传操作：</strong> 请点击下方按钮，选择您的CSV文件进行上传。</li>
      <li><strong>文件要求：</strong> 文件应包含字段 <code>text</code>，并采用 <code>UTF-8</code> 编码方式。</li>
      <li><strong>示例参考：</strong> 在上传前，您可以参照<a href="https://raw.githubusercontent.com/thunderhit/cnsenti/master/test/cnsenti_example.csv" target="_blank" class="link-secondary">CSV示例</a>调整您的文件结构。</li>
    </ul>
  </div>
</div>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader(label='点击上传CSV文件', type=['csv'])

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
def gen_wordcloud(wordfreqs):
    from pyecharts import options as opts
    from pyecharts.charts import WordCloud
    from streamlit_echarts import st_pyecharts
    b = (
        WordCloud()
        .add(series_name='WordCloud', data_pair=wordfreqs, word_size_range=[6, 66])
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="",
                title_textstyle_opts=opts.TextStyleOpts(font_size=23))
        )
    )
    return st_pyecharts(b)


wc = st.button(label='词云图')
try:
    wordfreqs = wordfreqs_count(uploaded_file=uploaded_file)
except:
    wordfreqs = wordfreqs_count()
if wc == True:
    st.balloons()
    gen_wordcloud(wordfreqs=wordfreqs)
# 当用户上传文件后，显示生成词云图的按钮


