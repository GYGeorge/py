# /*
#  * @Author: gaoyuan
#  * @Date: 2020-07-03 07:50:40
#  * @Last Modified by:   gaoyuan
#  * @Last Modified time: 2020-07-03 07:50:40
#  */

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'root.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import pymysql
import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class MyWindowROOT(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

    def startUi(self):

        self.conn = pymysql.connect(host='localhost', user='root',
                                    port=3306, passwd='496532343',
                                    db='curriculum'
                                    )
        self.cur = self.conn.cursor()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily("Papyrus")
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_root = QtWidgets.QLabel(self.centralwidget)
        self.label_root.setGeometry(QtCore.QRect(20, 220, 121, 81))
        font = QtGui.QFont()
        font.setFamily("Onyx")
        font.setPointSize(48)
        self.label_root.setFont(font)
        self.label_root.setObjectName("label_root")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(130, 40, 631, 471))
        font = QtGui.QFont()
        font.setFamily("华文仿宋")
        font.setPointSize(14)
        self.tabWidget.setFont(font)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setElideMode(QtCore.Qt.ElideLeft)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_sno = QtWidgets.QLabel(self.tab_2)
        self.label_sno.setGeometry(QtCore.QRect(20, 30, 61, 31))
        self.label_sno.setObjectName("label_sno")
        self.lineEdit_sno = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_sno.setGeometry(QtCore.QRect(90, 30, 141, 31))
        self.lineEdit_sno.setObjectName("lineEdit_sno")
        self.pushButton_Ssearch = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_Ssearch.setGeometry(QtCore.QRect(270, 30, 111, 41))
        self.pushButton_Ssearch.setObjectName("pushButton_Ssearch")
        self.textBrowser_S = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser_S.setGeometry(QtCore.QRect(30, 150, 561, 131))
        self.textBrowser_S.setObjectName("textBrowser_S")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_tno = QtWidgets.QLabel(self.tab)
        self.label_tno.setGeometry(QtCore.QRect(20, 30, 81, 31))
        self.label_tno.setObjectName("label_tno")
        self.lineEdit_tno = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_tno.setGeometry(QtCore.QRect(110, 30, 141, 31))
        self.lineEdit_tno.setObjectName("lineEdit_tno")
        self.pushButton_Tsearch = QtWidgets.QPushButton(self.tab)
        self.pushButton_Tsearch.setGeometry(QtCore.QRect(290, 30, 111, 41))
        self.pushButton_Tsearch.setObjectName("pushButton_Tsearch")
        self.textBrowser_T = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser_T.setGeometry(QtCore.QRect(30, 161, 561, 131))
        self.textBrowser_T.setObjectName("textBrowser_T")
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.textEdit_inputsql = QtWidgets.QTextEdit(self.tab_3)
        self.textEdit_inputsql.setGeometry(QtCore.QRect(40, 70, 541, 87))
        self.textEdit_inputsql.setObjectName("textEdit_inputsql")
        self.label_inputsql = QtWidgets.QLabel(self.tab_3)
        self.label_inputsql.setGeometry(QtCore.QRect(40, 20, 151, 41))
        font = QtGui.QFont()
        font.setFamily("华文仿宋")
        self.label_inputsql.setFont(font)
        self.label_inputsql.setObjectName("label_inputsql")
        self.textBrowser_result = QtWidgets.QTextBrowser(self.tab_3)
        self.textBrowser_result.setGeometry(QtCore.QRect(40, 221, 541, 181))
        self.textBrowser_result.setObjectName("textBrowser_result")
        self.label_result = QtWidgets.QLabel(self.tab_3)
        self.label_result.setGeometry(QtCore.QRect(40, 180, 111, 31))
        self.label_result.setObjectName("label_result")
        self.pushButtonsql = QtWidgets.QPushButton(self.tab_3)
        self.pushButtonsql.setGeometry(QtCore.QRect(420, 27, 161, 31))
        self.pushButtonsql.setObjectName("pushButtonsql")
        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.pushButton_Ssearch.clicked.connect(self.buttonS)
        self.pushButton_Tsearch.clicked.connect(self.buttonT)
        self.pushButtonsql.clicked.connect(self.buttonSQL)
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_root.setText(_translate("MainWindow", "ROOT"))
        self.label_sno.setText(_translate("MainWindow", "学号"))
        self.pushButton_Ssearch.setText(_translate("MainWindow", "查找"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab_2), _translate("MainWindow", "查看学生信息"))
        self.label_tno.setText(_translate("MainWindow", "职工号"))
        self.pushButton_Tsearch.setText(_translate("MainWindow", "查找"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab), _translate("MainWindow", "查看教师信息"))
        self.label_inputsql.setText(_translate("MainWindow", "输入sql"))
        self.label_result.setText(_translate("MainWindow", "结果"))
        self.pushButtonsql.setText(_translate("MainWindow", "提交"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab_3), _translate("MainWindow", "sql语句"))

    def buttonS(self):
        sno = self.lineEdit_sno.text()
        sqlstr = "SELECT Sno,Sname,Ssex,Sage,Sdept FROM s WHERE Sno = '%s'" % sno
        self.cur.execute(sqlstr)
        self.textBrowser_S.clear()
        back = self.cur.fetchone()
        if back != None:
            for i in back:
                self.textBrowser_S.append(str(i))
        else:
            QtWidgets.QMessageBox.information(self, "Information",
                                              self.tr("输入错误"))

    def buttonT(self):
        tno = self.lineEdit_tno.text()
        sqlstr = "SELECT t.Tno,c.Cname,t.Tname FROM t,c WHERE  t.Tno = '%s'" % tno

        self.cur.execute(sqlstr)
        self.textBrowser_T.clear()
        back = self.cur.fetchone()
        if back != None:
            for i in back:
                self.textBrowser_T.append(str(i))
        else:
            QtWidgets.QMessageBox.information(self, "Information",
                                              self.tr("输入错误"))

    def buttonSQL(self):
        sqlstr = self.textEdit_inputsql.toPlainText()
        try:
            self.cur.execute(sqlstr)
            for i in self.cur.fetchone():
                self.textBrowser_result.append(str(i))
            self.conn.commit()
        except pymysql.Error as e:
            self.textEdit_inputsql.clear()
            self.textBrowser_result.setText(str(e))
            # QtWidgets.QMessageBox.information(self,"Information",self.tr("两次密码不一致!"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myshow = MyWindowROOT()

    myshow.startUi()
    myshow.show()
    sys.exit(app.exec_())
