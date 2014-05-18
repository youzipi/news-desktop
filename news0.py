# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
import sys
import urllib2,urllib,re
from bs4 import BeautifulSoup
from PyQt4 import QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import pyqtSignature, QString
from PyQt4.QtSql import *

from Ui_news0 import Ui_MainWindow
#from html2text import _DeHTMLParser, dehtml, txt2html
#from text2html import *
from spider import *
#from SqlModel import Model


#QTextCodec::setCodecForCStrings(QTextCodec::codecForName("UTF-8"));


cid = 0    #全局变量cid

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)        

    
    @pyqtSignature("")
    def on_okbutton_released(self):
        """
        网址输入
        """
        url = self.ui.urlLine.text()
        print url
        url = str(url)
        print type(url)
        print ("ok_button realeased")
        #print load(url)
        title, body = load(url)
        print "title:"+title
        self.ui.titleedit.setPlainText(title)
        self.ui.bodyedit.setPlainText(body)
        #print type(title)
        #print url
        #print type(url)
        #self.ui.testText.setPlainText(title)

    @pyqtSignature("")
    def on_backbutton_released(self):
        """
        反向编辑
        """
        url = self.ui.testText.toPlainText()
        print type(url)
        self.ui.urlLine.setText(url)

    def showdata(self):
        q = QSqlQuery()
        select = "SELECT * FROM t_news;"
    
    @pyqtSignature("QModelIndex")
    def on_tableView_clicked(self, index):    #表格元素点击
        print ("clicked")
        
        item = QStandardItem()
        print type(item)
        row = index.row()
        column = index.column()
        self.ui.tableView.selectRow(row)
        #print self.ui.tableView.item(row, column).text()
        #print Model.data(Model.index(row, column)).text()
        #print Model.index(row, 0).data().toInt()[0]
        #print self.ui.tableView.selectionModel().model().index(row, 0).data().toInt()[0]
        nid = self.ui.tableView.model().index(row, 0).data().toInt()[0]
        print nid
        self.search(nid)

    def search(self, nid):
        q = QSqlQuery()
        nid = bytes(nid)
        selection = "SELECT cid,title,digest,body FROM t_news WHERE nid = "+nid+";"
        print selection
        q.exec_(selection)
        print type(q)
        if q.first():
            cid = q.value(0).toInt()
            title = q.value(1).toString()
            digest = q.value(2).toString()
            body = q.value(3).toString()
            body.replace('<p>', '')
            body.replace('</p>', '')
        print type(title)

        self.ui.titleedit.setPlainText(title)
        self.ui.digestedit.setPlainText(digest)
        #self.ui.bodyedit.setPlainText(body)
        #self.ui.bodyedit.setPlainText(body)
        #body = unicode(QString(body).toUtf8(), 'utf-8', 'ignore')
        #print type(body)
        #body = html_to_text(body)
        #print body
        #self.ui.bodyedit.setPlainText(body)
        #body = text_to_html(body)
        self.ui.bodyedit.setPlainText(body)
        print type(body)
       
        #print s

        #self.ui.bodyedit.setPlainText(dehtml(body))
        
        #self.ui.titleedit.
    '''
    数据库更新
    '''
    @pyqtSignature("")
    def on_updatebutton_clicked(self):
        """
        Slot documentation goes here.
        """

        body = self.ui.bodyedit.toPlainText()
        print type(body)
        self.ui.bodyedit.setPlainText(body)
        
    
    @pyqtSignature("")
    def on_resetbutton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError

  
        

"""
数据库连接
"""    
def createConnection():    
        db = QSqlDatabase.addDatabase("QMYSQL")
        host = "localhost"
        port = 3306
        database = "test"
        username = "root"
        password = ""
        db.setHostName(host)
        db.setPort(port)
        db.setDatabaseName(database)
        db.setUserName(username)
        db.setPassword(password)
        if not db.open():    #打印错误信息
            print("error")
            QMessageBox.warning(None, u"数据库连接出错", QSqlDatabase.lastError(db).text())
            print (QSqlDatabase.lastError(db).text()) 
        else:
            print ("ook")
            
"""
数据表操作
"""
class Model(QSqlTableModel):   
    def __init__(self, parent = None):
        QSqlTableModel.__init__(self, parent)
        self.setTable("t_news")
        #t = self.select()
        #print t
        #print self.selectStatement()
        #self.setEditStrategy(QSqlTableModel.OnManualSubmit)
        q = QSqlQuery()
        q.exec_("SELECT nid,cid,title FROM t_news;")
        self.setQuery(q)

        #self.setFilter("")
        #self.setQuery()
        self.select()
        #print(1, 1)
        #print self.index(5, 0).data().toInt()[0] 
        #print type(self.index(5, 0).data().toInt())
        
        mainWindow.ui.tableView.setModel(self)
        mainWindow.ui.tableView.resizeColumnToContents(0) #tableview列自适应宽度
        mainWindow.ui.tableView.resizeColumnToContents(1) #tableview列自适应宽度
        mainWindow.ui.tableView.resizeColumnToContents(2) #tableview列自适应宽度
    def search(nid):
        q = QSqlQuery()
        #q.exec_("SELECT title FROM t_news WHERE nid = "+nid+";")
        q.exec_("SELECT title,digest,body FROM t_news WHERE nid = "+nid+";")
        print ("select"+cid)
    def showdata(self):
        q = QSqlQuery()
        select = "SELECT * FROM t_news;"
        q.exec_(select)
            


if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)

    mainWindow = MainWindow()
    mainWindow.show()    #显示主窗口  
    createConnection()  #连接数据库
    Model()
    #while True:
    
    sys.exit(app.exec_())
