# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Documents\python\pyqt\demos\ericdemo\news\setting.ui'
#
# Created: Sun Aug 03 04:25:19 2014
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(345, 283)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(100, 240, 156, 23))
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.layoutWidget = QtGui.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(31, 11, 291, 221))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.hostedit = QtGui.QLineEdit(self.layoutWidget)
        self.hostedit.setObjectName(_fromUtf8("hostedit"))
        self.gridLayout.addWidget(self.hostedit, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.portedit = QtGui.QLineEdit(self.layoutWidget)
        self.portedit.setObjectName(_fromUtf8("portedit"))
        self.gridLayout.addWidget(self.portedit, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.databaseedit = QtGui.QLineEdit(self.layoutWidget)
        self.databaseedit.setObjectName(_fromUtf8("databaseedit"))
        self.gridLayout.addWidget(self.databaseedit, 2, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.usernameedit = QtGui.QLineEdit(self.layoutWidget)
        self.usernameedit.setObjectName(_fromUtf8("usernameedit"))
        self.gridLayout.addWidget(self.usernameedit, 3, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.layoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.pwedit = QtGui.QLineEdit(self.layoutWidget)
        self.pwedit.setObjectName(_fromUtf8("pwedit"))
        self.gridLayout.addWidget(self.pwedit, 4, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.layoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.pathEdit = QtGui.QLineEdit(self.layoutWidget)
        self.pathEdit.setObjectName(_fromUtf8("pathEdit"))
        self.gridLayout.addWidget(self.pathEdit, 5, 1, 1, 1)
        self.label.setBuddy(self.hostedit)
        self.label_2.setBuddy(self.portedit)
        self.label_3.setBuddy(self.databaseedit)
        self.label_4.setBuddy(self.usernameedit)
        self.label_5.setBuddy(self.pwedit)
        self.label_6.setBuddy(self.pathEdit)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "host:", None))
        self.hostedit.setText(_translate("Dialog", "localhost", None))
        self.label_2.setText(_translate("Dialog", "port:", None))
        self.portedit.setText(_translate("Dialog", "3306", None))
        self.label_3.setText(_translate("Dialog", "database:", None))
        self.databaseedit.setText(_translate("Dialog", "test", None))
        self.label_4.setText(_translate("Dialog", "username:", None))
        self.usernameedit.setText(_translate("Dialog", "root", None))
        self.label_5.setText(_translate("Dialog", "password:", None))
        self.pwedit.setText(_translate("Dialog", "123456", None))
        self.label_6.setText(_translate("Dialog", "图片路径", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

