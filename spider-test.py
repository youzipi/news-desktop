import unittest
from spider import *

class TestSpider(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_load(self):
        url1 = ""
        url2 = "123"
        url3 = "www.123.com"
        url4 = "http://www.tuicool.com/articles/Fruiqyj"
        url5 = "http://news.sina.com.cn/c/2014-05-23/142430211704.shtml"
        url6 = "http://www.jfdaily.com/shehui/new/201405/t20140523_374092.html"
        self.assertRaises(ValueError, load, url1)
        self.assertRaises(ValueError, load, url2)
        self.assertRaises(ValueError, load, url3)
        self.assertTrue(isinstance(load(url4), tuple))
        self.assertTrue(isinstance(load(url5), tuple))
        self.assertTrue(isinstance(load(url6), tuple))

if __name__ == '__main__':
    unittest.main()
