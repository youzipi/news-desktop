# -*- coding: utf-8 -*
import sys
import urllib2,urllib,re
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf-8')



def load(url):
    try:
        if('shtml' in url):
            html = urllib.urlopen(url).read()
        else:
            html = urllib2.urlopen(url).read()
        #print html.decode('GBK','ignore').encode("utf-8")
        #print html#.decode('utf-8').encode('gb2312')
        #print body
    except(urllib2.HTTPError):
        return 0
    soup = BeautifulSoup(html,from_encoding='GB18030')
    #print soup
    title = soup.head.title
    #title = soup.title
    #print title
    #print type(title)   #<class 'bs4.element.Tag'>
    #print title.string
    #print type(title.string)   #<class 'bs4.element.NavigableString'>
    title = str(title.string).decode('utf-8')
    #print "title:"+title
    #print type(title)
    t = soup.find_all("p")
    print "t:\n"
    #print t
    #img = t.find_all("img")
    print "img:\n"
    #print img
    text = ""
    dirname = "D:/Desktop/img/"
    filename = ""
    count= 0
    #print type(text)
    for i in t:
        #print "count"
        #print count
        body = str(i.string)
        #print body
        if body == "None":
            if count == 0 and i.find('img'):
                #print i
                src = i.find('img')['src']
                number = src[-10:-4]
                filename = dirname+number+".jpg"
                #print "filename:"
                i.find('img')['src'] = filename #更改路径
                print i
                #print filename
                try:    
                    urllib.urlretrieve(src, filename)
                    count = count+1
                except:     #图片无法下载
                    continue
            text = text+str(i)
        else:
            body = body.decode('utf-8')#.encode('gb2312')
            body = i
            #print "body:"
            #print body
            ##text  = text+body+"\n"
            text  = text+str(i)


    print "count:%d" % count
    #print text
    #print type(text)
    return title, text, filename

    
    
    
#url = "http://www.36kr.com/p/213937.html"
#url = "http://cs.nuist.edu.cn/toArticle.action?id=2336"
#url = "http://news.sina.com.cn/c/2014-05-23/142430211704.shtml"
#url = "http://www.jfdaily.com/shehui/new/201405/t20140523_374092.html"
#url = "http://www.36kr.com/p/214277.html"
#url = "http://news.ts.cn/content/2014-08/02/content_10291681.htm"


#title,body,imgsrc = load(url)
#print imgsrc
#print title
#print body
#print body#.decode('utf-8').encode('gbk')
