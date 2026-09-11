import string
# 第一步 读取文章
def read_file(filename):
    f = open(filename, encoding = "utf-8") # 读取文件
    text = f.read()         # 把 f 里的内容读出来，存进变量 text
    # print(text)           # 验证
    return text
# 第二步 转小写
def clean_split(text):
    text_lower = text.lower() # 将所有单词转成小写，并存进text_lower
    # print(text_lower) # 验证
    # 第三步 去标点
    text_clean = ""
    for ch in text_lower:
        if ch not in string.punctuation:
            text_clean += ch
    # print (text_clean) # 验证
    # 第四步 将单词切分放入列表
    words = text_clean.split() # 切割成单词，返回列表words
    print(len(words))
    return words
# print(words) # 验证
# 第五步 统计单词
def count_words(text):
    counts = {}
    for word in text:
        if word in counts:        # 这个单词已经见过了
            counts[word] += 1
        else:                     # 头一次见
            counts[word] = 1
    return counts
# print(counts) #验证
# counts = {}
# for word in words:
#     counts[word] = counts.get(word, 0) + 1 # 整体注释 Ctrl + /
# 第六步 排序
def top_words(counts):
    top_10 = sorted(counts.items(), key = lambda item : item[1], reverse = True) [:10]
    return top_10
# print(top_10) # 验证
if __name__ == "__main__":
    text = read_file("article.txt")
    words = clean_split(text)
    counts =count_words(words)
    top_10 = top_words(counts)
    print(top_10)