import requests, bs4
import lxml



def wscraping(url):
    res=requests.get(url,verify=False)
    try:
        res.raise_for_status()
    except Exception as exc:
        print('問題あり：{}'.format(exc))
    soup=bs4.BeautifulSoup(res.content, 'lxml')
    elems=soup.select('body')
        
    return elems

if __name__  == '__main__':
    url_name=input('urlを入力してください>>>')
    elems=wscraping(url_name)
    for elem in elems:
        print(elem.getText())