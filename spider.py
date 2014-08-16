# -*- coding: utf-8 -*
import os
import sys
#import time
#import re
import urllib2,urllib,re
from bs4 import BeautifulSoup,SoupStrainer
import chardet
from imgzip import *
import ConfigParser
#import base64

reload(sys)
sys.setdefaultencoding('utf-8')


config = ConfigParser.SafeConfigParser()
config.read("setting.ini")
dirpath = config.get("imgpath","dirpath")
dirpath=unicode(dirpath,"utf8")

#tags = SoupStrainer("head","p","span")
#tags = SoupStrainer("head")#,"p","span")

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
    encoding = chardet.detect(html)['encoding']     #获取网页编码
    #print encoding
    soup = BeautifulSoup(html,"lxml",from_encoding=encoding)
    #soup = BeautifulSoup(htmlfrom_encoding='GB18030')
    #soup = BeautifulSoup(html,from_encoding='utf-8')
    #soup = BeautifulSoup(html)  #同一
    #print soup
    #print "soup -end\n\n"
    #print soup.head
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
    span = soup.find_all("span")
    #print "t:\n"
    #print t
    #print "t-end\n\n\n\n"
    #img = t.find_all("img")
    #print "img:\n"
    #print img
    text = ""
    #dirpath = "E:/百度/"
    #dirname2 = "E:\\\\百度\\\\"
    #dirpath = "D:/自装软件/自装软件/安卓/apache-tomcat-7.0.47/webapps/WebRoot/Image/"
    #pa_url = "http://localhost:8080/WebRoot/Image/"
    #dirpath=unicode(dirpath,"utf8")#.encode("utf-8")
    filename = ""
    name0 = ""
    name = ""
    filepath = []
    #name[0] = ""
    count= 0
    #print type(text)
    for i in t:
        if i.find('p'):
            continue
        #print "count"
        #print count
        body = str(i.string)
        #print body
        #print body
        if body == "None":
            #print i
            #if count == 0 and i.find('img'):
            if i.find('img'):
                print "i.find('img')"
                print i.find('img')
                src = i.find('img')['src']
                name = src[-10:-4]+".jpg"
                if count == 0:
                    name0 = name
                filename = dirpath+name#下载路径
                #url = pa_url + number+".jpg"    #服务器路径
                #print "filename:"
                
                #i.find('img')['src'] = url 
                #print i
                number = 1
                while os.path.isfile(filename):
                    #filename.replace('.jpg','(%d).jpg' % number)
                    #filename = filename.replace('.jpg','%d.jpg' % number)
                    #tail = '(%d).jpg' % number
                    filename = re.sub('(\(\d+\))?.jpg','(%d).jpg' % number, filename)    #匹配.jpg,(1..999)
                    number += 1
                    #print number
                    #print filename
                    #time.sleep(5)
                try:    
                    urllib.urlretrieve(src, filename)
                    filepath += [filename]
                    count = count+1
                    #print "count:"
                    #print count
                    #print filename
                    #filename2 = dirname2+name
                    #print "replace"
                    #sprint filename2
                    #print i
                    i.find('img')['src'] = filename #更改路径
                    #print "update i:"
                    #print i
                    imgzip(filename)      #图片压缩
                except:     #图片无法下载
                    #print type(i)
                    i = "<p></p>"   
                    #print type(i)
                    continue
            else:
                i = "<p></p>"
            text = text+str(i)
        else:
            body = body.decode('utf-8')#.encode('gb2312')
            body = i
            #print "body:"
            #print body
            ##text  = text+body+"\n"
            text  = text+str(i)
    if count == 0:
         for i in span:
            if count == 0 and i.find('img'):
                src = i.find('img')['src']
                name = src[-10:-4]+".jpg"
                filename = dirpath+name#下载路径
                i.find('img')['src'] = filename #更改路径
                #print filename
                try:    
                    urllib.urlretrieve(src, filename)
                    count = count+1
                    i = '<p><img src="%s" alt=\"\"/></p>' % filename
                    text = i+text
                    #print i
                    break
                except:     #图片无法下载
                    i = "<p></p>"   
                    continue
            

    #print "count:%d" % count
    #print text
    #print type(text)
    #print type(filename)
    return title, text, name0,filepath#,unicode(filename)#,unicode(filename2)

    
    
    
#url = "http://news.163.com/14/0816/02/A3O3MTA500014AED.html"
#url = "http://cs.nuist.edu.cn/toArticle.action?id=2336"
#url = "http://news.sina.com.cn/c/2014-05-23/142430211704.shtml"
#url = "http://www.jfdaily.com/shehui/new/201405/t20140523_374092.html"
#url = "http://www.36kr.com/p/214604.html"
#url = "http://ent.firefox.news.cn/14/0813/08/ZONF6UWYVBS2M8HQ.html"


#title,body,imgsrc,filepath = load(url)
#print filepath
#print type(filepath)
#str = base64.b64encode(str(filepath))
#print type(str)
#print title
#print body
#print body#.decode('utf-8').encode('gbk')
