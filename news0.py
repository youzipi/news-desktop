# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
from PyQt4 import QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import pyqtSignature
from PyQt4.QtSql import *

from Ui_news0 import Ui_MainWindow

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
        self.ui.tableView.resizeColumnToContents(0)
        #model = Model()

    
    @pyqtSignature("")
    def on_okbutton_released(self):
        """
        网址输入
        """
        url = self.ui.urlLine.text()
        print type(url)
        self.ui.testText.setPlainText(url)

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
        print (index.column(), index.row())
    
    @pyqtSignature("QModelIndex")
    def on_tableView_doubleClicked(self, index):    #表格元素双击
        item = QStandardItem()
        print type(item)
        row = index.row()
        column = index.column()
        #print self.ui.tableView.item(row, column).text()
        #print Model.data(Model.index(row, column)).text()
        #print Model.index(row, 0).data().toInt()[0]
        #print self.ui.tableView.selectionModel().model().index(row, 0).data().toInt()[0]
        print self.ui.tableView.model().index(row, 0).data().toInt()[0]
        #print self.ui.tableView.model().index(row, 2).data().toString()[0]
        #print self.ui.tableView.currentIndex().row()
        cid = row

        #self.ui.titleedit.setPlainText(title)
        self.ui.tableView.selectRow(row)

class Model(QSqlTableModel):   #数据表操作
    def __init__(self, parent = None):
        QSqlTableModel.__init__(self, parent)
        self.setTable("t_news")
        #t = self.select()
        #print t
        print self.selectStatement()
        #self.setEditStrategy(QSqlTableModel.OnManualSubmit)
        q = QSqlQuery()
        q.exec_("SELECT nid,cid,title FROM t_news;")
        self.setQuery(q)

        #self.setFilter("")
        #self.setQuery()
        self.select()
        print(1, 1)
        print self.index(5, 0).data().toInt()[0] 
        #print type(self.index(5, 0).data().toInt())
        
        mainWindow.ui.tableView.setModel(self)
        mainWindow.ui.tableView.resizeColumnToContents(0) #tableview列自适应宽度
        mainWindow.ui.tableView.resizeColumnToContents(1) #tableview列自适应宽度
        mainWindow.ui.tableView.resizeColumnToContents(2) #tableview列自适应宽度
def createConnection():    #数据库操作
        db = QSqlDatabase.addDatabase("QMYSQL")
        host = "localhost"
        port = 3306
        database = "android"
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
    

    sys.exit(app.exec_())
