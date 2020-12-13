# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_bentry.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1058, 700)
        Form.setMinimumSize(QtCore.QSize(1058, 700))
        Form.setMaximumSize(QtCore.QSize(1058, 700))
        Form.setStyleSheet("QWidget{\n"
"    border: 4px solid grey;\n"
"    border-radius:5px;\n"
"\n"
"    background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 255, 240, 255), stop:1 rgba(161, 181, 255, 255));\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_2.setStyleSheet("background-color: transparent;\n"
"border-radius: 9px;\n"
"border:2px solid grey ;\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.find_bank_btn = QtWidgets.QPushButton(self.frame_2)
        self.find_bank_btn.setGeometry(QtCore.QRect(12, 12, 44, 42))
        self.find_bank_btn.setStyleSheet("border-top:0px;\n"
"border-right:0px;\n"
"border-left:0px;\n"
"border-radius:0px;")
        self.find_bank_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/Actions-document-preview-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.find_bank_btn.setIcon(icon)
        self.find_bank_btn.setIconSize(QtCore.QSize(40, 40))
        self.find_bank_btn.setObjectName("find_bank_btn")
        self.save_btn = QtWidgets.QPushButton(self.frame_2)
        self.save_btn.setGeometry(QtCore.QRect(64, 12, 44, 42))
        self.save_btn.setStyleSheet("border-top:0px;\n"
"border-right:0px;\n"
"border-left:0px;\n"
"border-radius:0px;")
        self.save_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_btn.setIcon(icon1)
        self.save_btn.setIconSize(QtCore.QSize(40, 40))
        self.save_btn.setObjectName("save_btn")
        self.add_bank = QtWidgets.QPushButton(self.frame_2)
        self.add_bank.setGeometry(QtCore.QRect(116, 12, 44, 42))
        self.add_bank.setStyleSheet("border-top:0px;\n"
"border-right:0px;\n"
"border-left:0px;\n"
"border-radius:0px;")
        self.add_bank.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/math-add-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_bank.setIcon(icon2)
        self.add_bank.setIconSize(QtCore.QSize(40, 40))
        self.add_bank.setObjectName("add_bank")
        self.previous_bank = QtWidgets.QPushButton(self.frame_2)
        self.previous_bank.setGeometry(QtCore.QRect(168, 12, 44, 42))
        self.previous_bank.setStyleSheet("border-top:0px;\n"
"border-right:0px;\n"
"border-left:0px;\n"
"border-radius:0px;")
        self.previous_bank.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/Actions-go-previous-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.previous_bank.setIcon(icon3)
        self.previous_bank.setIconSize(QtCore.QSize(40, 40))
        self.previous_bank.setShortcut("")
        self.previous_bank.setObjectName("previous_bank")
        self.next_bank = QtWidgets.QPushButton(self.frame_2)
        self.next_bank.setGeometry(QtCore.QRect(220, 12, 44, 42))
        self.next_bank.setStyleSheet("border-top:0px;\n"
"border-right:0px;\n"
"border-left:0px;\n"
"border-radius:0px;")
        self.next_bank.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/Actions-go-next-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.next_bank.setIcon(icon4)
        self.next_bank.setIconSize(QtCore.QSize(40, 40))
        self.next_bank.setObjectName("next_bank")
        self.change_to_design = QtWidgets.QPushButton(self.frame_2)
        self.change_to_design.setGeometry(QtCore.QRect(272, 12, 44, 42))
        self.change_to_design.setStyleSheet("border-top:0px;\n"
"border-right:0px;\n"
"border-left:0px;\n"
"border-radius:0px;")
        self.change_to_design.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/newPrefix/Letter-D-lg-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.change_to_design.setIcon(icon5)
        self.change_to_design.setIconSize(QtCore.QSize(40, 40))
        self.change_to_design.setObjectName("change_to_design")
        self.setting_btn = QtWidgets.QPushButton(self.frame_2)
        self.setting_btn.setGeometry(QtCore.QRect(324, 12, 44, 42))
        self.setting_btn.setStyleSheet("border-top:0px;\n"
"border-right:0px;\n"
"border-left:0px;\n"
"border-radius:0px;")
        self.setting_btn.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/newPrefix/Settings-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setting_btn.setIcon(icon6)
        self.setting_btn.setIconSize(QtCore.QSize(40, 40))
        self.setting_btn.setObjectName("setting_btn")
        self.setting_btn_2 = QtWidgets.QPushButton(self.frame_2)
        self.setting_btn_2.setGeometry(QtCore.QRect(380, 12, 44, 42))
        self.setting_btn_2.setStyleSheet("border-top:0px;\n"
"border-right:0px;\n"
"border-left:0px;\n"
"border-radius:0px;")
        self.setting_btn_2.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/newPrefix/Refresh-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setting_btn_2.setIcon(icon7)
        self.setting_btn_2.setIconSize(QtCore.QSize(40, 40))
        self.setting_btn_2.setObjectName("setting_btn_2")
        self.verticalLayout.addWidget(self.frame_2)
        self.groupBox = QtWidgets.QGroupBox(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("\n"
"QGroupBox {\n"
"    border: 2px solid gray;\n"
"    border-radius: 9px;\n"
"    margin-top: 0.8em;\n"
"    \n"
"background-color:transparent;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 40px;\n"
"    padding: 0 3px 0 3px;\n"
"}")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setContentsMargins(-1, 25, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.bank_name = QtWidgets.QComboBox(self.groupBox)
        self.bank_name.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bank_name.setFont(font)
        self.bank_name.setStyleSheet("QComboBox{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:3px;\n"
"}\n"
"QComboBox {\n"
"    border: 1px solid gray;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1,                 stop:0 rgba(0, 96, 255, 255), stop:1 rgba(218, 255, 251, 255));\n"
"    image: url(:/newPrefix/dropdown.png);\n"
"    width: 50px;\n"
"}")
        self.bank_name.setObjectName("bank_name")
        self.gridLayout.addWidget(self.bank_name, 0, 2, 1, 1)
        self.bfile_code = QtWidgets.QLineEdit(self.groupBox)
        self.bfile_code.setMinimumSize(QtCore.QSize(0, 40))
        self.bfile_code.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bfile_code.setFont(font)
        self.bfile_code.setStyleSheet("QLineEdit{\n"
"border:1px solid gray;\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:3px;\n"
"}")
        self.bfile_code.setObjectName("bfile_code")
        self.gridLayout.addWidget(self.bfile_code, 1, 4, 1, 1)
        self.brnach_name = QtWidgets.QComboBox(self.groupBox)
        self.brnach_name.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.brnach_name.setFont(font)
        self.brnach_name.setStyleSheet("QComboBox{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:3px;\n"
"}\n"
"QComboBox {\n"
"    border: 1px solid gray;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1,                 stop:0 rgba(0, 96, 255, 255), stop:1 rgba(218, 255, 251, 255));\n"
"    image: url(:/newPrefix/dropdown.png);\n"
"    width: 50px;\n"
"}")
        self.brnach_name.setObjectName("brnach_name")
        self.gridLayout.addWidget(self.brnach_name, 0, 4, 1, 1)
        self.label_129 = QtWidgets.QLabel(self.groupBox)
        self.label_129.setMinimumSize(QtCore.QSize(0, 40))
        self.label_129.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.label_129.setFont(font)
        self.label_129.setStyleSheet("background-color:transparent; border:0px")
        self.label_129.setAlignment(QtCore.Qt.AlignCenter)
        self.label_129.setObjectName("label_129")
        self.gridLayout.addWidget(self.label_129, 0, 0, 1, 1)
        self.label_130 = QtWidgets.QLabel(self.groupBox)
        self.label_130.setMinimumSize(QtCore.QSize(0, 40))
        self.label_130.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.label_130.setFont(font)
        self.label_130.setStyleSheet("background-color:transparent; border:0px")
        self.label_130.setAlignment(QtCore.Qt.AlignCenter)
        self.label_130.setObjectName("label_130")
        self.gridLayout.addWidget(self.label_130, 0, 3, 1, 1)
        self.label_132 = QtWidgets.QLabel(self.groupBox)
        self.label_132.setMinimumSize(QtCore.QSize(0, 40))
        self.label_132.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.label_132.setFont(font)
        self.label_132.setStyleSheet("background-color:transparent; border:0px")
        self.label_132.setAlignment(QtCore.Qt.AlignCenter)
        self.label_132.setObjectName("label_132")
        self.gridLayout.addWidget(self.label_132, 1, 3, 1, 1)
        self.provience = QtWidgets.QLineEdit(self.groupBox)
        self.provience.setMinimumSize(QtCore.QSize(0, 40))
        self.provience.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.provience.setFont(font)
        self.provience.setStyleSheet("QLineEdit{\n"
"border:1px solid gray;\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:3px;\n"
"}")
        self.provience.setObjectName("provience")
        self.gridLayout.addWidget(self.provience, 1, 2, 1, 1)
        self.label_131 = QtWidgets.QLabel(self.groupBox)
        self.label_131.setMinimumSize(QtCore.QSize(0, 40))
        self.label_131.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.label_131.setFont(font)
        self.label_131.setStyleSheet("background-color:transparent; border:0px")
        self.label_131.setAlignment(QtCore.Qt.AlignCenter)
        self.label_131.setObjectName("label_131")
        self.gridLayout.addWidget(self.label_131, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setStyleSheet("background-color:transparent; border:0px")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, -1)
        self.horizontalLayout.setSpacing(12)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox_18 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_18.setMinimumSize(QtCore.QSize(500, 0))
        self.groupBox_18.setMaximumSize(QtCore.QSize(600, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_18.setFont(font)
        self.groupBox_18.setStyleSheet("\n"
"QGroupBox {\n"
"    border: 2px solid gray;\n"
"    border-radius: 9px;\n"
"    margin-top: 0.8em;\n"
"    \n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 40px;\n"
"    padding: 0 3px 0 3px;\n"
"}")
        self.groupBox_18.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_18.setObjectName("groupBox_18")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_18)
        self.gridLayout_3.setContentsMargins(12, 20, -1, -1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_32 = QtWidgets.QFrame(self.groupBox_18)
        self.frame_32.setMinimumSize(QtCore.QSize(150, 0))
        self.frame_32.setMaximumSize(QtCore.QSize(250, 16777215))
        self.frame_32.setStyleSheet("background-color: transparent; border:0px;")
        self.frame_32.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_32.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_32.setObjectName("frame_32")
        self.verticalLayout_33 = QtWidgets.QVBoxLayout(self.frame_32)
        self.verticalLayout_33.setContentsMargins(0, 12, 0, 8)
        self.verticalLayout_33.setSpacing(10)
        self.verticalLayout_33.setObjectName("verticalLayout_33")
        self.label_104 = QtWidgets.QLabel(self.frame_32)
        self.label_104.setMinimumSize(QtCore.QSize(0, 40))
        self.label_104.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.label_104.setFont(font)
        self.label_104.setAlignment(QtCore.Qt.AlignCenter)
        self.label_104.setObjectName("label_104")
        self.verticalLayout_33.addWidget(self.label_104)
        self.label_105 = QtWidgets.QLabel(self.frame_32)
        self.label_105.setMinimumSize(QtCore.QSize(0, 40))
        self.label_105.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.label_105.setFont(font)
        self.label_105.setAlignment(QtCore.Qt.AlignCenter)
        self.label_105.setObjectName("label_105")
        self.verticalLayout_33.addWidget(self.label_105)
        self.label_106 = QtWidgets.QLabel(self.frame_32)
        self.label_106.setMinimumSize(QtCore.QSize(0, 40))
        self.label_106.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.label_106.setFont(font)
        self.label_106.setAlignment(QtCore.Qt.AlignCenter)
        self.label_106.setObjectName("label_106")
        self.verticalLayout_33.addWidget(self.label_106)
        self.label_107 = QtWidgets.QLabel(self.frame_32)
        self.label_107.setMinimumSize(QtCore.QSize(0, 40))
        self.label_107.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.label_107.setFont(font)
        self.label_107.setAlignment(QtCore.Qt.AlignCenter)
        self.label_107.setObjectName("label_107")
        self.verticalLayout_33.addWidget(self.label_107)
        self.label_108 = QtWidgets.QLabel(self.frame_32)
        self.label_108.setMinimumSize(QtCore.QSize(0, 40))
        self.label_108.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.label_108.setFont(font)
        self.label_108.setAlignment(QtCore.Qt.AlignCenter)
        self.label_108.setObjectName("label_108")
        self.verticalLayout_33.addWidget(self.label_108)
        self.label_109 = QtWidgets.QLabel(self.frame_32)
        self.label_109.setMinimumSize(QtCore.QSize(0, 40))
        self.label_109.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.label_109.setFont(font)
        self.label_109.setAlignment(QtCore.Qt.AlignCenter)
        self.label_109.setObjectName("label_109")
        self.verticalLayout_33.addWidget(self.label_109)
        self.gridLayout_3.addWidget(self.frame_32, 0, 0, 2, 1)
        self.frame_33 = QtWidgets.QFrame(self.groupBox_18)
        self.frame_33.setMaximumSize(QtCore.QSize(350, 16777215))
        self.frame_33.setStyleSheet("background-color: transparent; border:0px")
        self.frame_33.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_33.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_33.setObjectName("frame_33")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_33)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.bclient_name = QtWidgets.QLineEdit(self.frame_33)
        self.bclient_name.setMinimumSize(QtCore.QSize(0, 40))
        self.bclient_name.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bclient_name.setFont(font)
        self.bclient_name.setStyleSheet("QLineEdit{\n"
"border:1px solid gray;\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:3px;\n"
"}")
        self.bclient_name.setObjectName("bclient_name")
        self.verticalLayout_3.addWidget(self.bclient_name)
        self.bcontactt_no = QtWidgets.QLineEdit(self.frame_33)
        self.bcontactt_no.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bcontactt_no.setFont(font)
        self.bcontactt_no.setStyleSheet("QLineEdit{\n"
"border:1px solid gray;\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:3px;\n"
"}")
        self.bcontactt_no.setObjectName("bcontactt_no")
        self.verticalLayout_3.addWidget(self.bcontactt_no)
        self.baddress = QtWidgets.QLineEdit(self.frame_33)
        self.baddress.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.baddress.setFont(font)
        self.baddress.setStyleSheet("QLineEdit{\n"
"border:1px solid gray;\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:3px;\n"
"}")
        self.baddress.setText("")
        self.baddress.setObjectName("baddress")
        self.verticalLayout_3.addWidget(self.baddress)
        self.frame_15 = QtWidgets.QFrame(self.frame_33)
        self.frame_15.setMaximumSize(QtCore.QSize(350, 40))
        self.frame_15.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout(self.frame_15)
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.sv_bd = QtWidgets.QLineEdit(self.frame_15)
        self.sv_bd.setMinimumSize(QtCore.QSize(0, 40))
        self.sv_bd.setMaximumSize(QtCore.QSize(743, 1176))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sv_bd.setFont(font)
        self.sv_bd.setStyleSheet("QLineEdit{\n"
"border:1px solid gray;\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:3px;\n"
"}")
        self.sv_bd.setObjectName("sv_bd")
        self.horizontalLayout_28.addWidget(self.sv_bd)
        self.sv_mm = QtWidgets.QLineEdit(self.frame_15)
        self.sv_mm.setMinimumSize(QtCore.QSize(0, 40))
        self.sv_mm.setMaximumSize(QtCore.QSize(919, 624))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sv_mm.setFont(font)
        self.sv_mm.setStyleSheet("QLineEdit{\n"
"border:1px solid gray;\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:3px;\n"
"}")
        self.sv_mm.setObjectName("sv_mm")
        self.horizontalLayout_28.addWidget(self.sv_mm)
        self.sv_yy = QtWidgets.QLineEdit(self.frame_15)
        self.sv_yy.setMinimumSize(QtCore.QSize(180, 40))
        self.sv_yy.setMaximumSize(QtCore.QSize(627, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sv_yy.setFont(font)
        self.sv_yy.setStyleSheet("QLineEdit{\n"
"border:1px solid gray;\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:3px;\n"
"}")
        self.sv_yy.setObjectName("sv_yy")
        self.horizontalLayout_28.addWidget(self.sv_yy)
        self.verticalLayout_3.addWidget(self.frame_15)
        self.frame_16 = QtWidgets.QFrame(self.frame_33)
        self.frame_16.setMaximumSize(QtCore.QSize(350, 40))
        self.frame_16.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout(self.frame_16)
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.id_dd = QtWidgets.QLineEdit(self.frame_16)
        self.id_dd.setMinimumSize(QtCore.QSize(0, 40))
        self.id_dd.setMaximumSize(QtCore.QSize(743, 1176))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.id_dd.setFont(font)
        self.id_dd.setStyleSheet("QLineEdit{\n"
"border:1px solid gray;\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:3px;\n"
"}")
        self.id_dd.setObjectName("id_dd")
        self.horizontalLayout_29.addWidget(self.id_dd)
        self.id_mm = QtWidgets.QLineEdit(self.frame_16)
        self.id_mm.setMinimumSize(QtCore.QSize(0, 40))
        self.id_mm.setMaximumSize(QtCore.QSize(919, 624))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.id_mm.setFont(font)
        self.id_mm.setStyleSheet("QLineEdit{\n"
"border:1px solid gray;\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:3px;\n"
"}")
        self.id_mm.setObjectName("id_mm")
        self.horizontalLayout_29.addWidget(self.id_mm)
        self.id_yy = QtWidgets.QLineEdit(self.frame_16)
        self.id_yy.setMinimumSize(QtCore.QSize(180, 40))
        self.id_yy.setMaximumSize(QtCore.QSize(627, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.id_yy.setFont(font)
        self.id_yy.setStyleSheet("QLineEdit{\n"
"border:1px solid gray;\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:3px;\n"
"}")
        self.id_yy.setObjectName("id_yy")
        self.horizontalLayout_29.addWidget(self.id_yy)
        self.verticalLayout_3.addWidget(self.frame_16)
        self.frame_17 = QtWidgets.QFrame(self.frame_33)
        self.frame_17.setMaximumSize(QtCore.QSize(350, 40))
        self.frame_17.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout(self.frame_17)
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.fd_dd = QtWidgets.QLineEdit(self.frame_17)
        self.fd_dd.setMinimumSize(QtCore.QSize(0, 40))
        self.fd_dd.setMaximumSize(QtCore.QSize(743, 1176))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fd_dd.setFont(font)
        self.fd_dd.setStyleSheet("QLineEdit{\n"
"border:1px solid gray;\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:3px;\n"
"}")
        self.fd_dd.setObjectName("fd_dd")
        self.horizontalLayout_30.addWidget(self.fd_dd)
        self.fd_mm = QtWidgets.QLineEdit(self.frame_17)
        self.fd_mm.setMinimumSize(QtCore.QSize(0, 40))
        self.fd_mm.setMaximumSize(QtCore.QSize(919, 624))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fd_mm.setFont(font)
        self.fd_mm.setStyleSheet("QLineEdit{\n"
"border:1px solid gray;\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:3px;\n"
"}")
        self.fd_mm.setObjectName("fd_mm")
        self.horizontalLayout_30.addWidget(self.fd_mm)
        self.fd_yy = QtWidgets.QLineEdit(self.frame_17)
        self.fd_yy.setMinimumSize(QtCore.QSize(180, 40))
        self.fd_yy.setMaximumSize(QtCore.QSize(627, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fd_yy.setFont(font)
        self.fd_yy.setStyleSheet("QLineEdit{\n"
"border:1px solid gray;\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:3px;\n"
"}")
        self.fd_yy.setObjectName("fd_yy")
        self.horizontalLayout_30.addWidget(self.fd_yy)
        self.verticalLayout_3.addWidget(self.frame_17)
        self.gridLayout_3.addWidget(self.frame_33, 0, 1, 2, 1)
        self.horizontalLayout.addWidget(self.groupBox_18)
        self.groupBox_19 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_19.setMinimumSize(QtCore.QSize(500, 0))
        self.groupBox_19.setMaximumSize(QtCore.QSize(600, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_19.setFont(font)
        self.groupBox_19.setStyleSheet("\n"
"QGroupBox {\n"
"    border: 2px solid gray;\n"
"    border-radius: 9px;\n"
"    margin-top: 0.8em;\n"
"    \n"
"background-color:transparent;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 40px;\n"
"    padding: 0 3px 0 3px;\n"
"}")
        self.groupBox_19.setObjectName("groupBox_19")
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout(self.groupBox_19)
        self.horizontalLayout_31.setContentsMargins(12, 8, 0, 0)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.frame_34 = QtWidgets.QFrame(self.groupBox_19)
        self.frame_34.setMinimumSize(QtCore.QSize(150, 0))
        self.frame_34.setMaximumSize(QtCore.QSize(150, 16777215))
        self.frame_34.setStyleSheet("background-color: transparent;\n"
"border:0px;")
        self.frame_34.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_34.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_34.setObjectName("frame_34")
        self.verticalLayout_34 = QtWidgets.QVBoxLayout(self.frame_34)
        self.verticalLayout_34.setContentsMargins(0, 20, 0, 0)
        self.verticalLayout_34.setSpacing(12)
        self.verticalLayout_34.setObjectName("verticalLayout_34")
        self.label_110 = QtWidgets.QLabel(self.frame_34)
        self.label_110.setMinimumSize(QtCore.QSize(0, 40))
        self.label_110.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.label_110.setFont(font)
        self.label_110.setStyleSheet("border: 0px;")
        self.label_110.setAlignment(QtCore.Qt.AlignCenter)
        self.label_110.setObjectName("label_110")
        self.verticalLayout_34.addWidget(self.label_110)
        self.label_111 = QtWidgets.QLabel(self.frame_34)
        self.label_111.setMinimumSize(QtCore.QSize(0, 40))
        self.label_111.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.label_111.setFont(font)
        self.label_111.setAlignment(QtCore.Qt.AlignCenter)
        self.label_111.setObjectName("label_111")
        self.verticalLayout_34.addWidget(self.label_111)
        self.label_112 = QtWidgets.QLabel(self.frame_34)
        self.label_112.setMinimumSize(QtCore.QSize(0, 40))
        self.label_112.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.label_112.setFont(font)
        self.label_112.setAlignment(QtCore.Qt.AlignCenter)
        self.label_112.setObjectName("label_112")
        self.verticalLayout_34.addWidget(self.label_112)
        self.label_113 = QtWidgets.QLabel(self.frame_34)
        self.label_113.setMinimumSize(QtCore.QSize(0, 40))
        self.label_113.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.label_113.setFont(font)
        self.label_113.setAlignment(QtCore.Qt.AlignCenter)
        self.label_113.setObjectName("label_113")
        self.verticalLayout_34.addWidget(self.label_113)
        self.label_114 = QtWidgets.QLabel(self.frame_34)
        self.label_114.setMinimumSize(QtCore.QSize(0, 40))
        self.label_114.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.label_114.setFont(font)
        self.label_114.setAlignment(QtCore.Qt.AlignCenter)
        self.label_114.setObjectName("label_114")
        self.verticalLayout_34.addWidget(self.label_114)
        self.label_115 = QtWidgets.QLabel(self.frame_34)
        self.label_115.setMinimumSize(QtCore.QSize(0, 40))
        self.label_115.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.label_115.setFont(font)
        self.label_115.setAlignment(QtCore.Qt.AlignCenter)
        self.label_115.setObjectName("label_115")
        self.verticalLayout_34.addWidget(self.label_115)
        self.horizontalLayout_31.addWidget(self.frame_34, 0, QtCore.Qt.AlignTop)
        self.frame_35 = QtWidgets.QFrame(self.groupBox_19)
        self.frame_35.setMaximumSize(QtCore.QSize(350, 16777215))
        self.frame_35.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_35.setStyleSheet("background-color: transparent;\n"
"border : 0px;")
        self.frame_35.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_35.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_35.setObjectName("frame_35")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_35)
        self.verticalLayout_4.setContentsMargins(-1, 20, -1, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.remarks_bank = QtWidgets.QLineEdit(self.frame_35)
        self.remarks_bank.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.remarks_bank.setFont(font)
        self.remarks_bank.setStyleSheet("QLineEdit{\n"
"border:1px solid gray;\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:3px;\n"
"}")
        self.remarks_bank.setObjectName("remarks_bank")
        self.verticalLayout_4.addWidget(self.remarks_bank)
        self.bfmv = QtWidgets.QLineEdit(self.frame_35)
        self.bfmv.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bfmv.setFont(font)
        self.bfmv.setStyleSheet("QLineEdit{\n"
"border:1px solid gray;\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:3px;\n"
"}")
        self.bfmv.setObjectName("bfmv")
        self.verticalLayout_4.addWidget(self.bfmv)
        self.bcharges = QtWidgets.QLineEdit(self.frame_35)
        self.bcharges.setMinimumSize(QtCore.QSize(0, 40))
        self.bcharges.setMaximumSize(QtCore.QSize(350, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bcharges.setFont(font)
        self.bcharges.setStyleSheet("QLineEdit{\n"
"border:1px solid gray;\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:3px;\n"
"}")
        self.bcharges.setObjectName("bcharges")
        self.verticalLayout_4.addWidget(self.bcharges)
        self.binitial_payment = QtWidgets.QLineEdit(self.frame_35)
        self.binitial_payment.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.binitial_payment.setFont(font)
        self.binitial_payment.setStyleSheet("QLineEdit{\n"
"border:1px solid gray;\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:3px;\n"
"}")
        self.binitial_payment.setObjectName("binitial_payment")
        self.verticalLayout_4.addWidget(self.binitial_payment)
        self.bfinal_payment = QtWidgets.QLineEdit(self.frame_35)
        self.bfinal_payment.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bfinal_payment.setFont(font)
        self.bfinal_payment.setStyleSheet("QLineEdit{\n"
"border:1px solid gray;\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:3px;\n"
"}")
        self.bfinal_payment.setObjectName("bfinal_payment")
        self.verticalLayout_4.addWidget(self.bfinal_payment)
        self.bdew_balance = QtWidgets.QLineEdit(self.frame_35)
        self.bdew_balance.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bdew_balance.setFont(font)
        self.bdew_balance.setStyleSheet("QLineEdit{\n"
"border:1px solid gray;\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:3px;\n"
"}")
        self.bdew_balance.setObjectName("bdew_balance")
        self.verticalLayout_4.addWidget(self.bdew_balance)
        self.horizontalLayout_31.addWidget(self.frame_35)
        self.horizontalLayout.addWidget(self.groupBox_19)
        self.verticalLayout.addWidget(self.frame)
        self.frame_3 = QtWidgets.QFrame(Form)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_3.setStyleSheet("background-color: transparent;\n"
"border: 0px;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.frame_3)
        self.pushButton.setMinimumSize(QtCore.QSize(70, 40))
        self.pushButton.setStyleSheet("border:2px solid;\n"
"border-radius:9px;\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 96, 255, 255), stop:1 rgba(218, 255, 251, 255));")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_2.setMinimumSize(QtCore.QSize(70, 40))
        self.pushButton_2.setStyleSheet("border:2px solid;\n"
"border-radius:9px;\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 96, 255, 255), stop:1 rgba(218, 255, 251, 255));")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.verticalLayout.addWidget(self.frame_3, 0, QtCore.Qt.AlignHCenter)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "Bank Information"))
        self.label_129.setText(_translate("Form", "Bank Name"))
        self.label_130.setText(_translate("Form", "Branch Name"))
        self.label_132.setText(_translate("Form", "File Code"))
        self.label_131.setText(_translate("Form", "Province"))
        self.groupBox_18.setTitle(_translate("Form", "General Information"))
        self.label_104.setText(_translate("Form", "Client Name"))
        self.label_105.setText(_translate("Form", "Contact No"))
        self.label_106.setText(_translate("Form", "Address"))
        self.label_107.setText(_translate("Form", "Site Visit Date"))
        self.label_108.setText(_translate("Form", "Initial Date"))
        self.label_109.setText(_translate("Form", "Final Date"))
        self.sv_bd.setPlaceholderText(_translate("Form", "DD"))
        self.sv_mm.setPlaceholderText(_translate("Form", "MM"))
        self.sv_yy.setPlaceholderText(_translate("Form", "YYYY"))
        self.id_dd.setPlaceholderText(_translate("Form", "DD"))
        self.id_mm.setPlaceholderText(_translate("Form", "MM"))
        self.id_yy.setPlaceholderText(_translate("Form", "YYYY"))
        self.fd_dd.setPlaceholderText(_translate("Form", "DD"))
        self.fd_mm.setPlaceholderText(_translate("Form", "MM"))
        self.fd_yy.setPlaceholderText(_translate("Form", "YYYY"))
        self.groupBox_19.setTitle(_translate("Form", "Payment Information"))
        self.label_110.setText(_translate("Form", "Remarks"))
        self.label_111.setText(_translate("Form", "fmv"))
        self.label_112.setText(_translate("Form", "Charges"))
        self.label_113.setText(_translate("Form", "Initial Payment"))
        self.label_114.setText(_translate("Form", "Final Payment"))
        self.label_115.setText(_translate("Form", "Dew Balance"))
        self.pushButton.setText(_translate("Form", "OK"))
        self.pushButton_2.setText(_translate("Form", "Cancle"))
import source_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
