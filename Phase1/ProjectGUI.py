# CS204 Project
from PyQt5 import QtCore, QtGui, QtWidgets
from collections import defaultdict

import sys ,os

# File reading completed

#defining global variables____________________________
reg = [0]*32
reg[2] = int("0x7FFFFFF0",16) # sp - STACK POINTER
reg[3] = int("0x10000000",16) # pointer to begining of data segment
ui = 0
clk = 0

RS1,RS2,RD,RM,RZ,RY,RA,RB,PC,IR,MuxB_select,MuxC_select,MuxINC_select,MuxY_select,MuxPC_select,MuxMA_select,RegFileAddrA,RegFileAddrB,RegFileAddrC,RegFileInp,RegFileAOut,RegFileBOut,MAR,MDR,opcode,numBytes,RF_Write,immed,PC_Temp,Mem_Write,Mem_Read=[0]*31


from PyQt5 import QtCore, QtGui, QtWidgets
isStepClicked = 0

# from project import *

import sys ,os
run = 0

def resetButton():
    global clk
    init()
    clk=0
    ui.updateRegisters(reg,clk)
    ui.label_41.setText("")
    ui.label_2.setText("")
    ui.label_3.setText("")
    ui.label_4.setText("")
    ui.label_5.setText("")
    ui.label_40.setText("")
    ui.label_42.setText("")
    main()

