# 打开并读取包含短语的文件
with open('input_file.txt', 'r', encoding='utf-8') as file:
    content = file.read()

# 将文件内容分割成单独的短语
phrases = content.split('、')

# 将每个短语写入一个新的文件，每个短语占一行
with open('output_file.txt', 'w', encoding='utf-8') as output_file:
    for phrase in phrases:
        # 去掉前后空白（如果有的话），并写入文件
        output_file.write(phrase.strip() + '\n')

print("操作完成，短语已保存到 output_file.txt 中。")
