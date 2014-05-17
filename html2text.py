# -*- coding: utf-8 -*-

from HTMLParser import HTMLParser
from re import sub
from sys import stderr
from traceback import print_exc

class _DeHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.__text = []

    def handle_data(self, data):
        text = data.strip()
        if len(text) > 0:
            text = sub('[ \t\r\n]+', ' ', text)
            self.__text.append(text + ' ')

    def handle_starttag(self, tag, attrs):
        if tag == 'p':
            self.__text.append('\n\n')
        elif tag == 'br':
            self.__text.append('\n')

    def handle_startendtag(self, tag, attrs):
        if tag == 'br':
            self.__text.append('\n\n')

    def text(self):
        return ''.join(self.__text).strip()


def dehtml(text):
    try:
        parser = _DeHTMLParser()
        parser.feed(text)
        parser.close()
        return parser.text()
    except:
        print_exc(file=stderr)
        return text
        
def txt2html(txt):
    '''将txt以行为单位加上<li></li>标签'''
    def escape(txt):
        '''将txt文本中的空格、&、<、>、（"）、（'）转化成对应的的字符实体，以方便在html上显示'''
        txt = txt.replace('&','&')
        txt = txt.replace(' ','&#160;')
        txt = txt.replace('<','<')
        txt = txt.replace('>','>')
        txt = txt.replace('"','&#34;')
        txt = txt.replace('\'','&#38;#39;')
        return txt

    txt = escape(txt)
    lines = txt.split('\n')
    for i, line in enumerate(lines):
        lines[i] = '<li>' + line + '</li>'
        #lines[i] = '<p>' + line + '&#60;/p&#62;'
    txt = ''.join(lines)
    return txt

def main():
    text = r'''
        <html>
            <body>
                <b>Project:</b> DeHTML<br>
                <b>Description</b>:<br>
                This small script is intended to allow conversion from HTML markup to 
                plain text.
            </body>
        </html>
    '''

    print(dehtml(text))
    print(txt2html(text))
    



if __name__ == '__main__':
    main()

    
    
    

