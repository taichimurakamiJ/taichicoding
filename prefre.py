# coding: utf-8
from scraping import wscraping
from morana import morpheme
import csv
from get_link import get_url
from all_link import roop
from collections import Counter
from collections import OrderedDict

def get_frequency(unified_tokens):
    freq=[]
    lines=unified_tokens.split()

    for line in lines:
        words=line.split()

        for word in words:
            word=word.rstrip('.,。©:!?)’”').lstrip('(‛“')
            freq.append(word)
            
    return freq


#===================================
#　プログラムの起点
#===================================
if __name__  == '__main__':
    spam=input('urlを入力してください>>>')
    url=[]
    url.append(spam)
    links=roop(url,0)
    unified_elems = ''
    for link in links:
        elems= wscraping(link)
        for elem in elems:
            unified_elems=unified_elems+elem.getText()+'\n'
            
    
    
    unified_tokens=morpheme(unified_elems)
    
    freq=get_frequency(unified_tokens)
    freq_counter=Counter(freq)
    freqs=dict(freq_counter)

    sfreqs=OrderedDict(sorted(freqs.items(),key=lambda x:-x[1]))
    freq_name=['Word','Number']
    Word=sfreqs.keys()
    Number=sfreqs.values()

sname=input('ファイル名を入力してください>>>')
with open(sname,'a',encoding='UTF-8',newline='') as csvFile:
    writer=csv.writer(csvFile)
    writer.writerow(freq_name)

    for Word,Number in sfreqs.items():
            writer.writerow([Word,Number])
            
csvFile.close()
