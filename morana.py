from janome.tokenizer import Tokenizer


def morpheme(string):
    t = Tokenizer(r'dic.csv',udic_type='simpledic',udic_enc='utf-8')
    tokens=t.tokenize(string)
    unified_tokens=''
    for token in tokens:
       unified_tokens=unified_tokens+token.surface+'\n'
    return unified_tokens
#===================================
#　プログラムの起点
#===================================

if __name__  == '__main__':
    file = open('scrapingfile.py', 'r', encoding='UTF-8')
    text = file.read()
    unified_tokens = morpheme(text)
    print(unified_tokens)
