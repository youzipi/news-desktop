# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Documents\python\pyqt\demos\ericdemo\news\news0.ui'
#
<<<<<<< HEAD
<<<<<<< HEAD
# Created: Sun May 18 21:14:51 2014
=======
# Created: Tue May 20 20:20:07 2014
>>>>>>> dev3
=======
# Created: Tue May 20 21:08:32 2014
>>>>>>> stable
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
        MainWindow.resize(885, 616)
        MainWindow.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(30, 90, 461, 351))
        self.tabWidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tabWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab2 = QtGui.QWidget()
        self.tab2.setObjectName(_fromUtf8("tab2"))
        self.tableView = QtGui.QTableView(self.tab2)
        self.tableView.setGeometry(QtCore.QRect(0, 0, 601, 331))
        self.tableView.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableView.setDragEnabled(True)
        self.tableView.setSortingEnabled(True)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.tabWidget.addTab(self.tab2, _fromUtf8(""))
        self.urlLine = QtGui.QLineEdit(self.centralWidget)
        self.urlLine.setGeometry(QtCore.QRect(30, 30, 191, 20))
        self.urlLine.setText(_fromUtf8(""))
        self.urlLine.setObjectName(_fromUtf8("urlLine"))
        self.categorizebox_p = QtGui.QComboBox(self.centralWidget)
        self.categorizebox_p.setGeometry(QtCore.QRect(270, 30, 69, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("SimSun-ExtB"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.categorizebox_p.setFont(font)
        self.categorizebox_p.setObjectName(_fromUtf8("categorizebox_p"))
        self.categorizebox_p.addItem(_fromUtf8(""))
        self.categorizebox_p.addItem(_fromUtf8(""))
        self.categorizebox_p.addItem(_fromUtf8(""))
        self.categorizebox_p.addItem(_fromUtf8(""))
        self.categorizebox_p.addItem(_fromUtf8(""))
        self.categorizebox_p.addItem(_fromUtf8(""))
        self.okbutton = QtGui.QPushButton(self.centralWidget)
        self.okbutton.setGeometry(QtCore.QRect(370, 30, 75, 23))
        self.okbutton.setObjectName(_fromUtf8("okbutton"))
        self.bodyedit = QtGui.QTextEdit(self.centralWidget)
        self.bodyedit.setGeometry(QtCore.QRect(510, 170, 360, 321))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bodyedit.setFont(font)
        self.bodyedit.setObjectName(_fromUtf8("bodyedit"))
        self.pushButton = QtGui.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(300, 490, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.titleedit = QtGui.QTextEdit(self.centralWidget)
        self.titleedit.setGeometry(QtCore.QRect(510, 10, 360, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleedit.sizePolicy().hasHeightForWidth())
        self.titleedit.setSizePolicy(sizePolicy)
        self.titleedit.setSizeIncrement(QtCore.QSize(2, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.titleedit.setFont(font)
        self.titleedit.setObjectName(_fromUtf8("titleedit"))
        self.digestedit = QtGui.QTextEdit(self.centralWidget)
        self.digestedit.setGeometry(QtCore.QRect(510, 70, 360, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.digestedit.setFont(font)
        self.digestedit.setObjectName(_fromUtf8("digestedit"))
        self.updatebutton = QtGui.QPushButton(self.centralWidget)
<<<<<<< HEAD
<<<<<<< HEAD
        self.updatebutton.setGeometry(QtCore.QRect(700, 510, 80, 40))
=======
        self.updatebutton.setGeometry(QtCore.QRect(610, 510, 80, 40))
>>>>>>> dev3
=======
        self.updatebutton.setGeometry(QtCore.QRect(610, 510, 80, 40))
>>>>>>> stable
        self.updatebutton.setObjectName(_fromUtf8("updatebutton"))
        self.resetbutton = QtGui.QPushButton(self.centralWidget)
        self.resetbutton.setGeometry(QtCore.QRect(790, 510, 80, 40))
        self.resetbutton.setObjectName(_fromUtf8("resetbutton"))
        self.line = QtGui.QFrame(self.centralWidget)
        self.line.setGeometry(QtCore.QRect(490, 0, 20, 561))
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.categorizebox_m = QtGui.QComboBox(self.centralWidget)
<<<<<<< HEAD
<<<<<<< HEAD
        self.categorizebox_m.setGeometry(QtCore.QRect(590, 520, 69, 22))
=======
        self.categorizebox_m.setGeometry(QtCore.QRect(530, 510, 69, 22))
>>>>>>> dev3
=======
        self.categorizebox_m.setGeometry(QtCore.QRect(530, 510, 69, 22))
>>>>>>> stable
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("SimSun-ExtB"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.categorizebox_m.setFont(font)
        self.categorizebox_m.setObjectName(_fromUtf8("categorizebox_m"))
        self.categorizebox_m.addItem(_fromUtf8(""))
        self.categorizebox_m.addItem(_fromUtf8(""))
        self.categorizebox_m.addItem(_fromUtf8(""))
        self.categorizebox_m.addItem(_fromUtf8(""))
        self.categorizebox_m.addItem(_fromUtf8(""))
        self.categorizebox_m.addItem(_fromUtf8(""))
<<<<<<< HEAD
<<<<<<< HEAD
=======
        self.deletebutton = QtGui.QPushButton(self.centralWidget)
        self.deletebutton.setGeometry(QtCore.QRect(700, 510, 80, 40))
        self.deletebutton.setObjectName(_fromUtf8("deletebutton"))
>>>>>>> dev3
=======
        self.deletebutton = QtGui.QPushButton(self.centralWidget)
        self.deletebutton.setGeometry(QtCore.QRect(700, 510, 80, 40))
        self.deletebutton.setObjectName(_fromUtf8("deletebutton"))
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 151, 20))
        self.label.setObjectName(_fromUtf8("label"))
>>>>>>> stable
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 885, 23))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuAbout = QtGui.QMenu(self.menuBar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.newAction = QtGui.QAction(MainWindow)
        self.newAction.setObjectName(_fromUtf8("newAction"))
        self.menuAbout.addAction(self.actionAbout)
        self.menuBar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
<<<<<<< HEAD
<<<<<<< HEAD
        self.tabWidget.setCurrentIndex(1)
=======
        self.tabWidget.setCurrentIndex(4)
>>>>>>> dev3
=======
        self.tabWidget.setCurrentIndex(0)
>>>>>>> stable
        QtCore.QObject.connect(self.tableView, QtCore.SIGNAL(_fromUtf8("doubleClicked(QModelIndex)")), MainWindow.show)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.urlLine, self.categorizebox_p)
        MainWindow.setTabOrder(self.categorizebox_p, self.okbutton)
        MainWindow.setTabOrder(self.okbutton, self.tabWidget)
        MainWindow.setTabOrder(self.tabWidget, self.titleedit)
        MainWindow.setTabOrder(self.titleedit, self.digestedit)
        MainWindow.setTabOrder(self.digestedit, self.bodyedit)
        MainWindow.setTabOrder(self.bodyedit, self.updatebutton)
        MainWindow.setTabOrder(self.updatebutton, self.resetbutton)
        MainWindow.setTabOrder(self.resetbutton, self.pushButton)
        MainWindow.setTabOrder(self.pushButton, self.tableView)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("MainWindow", "新闻列表", None))
        self.categorizebox_p.setItemText(0, _translate("MainWindow", "焦点", None))
        self.categorizebox_p.setItemText(1, _translate("MainWindow", "国内", None))
        self.categorizebox_p.setItemText(2, _translate("MainWindow", "国际", None))
        self.categorizebox_p.setItemText(3, _translate("MainWindow", "体育", None))
        self.categorizebox_p.setItemText(4, _translate("MainWindow", "文娱", None))
        self.categorizebox_p.setItemText(5, _translate("MainWindow", "科技", None))
        self.okbutton.setText(_translate("MainWindow", "OK", None))
        self.pushButton.setText(_translate("MainWindow", "PushButton", None))
        self.updatebutton.setText(_translate("MainWindow", "update", None))
        self.resetbutton.setText(_translate("MainWindow", "reset", None))
        self.categorizebox_m.setItemText(0, _translate("MainWindow", "焦点", None))
        self.categorizebox_m.setItemText(1, _translate("MainWindow", "国内", None))
        self.categorizebox_m.setItemText(2, _translate("MainWindow", "国际", None))
        self.categorizebox_m.setItemText(3, _translate("MainWindow", "体育", None))
        self.categorizebox_m.setItemText(4, _translate("MainWindow", "文娱", None))
        self.categorizebox_m.setItemText(5, _translate("MainWindow", "科技", None))
<<<<<<< HEAD
<<<<<<< HEAD
=======
        self.deletebutton.setText(_translate("MainWindow", "delete", None))
>>>>>>> dev3
        self.toolBar_2.setWindowTitle(_translate("MainWindow", "toolBar_2", None))
        self.menu01.setTitle(_translate("MainWindow", "01", None))
        self.menu02.setTitle(_translate("MainWindow", "02", None))
        self.menu03.setTitle(_translate("MainWindow", "03", None))
=======
        self.deletebutton.setText(_translate("MainWindow", "delete", None))
        self.label.setText(_translate("MainWindow", "请拖拽网页链接到此处：", None))
>>>>>>> stable
        self.menuAbout.setTitle(_translate("MainWindow", "About", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.newAction.setText(_translate("MainWindow", "&New", None))
        self.newAction.setShortcut(_translate("MainWindow", "Ctrl+N", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

