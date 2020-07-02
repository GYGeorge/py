# /*
#  * @Author: gaoyuan 
#  * @Date: 2020-07-03 07:50:20 
#  * @Last Modified by:   gaoyuan 
#  * @Last Modified time: 2020-07-03 07:50:20 
#  */

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 's.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys
import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets


class MyWindow(QtWidgets.QMainWindow, QtWidgets.QTabWidget):

    sno = ""

    def __init__(self):
        super().__init__()

    def setsno(self, ip):
        self.sno = ip
        self.setupUi(self)

    def setupUi(self, MainWindow):
        """
        登入后初始化
        """
        self.conn = pymysql.connect(
            host='localhost', user='root', port=3306, password='496532343', db='curriculum')
        self.cur = self.conn.cursor()
        self.cname = ""
        self.sqlstring_info = "select * from s where Sno = '%s' " % self.sno

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 131, 41))
        self.label.setIndent(60)
        self.label.setObjectName("label")
        self.label_courses = QtWidgets.QLabel(self.centralwidget)
        self.label_courses.setGeometry(QtCore.QRect(0, 90, 131, 41))
        self.label_courses.setTextFormat(QtCore.Qt.AutoText)
        self.label_courses.setIndent(60)
        self.label_courses.setOpenExternalLinks(False)
        self.label_courses.setObjectName("label_courses")
        self.gradesquery = QtWidgets.QPushButton(self.centralwidget)
        self.gradesquery.setGeometry(QtCore.QRect(0, 131, 801, 41))
        self.gradesquery.setObjectName("gradesquery")
        self.gradesquery.clicked.connect(self.buttonTest)
        self.showinfo = QtWidgets.QPushButton(self.centralwidget)
        self.showinfo.setObjectName("showinfo")
        self.showinfo.setGeometry(QtCore.QRect(560, 90, 122, 41))
        self.showinfo.clicked.connect(self.buttonshow)
        self.clearinfo = QtWidgets.QPushButton(self.centralwidget)
        self.clearinfo.setObjectName("clearinfo")
        self.clearinfo.setGeometry(QtCore.QRect(679, 90, 122, 41))
        self.clearinfo.clicked.connect(self.buttonclear)
        self.coursesfillin = QtWidgets.QLineEdit(self.centralwidget)
        self.coursesfillin.setGeometry(QtCore.QRect(130, 90, 431, 41))
        self.coursesfillin.setObjectName("coursesfillin")
        self.Sno = QtWidgets.QLineEdit(self.centralwidget)
        self.Sno.setGeometry(QtCore.QRect(130, 0, 671, 41))
        self.Sno.setObjectName("Sno")
        self.Sno.setText(self.sno)
        self.info = QtWidgets.QLineEdit(self.centralwidget)
        self.info.setGeometry(QtCore.QRect(130, 40, 671, 51))
        self.info.setObjectName("info")
        settext = ""
        self.info.setText(settext)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 50, 131, 41))
        self.label_2.setIndent(60)
        self.label_2.setObjectName("label_2")

        self.Originallabel = QtWidgets.QLabel(self.centralwidget)
        self.Originallabel.setGeometry(QtCore.QRect(0, 180, 130, 41))
        self.changelabel = QtWidgets.QLabel(self.centralwidget)
        self.changelabel.setGeometry(QtCore.QRect(0, 220, 130, 41))
        self.confirmlabel = QtWidgets.QLabel(self.centralwidget)
        self.confirmlabel.setGeometry(QtCore.QRect(0, 260, 130, 41))
        self.OriginalPW = QtWidgets.QLineEdit(self.centralwidget)
        self.changePW = QtWidgets.QLineEdit(self.centralwidget)
        self.confirmPW = QtWidgets.QLineEdit(self.centralwidget)
        self.OriginalPW.setGeometry(QtCore.QRect(140, 190, 130, 21))
        self.changePW.setGeometry(QtCore.QRect(140, 230, 130, 21))
        self.confirmPW.setGeometry(QtCore.QRect(140, 270, 130, 21))
        self.change = QtWidgets.QPushButton(self.centralwidget)
        self.change.setGeometry(QtCore.QRect(140, 310, 100, 30))
        self.change.clicked.connect(self.buttonchange)

        self.OriginalPW.setToolTip("")
        self.OriginalPW.setEchoMode(QtWidgets.QLineEdit.Password)
        self.changePW.setToolTip("")
        self.changePW.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmPW.setToolTip("")
        self.confirmPW.setEchoMode(QtWidgets.QLineEdit.Password)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "学号"))
        self.label_courses.setText(_translate("MainWindow", "课程"))
        self.gradesquery.setText(_translate("MainWindow", "查询成绩"))
        self.clearinfo.setText(_translate("MainWindow", "清除"))
        self.showinfo.setText(_translate("MainWindow", "显示信息"))
        self.coursesfillin.setText(_translate("MainWindow", "请输入课程名"))
        self.label_2.setText(_translate("MainWindow", "显示"))
        self.Originallabel.setText(_translate("MainWindow", "原密码"))
        self.confirmlabel.setText(_translate("MainWindow", "确认密码"))
        self.changelabel.setText(_translate("MainWindow", "新密码"))
        self.change.setText(_translate("MainWindow", "修改密码"))

    def buttonshow(self):
        settext = ""
        self.cur.execute(self.sqlstring_info)
        for i in self.cur:
            for j in i:
                settext += " " + str(j)
        self.info.setText(settext)

    def buttonclear(self):
        self.info.clear()

    def buttonExit(self):
        self.conn.commit()
        self.cur.close()
        self.conn.close()
        self.close()

    def buttonTest(self):
        self.cname = self.coursesfillin.text()
        if self.cname == "请输入课程名":
            QtWidgets.QMessageBox.information(self, "Information",
                                              self.tr("请输入课程名!"))

        sqlcourse = "select sc.Grade from sc,c where sc.Sno = '%s' and c.Cno = sc.Cno and c.Cname = '%s'" % (
            self.sno, self.cname)
        self.cur.execute(sqlcourse)
        for i in self.cur:
            for j in i:
                self.info.setText(str(j))

    def buttonchange(self):
        if self.changePW.text() == self.confirmPW.text():
            pw = self.confirmPW.text()
            sqlstr = "select * from s where Sno = '%s' and passwd = '%s'" % (
                self.sno, self.OriginalPW.text())
            self.cur.execute(sqlstr)
            if self.cur.fetchone():
                sqlstr = " update s set passwd = '%s' where Sno = '%s'" % (
                    pw, self.sno)
                self.cur.execute(sqlstr)
                self.conn.commit()
                sqlcheck = "select * from s where Sno = '%s' and passwd = '%s'" % (
                    self.sno, pw)
                self.cur.execute(sqlcheck)
                if self.cur.fetchone():
                    self.confirmPW.clear()
                    self.changePW.clear()
                    self.OriginalPW.clear()
                    QtWidgets.QMessageBox.information(
                        self, "Information", self.tr("修改成功"))
            else:
                self.confirmPW.clear()
                self.changePW.clear()
                self.OriginalPW.clear()
                QtWidgets.QMessageBox.information(
                    self, "Information", self.tr("密码错误!"))
        else:
            self.confirmPW.clear()
            self.changePW.clear()
            self.OriginalPW.clear()
            QtWidgets.QMessageBox.information(
                self, "Information", self.tr("两次密码不一致!"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myshow = MyWindow()
    myshow.setsno(ip="161700001")
    myshow.show()
    sys.exit(app.exec_())
