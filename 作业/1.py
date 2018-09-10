# coding=utf-8

import requests
import re
from bs4 import BeautifulSoup

headers = {
"Accept": "*/*",
"Accept-Language": "zh,en;q=0.9,zh-CN;q=0.8",
"Connection": "keep-alive",
"Content-Type": "application/x-www-form-urlencoded",
'Cookie': '_xmLog=xm_1535095534089_jl7o8utltcbuce; trackType=H5; x_xmly_traffic=utm_source%3A%26utm_medium%3A%26utm_campaign%3A%26utm_content%3A%26utm_term%3A%26utm_from%3A; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; _ga=GA1.2.354406842.1535098158; _gat=1',
'Host': 'www.ximalaya.com',
'Origin': 'https://www.ximalaya.com',
'Referer': 'http://www.ximalaya.com/youshengshu/wenxue/',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}


# def getInfo(url):


def getBook(url):
    # url = 'https: // www.ximalaya.com / youshengshu / wenxue /'
    response = requests.get(url, headers=headers).text
    soup = BeautifulSoup(response, 'lxml')

    Booklist = soup.select("ul > li > div > a.u0jN.album-title.lg")
    for book in Booklist:
        book1 = book.text
        book2 = book1.split('（')[0]
        print(book1)
        # return book2
def geturl(url):
    response = requests.get(url, headers=headers).text
    soup = BeautifulSoup(response, 'lxml')
    Booklist = soup.select("ul > li > div > a.u0jN.album-title.lg")
    for url1 in Booklist:
        url2 = url1['href']
        bookurl = 'https://www.ximalaya.com/'+url2
        print(bookurl)
        # return bookurl

def getjianjie(url3):
    response = requests.get(url3, headers=headers).text
    print(response)
    soup = BeautifulSoup(response, 'lxml')
    Booklist = soup.select("div.vd4u.detail-wrapper > div.vd4u.album-intro.open > article > p")

    print(Booklist)


if __name__ == '__main__':
    url = 'http://www.ximalaya.com/youshengshu/wenxue/'
    getBook(url)
    geturl(url)
    url3 = geturl(url)
    getjianjie(url3)
