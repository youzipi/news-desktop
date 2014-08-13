#coding=utf-8
from PIL import Image


def imgzip(url):
    img = Image.open(url)
    w, h = img.size
    print w,h
    if w > 800:
        width = 600.0
    else:
        width = w
    #print (w/width)
    height = int(h/(w/width))
    width = int(width)
    print height
    
    small_img = img.resize((width,height),Image.ANTIALIAS)
    if small_img.mode != "RGB":  
                small_img = small_img.convert("RGB")
    print "url"
    print url
    small_img.save(url)

#url = "D:/Desktop/77.png"
#imgzip(url)