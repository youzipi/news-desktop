# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
import sys
reload(sys)
sys.setdefaultencoding('UTF-8')

from PyQt4 import QtGui,QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import pyqtSignature, QString
from PyQt4.QtSql import *

#from Ui_news0 import Ui_MainWindow
from Ui_news1 import Ui_MainWindow
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
        #print type(self)
        QMainWindow.__init__(self, parent)
        #QMainWindow.setStyle()
        self.ui = Ui_MainWindow()
        #print type(self.ui)
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
        url = str(url)
        self.ui.urlLine.setText("")

        #self.cid = self.ui.categorizebox_p.currentIndex()+1
        self.title, self.body = load(url)       #网页解析
        self.ui.titleedit.setPlainText(self.title)
        #self.ui.bodyedit.setPlainText(self.body)
        self.ui.bodyedit.setHtml(self.body)
        q = QSqlQuery()
        r = self.ui.tableView.model().rowCount()  
        self.nid = self.ui.tableView.model().index(r-1, 0).data().toInt()[0] + 1 #获取插入位置
        tuple1 = (self.nid, self.cid, self.title , self.body , "1")
        Model.insert(self.ui.tableView.model(), tuple1)

    def showdata(self):
        q = QSqlQuery()
        select = "SELECT * FROM t_news;"
    
    @pyqtSignature("QModelIndex")
    def on_tableView_clicked(self, index):    #表格元素点击
        
        item = QStandardItem()
        row = index.row()
        column = index.column()
        self.ui.tableView.selectRow(row)
        self.nid = self.ui.tableView.model().index(row, 0).data().toInt()[0]
        self.search(self.nid)
        
    @pyqtSignature("QModelIndex")
    def on_tableView_1_clicked(self, index):
        row = index.row()
        self.ui.tableView_1.selectRow(row)
        self.nid = self.ui.tableView_1.model().index(row, 0).data().toInt()[0]
        self.search(self.nid)
        
    @pyqtSignature("QModelIndex")
    def on_tableView_2_clicked(self, index):
        row = index.row()
        self.ui.tableView_2.selectRow(row)
        self.nid = self.ui.tableView_2.model().index(row, 0).data().toInt()[0]
        self.search(self.nid)

    @pyqtSignature("QModelIndex")
    def on_tableView_3_clicked(self, index):
        row = index.row()
        self.ui.tableView_3.selectRow(row)
        self.nid = self.ui.tableView_3.model().index(row, 0).data().toInt()[0]
        self.search(self.nid)
        
    @pyqtSignature("QModelIndex")
    def on_tableView_4_clicked(self, index):
        row = index.row()
        self.ui.tableView_4.selectRow(row)
        self.nid = self.ui.tableView_4.model().index(row, 0).data().toInt()[0]
        self.search(self.nid)
    @pyqtSignature("QModelIndex")
    def on_tableView_5_clicked(self, index):
        row = index.row()
        self.ui.tableView_5.selectRow(row)
        self.nid = self.ui.tableView_5.model().index(row, 0).data().toInt()[0]
        self.search(self.nid)
    @pyqtSignature("QModelIndex")
    def on_tableView_6_clicked(self, index):
        row = index.row()
        self.ui.tableView_6.selectRow(row)
        self.nid = self.ui.tableView_6.model().index(row, 0).data().toInt()[0]
        self.search(self.nid)

        
        
     
    def showtables(self):
        tab1 = QSqlTableModel()
        tab2 = QSqlTableModel()
        tab3 = QSqlTableModel()
        tab4 = QSqlTableModel()
        tab5 = QSqlTableModel()
        tab6 = QSqlTableModel()
        
        tab1.setTable("t_news")
        tab2.setTable("t_news")
        tab3.setTable("t_news")
        tab4.setTable("t_news")
        tab5.setTable("t_news")
        tab6.setTable("t_news")
        
        selection = "SELECT nid,title FROM t_news;"
        q = QSqlQuery()
        q.exec_(selection) #% 1
        
        tab1.setQuery(q)
        tab1.setFilter("cid = 1")
        tab1.select()
        self.ui.tableView_1.setModel(tab1) 
        self.ui.tableView_1.setColumnHidden(0,True) 
        self.ui.tableView_1.resizeColumnToContents(1) #tableview列自适应宽度
        self.ui.tableView_1.show()
        

        tab2.setQuery(q)
        tab2.setFilter("cid = 2")
        tab2.select()
        self.ui.tableView_2.setModel(tab2) 
        self.ui.tableView_2.setColumnHidden(0,True) #tableview列自适应宽度
        self.ui.tableView_2.resizeColumnToContents(1) #tableview列自适应宽度
        self.ui.tableView_2.show()
        
        tab3.q = QSqlQuery()
        tab3.q.exec_(selection) #% 1
        tab3.setQuery(q)
        tab3.setFilter("cid = 3")
        tab3.select()
        self.ui.tableView_3.setModel(tab3) 
        self.ui.tableView_3.setColumnHidden(0,True) #tableview列自适应宽度
        self.ui.tableView_3.resizeColumnToContents(1) #tableview列自适应宽度
        self.ui.tableView_3.show()
        
        tab4.q = QSqlQuery()
        tab4.q.exec_(selection) #% 1
        tab4.setQuery(q)
        tab4.setFilter("cid = 4")
        tab4.select()
        self.ui.tableView_4.setModel(tab4) 
        self.ui.tableView_4.setColumnHidden(0,True) #tableview列自适应宽度
        self.ui.tableView_4.resizeColumnToContents(1) #tableview列自适应宽度
        self.ui.tableView_4.show()
        
        tab5.q = QSqlQuery()
        tab5.q.exec_(selection) #% 1
        tab5.setQuery(q)
        tab5.setFilter("cid = 5")
        tab5.select()
        self.ui.tableView_5.setModel(tab5) 
        self.ui.tableView_5.setColumnHidden(0,True) #tableview列自适应宽度
        self.ui.tableView_5.resizeColumnToContents(1) #tableview列自适应宽度
        self.ui.tableView_5.show()
        
        tab6.q = QSqlQuery()
        tab6.q.exec_(selection) #% 1
        tab6.setQuery(q)
        tab6.setFilter("cid = 6")
        tab6.select()
        self.ui.tableView_6.setModel(tab6) 
        self.ui.tableView_6.setColumnHidden(0,True) #tableview列自适应宽度
        self.ui.tableView_6.resizeColumnToContents(1) #tableview列自适应宽度
        self.ui.tableView_6.show()
        

        
        #if flag2 == False: 
         #   print tab2.q.lastError()
         #   print (tab2.q.lastError().text())
         #   print type(tab2.q.lastError().text())
        
        
        #tab2.q.exec_("SELECT title FROM t_news where cid = 2;") #% 2
        #tab2.setQuery(tab2.q)


    def search(self, nid):
        q = QSqlQuery()
        #nid = bytes(nid)
        selection = "SELECT cid,title,digest,body FROM t_news WHERE nid = %d;" % nid
        q.exec_(selection)
        if q.first():        #读取cid，标题，摘要和正文
            self.cid = q.value(0).toInt()[0]

            self.title = q.value(1).toString()
            self.digest = q.value(2).toString()
            self.body = q.value(3).toString()
        '''
        显示分类，标题，摘要和正文
        '''
        self.ui.titleedit.setPlainText(self.title)
        self.ui.digestedit.setPlainText(self.digest)
        #self.ui.bodyedit.setPlainText(self.body)
        #print self.body
        self.ui.bodyedit.setHtml(self.body)
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
        print type(self.nid)
        tuple2 = (self.cid, self.title, self.digest, self.body, self.nid)
        Model.update(self.ui.tableView.model(), tuple2)
    
    @pyqtSignature("")
    def on_resetbutton_clicked(self):
        """
        重置编辑框中的内容：（标题，概要，正文）
        """

        self.ui.titleedit.setPlainText(self.title)
        self.ui.digestedit.setPlainText(self.digest)
        #self.ui.bodyedit.setPlainText(self.body)
        self.ui.bodyedit.setHtml(self.body)
        self.ui.categorizebox_m.setCurrentIndex(self.cid-1)
    @pyqtSignature("")
    def on_deletebutton_clicked(self):
        Model.delete(self.ui.tableView.model(), self.nid)
    @pyqtSignature("")
    def on_actionAbout_triggered(self):
        """
        Slot documentation goes here.
        """
        QMessageBox.about(None, u"About",u"Teemo news 桌面端")




