# -*- coding: utf-8 -*-
import re

s = '''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd"><html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:"SimSun"; font-size:14pt; font-weight:400; font-style:normal;"></body></html>'''
p = re.findall(r'<style(\s\S)*?</style>',s)
#print p
t = ''
m = s.replace( 'p, li { white-space: pre-wrap; }\n','')
print m
