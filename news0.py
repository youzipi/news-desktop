# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
import sys
reload(sys)
sys.setdefaultencoding('UTF-8')

from bs4 import BeautifulSoup
from PyQt4 import QtGui,QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import pyqtSignature, QString
from PyQt4.QtSql import *

from Ui_news0 import Ui_MainWindow
from spider import *


QtCore.QTextCodec.setCodecForCStrings(QtCore.QTextCodec.codecForName("UTF-8"))
QtCore.QTextCodec.setCodecForLocale ( QtCore.QTextCodec.codecForName("UTF-8"))





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
        r = self.ui.tableView.model().rowCount()
        print "Model.rowCount():"
        print r
        print "index(r,0).data().toInt()"
        self.nid = self.ui.tableView.model().index(r-1, 0).data().toInt()[0] + 1
        print self.nid
        tuple1 = (self.nid, self.cid, self.title , self.body , "1")
        Model.insert(self.ui.tableView.model(), tuple1)
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
        self.nid = self.ui.tableView.model().index(row, 0).data().toInt()[0]
        print "nid:"
        print self.nid
        self.search(self.nid)

    def search(self, nid):
        q = QSqlQuery()
        nid = bytes(nid)
        selection = "SELECT cid,title,digest,body FROM t_news WHERE nid = "+nid+";"
        print selection
        q.exec_(selection)
        if q.first():        #读取cid，标题，摘要和正文
            self.cid = q.value(0).toInt()[0]
            print type(self.cid)
            self.title = q.value(1).toString()
            self.digest = q.value(2).toString()
            self.body = q.value(3).toString()
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
        self.cid = self.ui.categorizebox_m.currentIndex()+1
        self.body = self.ui.bodyedit.toPlainText() #已修改的文本
        self.title = self.ui.titleedit.toPlainText()
        self.digest = self.ui.digestedit.toPlainText()
        tuple2 = (self.cid, self.title, self.digest, self.body, self.nid)
        Model.update(self.ui.tableView.model(), tuple2)
    
    @pyqtSignature("")
    def on_resetbutton_clicked(self):
        """
        Slot documentation goes here.
        """
        print ("reset Button clicked")
        print self.nid
        self.ui.titleedit.setPlainText(self.title)
        self.ui.digestedit.setPlainText(self.digest)
        self.ui.bodyedit.setPlainText(self.body)
        self.ui.categorizebox_m.setCurrentIndex(self.cid-1)
    @pyqtSignature("")
    def on_deletebutton_clicked(self):
        Model.delete(self.ui.tableView.model(), self.nid)


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
        self.q = QSqlQuery()
        self.q.exec_("SELECT nid,cid,title FROM t_news;")
        self.setQuery(self.q)
        self.select()

        mainWindow.ui.tableView.setModel(self)
        mainWindow.ui.tableView.resizeColumnToContents(0) #tableview列自适应宽度
        mainWindow.ui.tableView.resizeColumnToContents(1) #tableview列自适应宽度
        mainWindow.ui.tableView.resizeColumnToContents(2) #tableview列自适应宽度
        mainWindow.ui.tableView.show()
        print "Model()"
        
    def search(nid):
        q.exec_("SELECT title,digest,body FROM t_news WHERE nid = "+nid+";")
        
    def showdata(self):
        self.__init__()
    def update(self,tuple2):
        update = "UPDATE t_news SET cid= %d, title= '%s', digest= '%s', body= '%s' WHERE nid = %d;" % tuple2
        flag2 = self.q.exec_(unicode(update))
        print flag2
        print ("update succeed")
        if flag2 == False: 
            print self.q.lastError()
            print (self.q.lastError().text())
            print type(self.q.lastError().text())
        self.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.showdata()
        
    def insert(self, tuple1):
        insert = "insert into t_news (nid,cid,title,body,ptime) values (%d,%d,'%s','%s','%s');" % tuple1
        flag = self.q.exec_(unicode(insert))
        print flag
        print ("insert succeed")
        if flag == False: 
            print self.q.lastError()
            print (self.q.lastError().text())
            print type(self.q.lastError().text())
        self.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.showdata()
    def delete(self,nid):
        delete = "DELETE FROM t_news WHERE nid = %d;" % nid
        flag3 = self.q.exec_(unicode(delete))
        print flag3
        print ("delete succeed")
        if flag3 == False: 
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
