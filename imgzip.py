#coding=utf-8
from PIL import Image
def imgzip(url):
     
    img = Image.open(url)
    w, h = img.size
    #print w,h
    if w > 800:
        width = 600
    #width = w/10
    height = h/(w/width)
    small_img = img.resize((width,height),Image.ANTIALIAS)
    small_img.save(url)
