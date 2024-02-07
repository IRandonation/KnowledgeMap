import pdfplumber
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer

def extract_text_from_pdf(pdf_path):
    text = ''
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ''
    return text

nltk.download('punkt')
nltk.download('stopwords')

def preprocess_text(text):
    # 分词
    tokens = word_tokenize(text.lower())
    # 去除停用词
    tokens = [word for word in tokens if word not in stopwords.words('chinese')]
    # 词干提取
    stemmer = PorterStemmer()
    tokens = [stemmer.stem(word) for word in tokens]
    tv=TfidfVectorizer()#初始化一个空的tv。
    tv_test=tv.transform(tokens)#测试数据不会充实或者改变tv,但这步充实了tv_test。
    print("所有的词汇如下：")
    print(tv.get_feature_names())
    print("测试数据的向量化表示为：")
    print(tv_test.toarray())
    return ' '.join(tokens)

if __name__ == '__main__':
    pdfPath = "D:\\Project\\知识库\\笔记\\防爆AGV.pdf"
    text = extract_text_from_pdf(pdfPath)
    Token = preprocess_text(text)