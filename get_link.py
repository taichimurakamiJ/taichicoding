# -*- coding: utf_8 -*-  
import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin,urlparse
import lxml




def  get_url(url_list):
        global url_set
        url=[]    
        base_url=(url_list)
        res = requests.get(url_list,verify=False)
        try:
                res.raise_for_status()
        except Exception as exc:
                print('問題あり：{}'.format(exc))
        soup = BeautifulSoup(res.content,'lxml')
        links = soup.findAll('a')
        for link in links:
                bacon=str(link.get('href'))
                bacons=str(urljoin(base_url,bacon).replace('None',''))
                targets=str(base_url).replace('index.html', '').replace('index.htm','').replace('index.php','').rstrip('/')
                target=re.match(targets, bacons)
                if target == None:
                        pass
                else:
                        spams=str(bacons.replace('index.html', '').replace('index.htm','').split('#')[0])
                        url.append(spams)

                        url_set=list(dict.fromkeys(url))
        return url_set
                

    

if __name__  == '__main__':
    url_list=input('urlを入力してください>>>')
    get_url(url_list)