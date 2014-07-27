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
#texts = soup.body.find("section", "article").findAll(text=True)
#all_text = "\n".join(texts)
#print all_text.encode('GB18030')

t = soup.body.find_all("p")
i = t[0]
print i
img = i.find('img')
print img['src']

print 