class Ui_MainWindow(object):

    def errorUpdate(self,errorText):
        self.label_40.setText(errorText)

    def updateRegisters(self,reg,clk):
        self.label_6.setText('x0:' +str(reg[0]))
        self.label_7.setText('x1:' +str(reg[1]))
        self.label_8.setText('x16:' +str(reg[16]))
        self.label_9.setText('x17:' +str(reg[17]))
        self.label_10.setText('x2:' +str(reg[2]))
        self.label_11.setText('x18:' +str(reg[18]))
        self.label_12.setText('x3:' +str(reg[3]))
        self.label_13.setText('x19:' +str(reg[19]))
        self.label_14.setText('x4:' +str(reg[4]))
        self.label_15.setText('x20:' +str(reg[20]))
        self.label_16.setText('x5:' +str(reg[5]))
        self.label_17.setText('x21:' +str(reg[21]))
        self.label_18.setText('x6:' +str(reg[6]))
        self.label_19.setText('x22:' +str(reg[22]))
        self.label_20.setText('x7:' +str(reg[7]))
        self.label_21.setText('x23:' +str(reg[23]))
        self.label_22.setText('x8:' +str(reg[8]))
        self.label_23.setText('x24:' +str(reg[24]))
        self.label_24.setText('x9:' +str(reg[9]))
        self.label_25.setText('x25:' +str(reg[25]))
        self.label_26.setText('x10:' +str(reg[10]))
        self.label_27.setText('x26:' +str(reg[26]))
        self.label_28.setText('x28:' +str(reg[28]))
        self.label_29.setText('x29:' +str(reg[29]))
        self.label_30.setText('x24:' +str(reg[24]))
        self.label_31.setText('x14:' +str(reg[14]))
        self.label_32.setText('x30:' +str(reg[30]))
        self.label_33.setText('x27:' +str(reg[27]))
        self.label_34.setText('x12:' +str(reg[12]))
        self.label_35.setText('x11:' +str(reg[11]))
        self.label_36.setText('x27:' +str(reg[27]))
        self.label_37.setText('x13:' +str(reg[13]))
        self.label_39.setText('x15:' +str(reg[15]))
        self.label_38.setText('x31:' +str(reg[31]))
        self.label.setText("total clock cycles: "+str(clk))

        self.label_41.setText("Fetching instruction number "+str(clk))
        self.label_2.setText("Decoding instruction number "+str(clk))
        self.label_3.setText("Executing instruction number "+str(clk))
        self.label_4.setText("Memory Acessing for instruction number "+str(clk))
        self.label_5.setText("Register Update for instruction number "+str(clk))

    # def runClicked(self):
    #     global run
    #     run = 1

    def stepButton(self):
        global isStepClicked
        isStepClicked = 1
        run_RISC_simulator()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1938, 1025)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(48, 48, 48);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(210, 100, 160, 51))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(run_RISC_simulator)

        #clock
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 710, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        
        self.label.setStyleSheet("background: rgb(255, 255, 255)")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(210, 320, 500, 60))
        self.label_2.setStyleSheet("background: rgb(255, 255, 255)")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(210, 410, 500, 60))
        self.label_3.setStyleSheet("background: rgb(255, 255, 255)")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(210, 500, 500, 60))
        self.label_4.setStyleSheet("background: rgb(255, 255, 255)")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(210, 590, 500, 60))
        self.label_5.setStyleSheet("background: rgb(255, 255, 255)")
        self.label_5.setObjectName("label_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 100, 160, 51))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)

        #step button 
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.stepButton)  

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(550, 100, 160, 51))
        self.pushButton_4.clicked.connect(resetButton)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_4.setObjectName("pushButton_4")


        #register label starts
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(1100, 20, 291, 41))
        self.label_6.setStyleSheet("background: rgb(255, 255, 255)")
        self.label_6.setObjectName("label_6")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(926, -20, 6, 941))
        self.line.setStyleSheet("background: rgb(255, 255, 255)")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(1550, 20, 291, 41))
        self.label_8.setStyleSheet("background: rgb(255, 255, 255)")
        self.label_8.setObjectName("label_8")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(1100, 80, 291, 41))
        self.label_7.setStyleSheet("background: rgb(255, 255, 255)")
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(1550, 80, 291, 41))
        self.label_9.setStyleSheet("background: rgb(255, 255, 255)")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(1100, 140, 291, 41))
        self.label_10.setStyleSheet("background: rgb(255, 255, 255)")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(1550, 140, 291, 41))
        self.label_11.setStyleSheet("background: rgb(255, 255, 255)")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(1100, 200, 291, 41))
        self.label_12.setStyleSheet("background: rgb(255, 255, 255)")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(1550, 200, 291, 41))
        self.label_13.setStyleSheet("background: rgb(255, 255, 255)")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(1100, 260, 291, 41))
        self.label_14.setStyleSheet("background: rgb(255, 255, 255)")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(1550, 260, 291, 41))
        self.label_15.setStyleSheet("background: rgb(255, 255, 255)")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(1100, 320, 291, 41))
        self.label_16.setStyleSheet("background: rgb(255, 255, 255)")
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(1550, 320, 291, 41))
        self.label_17.setStyleSheet("background: rgb(255, 255, 255)")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(1100, 380, 291, 41))
        self.label_18.setStyleSheet("background: rgb(255, 255, 255)")
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(1550, 380, 291, 41))
        self.label_19.setStyleSheet("background: rgb(255, 255, 255)")
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(1100, 440, 291, 41))
        self.label_20.setStyleSheet("background: rgb(255, 255, 255)")
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(1550, 440, 291, 41))
        self.label_21.setStyleSheet("background: rgb(255, 255, 255)")
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(1100, 500, 291, 41))
        self.label_22.setStyleSheet("background: rgb(255, 255, 255)")
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(1550, 500, 291, 41))
        self.label_23.setStyleSheet("background: rgb(255, 255, 255)")
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(1100, 560, 291, 41))
        self.label_24.setStyleSheet("background: rgb(255, 255, 255)")
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(1550, 560, 291, 41))
        self.label_25.setStyleSheet("background: rgb(255, 255, 255)")
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(1100, 620, 291, 41))
        self.label_26.setStyleSheet("background: rgb(255, 255, 255)")
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setGeometry(QtCore.QRect(1550, 620, 291, 41))
        self.label_27.setStyleSheet("background: rgb(255, 255, 255)")
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        self.label_28.setGeometry(QtCore.QRect(1550, 740, 291, 41))
        self.label_28.setStyleSheet("background: rgb(255, 255, 255)")
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.centralwidget)
        self.label_29.setGeometry(QtCore.QRect(1550, 800, 291, 41))
        self.label_29.setStyleSheet("background: rgb(255, 255, 255)")
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.centralwidget)
        self.label_30.setGeometry(QtCore.QRect(1400, 1030, 291, 41))
        self.label_30.setStyleSheet("background: rgb(255, 255, 255)")
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.centralwidget)
        self.label_31.setGeometry(QtCore.QRect(1100, 860, 291, 41))
        self.label_31.setStyleSheet("background: rgb(255, 255, 255)")
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.centralwidget)
        self.label_32.setGeometry(QtCore.QRect(1550, 860, 291, 41))
        self.label_32.setStyleSheet("background: rgb(255, 255, 255)")
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.centralwidget)
        self.label_33.setGeometry(QtCore.QRect(1850, 1030, 291, 41))
        self.label_33.setStyleSheet("background: rgb(255, 255, 255)")
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.centralwidget)
        self.label_34.setGeometry(QtCore.QRect(1100, 740, 291, 41))
        self.label_34.setStyleSheet("background: rgb(255, 255, 255)")
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(self.centralwidget)
        self.label_35.setGeometry(QtCore.QRect(1100, 680, 291, 41))
        self.label_35.setStyleSheet("background: rgb(255, 255, 255)")
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(self.centralwidget)
        self.label_36.setGeometry(QtCore.QRect(1550, 680, 291, 41))
        self.label_36.setStyleSheet("background: rgb(255, 255, 255)")
        self.label_36.setObjectName("label_36")
        self.label_37 = QtWidgets.QLabel(self.centralwidget)
        self.label_37.setGeometry(QtCore.QRect(1100, 800, 291, 41))
        self.label_37.setStyleSheet("background: rgb(255, 255, 255)")
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self.centralwidget)
        self.label_38.setGeometry(QtCore.QRect(1550, 920, 291, 41))
        self.label_38.setStyleSheet("background: rgb(255, 255, 255)")
        self.label_38.setObjectName("label_38")
        #register label ends
        self.label_39 = QtWidgets.QLabel(self.centralwidget)
        self.label_39.setGeometry(QtCore.QRect(1100, 920, 291, 41))
        self.label_39.setStyleSheet("background: rgb(255, 255, 255)")
        self.label_39.setObjectName("label_39")
        self.label_42 = QtWidgets.QLabel(self.centralwidget)
        self.label_42.setGeometry(QtCore.QRect(60, 810, 801, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_42.setFont(font)
        self.label_42.setStyleSheet("background: rgb(255, 255, 255)")
        self.label_42.setObjectName("label_40")
        self.label_41 = QtWidgets.QLabel(self.centralwidget)
        self.label_41.setGeometry(QtCore.QRect(210, 240, 500, 60))
        self.label_41.setStyleSheet("background: rgb(255, 255, 255)")
        self.label_41.setObjectName("label_41")

        self.label_40 = QtWidgets.QLabel(self.centralwidget)
        self.label_40.setGeometry(QtCore.QRect(60, 900, 801, 41))
        self.label_40.setStyleSheet("background: rgb(255, 255, 255)")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1938, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.label.setFont(font)
        self.label_2.setFont(font)
        self.label_3.setFont(font)
        self.label_4.setFont(font)
        self.label_5.setFont(font)
        self.label_6.setFont(font)
        self.label_7.setFont(font)
        self.label_8.setFont(font)
        self.label_9.setFont(font)
        self.label_10.setFont(font)
        self.label_11.setFont(font)
        self.label_12.setFont(font)
        self.label_13.setFont(font)
        self.label_14.setFont(font)
        self.label_15.setFont(font)
        self.label_16.setFont(font)
        self.label_17.setFont(font)
        self.label_18.setFont(font)
        self.label_19.setFont(font)
        self.label_20.setFont(font)
        self.label_21.setFont(font)
        self.label_22.setFont(font)
        self.label_23.setFont(font)
        self.label_24.setFont(font)
        self.label_25.setFont(font)
        self.label_26.setFont(font)
        self.label_27.setFont(font)
        self.label_28.setFont(font)
        self.label_29.setFont(font)
        self.label_30.setFont(font)
        self.label_31.setFont(font)
        self.label_32.setFont(font)
        self.label_33.setFont(font)
        self.label_34.setFont(font)
        self.label_35.setFont(font)
        self.label_36.setFont(font)
        
        self.label_37.setFont(font)
        self.label_38.setFont(font)
        self.label_39.setFont(font)
        self.label_40.setFont(font)
        self.label_41.setFont(font)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "RUN"))
        self.label.setText(_translate("MainWindow", ""))
        self.label_2.setText(_translate("MainWindow", ""))
        self.label_3.setText(_translate("MainWindow", ""))
        self.label_4.setText(_translate("MainWindow", ""))
        self.label_5.setText(_translate("MainWindow", ""))
        self.pushButton_2.setText(_translate("MainWindow", "STEP"))
        self.pushButton_4.setText(_translate("MainWindow", "RESET"))
        self.label_6.setText(_translate("MainWindow", ""))
        self.label_8.setText(_translate("MainWindow", ""))
        self.label_7.setText(_translate("MainWindow", ""))
        self.label_9.setText(_translate("MainWindow", ""))
        self.label_10.setText(_translate("MainWindow", ""))
        self.label_11.setText(_translate("MainWindow", ""))
        self.label_12.setText(_translate("MainWindow", ""))
        self.label_13.setText(_translate("MainWindow", ""))
        self.label_14.setText(_translate("MainWindow", ""))
        self.label_15.setText(_translate("MainWindow", ""))
        self.label_16.setText(_translate("MainWindow", ""))
        self.label_17.setText(_translate("MainWindow", ""))
        self.label_18.setText(_translate("MainWindow", ""))
        self.label_19.setText(_translate("MainWindow", ""))
        self.label_20.setText(_translate("MainWindow", ""))
        self.label_21.setText(_translate("MainWindow", ""))
        self.label_22.setText(_translate("MainWindow", ""))
        self.label_23.setText(_translate("MainWindow", ""))
        self.label_24.setText(_translate("MainWindow", ""))
        self.label_25.setText(_translate("MainWindow", ""))
        self.label_26.setText(_translate("MainWindow", ""))
        self.label_27.setText(_translate("MainWindow", ""))
        self.label_28.setText(_translate("MainWindow", ""))
        self.label_29.setText(_translate("MainWindow", ""))
        self.label_30.setText(_translate("MainWindow", ""))
        self.label_31.setText(_translate("MainWindow", ""))
        self.label_32.setText(_translate("MainWindow", ""))
        self.label_33.setText(_translate("MainWindow", ""))
        self.label_34.setText(_translate("MainWindow", ""))
        self.label_35.setText(_translate("MainWindow", ""))
        self.label_36.setText(_translate("MainWindow", ""))
        self.label_37.setText(_translate("MainWindow", ""))
        self.label_38.setText(_translate("MainWindow", ""))
        self.label_39.setText(_translate("MainWindow", ""))
        self.label_40.setText(_translate("MainWindow", ""))
        self.label_41.setText(_translate("MainWindow", ""))


