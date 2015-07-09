# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settingsdialog.ui'
#
# Created: Thu Jul  9 16:23:58 2015
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

class Ui_db_connexion_form(object):
    def setupUi(self, db_connexion_form):
        db_connexion_form.setObjectName(_fromUtf8("db_connexion_form"))
        db_connexion_form.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(db_connexion_form)
        self.buttonBox.setGeometry(QtCore.QRect(50, 260, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.formLayoutWidget = QtGui.QWidget(db_connexion_form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 20, 321, 191))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.txt_db_port = QtGui.QLineEdit(self.formLayoutWidget)
        self.txt_db_port.setObjectName(_fromUtf8("txt_db_port"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.txt_db_port)
        self.lbl_db_port = QtGui.QLabel(self.formLayoutWidget)
        self.lbl_db_port.setObjectName(_fromUtf8("lbl_db_port"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.lbl_db_port)
        self.lbl_db_host = QtGui.QLabel(self.formLayoutWidget)
        self.lbl_db_host.setObjectName(_fromUtf8("lbl_db_host"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.lbl_db_host)
        self.txt_db_dbname = QtGui.QLineEdit(self.formLayoutWidget)
        self.txt_db_dbname.setObjectName(_fromUtf8("txt_db_dbname"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.txt_db_dbname)
        self.lbl_db_dbname = QtGui.QLabel(self.formLayoutWidget)
        self.lbl_db_dbname.setObjectName(_fromUtf8("lbl_db_dbname"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.lbl_db_dbname)
        self.lbl_db_user = QtGui.QLabel(self.formLayoutWidget)
        self.lbl_db_user.setObjectName(_fromUtf8("lbl_db_user"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.lbl_db_user)
        self.txt_db_user = QtGui.QLineEdit(self.formLayoutWidget)
        self.txt_db_user.setObjectName(_fromUtf8("txt_db_user"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.txt_db_user)
        self.txt_db_password = QtGui.QLineEdit(self.formLayoutWidget)
        self.txt_db_password.setInputMethodHints(QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText)
        self.txt_db_password.setObjectName(_fromUtf8("txt_db_password"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.txt_db_password)
        self.lbl_db_password = QtGui.QLabel(self.formLayoutWidget)
        self.lbl_db_password.setObjectName(_fromUtf8("lbl_db_password"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.lbl_db_password)
        self.txt_db_host = QtGui.QLineEdit(self.formLayoutWidget)
        self.txt_db_host.setObjectName(_fromUtf8("txt_db_host"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.txt_db_host)

        self.retranslateUi(db_connexion_form)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), db_connexion_form.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), db_connexion_form.reject)
        QtCore.QMetaObject.connectSlotsByName(db_connexion_form)

    def retranslateUi(self, db_connexion_form):
        db_connexion_form.setWindowTitle(_translate("db_connexion_form", "Connexion parameters", None))
        self.lbl_db_port.setText(_translate("db_connexion_form", "Port", None))
        self.lbl_db_host.setText(_translate("db_connexion_form", "Host", None))
        self.lbl_db_dbname.setText(_translate("db_connexion_form", "Database", None))
        self.lbl_db_user.setText(_translate("db_connexion_form", "User", None))
        self.lbl_db_password.setText(_translate("db_connexion_form", "Password", None))

