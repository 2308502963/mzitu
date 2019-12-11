# 爬取中国大学排名
import bs4
import requests
from bs4 import BeautifulSoup


def getHTML(url):
    try:
        r=requests.get(url)
        r.raise_for_status()
        r.enconing=r.apparent_enconing
        return r.text
    except:
        return""


def getInfo(list,html):
    soup=BeautifulSoup(html,"html.parser")
    for tr in soup.find('tbody').children:
        tds=soup.find_all('td')
        list.append(u[0],u[1],u[8])



def printinfo(list,num):
    print("{:^10}\t{:^6}\t{:^10}".format("排名","学校名称","总分"))
    for i in range(num):
        u=list[i]
        print("{:^10}\t{:^6}\t{:^10}".format(u[0],u[1],u[2]))

def main():
    uinfo=[]
    url="http://www.gaokaopai.com/paihang-otype-2.html?f=1&ly=bd&city=&cate=&batch_type="
    html=getHTML(url)
    getInfo(uinfo,html)
    printinfo(uinfo,20)