# def fun():
#     return Ui_MainWindow
# app = QtWidgets.QApplication(sys.argv)
# MainWindow = QtWidgets.QMainWindow()
# ui = Ui_MainWindow()
# ui.setupUi(MainWindow)
# MainWindow.show()
# sys.exit(app.exec_())

def GenerateControlSignals(reg_write,MuxB,MuxY,MemRead,MemWrite,MuxMA,MuxPC,MuxINC,numB):
    global RF_Write, MuxB_select, MuxY_select, MuxMA_select, MuxINC_select, MuxPC_select, Mem_Read, Mem_Write,numBytes

    RF_Write = reg_write
    MuxB_select = MuxB
    MuxY_select = MuxY
    Mem_Write = MemWrite
    Mem_Read = MemRead
    MuxMA_select = MuxMA
    MuxPC_select = MuxPC
    MuxINC_select = MuxINC
    numBytes = numB

ALUOp = [0]*15
#instructions
# add 0, sub 1, div 2, mul 3, remainder 4, xor 5,
# shift_left 6, shift_right_ari 7,shift_ri_lo 8, or 9,
# and 10, less_than 11, equal 12, not_equal 13, 
# greater_than_equal_to 14,


#Auxilary function______________
def init():
    global ALUOp,RS1,RS2,RD,RM,RZ,RY,RA,RB,PC,IR,MuxB_select,MuxC_select,MuxINC_select,MuxY_select,MuxPC_select,MuxMA_select,RegFileAddrA,RegFileAddrB,RegFileAddrC,RegFileInp,RegFileAOut,RegFileBOut,MAR,MDR,opcode,numBytes,RF_Write,immed,PC_Temp,Mem_Write,Mem_Read,reg,dataMemory,instructionMemory
    ALUOp = [0]*15
    RS1,RS2,RD,RM,RZ,RY,RA,RB,PC,IR,MuxB_select,MuxC_select,MuxINC_select,MuxY_select,MuxPC_select,MuxMA_select,RegFileAddrA,RegFileAddrB,RegFileAddrC,RegFileInp,RegFileAOut,RegFileBOut,MAR,MDR,opcode,numBytes,RF_Write,immed,PC_Temp,Mem_Write,Mem_Read=[0]*31
    reg = [0]*32
    reg[2] = int("0x7FFFFFF0",16) # sp - STACK POINTER
    reg[3] = int("0x10000000",16) # pointer to begining of data segment
    dataMemory = defaultdict(lambda : [0,0,0,0])
    instructionMemory = defaultdict(lambda: [0,0,0,0])