"""
数据库连接
    

    
    
"""
def createConnection():    
        db = QSqlDatabase.addDatabase("QMYSQL")
        host = "localhost"
        port = 3306
        database = "test"
        username = "root"
        password = "123456"
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
        #self.q.exec_("SELECT nid,cid, title FROM t_news where cid = 1;")
        self.setQuery(self.q)
        self.select()

        mainWindow.ui.tableView.setModel(self)
        #mainWindow.ui.tableView.resizeColumnToContents(0) #tableview列自适应宽度
        #mainWindow.ui.tableView.resizeColumnToContents(1) #tableview列自适应宽度
        mainWindow.ui.tableView.setColumnHidden(0,True) #tableview列自适应宽度
        mainWindow.ui.tableView.setColumnHidden(1,True) #tableview列自适应宽度
        mainWindow.ui.tableView.resizeColumnToContents(2) #tableview列自适应宽度
        mainWindow.ui.tableView.show()
        mainWindow.showtables()
        #self.search()
        
    

        
    def showdata(self):
        self.__init__()
        mainWindow.showtables()
    def update(self,tuple2):
        update = "UPDATE t_news SET cid= %d, title= '%s', digest= '%s', body= '%s' WHERE nid = %d;" % tuple2
        flag2 = self.q.exec_(unicode(update))

        if flag2 == False: 
            print self.q.lastError()
            print (self.q.lastError().text())
            print type(self.q.lastError().text())
        self.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.showdata()
        
    def insert(self, tuple1):
        insert = "insert into t_news (nid,cid,title,body,ptime) values (%d,%d,'%s','%s','%s');" % tuple1
        flag = self.q.exec_(unicode(insert))

        if flag == False: 
            print self.q.lastError()
            print (self.q.lastError().text())
            print type(self.q.lastError().text())
        self.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.showdata()
    def delete(self,nid):
        delete = "DELETE FROM t_news WHERE nid = %d;" % nid
        flag3 = self.q.exec_(unicode(delete))

        if flag3 == False: 
            print self.q.lastError()
            print (self.q.lastError().text())
            print type(self.q.lastError().text())
        self.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.showdata()
            

if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)
    #app.setStyle("cleanlooks")

    mainWindow = MainWindow()
    mainWindow.show()    #显示主窗口  
    createConnection()  #连接数据库
    Model()
    
    sys.exit(app.exec_())
