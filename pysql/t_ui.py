# /*
#  * @Author: gaoyuan 
#  * @Date: 2020-07-03 07:51:21 
#  * @Last Modified by:   gaoyuan 
#  * @Last Modified time: 2020-07-03 07:51:21 
#  */

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 't.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys
import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets


class MyWindowTeacher(QtWidgets.QMainWindow, QtWidgets.QTableWidget):

    tno = ""
    cno = ""

    def __init__(self):
        super().__init__()

    def getcno(self):
        cnostr = "SELECT Cno FROM t WHERE Tno = '%s' " % self.tno
        self.cur.execute(cnostr)
        for i in self.cur:
            for j in i:
                self.cno = str(j)

    def settno(self, ip):
        self.tno = ip
        self.setupUi(self)
        self.getcno()

    def setupUi(self, MainWindow):

        self.conn = pymysql.connect(host='localhost', user='root',
                                    port=3306, passwd='496532343',
                                    db='curriculum'
                                    )
        self.cur = self.conn.cursor()

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tab_4 = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_4.setGeometry(QtCore.QRect(40, 160, 701, 381))
        self.tab_4.setObjectName("tab_4")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_max = QtWidgets.QLabel(self.tab)
        self.label_max.setGeometry(QtCore.QRect(20, 20, 60, 31))
        self.label_max.setObjectName("label_max")
        self.max = QtWidgets.QTextBrowser(self.tab)
        self.max.setGeometry(QtCore.QRect(80, 20, 100, 31))
        self.max.setObjectName("max")
        self.label_min = QtWidgets.QLabel(self.tab)
        self.label_min.setGeometry(QtCore.QRect(200, 20, 60, 31))
        self.label_min.setObjectName("label_min")
        self.min = QtWidgets.QTextBrowser(self.tab)
        self.min.setGeometry(QtCore.QRect(260, 20, 100, 31))
        self.min.setObjectName("min")
        self.label_avg = QtWidgets.QLabel(self.tab)
        self.label_avg.setGeometry(QtCore.QRect(380, 20, 60, 31))
        self.label_avg.setObjectName("label_avg")
        self.avg = QtWidgets.QTextBrowser(self.tab)
        self.avg.setGeometry(QtCore.QRect(450, 20, 100, 31))
        self.avg.setObjectName("avg")

        self.searchallbutton = QtWidgets.QPushButton(self.tab)
        self.searchallbutton.setGeometry(QtCore.QRect(580, 20, 90, 31))
        self.result_out = QtWidgets.QTableWidget(self.tab)
        self.result_out.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)  # 不可编辑表格
        self.result_out.setGeometry(QtCore.QRect(20, 100, 650, 201))
        self.result_out.setObjectName("result_out")
        self.result_out.setColumnCount(2)
        self.result_out.resizeColumnsToContents()
        self.result_out.resizeRowsToContents()
        self.searchallbutton.clicked.connect(self.buttoncheckall)

        self.tab_4.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_sno2 = QtWidgets.QLabel(self.tab_2)
        self.label_sno2.setGeometry(QtCore.QRect(11, 20, 81, 31))
        self.label_sno2.setObjectName("label_sno2")
        self.edit_sno2 = QtWidgets.QLineEdit(self.tab_2)
        self.edit_sno2.setGeometry(QtCore.QRect(90, 20, 241, 31))
        self.edit_sno2.setObjectName("edit_sno2")
        self.line_2 = QtWidgets.QFrame(self.tab_2)
        self.line_2.setGeometry(QtCore.QRect(0, 70, 681, 21))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.textshowgrade = QtWidgets.QTextBrowser(self.tab_2)
        self.textshowgrade.setGeometry(QtCore.QRect(130, 120, 131, 51))
        self.textshowgrade.setObjectName("textshowgrade")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(50, 120, 72, 51))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(50, 190, 72, 51))
        self.label_8.setObjectName("label_8")
        self.edit_changegrade = QtWidgets.QLineEdit(self.tab_2)
        self.edit_changegrade.setGeometry(QtCore.QRect(130, 190, 131, 51))
        self.edit_changegrade.setObjectName("edit_changegrade")
        self.changegradebutton = QtWidgets.QPushButton(self.tab_2)
        self.changegradebutton.setGeometry(QtCore.QRect(290, 190, 141, 51))
        self.changegradebutton.setObjectName("changegradebutton")
        self.changegradebutton.clicked.connect(self.buttonupdategrade)
        self.showgradebutton = QtWidgets.QPushButton(self.tab_2)
        self.showgradebutton.setGeometry(QtCore.QRect(290, 120, 141, 51))
        self.showgradebutton.setObjectName("showgradebutton")
        self.showgradebutton.clicked.connect(self.buttonshowgrade)
        self.tab_4.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_4 = QtWidgets.QLabel(self.tab_3)
        self.label_4.setGeometry(QtCore.QRect(60, 70, 91, 41))
        self.label_4.setObjectName("label_4")
        self.oriPW = QtWidgets.QLineEdit(self.tab_3)
        self.oriPW.setGeometry(QtCore.QRect(160, 70, 351, 41))
        self.oriPW.setObjectName("oriPW")
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        self.label_5.setGeometry(QtCore.QRect(60, 140, 91, 41))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab_3)
        self.label_6.setGeometry(QtCore.QRect(60, 200, 91, 41))
        self.label_6.setObjectName("label_6")
        self.changePW = QtWidgets.QLineEdit(self.tab_3)
        self.changePW.setGeometry(QtCore.QRect(160, 140, 351, 41))
        self.changePW.setObjectName("changePW")
        self.confirmPW = QtWidgets.QLineEdit(self.tab_3)
        self.confirmPW.setGeometry(QtCore.QRect(160, 200, 351, 41))
        self.confirmPW.setObjectName("confirmPW")
        self.changePWbutton = QtWidgets.QPushButton(self.tab_3)
        self.changePWbutton.setGeometry(QtCore.QRect(260, 290, 151, 51))
        self.changePWbutton.setObjectName("changePWbutton")
        self.changePWbutton.clicked.connect(self.buttonchangePW)

        self.tab_4.addTab(self.tab_3, "")
        self.label_tno = QtWidgets.QLabel(self.centralwidget)
        self.label_tno.setGeometry(QtCore.QRect(60, 20, 72, 31))
        self.label_tno.setObjectName("label_tno")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(130, 20, 391, 31))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_2.setText(self.tno)

        self.label_tname = QtWidgets.QLabel(self.centralwidget)
        self.label_tname.setGeometry(QtCore.QRect(60, 80, 72, 31))
        self.label_tname.setObjectName("label_tname")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(130, 80, 141, 31))
        self.textBrowser_3.setObjectName("textBrowser_3")
        st1 = "select Tname from t where Tno = '%s'" % self.tno
        self.cur.execute(st1)
        for i in self.cur:
            for j in i:
                settext3 = str(j)
        self.textBrowser_3.setText(settext3)

        self.label_class = QtWidgets.QLabel(self.centralwidget)
        self.label_class.setGeometry(QtCore.QRect(310, 80, 72, 31))
        self.label_class.setObjectName("label_class")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_4.setGeometry(QtCore.QRect(380, 80, 141, 31))
        self.textBrowser_4.setObjectName("textBrowser_4")
        st2 = "select Cname from t,c where Tno = '%s' and t.Cno = c.Cno" % self.tno
        self.cur.execute(st2)
        for i in self.cur:
            for j in i:
                settext4 = str(j)
        self.textBrowser_4.setText(settext4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tab_4.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_max.setText(_translate("MainWindow", "最高分"))
        self.label_min.setText(_translate("MainWindow", "最低分"))
        self.searchallbutton.setText(_translate("MainWindow", "查询"))
        self.tab_4.setTabText(self.tab_4.indexOf(
            self.tab), _translate("MainWindow", "查看成绩"))
        self.label_sno2.setText(_translate("MainWindow", "学号"))
        self.label_7.setText(_translate("MainWindow", "成绩"))
        self.label_8.setText(_translate("MainWindow", "修改成绩"))
        self.changegradebutton.setText(_translate("MainWindow", "确认修改/添加"))
        self.showgradebutton.setText(_translate("MainWindow", "显示成绩"))
        self.tab_4.setTabText(self.tab_4.indexOf(
            self.tab_2), _translate("MainWindow", "修改成绩"))
        self.label_4.setText(_translate("MainWindow", "原密码"))
        self.label_5.setText(_translate("MainWindow", "修改密码"))
        self.label_6.setText(_translate("MainWindow", "确认密码"))
        self.changePWbutton.setText(_translate("MainWindow", "确认修改"))
        self.tab_4.setTabText(self.tab_4.indexOf(
            self.tab_3), _translate("MainWindow", "修改密码"))
        self.label_tno.setText(_translate("MainWindow", "职工号"))
        self.label_tname.setText(_translate("MainWindow", "姓名"))
        self.label_class.setText(_translate("MainWindow", "课程"))
        self.label_avg.setText(_translate("MainWindow", "平均成绩"))

    def buttonshowgrade(self):
        sno = self.edit_sno2.text()
        if sno == "":
            QtWidgets.QMessageBox.information(
                self, "Information", self.tr("请输入学号"))
            return
        selectstr = "SELECT Grade FROM sc WHERE sc.Cno = '%s' AND sc.Sno = '%s'" % (
            self.cno, sno)
        self.cur.execute(selectstr)
        for i in self.cur:
            for j in i:
                self.textshowgrade.setText(str(j))

    def buttonupdategrade(self):
        sno = self.edit_sno2.text()
        if self.edit_changegrade.text() == "":
            QtWidgets.QMessageBox.information(
                self, "Information", self.tr("请输入成绩"))
        else:
            updatestr = "UPDATE sc SET Grade = '%d' WHERE Cno = '%s' AND Sno = '%s' " % (
                int(self.edit_changegrade.text()), self.cno, sno)
            self.cur.execute(updatestr)
            self.conn.commit()
        self.edit_changegrade.clear()
        self.textshowgrade.clear()

    def buttoncheckall(self):
        maxstr = "SELECT MAX(Grade) FROM sc WHERE Cno = '%s'" % self.cno
        minstr = "SELECT MIN(Grade) FROM sc WHERE Cno = '%s'" % self.cno
        avgstr = "SELECT AVG(Grade) FROM sc WHERE Cno = '%s'" % self.cno
        self.cur.execute(maxstr)
        for i in self.cur:
            for j in i:
                self.max.setText(str(j))
        self.cur.execute(minstr)
        for i in self.cur:
            for j in i:
                self.min.setText(str(j))
        self.cur.execute(avgstr)
        for i in self.cur:
            for j in i:
                self.avg.setText(str(j))
        countstr = "SELECT COUNT(Grade) FROM sc WHERE Cno = '%s'" % self.cno
        self.cur.execute(countstr)
        for i in self.cur:
            for j in i:
                self.result_out.setRowCount(int(j))
        allstr = "SELECT Sno,Grade FROM sc WHERE Cno = '%s'" % self.cno
        self.cur.execute(allstr)
        k = 0
        self.result_out.clearContents()
        for i in self.cur:
            # print("----------",i)
            w = 0
            for j in i:
                newItem = QtWidgets.QTableWidgetItem(str(j))
                self.result_out.setItem(k, w, newItem)
                w += 1
            k += 1

    def buttonchangePW(self):
        if self.changePW.text() == self.confirmPW.text():
            pw = self.confirmPW.text()
            sqlstr = "select * from t where Tno = '%s' and Tpasswd = '%s'" % (
                self.tno, self.oriPW.text())
            self.cur.execute(sqlstr)
            if self.cur.fetchone():
                sqlstr = " update t set Tpasswd = '%s' where Tno = '%s'" % (
                    pw, self.tno)
                self.cur.execute(sqlstr)
                self.conn.commit()
                sqlcheck = "select * from t where Tno = '%s' and Tpasswd = '%s'" % (
                    self.tno, pw)
                self.cur.execute(sqlcheck)
                if self.cur.fetchone():
                    self.confirmPW.clear()
                    self.changePW.clear()
                    self.oriPW.clear()
                    QtWidgets.QMessageBox.information(
                        self, "Information", self.tr("修改成功"))
            else:
                self.confirmPW.clear()
                self.changePW.clear()
                self.oriPW.clear()
                QtWidgets.QMessageBox.information(
                    self, "Information", self.tr("密码错误!"))
        else:
            self.confirmPW.clear()
            self.changePW.clear()
            self.oriPW.clear()
            QtWidgets.QMessageBox.information(
                self, "Information", self.tr("两次密码不一致!"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myshow = MyWindowTeacher()
    Tno = "t1"
    myshow.settno(Tno)
    myshow.show()
    sys.exit(app.exec_())