def sra(number,times):     #correct function
    bx = bin(number)[2:]
    if len(bx)<32 or bx[0]=='0':
        return number>>times
    else:
        ans = '1'*times + bx[:32-times]
        twosCompli = [str(1-int(i)) for i in ans[1:]]
        twosCompli = (''.join(twosCompli))
        twosCompli = - (int(twosCompli,2) + 1)
        return twosCompli


#________________________

dataMemory = defaultdict(lambda : [0,0,0,0])
instructionMemory = defaultdict(lambda: [0,0,0,0])

def ProcessorMemoryInterface():
    # Set MAR in Fetch
    if MuxMA_select == 0:
        if Mem_Read == 1:
            temp = dataMemory[MAR][:numBytes]
            temp.reverse()
            ans = '0x'
            for i in temp:
                curr =  hex(i)[2:]
                ans += '0'*(2-len(curr)) + curr
                
            return ans
        elif Mem_Write == 1:
            for i in range (numBytes):
                dataMemory[MAR][i] = (MDR & int('0xFF'+'0'*(2*i),16))>>(8*i)
            return '0x1'
    else:
        ans = instructionMemory[MAR]
        newans = ""
        x=len(ans)
        for i in range(len(ans)):
            newans += ans[x-1-i]
        newans = '0x'+newans
        return newans

