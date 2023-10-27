#spy
import requests
from lxml import etree
from urllib.parse import urljoin
import re
import time
class w0rk():

    def mmain(a,dir):
        global c
        b = w0rk.getUrl(a)
        c = w0rk.getTxt(b)
        d = w0rk.save_as_txt(c=c,dir=dir)
        return 1
    def spy(url):
        tmp = requests.get(url=url)
        tmp.encoding='utf-8'
        return tmp.text
    def getUrl(tmp):
        result = []
        s = etree.HTML(tmp)
        se = s.xpath("//li[starts-with(@id,'line')]//a/@href")
        for i in se:
            result.append(urljoin(baseUrl,i))
        return result

    def getTxt(urls):
        results = {'Title':[],
                'Auther':[],
                'From':[],
                'Page':[],}
        for url in urls:
            tmp = w0rk.spy(url)
            s = etree.HTML(tmp)
            results['Title'].append(s.xpath("//h2/text()")[0])
            results['Auther'].append(s.xpath("//div[@class='zz'][1]/text()")[0].split()[0].lstrip('作者：'))
            results['From'].append(s.xpath("//div[@class='zz'][1]/text()")[0].split()[1].lstrip('来源：'))
            results['Page'].append(''.join(s.xpath("//div[@class='v_news_content']/p/text()")))

        return results

    def save_as_txt(c,dir):
        with open(dir,'a',encoding='utf-8') as dir:
            for i in range(len(c['Title'])):
                dir.write("《{}》\n{}-{}\n{}\n\n".format(c['Title'][i],c['Auther'][i],c['From'][i],c['Page'][i]))


print(
    ''''########:::::::'##:'####:'########::'######::
..... ##:::::::: ##:. ##::... ##..::'##... ##:
:::: ##::::::::: ##:: ##::::: ##:::: ##:::..::
::: ##:::::::::: ##:: ##::::: ##:::: ##:::::::
:: ##:::::'##::: ##:: ##::::: ##:::: ##:::::::
: ##:::::: ##::: ##:: ##::::: ##:::: ##::: ##:
 ########:. ######::'####:::: ##::::. ######::
News....:::https://www.zjitc.net/::::.....qizo'''
)
baseUrl = 'https://www.zjitc.net/'
urls = ['https://www.zjitc.net/xwzx/xxxw.htm']
dir = 'ZJITC_News.txt'
urllists=[]

a = w0rk.spy(url=urls[0])
s = etree.HTML(a)
pages = s.xpath("//span[@class='p_next p_fun']/a/@href")
pages = re.search('\d+',pages[0])
print('共有{}页,请输入要爬取多少页:'.format(pages.group()))

try:
    i = int(input())
    times=0
    if i == 1:
        times+=1
        url = urls[0]
        a = w0rk.spy(url=url)
        a = w0rk.mmain(a=a,dir=dir)
    elif i >1:
        while i > 1 :
            num=int(pages.group())-i
            tmpstr='https://www.zjitc.net/xwzx/xxxw/{}.htm'.format(num)
            urls.append(tmpstr)
            i-=1
        for url in urls:
            times += 1
            a = w0rk.spy(url=url)
            a = w0rk.mmain(a=a,dir=dir)
            print('成功爬取{}页'.format(times))

    print('\n成功爬取{}页,大约{}条新闻,都存在\'{}\'里面啦!'.format(times,times*8,dir))
    k=input()
except:
    time.sleep(0.5)
    print('程序出错啦')
