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
    span = soup.find_all("span")
    print "t:\n"
    #print t
    #img = t.find_all("img")
    print "img:\n"
    #print img
    text = ""
    #dirname = "E:/百度/"
    #dirname2 = "E:\\\\百度\\\\"
    dirname = "D:/自装软件/自装软件/安卓/apache-tomcat-7.0.47/webapps/WebRoot/Image/"
    #pa_url = "http://localhost:8080/WebRoot/Image/"
    dirname=unicode(dirname,"utf8")#.encode("utf-8")
    filename = ""
    name = ""
    count= 0
    #print type(text)
    for i in t:
        #print "count"
        #print count
        body = str(i.string)
        #print body
        #print body
        if body == "None":
            #print i
            if count == 0 and i.find('img'):
                print "i.find('img')"
                print i.find('img')
                src = i.find('img')['src']
                #number = src[-10:-4]
                name = src[-10:-4]+".jpg"
                filename = dirname+name#下载路径
                #url = pa_url + number+".jpg"    #服务器路径
                #print "filename:"
                
                #i.find('img')['src'] = url 
                #print i
                print filename
                try:    
                    urllib.urlretrieve(src, filename)
                    count = count+1
                    print "count:"
                    print count
                    print filename
                    #filename2 = dirname2+name
                    print "replace"
                    #sprint filename2
                    print i
                    i.find('img')['src'] = filename #更改路径
                    print "update i:"
                    print i
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
                filename = dirname+name#下载路径
                i.find('img')['src'] = filename #更改路径
                print filename
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
            

    print "count:%d" % count
    #print text
    #print type(text)
    #print type(filename)
    return title, text, name,unicode(filename)#,unicode(filename2)

    
    
    
url = "http://news.163.com/14/0806/08/A2V0CIAR00011229.html"
#url = "http://cs.nuist.edu.cn/toArticle.action?id=2336"
#url = "http://news.sina.com.cn/c/2014-05-23/142430211704.shtml"
#url = "http://www.jfdaily.com/shehui/new/201405/t20140523_374092.html"
#url = "http://www.36kr.com/p/214277.html"
#url = "http://china.firefox.ynet.com/3.1/1407/30/9228127.html"


title,body,imgsrc,filename = load(url)
#print imgsrc
#print title
#print body
#print body#.decode('utf-8').encode('gbk')
