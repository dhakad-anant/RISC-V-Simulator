# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'finalDesginFIle.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from main import *


class Ui_MainWindow(object):
    def regUpdateGUI(self):
        
        self.reg1.setText('x21:' +str(reg[21]))
        self.reg2.setText('x6:' +str(reg[6]))
        self.reg3.setText('x22:' +str(reg[22]))
        self.reg4.setText('x7:' +str(reg[7]))
        self.reg5.setText('x23:' +str(reg[23]))
        self.reg6.setText('x0:' +str(reg[0]))
        self.reg7.setText('x1:' +str(reg[1]))
        self.reg8.setText('x16:' +str(reg[16]))
        self.reg9.setText('x17:' +str(reg[17]))
        self.reg10.setText('x2:' +str(reg[2]))
        self.reg11.setText('x18:' +str(reg[18]))
        self.reg12.setText('x3:' +str(reg[3]))
        self.reg13.setText('x19:' +str(reg[19]))
        self.reg14.setText('x4:' +str(reg[4]))
        self.reg15.setText('x20:' +str(reg[20]))
        self.reg16.setText('x5:' +str(reg[5]))
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1173, 881)
        MainWindow.setStyleSheet("background:rgb(44, 44, 44)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(570, 40, 2, 1061))
        self.line_2.setStyleSheet("background:white")
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(890, 623, 247, 36))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("background:rgb(0, 255, 127)rgb(130, 130, 130);color:white")
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(890, 229, 247, 37))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background:rgb(0, 255, 127)rgb(130, 130, 130);color:white")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(890, 185, 247, 37))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background:rgb(0, 255, 127)rgb(130, 130, 130);color:white")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(890, 360, 247, 37))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background:rgb(0, 255, 127)rgb(130, 130, 130);color:white")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(890, 448, 247, 36))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background:rgb(0, 255, 127)rgb(130, 130, 130);color:white")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(890, 491, 247, 37))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background:rgb(0, 255, 127)rgb(130, 130, 130);color:white")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(890, 316, 247, 37))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background:rgb(0, 255, 127)rgb(130, 130, 130);color:white")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(890, 54, 247, 37))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_1.setFont(font)
        self.label_1.setStyleSheet("background:rgb(0, 255, 127)rgb(130, 130, 130);color:white")
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName("label_1")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(890, 580, 247, 37))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background:rgb(0, 255, 127)rgb(130, 130, 130);color:white")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(890, 98, 247, 36))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background:rgb(0, 255, 127)rgb(130, 130, 130);color:white")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(890, 404, 247, 37))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background:rgb(0, 255, 127)rgb(130, 130, 130);color:white")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(890, 535, 247, 37))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background:rgb(0, 255, 127)rgb(130, 130, 130);color:white")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(890, 141, 247, 37))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background:rgb(0, 255, 127)rgb(130, 130, 130);color:white")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(890, 666, 247, 37))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("background:rgb(0, 255, 127)rgb(130, 130, 130);color:white")
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(890, 273, 247, 36))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background:rgb(0, 255, 127)rgb(130, 130, 130);color:white")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(890, 710, 247, 37))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("background:rgb(0, 255, 127)rgb(130, 130, 130);color:white")
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(910, 760, 93, 41))
        self.pushButton.setStyleSheet("color:white\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1010, 760, 93, 41))
        self.pushButton_2.setStyleSheet("color:white")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(910, 9, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("background:rgb(0, 255, 127)rgb(130, 130, 130);color:white")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(960, 40, 118, 3))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.reg14 = QtWidgets.QLabel(self.centralwidget)
        self.reg14.setGeometry(QtCore.QRect(600, 623, 247, 36))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reg14.setFont(font)
        self.reg14.setStyleSheet("background:rgb(0, 255, 127)rgb(130, 130, 130);color:white")
        self.reg14.setAlignment(QtCore.Qt.AlignCenter)
        self.reg14.setObjectName("reg14")
        self.reg12 = QtWidgets.QLabel(self.centralwidget)
        self.reg12.setGeometry(QtCore.QRect(600, 535, 247, 37))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reg12.setFont(font)
        self.reg12.setStyleSheet("background:rgb(0, 255, 127)rgb(130, 130, 130);color:white")
        self.reg12.setAlignment(QtCore.Qt.AlignCenter)
        self.reg12.setObjectName("reg12")
        self.reg7 = QtWidgets.QLabel(self.centralwidget)
        self.reg7.setGeometry(QtCore.QRect(600, 316, 247, 37))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reg7.setFont(font)
        self.reg7.setStyleSheet("background:rgb(0, 255, 127)rgb(130, 130, 130);color:white\n"
"")
        self.reg7.setAlignment(QtCore.Qt.AlignCenter)
        self.reg7.setObjectName("reg7")
        self.reg16 = QtWidgets.QLabel(self.centralwidget)
        self.reg16.setGeometry(QtCore.QRect(600, 710, 247, 37))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reg16.setFont(font)
        self.reg16.setStyleSheet("background:rgb(0, 255, 127)rgb(130, 130, 130);color:white")
        self.reg16.setAlignment(QtCore.Qt.AlignCenter)
        self.reg16.setObjectName("reg16")
        self.reg3 = QtWidgets.QLabel(self.centralwidget)
        self.reg3.setGeometry(QtCore.QRect(600, 141, 247, 37))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reg3.setFont(font)
        self.reg3.setStyleSheet("background:rgb(0, 255, 127)rgb(130, 130, 130);color:white\n"
"")
        self.reg3.setAlignment(QtCore.Qt.AlignCenter)
        self.reg3.setObjectName("reg3")
        self.reg9 = QtWidgets.QLabel(self.centralwidget)
        self.reg9.setGeometry(QtCore.QRect(600, 404, 247, 37))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reg9.setFont(font)
        self.reg9.setStyleSheet("background:rgb(0, 255, 127)rgb(130, 130, 130);color:white")
        self.reg9.setAlignment(QtCore.Qt.AlignCenter)
        self.reg9.setObjectName("reg9")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(620, 9, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("background:rgb(0, 255, 127)rgb(130, 130, 130);color:white")
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.reg1 = QtWidgets.QLabel(self.centralwidget)
        self.reg1.setGeometry(QtCore.QRect(600, 54, 247, 37))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reg1.setFont(font)
        self.reg1.setStyleSheet("background:rgb(0, 255, 127)rgb(130, 130, 130);color:white\n"
"")
        self.reg1.setAlignment(QtCore.Qt.AlignCenter)
        self.reg1.setObjectName("reg1")
        self.reg6 = QtWidgets.QLabel(self.centralwidget)
        self.reg6.setGeometry(QtCore.QRect(600, 273, 247, 36))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reg6.setFont(font)
        self.reg6.setStyleSheet("background:rgb(0, 255, 127)rgb(130, 130, 130);color:white\n"
"")
        self.reg6.setAlignment(QtCore.Qt.AlignCenter)
        self.reg6.setObjectName("reg6")
        self.reg15 = QtWidgets.QLabel(self.centralwidget)
        self.reg15.setGeometry(QtCore.QRect(600, 666, 247, 37))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reg15.setFont(font)
        self.reg15.setStyleSheet("background:rgb(0, 255, 127)rgb(130, 130, 130);color:white")
        self.reg15.setAlignment(QtCore.Qt.AlignCenter)
        self.reg15.setObjectName("reg15")
        self.reg10 = QtWidgets.QLabel(self.centralwidget)
        self.reg10.setGeometry(QtCore.QRect(600, 448, 247, 36))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reg10.setFont(font)
        self.reg10.setStyleSheet("background:rgb(0, 255, 127)rgb(130, 130, 130);color:white")
        self.reg10.setAlignment(QtCore.Qt.AlignCenter)
        self.reg10.setObjectName("reg10")
        self.reg5 = QtWidgets.QLabel(self.centralwidget)
        self.reg5.setGeometry(QtCore.QRect(600, 229, 247, 37))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reg5.setFont(font)
        self.reg5.setStyleSheet("background:rgb(0, 255, 127)rgb(130, 130, 130);color:white\n"
"")
        self.reg5.setAlignment(QtCore.Qt.AlignCenter)
        self.reg5.setObjectName("reg5")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(670, 40, 118, 3))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.reg13 = QtWidgets.QLabel(self.centralwidget)
        self.reg13.setGeometry(QtCore.QRect(600, 580, 247, 37))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reg13.setFont(font)
        self.reg13.setStyleSheet("background:rgb(0, 255, 127)rgb(130, 130, 130);color:white")
        self.reg13.setAlignment(QtCore.Qt.AlignCenter)
        self.reg13.setObjectName("reg13")
        self.reg11 = QtWidgets.QLabel(self.centralwidget)
        self.reg11.setGeometry(QtCore.QRect(600, 491, 247, 37))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reg11.setFont(font)
        self.reg11.setStyleSheet("background:rgb(0, 255, 127)rgb(130, 130, 130);color:white")
        self.reg11.setAlignment(QtCore.Qt.AlignCenter)
        self.reg11.setObjectName("reg11")
        self.reg8 = QtWidgets.QLabel(self.centralwidget)
        self.reg8.setGeometry(QtCore.QRect(600, 360, 247, 37))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reg8.setFont(font)
        self.reg8.setStyleSheet("background:rgb(0, 255, 127)rgb(130, 130, 130);color:white\n"
"")
        self.reg8.setAlignment(QtCore.Qt.AlignCenter)
        self.reg8.setObjectName("reg8")
        self.reg4 = QtWidgets.QLabel(self.centralwidget)
        self.reg4.setGeometry(QtCore.QRect(600, 185, 247, 37))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reg4.setFont(font)
        self.reg4.setStyleSheet("background:rgb(0, 255, 127)rgb(130, 130, 130);color:white\n"
"")
        self.reg4.setAlignment(QtCore.Qt.AlignCenter)
        self.reg4.setObjectName("reg4")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(620, 760, 93, 41))
        self.pushButton_3.setStyleSheet("color:white")
        self.pushButton_3.setObjectName("pushButton_3")
        self.reg2 = QtWidgets.QLabel(self.centralwidget)
        self.reg2.setGeometry(QtCore.QRect(600, 98, 247, 36))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reg2.setFont(font)
        self.reg2.setStyleSheet("background:rgb(0, 255, 127)rgb(130, 130, 130);color:white\n"
"")
        self.reg2.setAlignment(QtCore.Qt.AlignCenter)
        self.reg2.setObjectName("reg2")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(720, 760, 93, 41))
        self.pushButton_4.setStyleSheet("color:white\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pipeline1 = QtWidgets.QLabel(self.centralwidget)
        self.pipeline1.setGeometry(QtCore.QRect(240, 591, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pipeline1.setFont(font)
        self.pipeline1.setStyleSheet("background:rgb(0, 255, 255)")
        self.pipeline1.setObjectName("pipeline1")
        self.pipeline2 = QtWidgets.QLabel(self.centralwidget)
        self.pipeline2.setGeometry(QtCore.QRect(240, 641, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pipeline2.setFont(font)
        self.pipeline2.setStyleSheet("background:rgb(0, 255, 255)")
        self.pipeline2.setObjectName("pipeline2")
        self.pipeline2_2 = QtWidgets.QLabel(self.centralwidget)
        self.pipeline2_2.setGeometry(QtCore.QRect(240, 741, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pipeline2_2.setFont(font)
        self.pipeline2_2.setStyleSheet("background:rgb(0, 255, 255)")
        self.pipeline2_2.setObjectName("pipeline2_2")
        self.pipeline1_2 = QtWidgets.QLabel(self.centralwidget)
        self.pipeline1_2.setGeometry(QtCore.QRect(240, 691, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pipeline1_2.setFont(font)
        self.pipeline1_2.setStyleSheet("background:rgb(0, 255, 255)")
        self.pipeline1_2.setObjectName("pipeline1_2")
        self.pipeline2_3 = QtWidgets.QLabel(self.centralwidget)
        self.pipeline2_3.setGeometry(QtCore.QRect(240, 791, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pipeline2_3.setFont(font)
        self.pipeline2_3.setStyleSheet("background:rgb(0, 255, 255)")
        self.pipeline2_3.setObjectName("pipeline2_3")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(30, 10, 120, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("color:white")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(380, 10, 120, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("color:white")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(200, 10, 120, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("color:white")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 70, 110, 35))
        self.pushButton_5.setStyleSheet("color:white")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(410, 70, 110, 35))
        self.pushButton_6.setStyleSheet("color:white")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(280, 70, 110, 35))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 44, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 44, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 44, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 44, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 44, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 44, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 44, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 44, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 44, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.pushButton_10.setPalette(palette)
        self.pushButton_10.setStyleSheet("color:white")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(210, 120, 110, 35))
        self.pushButton_11.setStyleSheet("color:white")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(150, 70, 110, 35))
        self.pushButton_12.setStyleSheet("color:white")
        self.pushButton_12.setObjectName("pushButton_12")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(310, 170, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("background:rgb(0, 255, 255)")
        self.label_19.setObjectName("label_19")
        self.pipeline2_4 = QtWidgets.QLabel(self.centralwidget)
        self.pipeline2_4.setGeometry(QtCore.QRect(80, 641, 130, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pipeline2_4.setFont(font)
        self.pipeline2_4.setStyleSheet("background:rgb(0, 255, 255)")
        self.pipeline2_4.setObjectName("pipeline2_4")
        self.pipeline2_5 = QtWidgets.QLabel(self.centralwidget)
        self.pipeline2_5.setGeometry(QtCore.QRect(80, 741, 130, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pipeline2_5.setFont(font)
        self.pipeline2_5.setStyleSheet("background:rgb(0, 255, 255)")
        self.pipeline2_5.setObjectName("pipeline2_5")
        self.pipeline1_3 = QtWidgets.QLabel(self.centralwidget)
        self.pipeline1_3.setGeometry(QtCore.QRect(80, 691, 130, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pipeline1_3.setFont(font)
        self.pipeline1_3.setStyleSheet("background:rgb(0, 255, 255)")
        self.pipeline1_3.setObjectName("pipeline1_3")
        self.pipeline1_4 = QtWidgets.QLabel(self.centralwidget)
        self.pipeline1_4.setGeometry(QtCore.QRect(80, 591, 130, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pipeline1_4.setFont(font)
        self.pipeline1_4.setStyleSheet("background:rgb(0, 255, 255)")
        self.pipeline1_4.setObjectName("pipeline1_4")
        self.pipeline2_6 = QtWidgets.QLabel(self.centralwidget)
        self.pipeline2_6.setGeometry(QtCore.QRect(80, 791, 130, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pipeline2_6.setFont(font)
        self.pipeline2_6.setStyleSheet("background:rgb(0, 255, 255)")
        self.pipeline2_6.setObjectName("pipeline2_6")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(20, 170, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("background:rgb(0, 255, 255)")
        self.label_20.setObjectName("label_20")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(40, 580, 481, 2))
        self.line_5.setStyleSheet("background:rgb(252, 252, 252)")
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(130, 480, 70, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("color:white;background:rgb(85, 255, 255)")
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setGeometry(QtCore.QRect(130, 320, 70, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("color:white;background:rgb(85, 255, 255)")
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        self.label_28.setGeometry(QtCore.QRect(130, 400, 70, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("color:white;background:rgb(85, 255, 255)")
        self.label_28.setAlignment(QtCore.Qt.AlignCenter)
        self.label_28.setObjectName("label_28")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(40, 250, 481, 2))
        self.line_7.setStyleSheet("background:rgb(252, 252, 252)")
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.label_29 = QtWidgets.QLabel(self.centralwidget)
        self.label_29.setGeometry(QtCore.QRect(250, 320, 70, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("color:white;background:rgb(85, 255, 255)")
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.centralwidget)
        self.label_30.setGeometry(QtCore.QRect(250, 480, 70, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("color:white;background:rgb(85, 255, 255)")
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.centralwidget)
        self.label_31.setGeometry(QtCore.QRect(250, 400, 70, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet("color:white;background:rgb(85, 255, 255)")
        self.label_31.setAlignment(QtCore.Qt.AlignCenter)
        self.label_31.setObjectName("label_31")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(870, 40, 2, 1061))
        self.line_6.setStyleSheet("background:white")
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1173, 26))
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
        self.label_14.setText(_translate("MainWindow", "TextLabel"))
        self.label_5.setText(_translate("MainWindow", "TextLabel"))
        self.label_4.setText(_translate("MainWindow", "TextLabel"))
        self.label_8.setText(_translate("MainWindow", "TextLabel"))
        self.label_10.setText(_translate("MainWindow", "TextLabel"))
        self.label_11.setText(_translate("MainWindow", "TextLabel"))
        self.label_7.setText(_translate("MainWindow", "TextLabel"))
        self.label_1.setText(_translate("MainWindow", "TextLabel"))
        self.label_13.setText(_translate("MainWindow", "TextLabel"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.label_9.setText(_translate("MainWindow", "TextLabel"))
        self.label_12.setText(_translate("MainWindow", "TextLabel"))
        self.label_3.setText(_translate("MainWindow", "TextLabel"))
        self.label_15.setText(_translate("MainWindow", "TextLabel"))
        self.label_6.setText(_translate("MainWindow", "TextLabel"))
        self.label_16.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton.setText(_translate("MainWindow", "UP"))
        self.pushButton_2.setText(_translate("MainWindow", "DOWN"))
        self.label.setText(_translate("MainWindow", "Memory"))
        self.reg14.setText(_translate("MainWindow", "TextLabel"))
        self.reg12.setText(_translate("MainWindow", "TextLabel"))
        self.reg7.setText(_translate("MainWindow", "TextLabel"))
        self.reg16.setText(_translate("MainWindow", "TextLabel"))
        self.reg3.setText(_translate("MainWindow", "TextLabel"))
        self.reg9.setText(_translate("MainWindow", "TextLabel"))
        self.label_23.setText(_translate("MainWindow", "Registers"))
        self.reg1.setText(_translate("MainWindow", "TextLabel"))
        self.reg6.setText(_translate("MainWindow", "TextLabel"))
        self.reg15.setText(_translate("MainWindow", "TextLabel"))
        self.reg10.setText(_translate("MainWindow", "TextLabel"))
        self.reg5.setText(_translate("MainWindow", "TextLabel"))
        self.line_4.setStyleSheet(_translate("MainWindow", "background:rgb(0, 255, 127)rgb(130, 130, 130)"))
        self.reg13.setText(_translate("MainWindow", "TextLabel"))
        self.reg11.setText(_translate("MainWindow", "TextLabel"))
        self.reg8.setText(_translate("MainWindow", "TextLabel"))
        self.reg4.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_3.setText(_translate("MainWindow", "UP"))
        self.reg2.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_4.setText(_translate("MainWindow", "DOWN"))
        self.pipeline1.setText(_translate("MainWindow", "Instruction that is currently being executed"))
        self.pipeline2.setText(_translate("MainWindow", "Instruction that is currently being executed"))
        self.pipeline2_2.setText(_translate("MainWindow", "Instruction that is currently being executed"))
        self.pipeline1_2.setText(_translate("MainWindow", "Instruction that is currently being executed"))
        self.pipeline2_3.setText(_translate("MainWindow", "Instruction that is currently being executed"))
        self.pushButton_7.setText(_translate("MainWindow", "RUN"))
        self.pushButton_9.setText(_translate("MainWindow", "RESET"))
        self.pushButton_8.setText(_translate("MainWindow", "STEP"))
        self.pushButton_5.setText(_translate("MainWindow", "5 knobs"))
        self.pushButton_6.setText(_translate("MainWindow", "5 knobs"))
        self.pushButton_10.setText(_translate("MainWindow", "5 knobs"))
        self.pushButton_11.setText(_translate("MainWindow", "5 knobs"))
        self.pushButton_12.setText(_translate("MainWindow", "5 knobs"))
        self.label_19.setText(_translate("MainWindow", "CLOCK:  7"))
        self.pipeline2_4.setText(_translate("MainWindow", "Instruction that is currently being executed"))
        self.pipeline2_5.setText(_translate("MainWindow", "Instruction that is currently being executed"))
        self.pipeline1_3.setText(_translate("MainWindow", "Instruction that is currently being executed"))
        self.pipeline1_4.setText(_translate("MainWindow", "Instruction that is currently being executed"))
        self.pipeline2_6.setText(_translate("MainWindow", "Instruction that is currently being executed"))
        self.label_20.setText(_translate("MainWindow", "ERROR"))
        self.label_26.setText(_translate("MainWindow", "M"))
        self.label_27.setText(_translate("MainWindow", "D"))
        self.label_28.setText(_translate("MainWindow", "E"))
        self.label_29.setText(_translate("MainWindow", "D"))
        self.label_30.setText(_translate("MainWindow", "M"))
        self.label_31.setText(_translate("MainWindow", "E"))

# label.setText()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
