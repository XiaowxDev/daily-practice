import math
import string

# ========== 复用之前的工具函数 ==========
def read_file(filename):
    with open(filename, encoding="utf-8") as f:
        return f.read()

def clean_split(text):
    text_lower = text.lower()
    text_clean = ""
    for ch in text_lower:
        if ch not in string.punctuation:
            text_clean += ch
    words = text_clean.split()
    return words

def filter_stopwords(words, stop_set):
    filtered = []
    for word in words:
        if word not in stop_set:
            filtered.append(word)
    return filtered

# ========== TF-IDF新增函数 ==========
def calculate_tf(word_list):
    """计算TF：单词在本文出现次数 / 文档总词数"""
    tf_dict = {}
    total_words = len(word_list)
    for w in word_list:
        tf_dict[w] = word_list.count(w) / total_words
    return tf_dict

def calculate_idf(corpus):
    """
    corpus：全部文档的分词列表组成的大列表
    计算IDF
    """
    idf_dict = {}
    doc_count = len(corpus)
    # 收集所有出现过的单词
    all_words = set()
    for doc in corpus:
        all_words.update(doc)
    # 遍历每个词，统计有多少文档包含这个词
    for word in all_words:
        contain_doc_num = 0
        for doc in corpus:
            if word in doc:
                contain_doc_num += 1
        idf_dict[word] = math.log(doc_count / (contain_doc_num + 1))
    return idf_dict

def calculate_tfidf(tf_dict, idf_dict):
    tfidf_dict = {}
    for word, tf in tf_dict.items():
        tfidf_dict[word] = tf * idf_dict[word]
    return tfidf_dict

def get_top_keywords(tfidf_dict, n=5):
    sorted_items = sorted(tfidf_dict.items(), key=lambda x:x[1], reverse=True)
    return sorted_items[:n]

if __name__ == "__main__":
    stop_words = {"the","a","an","is","are","of","in","on","at","to","and","or","but"}
    # 读取目标文档
    target_text = read_file("article.txt")
    target_words = clean_split(target_text)
    target_words = filter_stopwords(target_words, stop_words)

    # 读取语料库其他文档
    doc1 = filter_stopwords(clean_split(read_file("corpus/corpus_1.txt")), stop_words)
    doc2 = filter_stopwords(clean_split(read_file("corpus/corpus_2.txt")), stop_words)
    doc3 = filter_stopwords(clean_split(read_file("corpus/corpus_3.txt")), stop_words)
    corpus = [target_words, doc1, doc2, doc3]

    # 计算TF、IDF、TF-IDF
    tf = calculate_tf(target_words)
    idf = calculate_idf(corpus)
    tfidf = calculate_tfidf(tf, idf)

    top5 = get_top_keywords(tfidf,5)
    print("TF-IDF Top5关键词：")
    for word, score in top5:
        print(f"{word} : {score:.4f}")