# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
import sys
reload(sys)
sys.setdefaultencoding('UTF-8')
import urllib2,urllib,re
from bs4 import BeautifulSoup
from PyQt4 import QtGui,QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import pyqtSignature, QString
from PyQt4.QtSql import *

from Ui_news0 import Ui_MainWindow
#from html2text import _DeHTMLParser, dehtml, txt2html
#from text2html import *
from spider import *
#from SqlModel import Model

QtCore.QTextCodec.setCodecForCStrings(QtCore.QTextCodec.codecForName("UTF-8"))
QtCore.QTextCodec.setCodecForLocale ( QtCore.QTextCodec.codecForName("UTF-8"))

#QTextCodec::setCodecForCStrings(QTextCodec::codecForName("UTF-8"));



#nidmax = 0
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
        self.nid = 0
        self.nidmax = 0
        self.cid = 1
        self.title = ""       
        self.digest = ""       
        self.body = ""       

    
    @pyqtSignature("")
    def on_okbutton_released(self):
        """
        网址输入
        """
        url = self.ui.urlLine.text()
        print url
        url = str(url)
        print ("ok_button realeased")
        self.ui.urlLine.setText("")

        print self.ui.categorizebox_p.currentIndex()+1
        self.cid = self.ui.categorizebox_p.currentIndex()+1
        self.title, self.body = load(url)       #网页解析
        self.ui.titleedit.setPlainText(self.title)
        self.ui.bodyedit.setPlainText(self.body)
        q = QSqlQuery()
        #nidmax = Model.rowCount(Model)
        #tuple1 = (self.nidmax+1, self.cid, self.title.encode('utf-8') , self.body.encode('utf-8') , "1".encode('utf-8'))
        tuple1 = (self.nidmax+1, self.cid, self.title , self.body , "1")
        #tuple1 = (self.nidmax+1, self.cid, "1" , "1" , "1")
        Model.insert(self.ui.tableView.model(), tuple1)
        #print "self.nidmax:"
        #print self.nidmax


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
        print "nid:"
        print nid
        self.search(nid)

    def search(self, nid):
        q = QSqlQuery()
        nid = bytes(nid)
        selection = "SELECT cid,title,digest,body FROM t_news WHERE nid = "+nid+";"
        print selection
        q.exec_(selection)
        #print type(q)
        if q.first():        #读取cid，标题，摘要和正文
            self.cid = q.value(0).toInt()[0]
            print type(self.cid)
            self.title = q.value(1).toString()
            self.digest = q.value(2).toString()
            self.body = q.value(3).toString()
            #body.replace('<p>', '')
            #body.replace('</p>', '')
        '''
        显示分类，标题，摘要和正文
        '''
        self.ui.titleedit.setPlainText(self.title)
        self.ui.digestedit.setPlainText(self.digest)
        self.ui.bodyedit.setPlainText(self.body)
        self.ui.categorizebox_m.setCurrentIndex(self.cid-1)


    '''
    数据库更新
    '''
    @pyqtSignature("")
    def on_updatebutton_clicked(self):
        """
        Slot documentation goes here.
        """

        self.body = self.ui.bodyedit.toPlainText() #已修改的文本
        self.title = self.ui.titleedit.toPlainText()
        self.digest = self.ui.digestedit.toPlainText()
        
        #print type(body)
        self.ui.bodyedit.setPlainText(self.body)
        
    
    @pyqtSignature("")
    def on_resetbutton_clicked(self):
        """
        Slot documentation goes here.
        """
        print ("reset Button clicked")
        #search(nid)
        print self.nid
        self.ui.titleedit.setPlainText(self.title)
        self.ui.digestedit.setPlainText(self.digest)
        self.ui.bodyedit.setPlainText(self.body)
        self.ui.categorizebox_m.setCurrentIndex(self.cid-1)
    def tableupdate(self, parent = None):
        QSqlTableModel.__init__(self, parent)
        self.setTable("t_news")
        q = QSqlQuery()
        q.exec_("SELECT nid,cid,title FROM t_news;")
        self.setQuery(q)
        self.select()
        self.nidmax = self.rowCount()
        self.ui.tableView.setModel(self)
        self.ui.tableView.resizeColumnToContents(0) #tableview列自适应宽度
        self.ui.tableView.resizeColumnToContents(1) #tableview列自适应宽度
        self.ui.tableView.resizeColumnToContents(2) #tableview列自适应宽度



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
            print ("ok")
            
"""
数据表操作
"""
class Model(QSqlTableModel):   
    def __init__(self, parent = None):
        QSqlTableModel.__init__(self, parent)
        self.setTable("t_news")

        #print self.selectStatement()
        #self.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.q = QSqlQuery()
        self.q.exec_("SELECT nid,cid,title FROM t_news;")
        self.setQuery(self.q)

        self.select()
        mainWindow.nidmax = self.rowCount()

        mainWindow.ui.tableView.setModel(self)
        mainWindow.ui.tableView.resizeColumnToContents(0) #tableview列自适应宽度
        mainWindow.ui.tableView.resizeColumnToContents(1) #tableview列自适应宽度
        mainWindow.ui.tableView.resizeColumnToContents(2) #tableview列自适应宽度
        mainWindow.ui.tableView.show()
        print "Model()"
    def search(nid):
        #q = QSqlQuery()
        #q.exec_("SELECT title FROM t_news WHERE nid = "+nid+";")
        q.exec_("SELECT title,digest,body FROM t_news WHERE nid = "+nid+";")
        #print ("select"+cid)
    def showdata(self):
        self.__init__()
        r = self.rowCount()
        print "Model.rowCount():"
        print r

        
        print ("show data")
    def insert(self, tuple1):
        insert = "insert into t_news (nid,cid,title,body,ptime) values (%d,%d,'%s','%s','%s');" % tuple1
        flag = self.q.exec_(unicode(insert))
        #print unicode(insert)
        print flag
        print ("insert succeed")
        if flag == False: 
            print self.q.lastError()
            print (self.q.lastError().text())
            print type(self.q.lastError().text())
        self.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.showdata()
            


if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)

    mainWindow = MainWindow()
    mainWindow.show()    #显示主窗口  
    createConnection()  #连接数据库
    Model()
    
    sys.exit(app.exec_())