def Fetch():
    #Pc, ir
    global IR,MAR,MuxMA_select, PC_Temp, PC

    # print("Fetching the instruction")
    MAR = hex(PC)
    MuxMA_select = 1    
    IR = ProcessorMemoryInterface()
    PC_Temp = PC + 4
    

def decimalToBinary(num, length):
    ans=""
    while(num>0):
        if(num&1):
            ans+='1'
        else:
            ans+='0'
        num = num//2
    for i in range(length-len(ans)):
        ans+='0'
    return ans[::-1]   

def Decode():
    # print("Decoding the instruction")
    #getting the opcode
    global opcode,immed,RS1,RS2,RD,RF_Write,MuxB_select,numBytes,RM,RA,RB,reg,ALUOp
    ALUOp = [0]*15
    opcode = int(str(IR),16) & int("0x7f",16)
    fun3 = (int(str(IR),16) & int("0x7000",16)) >> 12
    
    # R format - (add,srl,sll,sub,slt,xor,sra,and,or,mul, div, rem)
    # R format - (0110011)  
    # I format - (lb-0,lh-1,lw-2)(addi-0, andi-7, ori-6,)(jalr-0)
    # I format - (0000011)(0010011)(1100111)
    # S format - (sb, sw, sh)
    # S format - (0100011) f3 - sb - 000, sh - 001, sw - 010
    # SB format - beq, bne, bge, blt
    # SB format - (1100011) f3 - beq - 000, bne - 001, blt - 100, bge - 101
    # U format - auipc-0010111, lui-0110111
    # UJ format - jal-1101111
    message = ""
    if opcode==int("0110011",2): # R format
        GenerateControlSignals(1, 0, 0, 0, 0, 0, 1, 0, 4)
        RD = (int(IR,16) & int('0xF80',16)) >> 7 # setting destination register
        RS1 = (int(IR,16) & int('0xF8000',16)) >> 15 # setting rs1 register
        RS2 = (int(IR,16) & int('0x1F00000',16)) >> 20 # setting rs2 register
        fun7 = (int(IR,16) & int('0xFE000000',16)) >> 25
        if fun3 == 0:  # add/sub/mul
            if fun7 == 0: 
                # add 
                ALUOp[0]=1
                message = "This is ADD instruction."
            elif fun7 == 32: # subtract
                ALUOp[1]=1
                message = "This is SUB instruction."
            elif fun7==1: # mul
                ALUOp[3]=1 
                message = "This is MUL instruction."
            else:
                print("Invalid Func7 for Add/Sub")
                ui.errorUpdate("Invalid Func7 for Add/Sub")
                exit(1)
        elif fun3==7: # and
            message = "This is AND instruction."
            if fun7==0:
                ALUOp[10]=1
            else:
                print("Invalid Fun7 for AND")
                ui.errorUpdate("Invalid Fun7 for AND")
                exit(1)
        elif fun3 == 6: # or/remainder
            if fun7==0: # or
                message = "This is OR instruction."
                ALUOp[9]=1
            elif fun7==1: # remainder
                ALUOp[4]=1
                message = "This is REMAINDER instruction."
            else:
                print("Invalid Func7 for OR/REM")
                ui.errorUpdate("Invalid Func7 for Add/Sub")
                exit(1)
        elif fun3 == 1: # sll - shift_left
            if fun7==0:
                ALUOp[6]=1
                message = "This is SLL instruction."
            else:
                print("Invalid Func7 for SLL")
                ui.errorUpdate("Invalid Func7 for SLL")
                exit(1)
        elif fun3 == 2: # slt - set_if_less_than
            message = "This is SLT instruction."
            if fun7==0:
                ALUOp[11]=1
            else:
                print("Invalid Func7 for SLT")
                ui.errorUpdate("Invalid Func7 for SLT")
                exit(1)
        elif fun3 == 5: # srl/sra
            if fun7==32: # shift_ri_ari
                message = "This is SRA instruction."
                ALUOp[7]=1
            elif fun7==0: #shift_ri_lo
                message = "This is SRL instruction."
                ALUOp[8]=1
            else:
                print("Invalid Func7 for SRA/SRL")
                ui.errorUpdate("Invalid Func7 for SRA/SRL")
                exit(1)
        elif fun3 == 4: #xor/div
            if fun7==0: # xor
                message = "This is XOR instruction."
                ALUOp[5]=1
            elif fun7==1: #div
                message = "This is DIV instruction."
                ALUOp[2]=1
            else:
                ui.errorUpdate("Invalid Func7 for XOR/div")
                exit(1)
        else:
            ui.errorUpdate("fun3 not matching in R format")
            exit(1)
        #setting ra rb rm -------------------------------------------------
        RA = reg[RS1]
        RB = reg[RS2] 
        RM = RB        # ---- DON'T CARES
        # -----------------------------------------------------------------
   
    elif opcode==int("0000011",2) or opcode==int("0010011",2) or opcode==int("1100111",2): # I format
        RD = (int(IR,16) & int('0xF80',16)) >> 7 # setting destination register
        RS1 = (int(IR,16) & int('0xF8000',16)) >> 15 # setting rs1 register
        immed = (int(IR,16) & int('0xFFF00000',16)) >> 20

        #  ADDING CONSTRAINTS ON IMMEDIATE
        if immed>2047:
            immed -= 4096
        
        if opcode==int("0000011",2): # lb/lh/lw
            ALUOp[0]=1
            if fun3 == 0: #lb
                message = "This is LB instruction."
                GenerateControlSignals(1,1,1,1,0,0,1,0,1)
            elif fun3 == 1: #lh
                message = "This is LH instruction."
                GenerateControlSignals(1,1,1,1,0,0,1,0,2)
            elif fun3 == 2: #lw
                message = "This is LW instruction."
                GenerateControlSignals(1,1,1,1,0,0,1,0,4)
            else:
                ui.errorUpdate("Wrong fun3 for lb/lh/lw")
                exit(1)
            #setting ra rb rm -------------------------------------------------
            RA = reg[RS1]
            # RB = reg[RS2]   ---- DON'T CARES
            # RM = RB         ---- DON'T CARES
            # -----------------------------------------------------------------
        elif opcode==int("0010011",2): #addi/andi/ori
            GenerateControlSignals(1,1,0,0,0,0,1,0,4)
            if fun3==0:#addi
                message = "This is ADDI instruction."
                ALUOp[0]=1
            elif fun3==7:#andi
                message = "This is ANDI instruction."
                ALUOp[10]=1
            elif fun3==6:#ori
                message = "This is ORI instruction."
                ALUOp[9]=1
            else:
                ui.errorUpdate("Error fun3 not matching for addi/andi/ori")
                exit(1)
            #setting ra rb rm -------------------------------------------------
            RA = reg[RS1]
            # RB = reg[RS2]   ---- DON'T CARES
            # RM = RB         ---- DON'T CARES
            # -----------------------------------------------------------------
        elif opcode==int("1100111",2): #jalr **ERROR(CHECK IT)****
            message = "This is JALR instruction."
            GenerateControlSignals(1,0,2,0,0,0,0,1,4)
            if fun3==0:
                ALUOp[0]=1
            else:
                ui.errorUpdate("Error wrong fun3 for jalr")
                exit(1)
            #setting ra rb rm -------------------------------------------------
            RA = reg[RS1]
            # RB = reg[RS2]   ---- DON'T CARES
            # RM = RB         ---- DON'T CARES
            # -----------------------------------------------------------------

    elif opcode==int("0100011",2): # S format
        RS2 = (int(str(IR),16) & int("0xF8000",16)) >> 15
        RS1 = (int(str(IR),16) & int("0x1F00000",16)) >> 20
        immed4to0 = (int(str(IR),16) & int("0xF80",16)) >> 7
        immed11to5 = (int(str(IR),16) & int("0xFE000000",16)) >> 25
        immed = immed4to0 | immed11to5
        ImmediateSign(12)
        ALUOp[0]=1
        if fun3 == int("000",2): # sb
            message = "This is SB instruction."
            GenerateControlSignals(0,1,1,0,1,0,1,0,1)
        elif fun3 == int("001",2): # sh
            message = "This is SH instruction."
            GenerateControlSignals(0,1,1,0,1,0,1,0,2)
        elif fun3 == int("010",2): # sw
            message = "This is SW instruction."
            GenerateControlSignals(0,1,1,0,1,0,1,0,4)
        else:
            ui.errorUpdate("invalid fun3 => S format")
            exit(1)
            return
        #setting ra rb rm -------------------------------------------------
        RA = reg[RS2]
        RB = reg[RS1]
        RM = RB
        # -----------------------------------------------------------------

    elif opcode==int("1100011",2): # SB format
        RS1 = (int(IR, 16) & int("0xF8000", 16)) >> 15
        RS2 = (int(IR, 16) & int("0x1F00000", 16)) >> 20
        RA = reg[RS1]
        RB = reg[RS2]
        imm1 = (int(IR, 16) & int("0xF80", 16)) >> 7
        imm2 = (int(IR, 16) & int("0xFE000000", 16)) >> 25
        immed = 0
        immed = immed | ((imm1 & int("0x1E", 16)) >> 1)
        immed = immed | ((imm2 & int("0x3F", 16)) << 4)
        immed = immed | ((imm1 & 1) << 10)
        immed = immed | (((imm2 & int("0x40", 16)) >> 6) << 11)
        ImmediateSign(12)
        immed *= 2
        # Setting control Signals
        if(fun3 == 0):
            message = "This is BEQ instruction."
            ALUOp[12] = 1
        elif(fun3 == 1):
            message = "This is BNE instruction."
            ALUOp[13] = 1
        elif(fun3 == 4):
            message = "This is BLT instruction."
            ALUOp[11] = 1
        elif(fun3 == 5):
            message = "This is BGE instruction."
            ALUOp[14] = 1
        else:
            ui.errorUpdate("Invalid fun3 for SB Format instruction. Terminating the program.")
            exit(1)
        GenerateControlSignals(0,0,0,0,0,0,1,1,0)

    elif opcode==int("0010111",2) or opcode==int("0110111",2): # U type
        RD = (int(IR, 16) & int("0xF80", 16)) >> 7
        immed = (int(IR, 16) & int("0xFFFFF000", 16)) >> 12
        ImmediateSign(20)
        if(opcode == int("0010111", 2)): # AUIPC
            message = "This is AUIPC instruction."
            ALUOp[0] = 1
            RA = PC
            immed = immed << 12
        else: #LUI
            message = "This is LUI instruction."
            ALUOp[6] = 1
            RA = immed
            immed = 12
        GenerateControlSignals(1,1,0,0,0,0,1,0,0)

    elif opcode==int("1101111",2): # UJ format
        message = "This is JALR instruction."
        RD = (int(IR, 16) & int("0xF80", 16)) >> 7
        immed_tmp = (int(IR, 16) & int("0xFFFFF000", 16)) >> 12
        immed = 0
        immed = immed | ((immed_tmp & int("0x7FE00", 16)) >> 9)
        immed = immed | ((immed_tmp & int("0x100", 16)) << 2)
        immed = immed | ((immed_tmp & int("0xFF", 16)) << 11)
        immed = immed | (immed_tmp & int("0x80000", 16))
        ImmediateSign(20)
        immed *= 2
        ALUOp[12] = 1
        RA = 0
        RB = 0
        # print("Immediate field : " + str(immed))
        GenerateControlSignals(1,0,2,0,0,0,1,1,0)

    else:
        print("invalid opcode")

    print(message)
    ui.label_42.setText(message)

