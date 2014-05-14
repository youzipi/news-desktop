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
        self.setupUi(self)
        #self.createConnection()
    
#    @pyqtSignature("QString")
#    def on_urlLine_textEdited(self, p0):
#        """
#        Slot documentation goes here.
#        """
#        #
#        raise NotImplementedError

    
    @pyqtSignature("")
    def on_okbutton_released(self):
        """
        网址输入
        """
        url = self.urlLine.text()
        print type(url)
        self.testText.setPlainText(url)
        #self.plainTextEdit.insertPlainText()
        #raise NotImplementedError
  
    @pyqtSignature("")
    def on_backbutton_released(self):
        """
        反向编辑
        """
        url = self.testText.toPlainText()
        print type(url)
        self.urlLine.setText(url)
        #raise NotImplementedError
    def createConnection(self):    #数据库操作
        #db = 
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
        if not db.open():
            print("error")
            QMessageBox.warning(None, u"数据库连接出错", QSqlDatabase.lastError(db).text())
            print (QSqlDatabase.lastError(db).text()) #打印错误信息

        else:
            print ("ok")
    def showdata(self):
        q = QSqlQuery()
        select = "SELECT * FROM t_news;"
    
    @pyqtSignature("QModelIndex")
    def on_tableView_doubleClicked(self, index):
        """
        Slot documentation goes here.
        """
        self.tableView.resizeColumnToContents(0)
        # TODO: not implemented yet
        #raise NotImplementedError
        print ("doubleclicked")
        #q.exec_(select)
class Model(QSqlTableModel):   #数据表操作
    def __init__(self, parent = None):
        QSqlTableModel.__init__(self, parent)
        self.setTable("t_news")
        #t = self.select()
        #print t
        print self.selectStatement()
        #self.setEditStrategy(QSqlTableModel.OnManualSubmit)
        q = QSqlQuery()
        q.exec_("SELECT title FROM t_news;")
        self.setQuery(q)

        #self.setFilter("")
        #self.setQuery()
        self.select()
        mainWindow.tableView.setModel(self)
def createConnection(self):    #数据库操作
        #db = 
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
        if not db.open():
            print("error")
            QMessageBox.warning(None, u"数据库连接出错", QSqlDatabase.lastError(db).text())
            print (QSqlDatabase.lastError(db).text()) #打印错误信息
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
    
    createConnection(1)  #连接数据库
    Model()
    

    sys.exit(app.exec_())
