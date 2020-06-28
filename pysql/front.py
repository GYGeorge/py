# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'front.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from s_ui import *
from t_ui import *
from root import *
import pymysql
class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow,self).__init__()
        self.setupUi(self)
    def setupUi(self, MainWindow):
        self.conn = pymysql.connect(host='localhost',user='root',port=3306,password='496532343',db='curriculum')
        self.cur = self.conn.cursor()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(432, 403)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 85, 221, 41))
        self.lineEdit.setMaxLength(20)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 144, 221, 41))
        self.lineEdit_2.setToolTip("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 85, 91, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 144, 91, 41))
        self.label_2.setObjectName("label_2")
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 260, 141, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.loginButton)
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(60, 210, 91, 19))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(170, 210, 91, 19))
        self.checkBox_2.setObjectName("checkBox_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 432, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        font = QtGui.QFont() 
        #字体
        font.setFamily('仿宋')
        #加粗
        font.setBold(True) 
        #大小
        font.setPointSize(10) 
        font.setWeight(90) 
        self.label.setFont(font) 
        self.label.setLineWidth(0)
        self.label.setMidLineWidth(0)
        self.label.setText("<font color=%s>%s</font>" %('#000000', "用户名")) 
        self.label_2.setFont(font) 
        self.label_2.setLineWidth(0)
        self.label_2.setMidLineWidth(0)
        self.label_2.setText("<font color=%s>%s</font>" %('#000000', "密码"))
        # self.pushButton.setFont(font)
        # self.checkBox.setFont(font)
        # self.checkBox_2.setFont(font)
        # self.pushButton.setText("<font color=%s>%s</font>" %('#000000', "连接"))
        # self.checkBox.setText("<font color=%s>%s</font>" %('#000000', "老师"))
        # self.checkBox_2.setText("<font color=%s>%s</font>" %('#000000', "学生"))
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        # self.label.setText(_translate("MainWindow", "学号/职工号"))
        # self.label_2.setText(_translate("MainWindow", "密码"))
        self.pushButton.setText(_translate("MainWindow", "连接"))
        self.checkBox.setText(_translate("MainWindow", "老师"))
        self.checkBox_2.setText(_translate("MainWindow", "学生"))

    def loginButton(self):
        no = self.lineEdit.text()
        passwd = self.lineEdit_2.text()
        if self.checkBox_2.isChecked():
            sqlstrStudent = "select * from s where Sno = '%s'" % no
            self.cur.execute(sqlstrStudent) 
            if self.cur.fetchone():
                sqlstrStudent = "select * from s where Sno = '%s' and passwd = '%s'" % (no, passwd)
                self.cur.execute(sqlstrStudent)
                if self.cur.fetchone():
                    mywindow.setsno(no)
                    mywindow.show()
                    self.cur.close()
                    self.conn.close()
                    self.close()
                    return
                else: 
                    QtWidgets.QMessageBox.information(self,"Information",  
                                self.tr("密码错误"))
            else:
                QtWidgets.QMessageBox.information(self,"Information",  
                            self.tr("用户不存在"))

        if self.checkBox.isChecked():
            sqlstrTeacher = "select * from t where Tno = '%s'" % no
            self.cur.execute(sqlstrTeacher) 
            if self.cur.fetchone():
                sqlstrT = "select * from t where Tno = '%s' and Tpasswd = '%s'" % (no, passwd)
                self.cur.execute(sqlstrT)
                if self.cur.fetchone():
                    mywindowT.settno(no)
                    mywindowT.show()
                    self.cur.close()
                    self.conn.close()
                    self.close()
                    return
                else: 
                    QtWidgets.QMessageBox.information(self,"Information",  
                                self.tr("密码错误"))
            else:
                QtWidgets.QMessageBox.information(self,"Information",  
                            self.tr("用户不存在")) 
        
        if no == "root":
            if passwd == "abc":
                mywindowRoot.startUi()
                mywindowRoot.show()
                self.cur.close()
                self.conn.close()
                self.close()
            else:
                QtWidgets.QMessageBox.information(self,"Information",  
                            self.tr("请选择用户")) 
        else:
            QtWidgets.QMessageBox.information(self,"Information",  
                            self.tr("请输入学号或工号")) 

            
            
        
    def returnno(self):
        return self.lineEdit.text()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_MainWindow()
    mywindow = MyWindow()
    mywindowT = MyWindowTeacher()
    mywindowRoot = MyWindowROOT()
    window.show()
    sys.exit(app.exec_())