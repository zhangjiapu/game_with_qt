# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chapter1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class ChapterOneMainUI(object):
    def setupUi(self, MainWindow, nextWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(784, 754)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(150, 180, 495, 170))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridOne = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridOne.setContentsMargins(0, 0, 0, 0)
        self.gridOne.setObjectName("gridOne")
        self.btn11 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn11.setObjectName("btn11")
        self.btn11.clicked.connect(lambda: self.change_btn_color(self.btn11))
        self.gridOne.addWidget(self.btn11, 2, 0, 1, 1)
        self.btn6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn6.setObjectName("btn6")
        self.btn6.clicked.connect(lambda: self.change_btn_color(self.btn6))
        self.gridOne.addWidget(self.btn6, 1, 0, 1, 1)
        self.btn5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn5.setObjectName("btn5")
        self.btn5.clicked.connect(lambda: self.change_btn_color(self.btn5))
        self.gridOne.addWidget(self.btn5, 0, 4, 1, 1)
        self.btn1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn1.setFlat(False)
        self.btn1.setObjectName("btn1")
        self.btn1.clicked.connect(lambda: self.change_btn_color(self.btn1))
        self.gridOne.addWidget(self.btn1, 0, 0, 1, 1)
        self.btn3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn3.setObjectName("btn3")
        self.btn3.clicked.connect(lambda: self.change_btn_color(self.btn3))
        self.gridOne.addWidget(self.btn3, 0, 2, 1, 1)
        self.btn2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn2.setObjectName("btn2")
        self.btn2.clicked.connect(lambda: self.change_btn_color(self.btn2))
        self.gridOne.addWidget(self.btn2, 0, 1, 1, 1)
        self.btn4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn4.setObjectName("btn4")
        self.btn4.clicked.connect(lambda: self.change_btn_color(self.btn4))
        self.gridOne.addWidget(self.btn4, 0, 3, 1, 1)
        self.btn21 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn21.setObjectName("btn21")
        self.btn21.clicked.connect(lambda: self.change_btn_color(self.btn21))
        self.gridOne.addWidget(self.btn21, 4, 0, 1, 1)
        self.btn16 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn16.setObjectName("btn16")
        self.btn16.clicked.connect(lambda: self.change_btn_color(self.btn16))
        self.gridOne.addWidget(self.btn16, 3, 0, 1, 1)
        self.btn12 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn12.setObjectName("btn12")
        self.btn12.clicked.connect(lambda: self.change_btn_color(self.btn12))
        self.gridOne.addWidget(self.btn12, 2, 1, 1, 1)
        self.btn17 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn17.setObjectName("btn17")
        self.btn17.clicked.connect(lambda: self.change_btn_color(self.btn17))
        self.gridOne.addWidget(self.btn17, 3, 1, 1, 1)
        self.btn9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn9.setObjectName("btn9")
        self.btn9.clicked.connect(lambda: self.change_btn_color(self.btn9))
        self.gridOne.addWidget(self.btn9, 1, 3, 1, 1)
        self.btn7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn7.setObjectName("btn7")
        self.btn7.clicked.connect(lambda: self.change_btn_color(self.btn7))
        self.gridOne.addWidget(self.btn7, 1, 1, 1, 1)
        self.btn8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn8.setObjectName("btn8")
        self.btn8.clicked.connect(lambda: self.change_btn_color(self.btn8))
        self.gridOne.addWidget(self.btn8, 1, 2, 1, 1)
        self.btn10 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn10.setObjectName("btn10")
        self.btn10.clicked.connect(lambda: self.change_btn_color(self.btn10))
        self.gridOne.addWidget(self.btn10, 1, 4, 1, 1)
        self.btn14 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn14.setObjectName("btn14")
        self.btn14.clicked.connect(lambda: self.change_btn_color(self.btn14))
        self.gridOne.addWidget(self.btn14, 2, 3, 1, 1)
        self.btn22 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn22.setObjectName("btn22")
        self.btn22.clicked.connect(lambda: self.change_btn_color(self.btn22))
        self.gridOne.addWidget(self.btn22, 4, 1, 1, 1)
        self.btn18 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn18.setObjectName("btn18")
        self.btn18.clicked.connect(lambda: self.change_btn_color(self.btn18))
        self.gridOne.addWidget(self.btn18, 3, 2, 1, 1)
        self.btn23 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn23.setObjectName("btn23")
        self.btn23.clicked.connect(lambda: self.change_btn_color(self.btn23))
        self.gridOne.addWidget(self.btn23, 4, 2, 1, 1)
        self.btn13 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn13.setObjectName("btn13")
        self.btn13.clicked.connect(lambda: self.change_btn_color(self.btn13))
        self.gridOne.addWidget(self.btn13, 2, 2, 1, 1)
        self.btn19 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn19.setObjectName("btn19")
        self.btn19.clicked.connect(lambda: self.change_btn_color(self.btn19))
        self.gridOne.addWidget(self.btn19, 3, 3, 1, 1)
        self.btn15 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn15.setObjectName("btn15")
        self.btn15.clicked.connect(lambda: self.change_btn_color(self.btn15))
        self.gridOne.addWidget(self.btn15, 2, 4, 1, 1)
        self.btn20 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn20.setObjectName("btn20")
        self.btn20.clicked.connect(lambda: self.change_btn_color(self.btn20))
        self.gridOne.addWidget(self.btn20, 3, 4, 1, 1)
        self.btn24 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn24.setObjectName("btn24")
        self.btn24.clicked.connect(lambda: self.change_btn_color(self.btn24))
        self.gridOne.addWidget(self.btn24, 4, 3, 1, 1)
        self.btn25 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn25.setObjectName("btn25")
        self.btn25.clicked.connect(lambda: self.change_btn_color(self.btn25))
        self.gridOne.addWidget(self.btn25, 4, 4, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(281, 20, 151, 20))
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(150, 430, 495, 170))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridTwo = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridTwo.setContentsMargins(0, 0, 0, 0)
        self.gridTwo.setObjectName("gridTwo")
        self.btn36 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn36.setObjectName("btn36")
        self.btn36.clicked.connect(lambda: self.change_btn_color(self.btn36))
        self.gridTwo.addWidget(self.btn36, 2, 0, 1, 1)
        self.btn31 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn31.setObjectName("btn31")
        self.btn31.clicked.connect(lambda: self.change_btn_color(self.btn31))
        self.gridTwo.addWidget(self.btn31, 1, 0, 1, 1)
        self.btn30 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn30.setObjectName("btn30")
        self.btn30.clicked.connect(lambda: self.change_btn_color(self.btn30))
        self.gridTwo.addWidget(self.btn30, 0, 4, 1, 1)
        self.btn26 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn26.setFlat(False)
        self.btn26.setObjectName("btn26")
        self.btn26.clicked.connect(lambda: self.change_btn_color(self.btn26))
        self.gridTwo.addWidget(self.btn26, 0, 0, 1, 1)
        self.btn28 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn28.setObjectName("btn28")
        self.btn28.clicked.connect(lambda: self.change_btn_color(self.btn28))
        self.gridTwo.addWidget(self.btn28, 0, 2, 1, 1)
        self.btn27 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn27.setObjectName("btn27")
        self.btn27.clicked.connect(lambda: self.change_btn_color(self.btn27))
        self.gridTwo.addWidget(self.btn27, 0, 1, 1, 1)
        self.btn29 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn29.setObjectName("btn29")
        self.btn29.clicked.connect(lambda: self.change_btn_color(self.btn29))
        self.gridTwo.addWidget(self.btn29, 0, 3, 1, 1)
        self.btn46 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn46.setObjectName("btn46")
        self.btn46.clicked.connect(lambda: self.change_btn_color(self.btn46))
        self.gridTwo.addWidget(self.btn46, 4, 0, 1, 1)
        self.btn41 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn41.setObjectName("btn41")
        self.btn41.clicked.connect(lambda: self.change_btn_color(self.btn41))
        self.gridTwo.addWidget(self.btn41, 3, 0, 1, 1)
        self.btn37 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn37.setObjectName("btn37")
        self.btn37.clicked.connect(lambda: self.change_btn_color(self.btn37))
        self.gridTwo.addWidget(self.btn37, 2, 1, 1, 1)
        self.btn42 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn42.setObjectName("btn42")
        self.btn42.clicked.connect(lambda: self.change_btn_color(self.btn42))
        self.gridTwo.addWidget(self.btn42, 3, 1, 1, 1)
        self.btn34 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn34.setObjectName("btn34")
        self.btn34.clicked.connect(lambda: self.change_btn_color(self.btn34))
        self.gridTwo.addWidget(self.btn34, 1, 3, 1, 1)
        self.btn32 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn32.setObjectName("btn32")
        self.btn32.clicked.connect(lambda: self.change_btn_color(self.btn32))
        self.gridTwo.addWidget(self.btn32, 1, 1, 1, 1)
        self.btn33 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn33.setObjectName("btn33")
        self.btn33.clicked.connect(lambda: self.change_btn_color(self.btn33))
        self.gridTwo.addWidget(self.btn33, 1, 2, 1, 1)
        self.btn35 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn35.setObjectName("btn35")
        self.btn35.clicked.connect(lambda: self.change_btn_color(self.btn35))
        self.gridTwo.addWidget(self.btn35, 1, 4, 1, 1)
        self.btn39 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn39.setObjectName("btn39")
        self.btn39.clicked.connect(lambda: self.change_btn_color(self.btn39))
        self.gridTwo.addWidget(self.btn39, 2, 3, 1, 1)
        self.btn47 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn47.setObjectName("btn47")
        self.btn47.clicked.connect(lambda: self.change_btn_color(self.btn47))
        self.gridTwo.addWidget(self.btn47, 4, 1, 1, 1)
        self.btn43 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn43.setObjectName("btn43")
        self.btn43.clicked.connect(lambda: self.change_btn_color(self.btn43))
        self.gridTwo.addWidget(self.btn43, 3, 2, 1, 1)
        self.btn48 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn48.setObjectName("btn48")
        self.btn48.clicked.connect(lambda: self.change_btn_color(self.btn48))
        self.gridTwo.addWidget(self.btn48, 4, 2, 1, 1)
        self.btn38 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn38.setObjectName("btn38")
        self.btn38.clicked.connect(lambda: self.change_btn_color(self.btn38))
        self.gridTwo.addWidget(self.btn38, 2, 2, 1, 1)
        self.btn44 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn44.setObjectName("btn44")
        self.btn44.clicked.connect(lambda: self.change_btn_color(self.btn44))
        self.gridTwo.addWidget(self.btn44, 3, 3, 1, 1)
        self.btn40 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn40.setObjectName("btn40")
        self.btn40.clicked.connect(lambda: self.change_btn_color(self.btn40))
        self.gridTwo.addWidget(self.btn40, 2, 4, 1, 1)
        self.btn45 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn45.setObjectName("btn45")
        self.btn45.clicked.connect(lambda: self.change_btn_color(self.btn45))
        self.gridTwo.addWidget(self.btn45, 3, 4, 1, 1)
        self.btn49 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn49.setObjectName("btn49")
        self.btn49.clicked.connect(lambda: self.change_btn_color(self.btn49))
        self.gridTwo.addWidget(self.btn49, 4, 3, 1, 1)
        self.btn50 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn50.setObjectName("btn50")
        self.btn50.clicked.connect(lambda: self.change_btn_color(self.btn50))
        self.gridTwo.addWidget(self.btn50, 4, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 10, 141, 16))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(160, 40, 231, 16))
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 70, 231, 16))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(160, 100, 72, 15))
        self.label_5.setObjectName("label_5")

        self.btnCheck = QtWidgets.QPushButton(self.centralwidget)
        self.btnCheck.setGeometry(QtCore.QRect(260, 670, 93, 28))
        self.btnCheck.setObjectName("btnCheck")
        self.btnCheck.clicked.connect(lambda: self.check_pwd(MainWindow, nextWindow))

        MainWindow.setCentralWidget(self.centralwidget)
        self.btnReset = QtWidgets.QPushButton(self.centralwidget)
        self.btnReset.setGeometry(QtCore.QRect(410, 670, 93, 28))
        self.btnReset.setObjectName("btnReset")
        self.btnReset.clicked.connect(self.init_btn_color)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 784, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.init_btn_color()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def init_flag(self):
        # 第一个表的答案：51324
        self.grid1_btn5 = False
        self.grid1_btn8 = False
        self.grid1_btn11 = False
        self.grid1_btn19 = False
        self.grid1_btn22 = False

        # 第二个的答案：23541
        self.grid2_btn27 = False
        self.grid2_btn33 = False
        self.grid2_btn40 = False
        self.grid2_btn44 = False
        self.grid2_btn46 = False

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.btn11.setText(_translate("MainWindow", "1"))
        self.btn6.setText(_translate("MainWindow", "1"))
        self.btn5.setText(_translate("MainWindow", "5"))
        self.btn1.setText(_translate("MainWindow", "1"))
        self.btn3.setText(_translate("MainWindow", "3"))
        self.btn2.setText(_translate("MainWindow", "2"))
        self.btn4.setText(_translate("MainWindow", "4"))
        self.btn21.setText(_translate("MainWindow", "1"))
        self.btn16.setText(_translate("MainWindow", "1"))
        self.btn12.setText(_translate("MainWindow", "2"))
        self.btn17.setText(_translate("MainWindow", "2"))
        self.btn9.setText(_translate("MainWindow", "4"))
        self.btn7.setText(_translate("MainWindow", "2"))
        self.btn8.setText(_translate("MainWindow", "3"))
        self.btn10.setText(_translate("MainWindow", "5"))
        self.btn14.setText(_translate("MainWindow", "4"))
        self.btn22.setText(_translate("MainWindow", "2"))
        self.btn18.setText(_translate("MainWindow", "3"))
        self.btn23.setText(_translate("MainWindow", "3"))
        self.btn13.setText(_translate("MainWindow", "3"))
        self.btn19.setText(_translate("MainWindow", "4"))
        self.btn15.setText(_translate("MainWindow", "5"))
        self.btn20.setText(_translate("MainWindow", "5"))
        self.btn24.setText(_translate("MainWindow", "4"))
        self.btn25.setText(_translate("MainWindow", "5"))
        self.btn36.setText(_translate("MainWindow", "1"))
        self.btn31.setText(_translate("MainWindow", "1"))
        self.btn30.setText(_translate("MainWindow", "5"))
        self.btn26.setText(_translate("MainWindow", "1"))
        self.btn28.setText(_translate("MainWindow", "3"))
        self.btn27.setText(_translate("MainWindow", "2"))
        self.btn29.setText(_translate("MainWindow", "4"))
        self.btn46.setText(_translate("MainWindow", "1"))
        self.btn41.setText(_translate("MainWindow", "1"))
        self.btn37.setText(_translate("MainWindow", "2"))
        self.btn42.setText(_translate("MainWindow", "2"))
        self.btn34.setText(_translate("MainWindow", "4"))
        self.btn32.setText(_translate("MainWindow", "2"))
        self.btn33.setText(_translate("MainWindow", "3"))
        self.btn35.setText(_translate("MainWindow", "5"))
        self.btn39.setText(_translate("MainWindow", "4"))
        self.btn47.setText(_translate("MainWindow", "2"))
        self.btn43.setText(_translate("MainWindow", "3"))
        self.btn48.setText(_translate("MainWindow", "3"))
        self.btn38.setText(_translate("MainWindow", "3"))
        self.btn44.setText(_translate("MainWindow", "4"))
        self.btn40.setText(_translate("MainWindow", "5"))
        self.btn45.setText(_translate("MainWindow", "5"))
        self.btn49.setText(_translate("MainWindow", "4"))
        self.btn50.setText(_translate("MainWindow", "5"))
        self.label_2.setText(_translate("MainWindow", "Chapter1  双子"))
        self.label_4.setText(_translate("MainWindow", "密码就藏在下面的两幅图中"))
        self.label_3.setText(_translate("MainWindow", "找出密码后，在最下面check"))
        self.label_5.setText(_translate("MainWindow", "加油~"))
        self.btnCheck.setText(_translate("MainWindow", "check"))
        self.btnReset.setText(_translate("MainWindow", "reset"))

    def check_pwd(self, mainWindow, nextWindow):
        # 如果成功，则关闭当前窗口，开启下一个窗口
        if self.check_grid1() is True and self.check_grid2() is True:
            mainWindow.close()
            nextWindow.show()
        else:
            QtWidgets.QMessageBox.about(mainWindow, "提示信息", "不对哦，再试试~")

    def check_grid2(self):
        if self.grid2_btn27 is True \
                and self.grid2_btn33 is True \
                and self.grid2_btn40 is True \
                and self.grid2_btn44 is True \
                and self.grid2_btn46 is True:
            return True
        else:
            return False

    def check_grid1(self):
        if self.grid1_btn5 is True \
                and self.grid1_btn6 is True \
                and self.grid1_btn13 is True \
                and self.grid1_btn17 is True \
                and self.grid1_btn24 is True:
            return True
        else:
            return False

    def init_btn_color(self):
        # 第一个初始值是：23541
        self.change_btn_color(self.btn2)
        self.change_btn_color(self.btn8)
        self.change_btn_color(self.btn15)
        self.change_btn_color(self.btn19)
        self.change_btn_color(self.btn21)

        # 第二个初始值是：51324
        self.change_btn_color(self.btn30)
        self.change_btn_color(self.btn31)
        self.change_btn_color(self.btn38)
        self.change_btn_color(self.btn42)
        self.change_btn_color(self.btn49)

        self.init_flag()

    def change_btn_color(self, btn):
        if btn.objectName() in ["btn1", "btn2", "btn3", "btn4", "btn5"]:
            self.btn1.setStyleSheet("background-color:")
            self.btn2.setStyleSheet("background-color:")
            self.btn3.setStyleSheet("background-color:")
            self.btn4.setStyleSheet("background-color:")
            self.btn5.setStyleSheet("background-color:")
            btn.setStyleSheet("background-color:pink")
            if btn.objectName() == "btn5":
                self.grid1_btn5 = True
            else:
                self.grid1_btn5 = False

        elif btn.objectName() in ["btn6", "btn7", "btn8", "btn9", "btn10"]:
            self.btn6.setStyleSheet("background-color:")
            self.btn7.setStyleSheet("background-color:")
            self.btn8.setStyleSheet("background-color:")
            self.btn9.setStyleSheet("background-color:")
            self.btn10.setStyleSheet("background-color:")
            btn.setStyleSheet("background-color:pink")
            if btn.objectName() == "btn6":
                self.grid1_btn6 = True
            else:
                self.grid1_btn6 = False

        elif btn.objectName() in ["btn11", "btn12", "btn13", "btn14", "btn15"]:
            self.btn11.setStyleSheet("background-color:")
            self.btn12.setStyleSheet("background-color:")
            self.btn13.setStyleSheet("background-color:")
            self.btn14.setStyleSheet("background-color:")
            self.btn15.setStyleSheet("background-color:")
            btn.setStyleSheet("background-color:pink")
            if btn.objectName() == "btn13":
                self.grid1_btn13 = True
            else:
                self.grid1_btn13 = False

        elif btn.objectName() in ["btn16", "btn17", "btn18", "btn19", "btn20"]:
            self.btn16.setStyleSheet("background-color:")
            self.btn17.setStyleSheet("background-color:")
            self.btn18.setStyleSheet("background-color:")
            self.btn19.setStyleSheet("background-color:")
            self.btn20.setStyleSheet("background-color:")
            btn.setStyleSheet("background-color:pink")
            if btn.objectName() == "btn17":
                self.grid1_btn17 = True
            else:
                self.grid1_btn17 = False

        elif btn.objectName() in ["btn21", "btn22", "btn23", "btn24", "btn25"]:
            self.btn21.setStyleSheet("background-color:")
            self.btn22.setStyleSheet("background-color:")
            self.btn23.setStyleSheet("background-color:")
            self.btn24.setStyleSheet("background-color:")
            self.btn25.setStyleSheet("background-color:")
            btn.setStyleSheet("background-color:pink")
            if btn.objectName() == "btn24":
                self.grid1_btn24 = True
            else:
                self.grid1_btn24 = False

        elif btn.objectName() in ["btn26", "btn27", "btn28", "btn29", "btn30"]:
            self.btn26.setStyleSheet("background-color:")
            self.btn27.setStyleSheet("background-color:")
            self.btn28.setStyleSheet("background-color:")
            self.btn29.setStyleSheet("background-color:")
            self.btn30.setStyleSheet("background-color:")
            btn.setStyleSheet("background-color:pink")
            if btn.objectName() == "btn27":
                self.grid2_btn27 = True
            else:
                self.grid2_btn27 = False

        elif btn.objectName() in ["btn31", "btn32", "btn33", "btn34", "btn35"]:
            self.btn31.setStyleSheet("background-color:")
            self.btn32.setStyleSheet("background-color:")
            self.btn33.setStyleSheet("background-color:")
            self.btn34.setStyleSheet("background-color:")
            self.btn35.setStyleSheet("background-color:")
            btn.setStyleSheet("background-color:pink")
            if btn.objectName() == "btn33":
                self.grid2_btn33 = True
            else:
                self.grid2_btn33 = False

        elif btn.objectName() in ["btn36", "btn37", "btn38", "btn39", "btn40"]:
            self.btn36.setStyleSheet("background-color:")
            self.btn37.setStyleSheet("background-color:")
            self.btn38.setStyleSheet("background-color:")
            self.btn39.setStyleSheet("background-color:")
            self.btn40.setStyleSheet("background-color:")
            btn.setStyleSheet("background-color:pink")
            if btn.objectName() == "btn40":
                self.grid2_btn40 = True
            else:
                self.grid2_btn40 = False

        elif btn.objectName() in ["btn41", "btn42", "btn43", "btn44", "btn45"]:
            self.btn41.setStyleSheet("background-color:")
            self.btn42.setStyleSheet("background-color:")
            self.btn43.setStyleSheet("background-color:")
            self.btn44.setStyleSheet("background-color:")
            self.btn45.setStyleSheet("background-color:")
            btn.setStyleSheet("background-color:pink")
            if btn.objectName() == "btn44":
                self.grid2_btn44 = True
            else:
                self.grid2_btn44 = False

        elif btn.objectName() in ["btn46", "btn47", "btn48", "btn49", "btn50"]:
            self.btn46.setStyleSheet("background-color:")
            self.btn47.setStyleSheet("background-color:")
            self.btn48.setStyleSheet("background-color:")
            self.btn49.setStyleSheet("background-color:")
            self.btn50.setStyleSheet("background-color:")
            btn.setStyleSheet("background-color:pink")
            if btn.objectName() == "btn46":
                self.grid2_btn46 = True
            else:
                self.grid2_btn46 = False
        else:
            pass