def ImmediateSign(num):
    global immed
    if(immed & 2**(num-1) == 0):
        return
    immed = immed ^ (2**num-1)
    immed += 1
    immed *= (-1)

def Execute():
    global immed,ALUOp,RZ, reg,MuxINC_select
    operation = ALUOp.index(1)
    ALUOp = [0]*15
    InA = RA
    if(MuxB_select == 1):
        InB = immed
    else:
        InB = RB
    if(operation == 0): #add
        RZ = InA + InB
    elif(operation == 1): #sub
        RZ = InA - InB
    elif(operation == 2): #div
        if(InB == 0):
            ui.errorUpdate("Error : Division by zero")
            exit(1)
        RZ = int(InA/InB)
    elif(operation == 3): #mul
        RZ = InA*InB
    elif(operation == 4): #remainder
        if(InB == 0):
            ui.errorUpdate("Error : Remainder by zero")
            exit(1)
        RZ = InA%InB
    elif(operation == 5): #xor
        RZ = InA^InB
    elif(operation == 6): #shift_left
        if (InB<0):
            ui.errorUpdate("Cannot  left shift a number negative times")
            exit(1)
        RZ = InA<<InB
    elif(operation == 7): #shift_right_ari 
        # ********************ERROR***************** WRITE SRA
        pass
    elif(operation == 8): #shift_ri_lo  
        if (InB<0):
            ui.errorUpdate("Cannot  right shift a number negative times")
            exit(1)
        RZ = InA>>InB
    elif(operation == 9): #or  
        RZ = (InA|InB)
    elif(operation == 10): #and  
        RZ = (InA&InB)
    elif(operation == 11): #less_than 
        RZ = int(InA<InB)
        MuxINC_select = RZ
    elif(operation == 12): #equal  
        RZ = int(InA==InB)
        MuxINC_select = RZ
    elif(operation == 13): #not_equal  
        RZ = int(InA!=InB)
        MuxINC_select = RZ
    elif(operation == 14): #greater_than_equal_to  
        RZ = int(InA>=InB)
        MuxINC_select = RZ
    # return RZ

