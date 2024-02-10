from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import jieba

def jieba_tokenizer(text):
    return jieba.lcut(text)

def PreProcess(train,tv):
    # 初始化TfidfVectorizer并用训练数据进行拟合
    tv_fit = tv.fit_transform(train)
    print("fit后，所有的词汇如下：")
    print(tv.get_feature_names_out())
    print("fit后，训练数据的向量化表示为：")
    print(tv_fit.toarray())
    # 测试数据
    return tv_fit

def process_text(tv, text):
    # 使用已经拟合过的TfidfVectorizer对象进行变换
    tv_test = tv.transform(text)
    print("所有的词汇如下：")
    print(tv.get_feature_names_out())
    print("测试数据的向量化表示为：")
    print(tv_test.toarray())
    return tv.get_feature_names_out(), tv_test.toarray()

def calculate_cosine_similarity(tv_fit):
    # 计算特征向量之间的余弦相似度
    cosine_sim_matrix = cosine_similarity(tv_fit)
    
    print("文档间的余弦相似度矩阵：")
    print(cosine_sim_matrix)