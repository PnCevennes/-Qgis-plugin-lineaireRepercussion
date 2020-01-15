# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settingsdialog_qt5.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_db_connexion_form(object):
    def setupUi(self, db_connexion_form):
        db_connexion_form.setObjectName("db_connexion_form")
        db_connexion_form.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(db_connexion_form)
        self.buttonBox.setGeometry(QtCore.QRect(50, 260, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayoutWidget = QtWidgets.QWidget(db_connexion_form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 20, 321, 191))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.txt_db_port = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txt_db_port.setObjectName("txt_db_port")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txt_db_port)
        self.lbl_db_port = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_db_port.setObjectName("lbl_db_port")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lbl_db_port)
        self.lbl_db_host = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_db_host.setObjectName("lbl_db_host")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_db_host)
        self.txt_db_dbname = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txt_db_dbname.setObjectName("txt_db_dbname")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txt_db_dbname)
        self.lbl_db_dbname = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_db_dbname.setObjectName("lbl_db_dbname")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lbl_db_dbname)
        self.lbl_db_user = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_db_user.setObjectName("lbl_db_user")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lbl_db_user)
        self.txt_db_user = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txt_db_user.setObjectName("txt_db_user")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.txt_db_user)
        self.txt_db_password = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txt_db_password.setInputMethodHints(QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText)
        self.txt_db_password.setObjectName("txt_db_password")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.txt_db_password)
        self.lbl_db_password = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_db_password.setObjectName("lbl_db_password")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.lbl_db_password)
        self.txt_db_host = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txt_db_host.setObjectName("txt_db_host")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_db_host)

        self.retranslateUi(db_connexion_form)
        self.buttonBox.accepted.connect(db_connexion_form.accept)
        self.buttonBox.rejected.connect(db_connexion_form.reject)
        QtCore.QMetaObject.connectSlotsByName(db_connexion_form)

    def retranslateUi(self, db_connexion_form):
        _translate = QtCore.QCoreApplication.translate
        db_connexion_form.setWindowTitle(_translate("db_connexion_form", "Connexion parameters"))
        self.lbl_db_port.setText(_translate("db_connexion_form", "Port"))
        self.lbl_db_host.setText(_translate("db_connexion_form", "Host"))
        self.lbl_db_dbname.setText(_translate("db_connexion_form", "Database"))
        self.lbl_db_user.setText(_translate("db_connexion_form", "User"))
        self.lbl_db_password.setText(_translate("db_connexion_form", "Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    db_connexion_form = QtWidgets.QDialog()
    ui = Ui_db_connexion_form()
    ui.setupUi(db_connexion_form)
    db_connexion_form.show()
    sys.exit(app.exec_())

