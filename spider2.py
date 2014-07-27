# -*- coding: utf-8 -*
import sys
import urllib2,urllib,re
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf-8')


url = "http://www.36kr.com/p/213937.html"
#url = "<p><img src=\"http://a.36krcnd.com/photo/2014/0b4fc0244b111a9e063935eefff63474.png\" alt=\"\"></p>"
html = urllib2.urlopen(url).read()
soup = BeautifulSoup(html,from_encoding='GB18030')
#print soup
#print "title:"+title
#print type(title)
t = soup.body.find_all("p")
print "t:\n"
#print t
#img = t.find_all("img")
print "img:\n"
#print img
count = 0
text = ""
#print type(text)
dirname = "D:/Desktop/img/"
for i in t:
        #print i
        if i.find('img'):
            print i
            src = i.find('img')['src']
            print src
            filename = dirname+str(count)+".png"
            print filename
            try:    
                urllib.urlretrieve(src, filename)
                count = count+1
            except:     #图片无法下载
                continue
        #print type(i)
        #if i.img
        #print i['img']
        body = "\n"
        ###text  = text+body
        text = text+str(i)
        