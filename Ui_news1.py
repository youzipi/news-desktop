# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Documents\python\pyqt\demos\ericdemo\news\news1.ui'
#
# Created: Fri Jul 18 20:04:22 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1040, 604)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setOpaqueResize(True)
        self.splitter.setHandleWidth(5)
        self.splitter.setChildrenCollapsible(True)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.groupBox = QtGui.QGroupBox(self.splitter)
        self.groupBox.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(200, 0))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.urlLine = QtGui.QLineEdit(self.groupBox)
        self.urlLine.setStyleSheet(_fromUtf8("background:white;"))
        self.urlLine.setText(_fromUtf8(""))
        self.urlLine.setObjectName(_fromUtf8("urlLine"))
        self.horizontalLayout.addWidget(self.urlLine)
        self.okbutton = QtGui.QPushButton(self.groupBox)
        self.okbutton.setStyleSheet(_fromUtf8("background:#669966;\n"
"font: 10pt \"Arial\";"))
        self.okbutton.setObjectName(_fromUtf8("okbutton"))
        self.horizontalLayout.addWidget(self.okbutton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem)
        self.tabWidget = QtGui.QTabWidget(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(200, 0))
        self.tabWidget.setMouseTracking(False)
        self.tabWidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tabWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tabWidget.setAcceptDrops(True)
        self.tabWidget.setStyleSheet(_fromUtf8("background:rgb(229, 229, 229)"))
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab2 = QtGui.QWidget()
        self.tab2.setObjectName(_fromUtf8("tab2"))
        self.tableView = QtGui.QTableView(self.tab2)
        self.tableView.setGeometry(QtCore.QRect(0, 0, 8000, 8000))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        self.tableView.setMinimumSize(QtCore.QSize(0, 0))
        self.tableView.setStyleSheet(_fromUtf8("background:white;"))
        self.tableView.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableView.setDragEnabled(True)
        self.tableView.setSortingEnabled(True)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.tabWidget.addTab(self.tab2, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.tableView_1 = QtGui.QTableView(self.tab)
        self.tableView_1.setGeometry(QtCore.QRect(0, 0, 8000, 8000))
        self.tableView_1.setStyleSheet(_fromUtf8("background:white;"))
        self.tableView_1.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableView_1.setDragEnabled(True)
        self.tableView_1.setSortingEnabled(True)
        self.tableView_1.setObjectName(_fromUtf8("tableView_1"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tableView_2 = QtGui.QTableView(self.tab_2)
        self.tableView_2.setGeometry(QtCore.QRect(0, 0, 8000, 8000))
        self.tableView_2.setStyleSheet(_fromUtf8("background:white;"))
        self.tableView_2.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableView_2.setDragEnabled(True)
        self.tableView_2.setSortingEnabled(True)
        self.tableView_2.setObjectName(_fromUtf8("tableView_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.tableView_3 = QtGui.QTableView(self.tab_3)
        self.tableView_3.setGeometry(QtCore.QRect(0, 0, 8000, 8000))
        self.tableView_3.setStyleSheet(_fromUtf8("background:white;"))
        self.tableView_3.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableView_3.setDragEnabled(True)
        self.tableView_3.setSortingEnabled(True)
        self.tableView_3.setObjectName(_fromUtf8("tableView_3"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.tableView_4 = QtGui.QTableView(self.tab_4)
        self.tableView_4.setGeometry(QtCore.QRect(0, 0, 8000, 8000))
        self.tableView_4.setStyleSheet(_fromUtf8("background:white;"))
        self.tableView_4.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableView_4.setDragEnabled(True)
        self.tableView_4.setSortingEnabled(True)
        self.tableView_4.setObjectName(_fromUtf8("tableView_4"))
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName(_fromUtf8("tab_6"))
        self.tableView_6 = QtGui.QTableView(self.tab_6)
        self.tableView_6.setGeometry(QtCore.QRect(0, 0, 8000, 8000))
        self.tableView_6.setStyleSheet(_fromUtf8("background:white;"))
        self.tableView_6.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableView_6.setDragEnabled(True)
        self.tableView_6.setSortingEnabled(True)
        self.tableView_6.setObjectName(_fromUtf8("tableView_6"))
        self.tabWidget.addTab(self.tab_6, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.tableView_5 = QtGui.QTableView(self.tab_5)
        self.tableView_5.setGeometry(QtCore.QRect(0, 0, 8000, 8000))
        self.tableView_5.setStyleSheet(_fromUtf8("background:white;"))
        self.tableView_5.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableView_5.setDragEnabled(True)
        self.tableView_5.setSortingEnabled(True)
        self.tableView_5.setObjectName(_fromUtf8("tableView_5"))
        self.tabWidget.addTab(self.tab_5, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.groupBox_2 = QtGui.QGroupBox(self.splitter)
        self.groupBox_2.setEnabled(True)
        self.groupBox_2.setMinimumSize(QtCore.QSize(200, 0))
        self.groupBox_2.setStyleSheet(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.titleedit = QtGui.QTextEdit(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleedit.sizePolicy().hasHeightForWidth())
        self.titleedit.setSizePolicy(sizePolicy)
        self.titleedit.setMaximumSize(QtCore.QSize(16777215, 30))
        self.titleedit.setSizeIncrement(QtCore.QSize(2, 0))
        self.titleedit.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.titleedit.setFont(font)
        self.titleedit.setStyleSheet(_fromUtf8(""))
        self.titleedit.setObjectName(_fromUtf8("titleedit"))
        self.verticalLayout_3.addWidget(self.titleedit)
        self.digestedit = QtGui.QTextEdit(self.groupBox_2)
        self.digestedit.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.digestedit.setFont(font)
        self.digestedit.setStyleSheet(_fromUtf8(""))
        self.digestedit.setObjectName(_fromUtf8("digestedit"))
        self.verticalLayout_3.addWidget(self.digestedit)
        self.bodyedit = QtGui.QTextEdit(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bodyedit.sizePolicy().hasHeightForWidth())
        self.bodyedit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bodyedit.setFont(font)
        self.bodyedit.setStyleSheet(_fromUtf8(""))
        self.bodyedit.setObjectName(_fromUtf8("bodyedit"))
        self.verticalLayout_3.addWidget(self.bodyedit)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(30, 30))
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.categorizebox_m = QtGui.QComboBox(self.groupBox_2)
        self.categorizebox_m.setMinimumSize(QtCore.QSize(80, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("SimSun-ExtB"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.categorizebox_m.setFont(font)
        self.categorizebox_m.setStyleSheet(_fromUtf8("background:#FFFFFF;"))
        self.categorizebox_m.setObjectName(_fromUtf8("categorizebox_m"))
        self.categorizebox_m.addItem(_fromUtf8(""))
        self.categorizebox_m.addItem(_fromUtf8(""))
        self.categorizebox_m.addItem(_fromUtf8(""))
        self.categorizebox_m.addItem(_fromUtf8(""))
        self.categorizebox_m.addItem(_fromUtf8(""))
        self.categorizebox_m.addItem(_fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.categorizebox_m)
        spacerItem1 = QtGui.QSpacerItem(0, 0, QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.updatebutton = QtGui.QPushButton(self.groupBox_2)
        self.updatebutton.setStyleSheet(_fromUtf8("color: #3e5706;\n"
"background: #a5cd4e;\n"
"font: 15pt \"Arial\";\n"
"   "))
        self.updatebutton.setObjectName(_fromUtf8("updatebutton"))
        self.horizontalLayout_2.addWidget(self.updatebutton)
        self.deletebutton = QtGui.QPushButton(self.groupBox_2)
        self.deletebutton.setStyleSheet(_fromUtf8("color:#CC0000;\n"
"background:#FF6600;\n"
"font: 15pt \"Arial\";\n"
""))
        self.deletebutton.setObjectName(_fromUtf8("deletebutton"))
        self.horizontalLayout_2.addWidget(self.deletebutton)
        self.resetbutton = QtGui.QPushButton(self.groupBox_2)
        self.resetbutton.setStyleSheet(_fromUtf8("color: #19667d;\n"
"background: #70c9e3;\n"
"font: 15pt \"\";\n"
"font: 75 16pt \"Arial\";"))
        self.resetbutton.setObjectName(_fromUtf8("resetbutton"))
        self.horizontalLayout_2.addWidget(self.resetbutton)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1040, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName(_fromUtf8("menu"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.groupBox.setTitle(_translate("MainWindow", "加载区", None))
        self.label.setText(_translate("MainWindow", "请拖拽网页链接到此处：", None))
        self.okbutton.setText(_translate("MainWindow", "OK", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("MainWindow", "新闻列表", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "焦点", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "国内", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "国际", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "体育", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "科技", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "文娱", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "编辑区", None))
        self.label_2.setText(_translate("MainWindow", "分类：", None))
        self.categorizebox_m.setItemText(0, _translate("MainWindow", "焦点", None))
        self.categorizebox_m.setItemText(1, _translate("MainWindow", "国内", None))
        self.categorizebox_m.setItemText(2, _translate("MainWindow", "国际", None))
        self.categorizebox_m.setItemText(3, _translate("MainWindow", "体育", None))
        self.categorizebox_m.setItemText(4, _translate("MainWindow", "文娱", None))
        self.categorizebox_m.setItemText(5, _translate("MainWindow", "科技", None))
        self.updatebutton.setText(_translate("MainWindow", "update", None))
        self.deletebutton.setText(_translate("MainWindow", "delete", None))
        self.resetbutton.setText(_translate("MainWindow", "reset", None))
        self.menuAbout.setTitle(_translate("MainWindow", "About", None))
        self.menu.setTitle(_translate("MainWindow", "Setting", None))
        self.actionAbout.setText(_translate("MainWindow", "about", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

