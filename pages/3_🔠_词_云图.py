import streamlit as st
import pandas as pd
import re
import jieba
from pyecharts import options as opts
from pyecharts.charts import WordCloud
from streamlit_echarts import st_pyecharts

st.title("中运博网络情感分析")
st.markdown("""
*这是中文情感分析**中运博 **对应的测试网站，可以提供简单中文文本的情绪及情感计算。*
""")

st.title('准备数据')
uploaded_file = st.file_uploader(label='可以对自有的CSV文件进行上传、分析情感、制作词云图', type=['csv'])
st.markdown("""
**注意: **上传前请参考[**CSV示例**](https://raw.githubusercontent.com/thunderhit/cnsenti/master/test/cnsenti_example.csv)，将数据文件改为字段名为 **text**, 编码方式为 **UTF-8** 的 CSV
    """)


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


st.title('数据分析')
st.write('\n\n\n\n')
wc = st.button(label='词云图')
try:
    wordfreqs = wordfreqs_count(uploaded_file=uploaded_file)
except:
    wordfreqs = wordfreqs_count()
if wc == True:
    st.balloons()
    gen_wordcloud(wordfreqs=wordfreqs)

