import string

# 读取本地文本文件函数
def read_file(filename):
    # 以utf-8编码打开文件，避免乱码，with自动关闭文件，更安全
    with open(filename, encoding = "utf-8") as f:
        return f.read()

# 文本清洗、转小写、去标点、切割单词
def clean_split(text):
    # 归一化
    text_lower = text.lower()
    # 去标点
    text_clean = ""
    for ch in text_lower:
        if ch not in string.punctuation:
            text_clean += ch
    # 切割
    words = text_clean.split()
    return words

# 停用词过滤
def filter_stopwords(words, stop_set):
    # 定义空列表，存储过滤后的有效单词
    filtered = []
    # 遍历所有单词，只保留非停用词
    for word in words:
        if word not in stop_set:
            filtered.append(word)
    return filtered

# 词频统计函数
def count_words(words):
    counts = {}
    for w in words:
        # 单词存在则+1，不存在则初始化为0再+1
        counts[w] = counts.get(w,0)+1
    return counts

# 提取TopN高频词并降序排序
def get_top_n(count_dict, n):
    # 按词频数值降序排序
    sorted_items = sorted(count_dict.items(), key=lambda x:x[1], reverse=True)
    # 截取前n个高频词
    return sorted_items[:n]

#####主函数#####
if __name__ == "__main__":
    # 定义英文通用停用词集合（set查询效率O(1)）
    stop_words = {"the","a","an","is","are","of","in","on","at","to","and","or","but","as","that","this"}
    # 1.读取文本
    content = read_file("article.txt")
    # 2.清洗文本、切割单词
    word_list = clean_split(content)
    # 3.过滤停用词，得到有效实词列表
    filtered_words = filter_stopwords(word_list, stop_words)
    # 4.统计精准词频
    word_counts = count_words(filtered_words)
    # 5.获取Top10高频核心词汇
    top_10 = get_top_n(word_counts,10)
    # 6.打印结果
    print("过滤停用词后的Top10高频实词：")
    for word, cnt in top_10:
        print(f"{word}: {cnt}次")