def IAG():
    global PC
    if(MuxPC_select == 0):
        PC = RA
    else:
        if(MuxINC_select == 0):
            PC = PC + 4
        else:
            PC = PC + immed
    
def MemoryAccess():
    # =========== CHECK =============
    global MAR,RY,PC, MDR
    
    # PC update (IAG module)    
    # if(MuxPC_select == 0):
    #     PC = RA
    # else:
    #     if(MuxINC_select == 0):
    #         PC = PC + 4
    #     else:
    #         PC = PC + immed
    IAG()

    if MuxY_select == 0:
        RY = RZ
    elif MuxY_select == 1:
        MAR = str(hex(RZ)).lower()
        MDR = RM
        RY = int(ProcessorMemoryInterface(),16)
        if RY > 2**31 - 1:
            RY = -(2**32 - RY)
    elif MuxY_select == 2:
        RY = PC_Temp


def RegisterUpdate():
    global reg,RD
    if RF_Write == 1 and RD != 0:
        reg[RD] = RY

def validateDataSegment(y):
    if len(y)!=2:
        return False
    addr,data = y[0],y[1]
    if addr[:2]!='0x' or data[:2]!='0x':
        return False
    try:
        if int(addr,16)<int("0x10000000",16):
            return False
        int(data,16)
    except:
        return False 
    return True

