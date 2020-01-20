# encoding=utf8
import urllib.request
import re

def open_url(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    return html


def save(listurl):
    i = 0
    for url in listurl:
        print(url)
        html = open_url(url)
        with open_url(url, 'wb') as f :
            f.write(html)

        print('保存了第 %d 张图片 '%i)
        i += 1




def findurl(url):
    '<img alt="黄色法拉利跑车局部摄影" src="http://pic1.sc.chinaz.com/Files/pic/pic9/201711/zzpic7855_s.jpg">'
    html = open_url(url)
    with open('html','wb') as f:
        f.write(html)
    html = html.decode()
    pattern = re.compile('src2=(.+) ')
    urllist = re.findall(pattern, html)
    return urllist

if __name__ == '__main__':
    url = 'http://sc.chinaz.com/tag_tupian/PaoChe_2.html'
    urllist = findurl(url)
    save(urllist)