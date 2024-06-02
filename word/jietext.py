import jieba
import jieba.posseg as pseg
from collections import defaultdict
import jieba.analyse
import openpyxl
from sklearn.feature_extraction.text import TfidfVectorizer

jieba.load_userdict(r"C:/Users/lbw/Desktop/chat/dayun/dayunhe/output_file.txt")
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


# 储存自定义词典的词汇
custom_words = set()
#output_file.txt是存储指定分类词汇
with open('C:/Users/lbw/Desktop/chat/dayun/dayunhe/output_file.txt', 'r', encoding='utf-8') as f:
    for line in f:
        custom_words.add(line.strip())

# 分词并筛选出自定义词典中的词，同时获取词性和统计次数
with open("C:/Users/lbw/Desktop/chat/dayun/dayunhe/123.txt", "rb") as f:
    text = f.read()
words_and_tags = pseg.cut(text)

custom_word_counts = defaultdict(lambda: {'count': 0, 'tags': set()})
for word,tag in words_and_tags:
    if word in custom_words:
        custom_word_counts[word]['count'] += 1
        custom_word_counts[word]['tags'].add(flag_en2cn.get(tag, tag))  # 使用映射替换词性标签

# 将结果写入Excel文件
filename = 'output.xlsx'
wb = openpyxl.Workbook()
ws = wb.active

headers = ['关键词', '词频数', '词性', '出现频率']
ws.append(headers)

for word, data in custom_word_counts.items():
    count = data['count']
    flags = ', '.join(sorted(data['tags']))  # 以字母顺序排序词性，确保结果一致
    weight = count / 19500 # 假设权值为词频数的倒数，可根据需要调整计算方式
    ws.append([word, count, flags, weight])

wb.save(filename)
print("Results saved to", filename)