def validateInstruction(y):
    if len(y)!=2:
        return False
    addr,data = y[0],y[1]
    if addr[:2]!='0x' or data[:2]!='0x':
        return False
    try:
        temp = int(addr,16)
        temp1 = int(data,16)
    except:
        return False
    return True
# global ui

def main():

    # Read the .mc file as input
    mcFile = open("input.mc","r")
    # load the data segment
    flag = 0
    for x in mcFile:
        #creating a hashmap, data segment stored
        y = x.split('\n')[0].split()
        y[1] = y[1].lower()
        if flag==1:
            if validateDataSegment(y)==False:
                print("ERROR : INVALID DATA SEGMENT")
                ui.errorUpdate("ERROR : INVALID DATA SEGMENT")
                exit(1)
            dataMemory[y[0]][0] = (int(y[1],16) & int('0xFF',16))
            dataMemory[y[0]][1] = (int(y[1],16) & int('0xFF00',16))>>8
            dataMemory[y[0]][2] = (int(y[1],16) & int('0xFF0000',16))>>16
            dataMemory[y[0]][3] = (int(y[1],16) & int('0xFF000000',16))>>24

        if '$' in y:
            flag = 1    
        if flag==0:
            #TODO : Add Validation______
            y = x.split('\n')[0].split()
            if validateInstruction(y)== False:
                print("ERROR : INVALID INSTRUCTION")
                ui.errorUpdate("ERROR : INVALID INSTRUCTION")
                exit(1)
            y[1] = y[1].lower() 
            for i in range (4):
                instructionMemory[y[0]][i] = hex((int(y[1],16) & int('0xFF'+'0'*(2*i),16))>>(8*i))[2:]
                instructionMemory[y[0]][i] = '0'*(2-len(instructionMemory[y[0]][i])) + instructionMemory[y[0]][i]
                instructionMemory[y[0]][i] = instructionMemory[y[0]][i].lower()

    
    
    


def UpdateFile(filename):
    mcFile = open(filename,"w")
    i = '0x0'
    for i in instructionMemory:
        curr = '0x' + (''.join(instructionMemory[i][::-1]))
        mcFile.write (i+' '+curr+"\n")
    i = hex(int(i,16) + 4)
    mcFile.write(i+' $\n')
    for i in dataMemory:
        if i== '0x7fffffec':
            break
        curr = '0x'
        for j in dataMemory[i][::-1]:
            curr += '0'*(2-len(hex(j)[2:])) + hex(j)[2:]
        mcFile.write(i+' '+curr+'\n')
    

def run_RISC_simulator():
    global clk,isStepClicked
    flag=1
    while (hex(PC) in instructionMemory) and flag==1:
        Fetch()
        Decode()
        Execute()
        MemoryAccess()
        RegisterUpdate()
        clk+=1
        ui.updateRegisters(reg,clk)
        
        if isStepClicked==1:
            isStepClicked=0
            flag=0
    UpdateFile("output.mc")
    outFile = open("output.txt",'w')
    print("============= REGISTERS =============")
    outFile.write("============= REGISTERS =============\n")
    for i in range (len(reg)):
        print('x'+str(i)+' =',reg[i])
        outFile.write('x'+str(i)+' = '+str(reg[i])+'\n')
    print()
    outFile.write('\n')
    print("============= DATA MEMORY =============")
    outFile.write("============= DATA MEMORY =============\n")

    for i in dataMemory:
        print(i+' =',dataMemory[i])
        currStr = i + " = "
        for j in dataMemory[i]:
            currStr += hex(j)+' '
        outFile.write(currStr+ '\n')
    print()
    outFile.write('\n')
    print("PC = ",hex(PC))
    outFile.write("PC = "+hex(PC))
    print()
    outFile.write('\n')
    UpdateFile("output.mc")
    if hex(PC) not in instructionMemory:
        print("PROGRAM EXECUTED SUCCESSFULLY")
        ui.label_40.setText("PROGRAM EXECUTED SUCCESSFULLY")

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
main()
sys.exit(app.exec_())
