# -*- coding: utf_8 -*-  
import time
from get_link import get_url
from scraping import wscraping
import sys

sys.setrecursionlimit(10000)

def roop(url, pos):
    links=get_url(url[pos])
    for link in links:
        if link  not in url:
            url.append(link)
         
        time.sleep(5.0)
    if(pos+1 != len(url)):
        roop(url, pos+1)
    return url
            
  
if __name__=='__main__':
    url_name=input('URLを入力してください>>>')
    url_list=[]
    url_list.append((url_name).rstrip('/'))
    roop(url_list, 0)
    
    