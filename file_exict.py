# -*- coding: utf-8 -*-
import os 
import re
filename = 'E:/百度/00.jpg'
print filename
filename = unicode(filename,"utf8")
print filename
print os.path.exists(filename)
#if os.path.exists(filename):
 #   os.save()
filename = 'E:/百度/00(1).jpg'
number = 2
print filename
#print  filename.replace('.jpg','(%d).jpg' % number)
tail = '(2).jpg'# % number
#print re.sub(r'\(?[^)]*\)?.jpg',tail, 'E:/百度/00(1).jpg')
print re.sub(r'(\(\d\))?.jpg','\(\%d\).jpg' % number, 'E:/百度/00(1).jpg')
#r'\(/d\).jpg' % number