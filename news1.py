# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
import sys
reload(sys)
sys.setdefaultencoding('UTF-8')
import time

from PyQt4 import QtGui,QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import pyqtSignature, QString
from PyQt4.QtSql import *

#from Ui_news0 import Ui_MainWindow
from Ui_news1 import Ui_MainWindow
from Ui_setting import Ui_Dialog
from spider import *
import base64
import os
import ConfigParser
#from imgzip import *


QtCore.QTextCodec.setCodecForCStrings(QtCore.QTextCodec.codecForName("UTF-8"))
QtCore.QTextCodec.setCodecForLocale ( QtCore.QTextCodec.codecForName("UTF-8"))


class dlgSetting(QDialog, Ui_Dialog):
    def __init__(self, parent = None):
        QDialog.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        


class MainWindow(QMainWindow, Ui_MainWindow):
    
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
        
        self.nid = 1
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
        #url = str(url)
        print type(url)
        self.ui.urlLine.setText("")

        #self.cid = self.ui.categorizebox_p.currentIndex()+1
        #self.title, self.body, self.imgsrc,self.filename = load(url)       #**********网页解析********
        self.title, self.body, self.imgsrc,self.imgpath = load(str(url))       #**********网页解析********
        print "self.imgsrc:"
        print self.imgsrc
        #print "self.filename:"
        #print self.filename
        #self.filename = unicode(self.filename,"utf8")
        #print self.filename
        
        self.ui.titleedit.setPlainText(self.title)
        #self.ui.bodyedit.setPlainText(self.body)
        self.ui.bodyedit.setHtml(self.body)
        q = QSqlQuery()
        r = self.ui.tableView.model().rowCount()  
        self.nid = self.ui.tableView.model().index(r-1, 0).data().toInt()[0] + 1 #获取插入位置
        ptime = time.strftime('%Y-%m-%d',time.localtime(time.time()))  #
        imgpath = str(self.imgpath)
        imgpath = base64.b64encode(imgpath)
        stared = 0
        tuple1 = (self.nid, self.cid, self.title , self.body , ptime, self.imgsrc,imgpath, stared)
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
        selection = "SELECT cid,title,digest,body,deleted FROM t_news WHERE nid = %d;" % nid
        q.exec_(selection)
        if q.first():        #读取cid，标题，摘要和正文
            self.cid = q.value(0).toInt()[0]

            self.title = q.value(1).toString()
            self.digest = q.value(2).toString()
            self.body = q.value(3).toString()
            self.stared = q.value(4).toInt()[0]*2 #0 -- 未选中 2 -- 选中

        '''
        显示分类，标题，摘要和正文
        '''
        self.ui.titleedit.setPlainText(self.title)
        self.ui.digestedit.setPlainText(self.digest)
        #self.ui.bodyedit.setPlainText(self.body)
        #print self.body
        self.ui.bodyedit.setHtml(self.body)
        self.ui.categorizebox_m.setCurrentIndex(self.cid-1)
        self.ui.starbox.setCheckState(self.stared)


    '''
    数据库更新
    '''
    @pyqtSignature("")
    def on_updatebutton_clicked(self):
        """
        Slot documentation goes here.
        """
        self.cid = self.ui.categorizebox_m.currentIndex()+1
        #self.body = self.ui.bodyedit.toPlainText() #已修改的文本
        self.body = self.ui.bodyedit.toHtml() #已修改的文本
        self.body.replace("'","\\'")
        self.body.replace( 'p, li { white-space: pre-wrap; }\n','')
        self.title = self.ui.titleedit.toPlainText()
        self.digest = self.ui.digestedit.toPlainText()
        self.stared = self.ui.starbox.checkState() / 2
        print "self.stared"
        print self.stared
        tuple2 = (self.cid, self.title, self.digest, self.body, self.stared, self.nid)
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
        self.ui.starbox.setCheckState(self.stared)
    @pyqtSignature("")
    def on_deletebutton_clicked(self):
        Model.delete(self.ui.tableView.model(), self.nid)
        self.ui.titleedit.setPlainText("")
        self.ui.digestedit.setPlainText("")
        #self.ui.bodyedit.setPlainText(self.body)
        self.ui.bodyedit.setHtml("")
        self.ui.categorizebox_m.setCurrentIndex(0)
        self.ui.starbox.setCheckState(0)
        
    @pyqtSignature("")
    def on_actionAbout_triggered(self):
        """
        Slot documentation goes here.
        """
        QMessageBox.about(None, u"About",u"Teemo news 桌面端")
    @pyqtSignature("")
    def on_actionSetting_triggered(self):
        """
        Slot documentation goes here.
        """
        #QMessageBox.about(None, u"About",u"Teemo news 桌面端")
        dialog = dlgSetting()
        dialog.exec_()    #显示主窗口  
        



"""
数据库连接
    

    
    
"""
def createConnection():
        
        #host = "localhost"
        #port = 3306
        #database = "test"
        #username = "root"
        #password = "123456"
        
        config = ConfigParser.SafeConfigParser()
        config.read("setting.ini")
        sections = config.sections()
        host = config.get("mysql","host")
        port = int(config.get("mysql","port"))
        database = config.get("mysql","database")
        username = config.get("mysql","username")
        password = config.get("mysql","password")
        
        db = QSqlDatabase.addDatabase("QMYSQL")

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
        mainWindow.ui.tableView.setColumnHidden(0,True) #隐藏cid，nid
        mainWindow.ui.tableView.setColumnHidden(1,True) #
        mainWindow.ui.tableView.resizeColumnToContents(2) #tableview列自适应宽度
        mainWindow.ui.tableView.show()
        mainWindow.showtables()
        #self.search()
        
    

        
    def showdata(self):
        self.__init__()
        mainWindow.showtables()
    def update(self,tuple2):
        update = "UPDATE t_news SET cid= %d, title= '%s', digest= '%s', body= '%s',deleted = %d WHERE nid = %d;" % tuple2
        print tuple2
        flag2 = self.q.exec_(unicode(update))

        if flag2 == False: 
            print self.q.lastError()
            print (self.q.lastError().text())
            print type(self.q.lastError().text())
        self.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.showdata()
        
    def insert(self, tuple1):
        insert = "insert into t_news (nid,cid,title,body,ptime,imgsrc, imgpath, deleted) values (%d,%d,'%s','%s','%s','%s','%s',%d);" % tuple1
        flag = self.q.exec_(unicode(insert))
        print tuple1
        if flag == False: 
            print self.q.lastError()
            print (self.q.lastError().text())
            print type(self.q.lastError().text())
        self.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.showdata()
    def delete(self,nid):
        ###删除图片
        selection = "SELECT imgpath FROM t_news WHERE nid = %d;" % nid
        self.q.exec_(selection)
        if self.q.first():        #读取cid，标题，摘要和正文
            imgpath = self.q.value(0).toString()
        print imgpath
        print type(imgpath)     #str
        imgpath = eval(base64.b64decode(imgpath)) #eval():str->tuple
        print imgpath
        print type(imgpath)     #list  
        for img in imgpath:
            try:
                os.remove(img)      #删除图片
            except:
                continue
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
