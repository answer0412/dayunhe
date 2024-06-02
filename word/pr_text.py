from collections import Counter
import openpyxl
import pandas as pd
from jieba import posseg
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

jieba.load_userdict(r"C:/Users/lbw/Desktop/chat/dayun/dayunhe/add.txt")#add是自定义添加的词库

# 1. 读取数据进行分析
with open("C:/Users/lbw/Desktop/chat/dayun/dayunhe/123.txt", "rb") as f:
    text_bytes = f.read()

text = text_bytes.decode('utf-8')
# 进行精确分词
words_with_pos = jieba.posseg.cut(text)

# 将分词结果中的单词部分连接成字符串
seg_text = ' '.join(word for word, flag in words_with_pos)
# 2. 基于 TF-IDF算法提取的关键词抽取
keywords = jieba.analyse.extract_tags(seg_text, withWeight=True, topK=10000)

# 创建一个Workbook对象
wb = openpyxl.Workbook()

# 选择默认的工作表
sheet = wb.active

# 设置工作表标题
sheet.title = "关键词分析"

# 设置表头
sheet.append(["关键词", "词频数", "词性", "TF-IDF值"])

# 遍历关键词列表
for word, weight in keywords:
    # 使用结巴分词的词性标注功能获取词性
    words = pseg.cut(word)
    for w, flag in words:
        # 计算词频数，使用jieba的词频统计
        count = text.count(w)
        # 将英文词性转换为中文词性
        flag_cn = flag_en2cn.get(flag, '未知')
        # 将关键词、词频数、词性和权值添加到工作表中
        sheet.append([w, count, flag_cn, weight])

# 保存工作簿到xlsx文件
wb.save("keywords_analysis1.xlsx")
print("关键词分析结果已保存到keywords_analysis.xlsx文件中。")