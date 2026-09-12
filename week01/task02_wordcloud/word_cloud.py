import string
from wordcloud import WordCloud  # 导入词云第三方库
import matplotlib.pyplot as plt # 导入绘图库

# 定义词云生成函数：接收词频字典，生成、保存、展示词云图
def generate_wordcloud(counts):
    # 配置词云画布基础参数：图片宽、高、背景色、最大展示单词数
    wc = WordCloud(
        width=1000,
        height=600,
        background_color="white",
        max_words=100
    )

    # 根据词频字典自动生成词云：频次越高、字体越大，无需手动排序
    wc.generate_from_frequencies(counts)

    # 将生成的词云保存为图片，自动存入当前项目文件夹
    wc.to_file("wordcloud.png")

    # 加载词云图片用于窗口展示
    plt.imshow(wc)
    # 关闭坐标轴，界面更整洁
    plt.axis("off")
    # 弹出窗口展示最终词云效果图
    plt.show()


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

######主函数#####
if __name__ == "__main__":
    # 1. 读取本地文本文件
    content = read_file("article.txt")
    # 2. 文本清洗，得到纯单词列表
    word_list = clean_split(content)
    # 3. 统计词频，生成词频字典
    word_counts = count_words(word_list)
    # 4. 传入词频字典，生成并展示词云图
    generate_wordcloud(word_counts)
