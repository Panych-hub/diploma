# from summa import keywords
# from keybert import KeyBERT
# from yake import KeywordExtractor
from gensim import summarization

def summa_extr(text):
    keywords = (keywords.keywords(text, words=5)).split("\n")
    return(keywords)

def BERT_extr(text):
    kw_extractor = KeyBERT('distilbert-base-nli-mean-tokens')
    keywords = kw_extractor.extract_keywords(text)
    keywords = [x for x, y in keywords]
    return(keywords)

def YAKE_extr(text):
    kw_extractor = KeywordExtractor(lan="en", n=1, top=6)
    keywords = kw_extractor.extract_keywords(text=text)
    keywords = [x for x, y in keywords]
    return(keywords)

def gensim_extr(text):
    keywords = summarization.keywords(text)
    return(keywords)

def kw_extr(text, name_alg = 'BERT'):
    if name_alg == 'TextRank':
        keywords = summa_extr(text)
    elif name_alg == ' BERT':
        keywords = BERT_extr(text)
    elif name_alg == 'TopicRank':
        keywords = YAKE_extr(text)
    elif name_alg == 'gensim':
        keywords = gensim_extr(text)
    return(keywords)