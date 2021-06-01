from deepsegment import DeepSegment
from nnsplit import NNSplit
import requests

def deepsegment_(text):    
    segmenter = DeepSegment('en')
    arr_seg = segmenter.segment_long(text)
    text_seg = ''.join([arr_seg[i]+'. ' for i in range(len(arr_seg))])
    return(text_seg)
    
def NNsplit(text):   
    splitter = NNSplit("en")
    split_text_arr = splitter.split([text])
    text_split_all = ''
    t = False
    for i in range(len(split_text_arr[0])):
        text_split_sen = ''.join([split_text_arr[0][i][j].text+' '\
                        for j in range(len(split_text_arr[0][i]))])[:-1]
        if text_split_sen != '': text_split_all += text_split_sen + '. ' 
    return(text_split_all)
    
def punctuator(text1): 
    response = requests.post('http://bark.phon.ioc.ee/punctuator', data=dict(text=text1))
    r_text = response.text
    return r_text.replace(',', '.').replace('?', '.').replace('!', '.').replace(';', '.').replace(':', '.').replace('-', '')
    
def segment(text, method_name='NNsplit'):
    if method_name == 'deepsegment':
        return deepsegment_(text)
    elif method_name == 'NNsplit':
        return NNsplit(text)
    elif method_name == 'punctuator':
        return punctuator(text)