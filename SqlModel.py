# -*- coding: utf-8 -*-
from PyQt4.QtSql import *

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
    def search(cid):
        print ("select"+cid)
    def showdata(self):
        q = QSqlQuery()
        select = "SELECT * FROM t_news;"
        q.exec_(select)
