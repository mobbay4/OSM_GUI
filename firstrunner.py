# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'firstrunner.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

import pandas as pd
import numpy as np
#from openpyxl.workbook import Workbook
import folium
from folium.plugins import MarkerCluster
from PyQt5.QtWidgets import QMessageBox, QTableWidget,QTableWidgetItem, QProgressDialog
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_lcd_display(object):
    def setupUi(self, lcd_display):
        lcd_display.setObjectName("lcd_display")
        lcd_display.setEnabled(True)
        lcd_display.resize(2672, 1930)
        font = QtGui.QFont()
        font.setPointSize(8)
        lcd_display.setFont(font)
        self.centralwidget = QtWidgets.QWidget(lcd_display)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_28.setAutoFillBackground(True)
        self.label_28.setObjectName("label_28")
        self.verticalLayout_3.addWidget(self.label_28)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 5, 9, 1, 1)
        self.QComboBox_Longetude_val = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.QComboBox_Longetude_val.sizePolicy().hasHeightForWidth())
        self.QComboBox_Longetude_val.setSizePolicy(sizePolicy)
        self.QComboBox_Longetude_val.setObjectName("QComboBox_Longetude_val")
        self.gridLayout_4.addWidget(self.QComboBox_Longetude_val, 6, 6, 1, 4)
        self.QComboBox_Timstamp = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.QComboBox_Timstamp.sizePolicy().hasHeightForWidth())
        self.QComboBox_Timstamp.setSizePolicy(sizePolicy)
        self.QComboBox_Timstamp.setObjectName("QComboBox_Timstamp")
        self.gridLayout_4.addWidget(self.QComboBox_Timstamp, 6, 11, 1, 2)
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.gridLayout_4.addWidget(self.label_20, 0, 1, 1, 5)
        self.bt_sort = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt_sort.sizePolicy().hasHeightForWidth())
        self.bt_sort.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.bt_sort.setFont(font)
        self.bt_sort.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_sort.setObjectName("bt_sort")
        self.gridLayout_4.addWidget(self.bt_sort, 7, 11, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 7, 13, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem2, 3, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem3, 6, 13, 1, 1)
        self.QComboBox_Latetude_val = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.QComboBox_Latetude_val.sizePolicy().hasHeightForWidth())
        self.QComboBox_Latetude_val.setSizePolicy(sizePolicy)
        self.QComboBox_Latetude_val.setCurrentText("")
        self.QComboBox_Latetude_val.setObjectName("QComboBox_Latetude_val")
        self.gridLayout_4.addWidget(self.QComboBox_Latetude_val, 6, 1, 1, 4)
        self.text_filepath = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.text_filepath.setFont(font)
        self.text_filepath.setToolTip("")
        self.text_filepath.setObjectName("text_filepath")
        self.gridLayout_4.addWidget(self.text_filepath, 1, 1, 1, 9)
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.gridLayout_4.addWidget(self.label_25, 4, 1, 1, 5)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem4, 5, 4, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem5, 5, 7, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.centralwidget)
        self.label_32.setObjectName("label_32")
        self.gridLayout_4.addWidget(self.label_32, 2, 1, 1, 5)
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        self.label_18.setObjectName("label_18")
        self.gridLayout_4.addWidget(self.label_18, 5, 11, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem6, 6, 5, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 5, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setObjectName("label_16")
        self.gridLayout_4.addWidget(self.label_16, 5, 6, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem7, 5, 3, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.centralwidget)
        self.label_29.setObjectName("label_29")
        self.gridLayout_4.addWidget(self.label_29, 5, 12, 1, 1)
        self.bt_fileread = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.bt_fileread.sizePolicy().hasHeightForWidth())
        self.bt_fileread.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.bt_fileread.setFont(font)
        self.bt_fileread.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_fileread.setToolTip("")
        self.bt_fileread.setStatusTip("")
        self.bt_fileread.setWhatsThis("")
        self.bt_fileread.setObjectName("bt_fileread")
        self.gridLayout_4.addWidget(self.bt_fileread, 1, 11, 1, 3)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem8, 6, 10, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_4)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem9)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem10)
        spacerItem11 = QtWidgets.QSpacerItem(17, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem11)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setObjectName("label_19")
        self.gridLayout_3.addWidget(self.label_19, 6, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 4, 0, 1, 1)
        self.checkbox_filter_t1 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkbox_filter_t1.setObjectName("checkbox_filter_t1")
        self.gridLayout_3.addWidget(self.checkbox_filter_t1, 9, 6, 1, 1)
        self.checkbox_filter_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkbox_filter_2.setObjectName("checkbox_filter_2")
        self.gridLayout_3.addWidget(self.checkbox_filter_2, 3, 6, 1, 1)
        self.text_filter_par1 = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_filter_par1.sizePolicy().hasHeightForWidth())
        self.text_filter_par1.setSizePolicy(sizePolicy)
        self.text_filter_par1.setText("")
        self.text_filter_par1.setObjectName("text_filter_par1")
        self.gridLayout_3.addWidget(self.text_filter_par1, 2, 3, 1, 2)
        self.checkbox_filter_1 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkbox_filter_1.setObjectName("checkbox_filter_1")
        self.gridLayout_3.addWidget(self.checkbox_filter_1, 2, 6, 1, 1)
        self.comboBox_filter_op2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_filter_op2.setObjectName("comboBox_filter_op2")
        self.comboBox_filter_op2.addItem("")
        self.comboBox_filter_op2.addItem("")
        self.comboBox_filter_op2.addItem("")
        self.comboBox_filter_op2.addItem("")
        self.comboBox_filter_op2.addItem("")
        self.comboBox_filter_op2.addItem("")
        self.gridLayout_3.addWidget(self.comboBox_filter_op2, 3, 2, 1, 1)
        self.comboBox_filter_op1 = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_filter_op1.sizePolicy().hasHeightForWidth())
        self.comboBox_filter_op1.setSizePolicy(sizePolicy)
        self.comboBox_filter_op1.setObjectName("comboBox_filter_op1")
        self.comboBox_filter_op1.addItem("")
        self.comboBox_filter_op1.addItem("")
        self.comboBox_filter_op1.addItem("")
        self.comboBox_filter_op1.addItem("")
        self.comboBox_filter_op1.addItem("")
        self.comboBox_filter_op1.addItem("")
        self.gridLayout_3.addWidget(self.comboBox_filter_op1, 2, 2, 1, 1)
        self.comboBox_filter_par2 = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_filter_par2.sizePolicy().hasHeightForWidth())
        self.comboBox_filter_par2.setSizePolicy(sizePolicy)
        self.comboBox_filter_par2.setObjectName("comboBox_filter_par2")
        self.gridLayout_3.addWidget(self.comboBox_filter_par2, 3, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 1, 1, 1, 1)
        self.comboBox_filter_par5 = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_filter_par5.sizePolicy().hasHeightForWidth())
        self.comboBox_filter_par5.setSizePolicy(sizePolicy)
        self.comboBox_filter_par5.setObjectName("comboBox_filter_par5")
        self.gridLayout_3.addWidget(self.comboBox_filter_par5, 6, 1, 1, 1)
        self.comboBox_filter_op4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_filter_op4.setObjectName("comboBox_filter_op4")
        self.comboBox_filter_op4.addItem("")
        self.comboBox_filter_op4.addItem("")
        self.comboBox_filter_op4.addItem("")
        self.comboBox_filter_op4.addItem("")
        self.comboBox_filter_op4.addItem("")
        self.comboBox_filter_op4.addItem("")
        self.gridLayout_3.addWidget(self.comboBox_filter_op4, 5, 2, 1, 1)
        self.comboBox_filter_op6 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_filter_op6.setObjectName("comboBox_filter_op6")
        self.comboBox_filter_op6.addItem("")
        self.comboBox_filter_op6.addItem("")
        self.comboBox_filter_op6.addItem("")
        self.comboBox_filter_op6.addItem("")
        self.comboBox_filter_op6.addItem("")
        self.comboBox_filter_op6.addItem("")
        self.gridLayout_3.addWidget(self.comboBox_filter_op6, 7, 2, 1, 1)
        self.text_filter_par2 = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_filter_par2.sizePolicy().hasHeightForWidth())
        self.text_filter_par2.setSizePolicy(sizePolicy)
        self.text_filter_par2.setText("")
        self.text_filter_par2.setObjectName("text_filter_par2")
        self.gridLayout_3.addWidget(self.text_filter_par2, 3, 3, 1, 2)
        self.checkbox_filter_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkbox_filter_4.setObjectName("checkbox_filter_4")
        self.gridLayout_3.addWidget(self.checkbox_filter_4, 5, 6, 1, 1)
        self.comboBox_filter_par4 = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_filter_par4.sizePolicy().hasHeightForWidth())
        self.comboBox_filter_par4.setSizePolicy(sizePolicy)
        self.comboBox_filter_par4.setObjectName("comboBox_filter_par4")
        self.gridLayout_3.addWidget(self.comboBox_filter_par4, 5, 1, 1, 1)
        self.comboBox_filter_op_t2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_filter_op_t2.setObjectName("comboBox_filter_op_t2")
        self.comboBox_filter_op_t2.addItem("")
        self.comboBox_filter_op_t2.addItem("")
        self.comboBox_filter_op_t2.addItem("")
        self.comboBox_filter_op_t2.addItem("")
        self.comboBox_filter_op_t2.addItem("")
        self.comboBox_filter_op_t2.addItem("")
        self.gridLayout_3.addWidget(self.comboBox_filter_op_t2, 10, 2, 1, 1)
        self.comboBox_filter_op5 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_filter_op5.setObjectName("comboBox_filter_op5")
        self.comboBox_filter_op5.addItem("")
        self.comboBox_filter_op5.addItem("")
        self.comboBox_filter_op5.addItem("")
        self.comboBox_filter_op5.addItem("")
        self.comboBox_filter_op5.addItem("")
        self.comboBox_filter_op5.addItem("")
        self.gridLayout_3.addWidget(self.comboBox_filter_op5, 6, 2, 1, 1)
        self.comboBox_filter_time2 = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_filter_time2.sizePolicy().hasHeightForWidth())
        self.comboBox_filter_time2.setSizePolicy(sizePolicy)
        self.comboBox_filter_time2.setObjectName("comboBox_filter_time2")
        self.gridLayout_3.addWidget(self.comboBox_filter_time2, 10, 1, 1, 1)
        self.checkbox_filter_6 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkbox_filter_6.setObjectName("checkbox_filter_6")
        self.gridLayout_3.addWidget(self.checkbox_filter_6, 7, 6, 1, 1)
        self.comboBox_filter_par3 = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_filter_par3.sizePolicy().hasHeightForWidth())
        self.comboBox_filter_par3.setSizePolicy(sizePolicy)
        self.comboBox_filter_par3.setObjectName("comboBox_filter_par3")
        self.gridLayout_3.addWidget(self.comboBox_filter_par3, 4, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 3, 0, 1, 1)
        self.comboBox_filter_op_t1 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_filter_op_t1.setObjectName("comboBox_filter_op_t1")
        self.comboBox_filter_op_t1.addItem("")
        self.comboBox_filter_op_t1.addItem("")
        self.comboBox_filter_op_t1.addItem("")
        self.comboBox_filter_op_t1.addItem("")
        self.comboBox_filter_op_t1.addItem("")
        self.comboBox_filter_op_t1.addItem("")
        self.gridLayout_3.addWidget(self.comboBox_filter_op_t1, 9, 2, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setObjectName("label_21")
        self.gridLayout_3.addWidget(self.label_21, 7, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setObjectName("label_22")
        self.gridLayout_3.addWidget(self.label_22, 9, 0, 1, 1)
        self.text_filter_par6 = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_filter_par6.sizePolicy().hasHeightForWidth())
        self.text_filter_par6.setSizePolicy(sizePolicy)
        self.text_filter_par6.setText("")
        self.text_filter_par6.setObjectName("text_filter_par6")
        self.gridLayout_3.addWidget(self.text_filter_par6, 7, 3, 1, 2)
        self.comboBox_filter_op3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_filter_op3.setObjectName("comboBox_filter_op3")
        self.comboBox_filter_op3.addItem("")
        self.comboBox_filter_op3.addItem("")
        self.comboBox_filter_op3.addItem("")
        self.comboBox_filter_op3.addItem("")
        self.comboBox_filter_op3.addItem("")
        self.comboBox_filter_op3.addItem("")
        self.gridLayout_3.addWidget(self.comboBox_filter_op3, 4, 2, 1, 1)
        self.comboBox_filter_par1 = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_filter_par1.sizePolicy().hasHeightForWidth())
        self.comboBox_filter_par1.setSizePolicy(sizePolicy)
        self.comboBox_filter_par1.setObjectName("comboBox_filter_par1")
        self.gridLayout_3.addWidget(self.comboBox_filter_par1, 2, 1, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setObjectName("label_27")
        self.gridLayout_3.addWidget(self.label_27, 1, 6, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setObjectName("label_23")
        self.gridLayout_3.addWidget(self.label_23, 10, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 2, 0, 1, 1)
        self.comboBox_filter_par6 = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_filter_par6.sizePolicy().hasHeightForWidth())
        self.comboBox_filter_par6.setSizePolicy(sizePolicy)
        self.comboBox_filter_par6.setObjectName("comboBox_filter_par6")
        self.gridLayout_3.addWidget(self.comboBox_filter_par6, 7, 1, 1, 1)
        self.comboBox_filter_time1 = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_filter_time1.sizePolicy().hasHeightForWidth())
        self.comboBox_filter_time1.setSizePolicy(sizePolicy)
        self.comboBox_filter_time1.setObjectName("comboBox_filter_time1")
        self.gridLayout_3.addWidget(self.comboBox_filter_time1, 9, 1, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem12, 18, 3, 1, 1)
        self.checkBox_filter_cutoff = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_filter_cutoff.setObjectName("checkBox_filter_cutoff")
        self.gridLayout_3.addWidget(self.checkBox_filter_cutoff, 14, 6, 1, 1)
        self.label_36 = QtWidgets.QLabel(self.centralwidget)
        self.label_36.setObjectName("label_36")
        self.gridLayout_3.addWidget(self.label_36, 10, 5, 1, 1)
        self.label_35 = QtWidgets.QLabel(self.centralwidget)
        self.label_35.setObjectName("label_35")
        self.gridLayout_3.addWidget(self.label_35, 2, 5, 1, 1)
        self.label_41 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setStrikeOut(False)
        self.label_41.setFont(font)
        self.label_41.setObjectName("label_41")
        self.gridLayout_3.addWidget(self.label_41, 11, 0, 3, 1)
        self.checkBox_filter_firstrow = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_filter_firstrow.setObjectName("checkBox_filter_firstrow")
        self.gridLayout_3.addWidget(self.checkBox_filter_firstrow, 11, 6, 3, 1)
        self.label_45 = QtWidgets.QLabel(self.centralwidget)
        self.label_45.setObjectName("label_45")
        self.gridLayout_3.addWidget(self.label_45, 16, 5, 1, 1)
        self.label_42 = QtWidgets.QLabel(self.centralwidget)
        self.label_42.setObjectName("label_42")
        self.gridLayout_3.addWidget(self.label_42, 12, 5, 1, 1)
        self.checkbox_filter_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkbox_filter_5.setObjectName("checkbox_filter_5")
        self.gridLayout_3.addWidget(self.checkbox_filter_5, 6, 6, 1, 1)
        self.text_filter_time1 = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_filter_time1.sizePolicy().hasHeightForWidth())
        self.text_filter_time1.setSizePolicy(sizePolicy)
        self.text_filter_time1.setText("")
        self.text_filter_time1.setObjectName("text_filter_time1")
        self.gridLayout_3.addWidget(self.text_filter_time1, 9, 3, 1, 2)
        self.label_40 = QtWidgets.QLabel(self.centralwidget)
        self.label_40.setObjectName("label_40")
        self.gridLayout_3.addWidget(self.label_40, 14, 5, 1, 1)
        self.checkbox_filter_t2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkbox_filter_t2.setObjectName("checkbox_filter_t2")
        self.gridLayout_3.addWidget(self.checkbox_filter_t2, 10, 6, 1, 1)
        self.checkBox_filter_repeat = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_filter_repeat.setObjectName("checkBox_filter_repeat")
        self.gridLayout_3.addWidget(self.checkBox_filter_repeat, 16, 6, 1, 1)
        self.label_44 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setStrikeOut(False)
        self.label_44.setFont(font)
        self.label_44.setObjectName("label_44")
        self.gridLayout_3.addWidget(self.label_44, 16, 0, 1, 1)
        self.checkbox_filter_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkbox_filter_3.setObjectName("checkbox_filter_3")
        self.gridLayout_3.addWidget(self.checkbox_filter_3, 4, 6, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(215, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem13, 11, 5, 1, 1)
        self.text_filter_par5 = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_filter_par5.sizePolicy().hasHeightForWidth())
        self.text_filter_par5.setSizePolicy(sizePolicy)
        self.text_filter_par5.setText("")
        self.text_filter_par5.setObjectName("text_filter_par5")
        self.gridLayout_3.addWidget(self.text_filter_par5, 6, 3, 1, 2)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 1, 3, 1, 2)
        self.text_filter_time2 = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_filter_time2.sizePolicy().hasHeightForWidth())
        self.text_filter_time2.setSizePolicy(sizePolicy)
        self.text_filter_time2.setText("")
        self.text_filter_time2.setObjectName("text_filter_time2")
        self.gridLayout_3.addWidget(self.text_filter_time2, 10, 3, 1, 2)
        self.text_filter_par4 = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_filter_par4.sizePolicy().hasHeightForWidth())
        self.text_filter_par4.setSizePolicy(sizePolicy)
        self.text_filter_par4.setText("")
        self.text_filter_par4.setObjectName("text_filter_par4")
        self.gridLayout_3.addWidget(self.text_filter_par4, 5, 3, 1, 2)
        self.text_filter_par3 = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_filter_par3.sizePolicy().hasHeightForWidth())
        self.text_filter_par3.setSizePolicy(sizePolicy)
        self.text_filter_par3.setText("")
        self.text_filter_par3.setObjectName("text_filter_par3")
        self.gridLayout_3.addWidget(self.text_filter_par3, 4, 3, 1, 2)
        self.text_filter_cutoff = QtWidgets.QLineEdit(self.centralwidget)
        self.text_filter_cutoff.setObjectName("text_filter_cutoff")
        self.gridLayout_3.addWidget(self.text_filter_cutoff, 14, 3, 1, 2)
        self.label_39 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setStrikeOut(False)
        self.label_39.setFont(font)
        self.label_39.setObjectName("label_39")
        self.gridLayout_3.addWidget(self.label_39, 14, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setObjectName("label_17")
        self.gridLayout_3.addWidget(self.label_17, 5, 0, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setObjectName("label_26")
        self.gridLayout_3.addWidget(self.label_26, 1, 2, 1, 1)
        self.text_filter_firstrow = QtWidgets.QLineEdit(self.centralwidget)
        self.text_filter_firstrow.setObjectName("text_filter_firstrow")
        self.gridLayout_3.addWidget(self.text_filter_firstrow, 11, 3, 3, 2)
        self.label_48 = QtWidgets.QLabel(self.centralwidget)
        self.label_48.setObjectName("label_48")
        self.gridLayout_3.addWidget(self.label_48, 15, 0, 1, 1)
        self.label_49 = QtWidgets.QLabel(self.centralwidget)
        self.label_49.setObjectName("label_49")
        self.gridLayout_3.addWidget(self.label_49, 15, 5, 1, 1)
        self.checkBox_filter_jumppoints = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_filter_jumppoints.setObjectName("checkBox_filter_jumppoints")
        self.gridLayout_3.addWidget(self.checkBox_filter_jumppoints, 15, 6, 1, 1)
        self.text_filter_jumpborder = QtWidgets.QLineEdit(self.centralwidget)
        self.text_filter_jumpborder.setObjectName("text_filter_jumpborder")
        self.gridLayout_3.addWidget(self.text_filter_jumpborder, 15, 3, 1, 2)
        self.bt_applyfilter = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.bt_applyfilter.setFont(font)
        self.bt_applyfilter.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_applyfilter.setObjectName("bt_applyfilter")
        self.gridLayout_3.addWidget(self.bt_applyfilter, 19, 3, 2, 3)
        self.bt_undofilter = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.bt_undofilter.setFont(font)
        self.bt_undofilter.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_undofilter.setObjectName("bt_undofilter")
        self.gridLayout_3.addWidget(self.bt_undofilter, 19, 6, 2, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem14)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.comboBox_tooltip_1 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_tooltip_1.setObjectName("comboBox_tooltip_1")
        self.gridLayout_2.addWidget(self.comboBox_tooltip_1, 5, 1, 1, 2)
        self.label_43 = QtWidgets.QLabel(self.centralwidget)
        self.label_43.setObjectName("label_43")
        self.gridLayout_2.addWidget(self.label_43, 7, 2, 1, 1)
        self.comboBox_tooltip_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_tooltip_2.setObjectName("comboBox_tooltip_2")
        self.gridLayout_2.addWidget(self.comboBox_tooltip_2, 6, 1, 1, 2)
        self.text_jumprate = QtWidgets.QLineEdit(self.centralwidget)
        self.text_jumprate.setObjectName("text_jumprate")
        self.gridLayout_2.addWidget(self.text_jumprate, 3, 1, 1, 1)
        self.checkBox_jump = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_jump.setObjectName("checkBox_jump")
        self.gridLayout_2.addWidget(self.checkBox_jump, 3, 2, 1, 2)
        self.comboBox_Maptype = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_Maptype.setObjectName("comboBox_Maptype")
        self.comboBox_Maptype.addItem("")
        self.comboBox_Maptype.addItem("")
        self.comboBox_Maptype.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_Maptype, 8, 1, 1, 2)
        self.label_37 = QtWidgets.QLabel(self.centralwidget)
        self.label_37.setObjectName("label_37")
        self.gridLayout_2.addWidget(self.label_37, 2, 2, 1, 3)
        self.label_46 = QtWidgets.QLabel(self.centralwidget)
        self.label_46.setObjectName("label_46")
        self.gridLayout_2.addWidget(self.label_46, 4, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 5, 0, 1, 1)
        self.label_38 = QtWidgets.QLabel(self.centralwidget)
        self.label_38.setObjectName("label_38")
        self.gridLayout_2.addWidget(self.label_38, 10, 1, 1, 2)
        self.label_47 = QtWidgets.QLabel(self.centralwidget)
        self.label_47.setObjectName("label_47")
        self.gridLayout_2.addWidget(self.label_47, 4, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 9, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)
        self.text_Mapname = QtWidgets.QLineEdit(self.centralwidget)
        self.text_Mapname.setObjectName("text_Mapname")
        self.gridLayout_2.addWidget(self.text_Mapname, 9, 1, 1, 2)
        self.label_34 = QtWidgets.QLabel(self.centralwidget)
        self.label_34.setObjectName("label_34")
        self.gridLayout_2.addWidget(self.label_34, 1, 2, 1, 3)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem15, 10, 0, 1, 1)
        self.bt_Mapping = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.bt_Mapping.setFont(font)
        self.bt_Mapping.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_Mapping.setObjectName("bt_Mapping")
        self.gridLayout_2.addWidget(self.bt_Mapping, 11, 0, 1, 3)
        self.label_31 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setStrikeOut(False)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.gridLayout_2.addWidget(self.label_31, 3, 0, 1, 1)
        self.label_Maptype = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_Maptype.setFont(font)
        self.label_Maptype.setObjectName("label_Maptype")
        self.gridLayout_2.addWidget(self.label_Maptype, 8, 0, 1, 1)
        self.checkBox_cluster = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_cluster.setObjectName("checkBox_cluster")
        self.gridLayout_2.addWidget(self.checkBox_cluster, 2, 0, 1, 2)
        self.checkBox_Marker = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_Marker.setChecked(False)
        self.checkBox_Marker.setObjectName("checkBox_Marker")
        self.gridLayout_2.addWidget(self.checkBox_Marker, 1, 0, 1, 2)
        self.checkBox_Polyline = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_Polyline.setChecked(True)
        self.checkBox_Polyline.setObjectName("checkBox_Polyline")
        self.gridLayout_2.addWidget(self.checkBox_Polyline, 7, 0, 1, 2)
        self.horizontalLayout_2.addLayout(self.gridLayout_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 1, 0, 1, 1)
        self.text_datasave_seperator = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_datasave_seperator.sizePolicy().hasHeightForWidth())
        self.text_datasave_seperator.setSizePolicy(sizePolicy)
        self.text_datasave_seperator.setObjectName("text_datasave_seperator")
        self.gridLayout.addWidget(self.text_datasave_seperator, 1, 1, 1, 1)
        self.comboBox_datasave_format = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_datasave_format.setObjectName("comboBox_datasave_format")
        self.comboBox_datasave_format.addItem("")
        self.comboBox_datasave_format.addItem("")
        self.gridLayout.addWidget(self.comboBox_datasave_format, 5, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 2, 0, 1, 1)
        self.text_datasave_filename = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_datasave_filename.sizePolicy().hasHeightForWidth())
        self.text_datasave_filename.setSizePolicy(sizePolicy)
        self.text_datasave_filename.setObjectName("text_datasave_filename")
        self.gridLayout.addWidget(self.text_datasave_filename, 2, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 5, 0, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 1, 2, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem16, 8, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 0, 0, 1, 2)
        self.bt_savefiltered = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.bt_savefiltered.setFont(font)
        self.bt_savefiltered.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_savefiltered.setObjectName("bt_savefiltered")
        self.gridLayout.addWidget(self.bt_savefiltered, 7, 1, 1, 2)
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 6, 0, 1, 3)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_2.addWidget(self.label_15)
        self.TableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.TableWidget.setToolTip("")
        self.TableWidget.setAutoFillBackground(False)
        self.TableWidget.setObjectName("TableWidget")
        self.TableWidget.setColumnCount(0)
        self.TableWidget.setRowCount(0)
        self.verticalLayout_2.addWidget(self.TableWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_30 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.horizontalLayout.addWidget(self.label_30)
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setObjectName("lcdNumber")
        self.horizontalLayout.addWidget(self.lcdNumber)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.bt_cleardata = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.bt_cleardata.setFont(font)
        self.bt_cleardata.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_cleardata.setToolTip("")
        self.bt_cleardata.setObjectName("bt_cleardata")
        self.verticalLayout_2.addWidget(self.bt_cleardata)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        lcd_display.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(lcd_display)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 2672, 38))
        self.menubar.setObjectName("menubar")
        lcd_display.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(lcd_display)
        self.statusbar.setObjectName("statusbar")
        lcd_display.setStatusBar(self.statusbar)

        self.retranslateUi(lcd_display)
        QtCore.QMetaObject.connectSlotsByName(lcd_display)
        lcd_display.setTabOrder(self.comboBox_Maptype, self.text_Mapname)
        lcd_display.setTabOrder(self.text_Mapname, self.comboBox_filter_par1)
        lcd_display.setTabOrder(self.comboBox_filter_par1, self.comboBox_filter_par2)
        lcd_display.setTabOrder(self.comboBox_filter_par2, self.comboBox_filter_par3)

        self.bt_Mapping.clicked.connect(self.mapping_bt)
        self.bt_fileread.clicked.connect(self.readfile_bt)
        self.bt_cleardata.clicked.connect(self.cleardata_bt)
        self.bt_applyfilter.clicked.connect(lambda:self.filteroptions(activ=True))
        self.bt_undofilter.clicked.connect(lambda:self.filteroptions(activ=False))
        self.bt_sort.clicked.connect(self.sort_bt)
        self.bt_savefiltered.clicked.connect(self.savefiltered_bt)
        self.markerexistance = False
        self.dataloaded      = False

    def savefiltered_bt(self):
        try:
            name=self.text_datasave_filename.text()
            self.df.reset_index(drop=True, inplace=True)
            if self.comboBox_datasave_format.currentText() == ".csv":
                name      = name + ".csv"
                seperator = self.text_datasave_seperator.text()
                if len(seperator)==1:

                    self.df.to_csv(name,index=True,sep=seperator)

                else:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                    msg.setText("seperator shoult have length=1")
                    msg.setWindowTitle("WARNING")
                    msg.exec_()
            elif self.comboBox_datasave_format.currentText() == ".xlsx":
                name      = name + ".xlsx"
                self.df.to_excel(name)

        except (IOError,NameError,FileNotFoundError,TypeError,ValueError) as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText(str(e))
            msg.setWindowTitle("WARNING")
            msg.exec_()
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Unknown Error, (No IOError, NameError, FileNotFoundError,TypeError or ValueError ")
            msg.setWindowTitle("WARNING")
            msg.exec_()

    def cleardata_bt(self):
        #clears data
        self.QComboBox_Longetude_val.clear()       # delete all items from comboBox
        self.QComboBox_Latetude_val.clear()       # delete all items from comboBox
        self.comboBox_filter_par1.clear()
        self.comboBox_filter_par2.clear()
        self.comboBox_filter_par3.clear()
        self.comboBox_filter_par4.clear()
        self.comboBox_filter_par5.clear()
        self.comboBox_filter_par6.clear()
        self.comboBox_filter_time1.clear()
        self.comboBox_filter_time2.clear()
        self.comboBox_tooltip_1.clear()
        self.comboBox_tooltip_2.clear()
        self.comboBox_tooltip_1.clear()
        self.comboBox_tooltip_2.clear()
        self.df=pd.DataFrame()
        self.tablefiller()
        self.markerexistance = False
        self.dataloaded      = False

    def tablefiller(self):
        #fills the TableWidget with current Data
        self.df.reset_index(drop=True, inplace=True)
        columnames=self.df.columns
        indexnames=self.df.index
        self.lcdNumber.display(len(indexnames))
        self.TableWidget.setColumnCount(len(columnames))
        if len(indexnames)>100:
            self.TableWidget.setRowCount(100)
            indexlaenge=100
        else:
            self.TableWidget.setRowCount(len(indexnames))
            indexlaenge=len(indexnames)
        horHeaders=[]
        for i in range(0,indexlaenge):
            for j in range(0,len(columnames)):
                horHeaders.append(columnames[j])
                a=(self.df.loc[indexnames[i]][columnames[j]])
                self.TableWidget.setItem(i,j,QTableWidgetItem(str(a)))
        self.TableWidget.setHorizontalHeaderLabels(horHeaders)

    def readfile_bt(self):
        try:
            path = self.text_filepath.text()
            raw_path = fr"{path}"
            self.DF = pd.read_csv(raw_path)
            self.textfilter=[]

            self.QComboBox_Longetude_val.clear()       # delete all items from comboBox
            self.QComboBox_Latetude_val.clear()       # delete all items from comboBox
            self.comboBox_filter_par1.clear()
            self.comboBox_filter_par2.clear()
            self.comboBox_filter_par3.clear()
            self.comboBox_filter_par4.clear()
            self.comboBox_filter_par5.clear()
            self.comboBox_filter_par6.clear()
            self.comboBox_filter_time1.clear()
            self.comboBox_filter_time2.clear()
            self.comboBox_tooltip_1.clear()
            self.comboBox_tooltip_2.clear()

            #befüllen der latitude/longitude Comboboxen
            for i in self.DF.axes[1]:
                if i == 'timestamp':
                    self.QComboBox_Timstamp.addItem('timestamp')
                    self.comboBox_tooltip_1.addItem("timestamp")
            for i in self.DF.axes[1]:
                self.QComboBox_Longetude_val.addItem(i)
                self.QComboBox_Latetude_val.addItem(i)
                self.comboBox_filter_par1.addItem(i)
                self.comboBox_filter_par2.addItem(i)
                self.comboBox_filter_par3.addItem(i)
                self.comboBox_filter_par4.addItem(i)
                self.comboBox_filter_par5.addItem(i)
                self.comboBox_filter_par6.addItem(i)
                self.comboBox_filter_time1.addItem(i)
                self.comboBox_filter_time2.addItem(i)
                self.comboBox_tooltip_2.addItem(i)
                if i == 'timestamp':
                    self.DF = self.DF.sort_values(by=['timestamp'])
                else:
                    self.QComboBox_Timstamp.addItem(i)
                    self.comboBox_tooltip_1.addItem(i)
            #set working frame
            self.DF.reset_index(drop=True, inplace=True)
            self.df = self.DF
            #check if no error ocured
            self.markerexistance = True
            self.dataloaded      = True
        except (IOError,NameError,FileNotFoundError) as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText(str(e))
            msg.setWindowTitle("WARNING")
            msg.exec_()
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("WARNING")
            msg.setText("Unknown Error, (No IOError, FileNotFoundError ")
            msg.exec_()
        self.tablefiller()

    def sort_bt(self):
        try:
            sortname  = self.QComboBox_Timstamp.currentText()
            self.DF = self.DF.sort_values(by=[sortname])
            self.df = self.df.sort_values(by=[sortname])
            self.df.reset_index(drop=True, inplace=True)
            self.DF.reset_index(drop=True, inplace=True)
            self.tablefiller()
        except (IOError,NameError,FileNotFoundError,TypeError,ValueError) as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText(str(e))
            msg.setWindowTitle("WARNING")
            msg.exec_()
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Unknown Error, (No IOError, NameError, FileNotFoundError,TypeError or ValueError ")
            msg.setWindowTitle("WARNING")
            msg.exec_()

    def mapping_bt(self):

        # try:
            #Mappingsetup
            tile  = self.comboBox_Maptype.currentText()
            map = folium.Map( tiles= tile,zoom_start = 20,control_scale=True)
            mc  = MarkerCluster()
            if self.markerexistance & self.dataloaded:
                #Auslesen der Markercoordinaten
                i_lat = self.QComboBox_Latetude_val.currentText()
                i_lon = self.QComboBox_Longetude_val.currentText()

                if self.checkBox_jump.isChecked():#für den Jumpfilter
                    self.df.reset_index(drop=True, inplace=True)
                    jumpstring = self.comboBox_markerjump.currentText()
                    jumprate = int(jumpstring[0])
                    goodindex = range(0, len(self.df.index), jumprate)
                    x = self.df
                    del(self.df)
                    self.df = x.iloc[goodindex,:]
                    del(x)

                lat = self.df.loc[:][i_lat]
                lon = self.df.loc[:][i_lon]

                if self.checkBox_Marker.isChecked() and len(lat)>3000:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                    msg.setText("WARNING: You have printed over 3000 Markers maybe your map will be unstable try using MarkerClusters or the Jumpfilter")
                    msg.setWindowTitle("WARNING")
                    msg.exec_()
                #vorbereiten der Markercoordinaten
                points = [] #liste für PolyLine
                tool1       = self.comboBox_tooltip_1.currentText()#auslesen der tooltipspalte1
                tool2       = self.comboBox_tooltip_2.currentText()#auslesen der tooltipspalte2
                clustercheck = self.checkBox_cluster.isChecked()#auslesen ob cluster geplottet werden sollen
                markercheck  = self.checkBox_Marker.isChecked()#auslesen ob marker geplottet werden sollen
                jumppoints = self.findjumps(60)
                print(jumppoints)
                deadindex = jumppoints.loc[:,"oldindex"]
                print(deadindex)
                if markercheck:
                    for i in lat.index:#erstellen der Marker und hinzufügen zu Map
                        curentpoint = [lat.loc[i],lon.loc[i]]#erstellt aktuellen lat lon punkt
                        tooltip = tool1 + " = " + str(self.df.loc[i][tool1]) + " ; " +tool2 + " = " + str(self.df.loc[i][tool2]) #erzeugt tooltip
                        for jk in deadindex:
                            if jk == i:
                                folium.Marker(curentpoint,tooltip = tooltip,icon=folium.Icon(color='red')).add_to(map)
                            else:
                                folium.Marker(curentpoint,tooltip = tooltip).add_to(map)#fügt marker hinzu

                if clustercheck:
                    for i in lat.index:#erstellen der Marker und hinzufügen zu Map
                        curentpoint = [lat.loc[i],lon.loc[i]]#erstellt aktuellen lat lon punkt
                        tooltip = tool1 + " = " + str(self.df.loc[i][tool1]) + " ; " +tool2 + " = " + str(self.df.loc[i][tool2]) #erzeugt tooltip
                        mc.add_child(folium.Marker(curentpoint,tooltip = tooltip))#fügt cluster hinzu
                for i in lat.index:
                    for jk in deadindex:
                        if jk != i:
                            points.append(tuple(curentpoint))#sammelt punkte für die PolyLine
                if self.checkBox_Polyline.isChecked() & len(points)>0:
                    folium.PolyLine(points).add_to(map) #erstellen einer PolyLine
                if clustercheck:
                    map.add_child(mc)
                #Zoom auf auf kooridinaten einstellen
                sw = self.df.loc[:,[i_lat, i_lon]].min().values.tolist()
                ne = self.df.loc[:,[i_lat, i_lon]].max().values.tolist()
                map.fit_bounds([sw, ne])

                #Darstellen der filtersettings
                s= self.textfilter
                if len(s)>0:
                    for i in range(0,len(s)):
                       popfiltertext = ''.join([str(elem)+"<br>" for elem in s])
                    infopos     = [(sw[0]+ne[0])/2,(sw[1]+ne[1])/2]
                    infomarker  = folium.Marker(infopos,tooltip="filtersettings",icon=folium.Icon(color='red', icon='info-sign'))
                    pop         = folium.map.Popup(html=popfiltertext, max_width=200,min_width=200).add_to(infomarker)
                    infomarker.add_to(map)
            #Speichern der Karte
            mapname = self.text_Mapname.text()
            map.save(mapname+'.html')

            if self.dataloaded is not True:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("WARNING: No data selected")
                msg.setWindowTitle("WARNING")
                msg.exec_()
        # except (IOError,NameError,TypeError,ValueError) as e:
        #     msg = QMessageBox()
        #     msg.setIcon(QMessageBox.Warning)
        #     msg.setText(str(e))
        #     msg.setWindowTitle("WARNING")
        #     msg.exec_()
        # except:
        #     msg = QMessageBox()
        #     msg.setIcon(QMessageBox.Warning)
        #     msg.setText("Unknown Error, (No IOError, NameError, TypeError or ValueError ")
        #     msg.setWindowTitle("WARNING")
        #     msg.exec_()

    def filteroptions(self,activ):
        #Filter the data as said by the Filteroptions
        #Input Parameter:
        #activ....[bolian] if True ->filteroptions get aplyed
        #                  if False ->filteroptions get undone

        if activ: #Apply filter button
                self.df = self.DF

                def filtering(operator, DataFr, argument,i_par):
                    #translate Filteroptions into boolians
                    if operator=='<':
                        x=DataFr.loc[DataFr[i_par]<argument]
                        return x
                    elif operator == '>':
                        x=DataFr.loc[DataFr[i_par]>argument]
                        return x
                    elif operator == '<=':
                        x=DataFr.loc[DataFr[i_par]<=argument]
                        return x
                    elif operator == '>=':
                        x=DataFr.loc[DataFr[i_par]>=argument]
                        return x
                    elif operator == '==':
                        x=DataFr.loc[DataFr[i_par]==argument]
                        return x
                    elif operator == '!=':
                        x=DataFr.loc[DataFr[i_par]!=argument]
                        return x
            # try:
                #Auslesen der Datenfelder
                i_par1 = self.comboBox_filter_par1.currentText() #Spaltenauswahl
                i_par2 = self.comboBox_filter_par2.currentText()
                i_par3 = self.comboBox_filter_par3.currentText()
                i_par4 = self.comboBox_filter_par4.currentText()
                i_par5 = self.comboBox_filter_par5.currentText()
                i_par6 = self.comboBox_filter_par6.currentText()
                i_time1 = self.comboBox_filter_time1.currentText()
                i_time2 = self.comboBox_filter_time2.currentText()
                op1 = self.comboBox_filter_op1.currentText() #Operatorauswahl
                op2 = self.comboBox_filter_op2.currentText()
                op3 = self.comboBox_filter_op3.currentText()
                op4 = self.comboBox_filter_op4.currentText()
                op5 = self.comboBox_filter_op5.currentText()
                op6 = self.comboBox_filter_op6.currentText()
                op_t1 = self.comboBox_filter_op_t1.currentText()
                op_t2 = self.comboBox_filter_op_t2.currentText()
                arg1 = self.text_filter_par1.text() #Filterargument
                arg2 = self.text_filter_par2.text()
                arg3 = self.text_filter_par3.text()
                arg4 = self.text_filter_par4.text()
                arg5 = self.text_filter_par5.text()
                arg6 = self.text_filter_par6.text()
                #Timefilter
                arg_t1 = self.text_filter_time1.text()
                arg_t2 = self.text_filter_time2.text()
                #cutoff Filtern
                first = self.text_filter_firstrow.text()
                last  = self.text_filter_cutoff.text()


                #Filtersettings prealocate
                self.textfilter=[]

                #Filtern
                if self.checkbox_filter_1.isChecked():
                    x = filtering(op1,self.df,float(arg1),i_par1)#filter data
                    del(self.df)
                    self.df=x
                    del(x)
                    self.textfilter.append(i_par1+" "+op1+" "+arg1)#save text for filtersettings.txt
                if self.checkbox_filter_2.isChecked():
                    x = filtering(op2,self.df,float(arg2),i_par2)
                    del(self.df)
                    self.df=x
                    del(x)
                    self.textfilter.append(i_par2+" "+op2+" "+arg2)
                if self.checkbox_filter_3.isChecked():
                    x = filtering(op3,self.df,float(arg3),i_par3)
                    del(self.df)
                    self.df=x
                    del(x)
                    self.textfilter.append(i_par3+" "+op3+" "+arg3)
                if self.checkbox_filter_4.isChecked():
                    x = filtering(op4,self.df,float(arg4),i_par4)
                    del(self.df)
                    self.df=x
                    del(x)
                    self.textfilter.append(i_par4+" "+op4+" "+arg4)
                if self.checkbox_filter_5.isChecked():
                    x = filtering(op5,self.df,float(arg5),i_par5)
                    del(self.df)
                    self.df=x
                    del(x)
                    self.textfilter.append(i_par5+" "+op5+" "+arg5)
                if self.checkbox_filter_6.isChecked():
                    x = filtering(op6,self.df,float(arg6),i_par6)
                    del(self.df)
                    self.df=x
                    del(x)
                    self.textfilter.append(i_par6+" "+op6+" "+arg6)
                if self.checkbox_filter_t1.isChecked():#Timestamp Filter
                    x = filtering(op_t1,self.df,arg_t1,i_time1)
                    del(self.df)
                    self.df=x
                    del(x)
                    self.textfilter.append(i_time1+" "+op_t1+" "+arg_t1)
                if self.checkbox_filter_t2.isChecked():#Timestamp Filter
                    x = filtering(op_t2,self.df,arg_t2,i_time2)
                    del(self.df)
                    self.df=x
                    del(x)
                    self.textfilter.append(i_time2+" "+op_t2+" "+arg_t2)
                self.df.reset_index(drop=True, inplace=True) #reset index for potential filtering
                if self.checkBox_filter_jumppoints.isChecked():
                    jumpborder = float(self.text_filter_jumpborder.text()) #[km] #set classification for a jump
                    jumppoints = self.findjumps(jumpborder)
                    deadindex = jumppoints.loc[:,"oldindex"]
                    for i in jumppoints.loc[:,"oldindex"]:
                        self.df=self.df.drop(i)
                    self.df.reset_index(drop=True, inplace=True)
                    self.textfilter.append("jumpfilter = True, jumpborder = "+str(jumpborder)+"km")

                if self.checkBox_filter_repeat.isChecked():#Filter for repeating Datapoints
                    self.df.reset_index(drop=True, inplace=True)
                    x = self.df
                    del(self.df)
                    ilat = self.QComboBox_Latetude_val.currentText()
                    ilon = self.QComboBox_Longetude_val.currentText()
                    un= x.loc[:,[ilon,ilat]].drop_duplicates()
                    self.df=x.iloc[un.index,:]
                    del(x)
                    self.textfilter.append("repeatfilter = True")
                #Cutoff Filter Cuts at firstrow and at lastrow
                if self.checkBox_filter_firstrow.isChecked() | self.checkBox_filter_cutoff.isChecked():
                    if (self.checkBox_filter_firstrow.isChecked()):
                        firstrow = int(first)
                    else:
                        firstrow = 1
                    if (self.checkBox_filter_cutoff.isChecked()):
                        lastrow = int(last)
                    else:
                        lastrow = len(self.df.index)

                    if (firstrow)<(lastrow):
                        if lastrow<=len(self.df.index):
                            x = self.df
                            del(self.df)
                            self.df = x.iloc[firstrow:lastrow,:]
                            del(x)
                            self.textfilter.append("firstrow = " +str(firstrow))
                            self.textfilter.append("lastrow = "+str(lastrow))
                        else:
                            msg = QMessageBox()
                            msg.setIcon(QMessageBox.Warning)
                            msg.setText("ERROR: lastrow > data length")
                            msg.setWindowTitle("ERROR")
                            msg.exec_()
                    else:
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Warning)
                        msg.setText("ERROR: firstrow >= lastrow")
                        msg.setWindowTitle("ERROR")
                        msg.exec_()

                self.df.reset_index(drop=True, inplace=True)#resets indexes of the Dataframe to 1,2,3,4,...

                #gives a waring if you have Filtered all points and swich markers off
                if len(self.df.index) == 0:
                    self.markerexistance = False
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                    msg.setText("WARNING: The selected data range is empty")
                    msg.setWindowTitle("WARNING")
                    msg.exec_()
                else:#if filtered data is not empty shich markers on
                    self.markerexistance = True

            # except (IOError,NameError,FileNotFoundError,TypeError,ValueError) as e:
            #     msg = QMessageBox()
            #     msg.setIcon(QMessageBox.Warning)
            #     msg.setText(str(e))
            #     msg.setWindowTitle("WARNING")
            #     msg.exec_()
            # except:
            #     msg = QMessageBox()
            #     msg.setIcon(QMessageBox.Warning)
            #     msg.setText("Unknown Error, (No IOError, NameError, FileNotFoundError,TypeError or ValueError ")
            #     msg.setWindowTitle("WARNING")
            #     msg.exec_()

        elif ~activ:#undo filter Button, resets Dataset
                    self.df = self.DF
                    self.textfilter=[]
        self.tablefiller()

    def findjumps(self,jumpborder):
        ilat = self.QComboBox_Latetude_val.currentText()
        ilon = self.QComboBox_Longetude_val.currentText()
        gps = self.df.loc[:,[ilat,ilon]]#build working dataframe
        gps.loc[:,"oldindex"] = range(0,len(gps.loc[:,ilat]))#save current index
        lat = gps.loc[:,[ilat,"oldindex"]]#build Latitude
        lon = gps.loc[:,[ilon,"oldindex"]]#build Longitude

        #setting 2 dataframes for next neighbours
        lat_i  = lat.iloc[range(1,len(lat),2),:]
        lat_ii = lat.iloc[range(0,len(lat),2),:]
        lat_i.reset_index(drop=True, inplace=True)#resetting indexes nessesary to subtrackting 2 frames
        lat_ii.reset_index(drop=True, inplace=True)
        delta_lat=lat_i[ilat].sub(lat_ii[ilat])#subtrackting next neighbours

        lon_i  = lon.loc[range(1,len(lon),2),:]
        lon_ii = lon.loc[range(0,len(lon),2),:]
        lon_i.reset_index(drop=True, inplace=True)
        lon_ii.reset_index(drop=True, inplace=True)
        delta_lon = lon_i[ilon] - lon_ii[ilon]

        R = np.sqrt(delta_lat**2 + delta_lon**2)#build a distance vector
        jumpborder_grad= jumpborder/11.3 #km to °
        jumps = R[R>jumpborder_grad]# find jump
        #build dataframe for jumppoints
        lat=pd.concat([lat_i.loc[jumps.index.values,:],lat_ii.loc[jumps.index.values,:]])
        lon=pd.concat([lon_i.loc[jumps.index.values,:],lon_ii.loc[jumps.index.values,:]])
        jumppoints = lat
        jumppoints.loc[:,ilon]=lon.loc[:,ilon]
        return jumppoints

    def retranslateUi(self, lcd_display):
        _translate = QtCore.QCoreApplication.translate
        lcd_display.setWindowTitle(_translate("lcd_display", "MainWindow"))
        self.label_28.setText(_translate("lcd_display", "GPS-data to ineraktive Map "))
        self.label_20.setText(_translate("lcd_display", "Read Data"))
        self.bt_sort.setText(_translate("lcd_display", "Sortbutton"))
        self.text_filepath.setText(_translate("lcd_display", "Enter Filepath/Filename"))
        self.label_25.setText(_translate("lcd_display", "Basic setings"))
        self.label_32.setText(_translate("lcd_display", "(add data format if nessesary)"))
        self.label_18.setText(_translate("lcd_display", "Sort by"))
        self.label.setText(_translate("lcd_display", "Latitude"))
        self.label_16.setText(_translate("lcd_display", "Longitude"))
        self.label_29.setText(_translate("lcd_display", "(Default: timestamp)"))
        self.bt_fileread.setText(_translate("lcd_display", "Readfile"))
        self.textBrowser.setHtml(_translate("lcd_display", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">How to use:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">1) Read the Data</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- Enter a filename or a filepath and push &quot;Readfile&quot;-Button</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- add the fileformat .csv if nessesary</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- now Data will displayed in the table and comboboxes will be filled</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">2) Basic Setings</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- Choose column name of latetude and longetude with comboboxes</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    2.1) <span style=\" text-decoration: underline;\">Sorting</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    - The gui sorts automaticly by the &quot;timestamp&quot; column name </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    - if you want to sort by an other column name choose the column name and push the &quot;Sortbutton&quot;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">3) Filter Options</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- If you want to use a filter choose a column name and enter a if argument. </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- Then check the checkbox and push the &quot;Apply Filter&quot;-button.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- The &quot;Undo Filter&quot;-button will reset the filter. </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- For the time filter you have to enter in the same format as the refering data!</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">4) Save Data</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- Now you can save the filtered data in CSV or Excel</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- The seperator has to be one character</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">5) Map Options</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- Choose if you want Markers/Polyline and witch Maptype\\Mapname you want</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- the chosen tooltips will be displayed in the tooltip of every individual marker</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- push the &quot;Save Map&quot;-button to create a .html file with your map</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">6) Current Data</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- the table on the right shows the first 500 rows of the current loadet (and filtered) data</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- the &quot;Clear Data&quot;-button will delete all loadet data in the cash</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_3.setText(_translate("lcd_display", "Filter Options"))
        self.label_19.setText(_translate("lcd_display", "Parameter 5"))
        self.label_9.setText(_translate("lcd_display", "Parameter 3"))
        self.checkbox_filter_t1.setText(_translate("lcd_display", "Time Filter 1 on/off"))
        self.checkbox_filter_2.setText(_translate("lcd_display", "Filter 2 on/off"))
        self.checkbox_filter_1.setText(_translate("lcd_display", "Filter 1 on/off"))
        self.comboBox_filter_op2.setItemText(0, _translate("lcd_display", "<"))
        self.comboBox_filter_op2.setItemText(1, _translate("lcd_display", ">"))
        self.comboBox_filter_op2.setItemText(2, _translate("lcd_display", "<="))
        self.comboBox_filter_op2.setItemText(3, _translate("lcd_display", ">="))
        self.comboBox_filter_op2.setItemText(4, _translate("lcd_display", "=="))
        self.comboBox_filter_op2.setItemText(5, _translate("lcd_display", "!="))
        self.comboBox_filter_op1.setItemText(0, _translate("lcd_display", "<"))
        self.comboBox_filter_op1.setItemText(1, _translate("lcd_display", ">"))
        self.comboBox_filter_op1.setItemText(2, _translate("lcd_display", "<="))
        self.comboBox_filter_op1.setItemText(3, _translate("lcd_display", ">="))
        self.comboBox_filter_op1.setItemText(4, _translate("lcd_display", "=="))
        self.comboBox_filter_op1.setItemText(5, _translate("lcd_display", "!="))
        self.label_10.setText(_translate("lcd_display", "Column name"))
        self.comboBox_filter_op4.setItemText(0, _translate("lcd_display", "<"))
        self.comboBox_filter_op4.setItemText(1, _translate("lcd_display", ">"))
        self.comboBox_filter_op4.setItemText(2, _translate("lcd_display", "<="))
        self.comboBox_filter_op4.setItemText(3, _translate("lcd_display", ">="))
        self.comboBox_filter_op4.setItemText(4, _translate("lcd_display", "=="))
        self.comboBox_filter_op4.setItemText(5, _translate("lcd_display", "!="))
        self.comboBox_filter_op6.setItemText(0, _translate("lcd_display", "<"))
        self.comboBox_filter_op6.setItemText(1, _translate("lcd_display", ">"))
        self.comboBox_filter_op6.setItemText(2, _translate("lcd_display", "<="))
        self.comboBox_filter_op6.setItemText(3, _translate("lcd_display", ">="))
        self.comboBox_filter_op6.setItemText(4, _translate("lcd_display", "=="))
        self.comboBox_filter_op6.setItemText(5, _translate("lcd_display", "!="))
        self.checkbox_filter_4.setText(_translate("lcd_display", "Filter 4 on/off"))
        self.comboBox_filter_op_t2.setItemText(0, _translate("lcd_display", "<"))
        self.comboBox_filter_op_t2.setItemText(1, _translate("lcd_display", ">"))
        self.comboBox_filter_op_t2.setItemText(2, _translate("lcd_display", "<="))
        self.comboBox_filter_op_t2.setItemText(3, _translate("lcd_display", ">="))
        self.comboBox_filter_op_t2.setItemText(4, _translate("lcd_display", "=="))
        self.comboBox_filter_op_t2.setItemText(5, _translate("lcd_display", "!="))
        self.comboBox_filter_op5.setItemText(0, _translate("lcd_display", "<"))
        self.comboBox_filter_op5.setItemText(1, _translate("lcd_display", ">"))
        self.comboBox_filter_op5.setItemText(2, _translate("lcd_display", "<="))
        self.comboBox_filter_op5.setItemText(3, _translate("lcd_display", ">="))
        self.comboBox_filter_op5.setItemText(4, _translate("lcd_display", "=="))
        self.comboBox_filter_op5.setItemText(5, _translate("lcd_display", "!="))
        self.checkbox_filter_6.setText(_translate("lcd_display", "Filter 6 on/off"))
        self.label_8.setText(_translate("lcd_display", "Parameter 2"))
        self.comboBox_filter_op_t1.setItemText(0, _translate("lcd_display", "<"))
        self.comboBox_filter_op_t1.setItemText(1, _translate("lcd_display", ">"))
        self.comboBox_filter_op_t1.setItemText(2, _translate("lcd_display", "<="))
        self.comboBox_filter_op_t1.setItemText(3, _translate("lcd_display", ">="))
        self.comboBox_filter_op_t1.setItemText(4, _translate("lcd_display", "=="))
        self.comboBox_filter_op_t1.setItemText(5, _translate("lcd_display", "!="))
        self.label_21.setText(_translate("lcd_display", "Parameter 6"))
        self.label_22.setText(_translate("lcd_display", "Filter by Timestamp 1"))
        self.comboBox_filter_op3.setItemText(0, _translate("lcd_display", "<"))
        self.comboBox_filter_op3.setItemText(1, _translate("lcd_display", ">"))
        self.comboBox_filter_op3.setItemText(2, _translate("lcd_display", "<="))
        self.comboBox_filter_op3.setItemText(3, _translate("lcd_display", ">="))
        self.comboBox_filter_op3.setItemText(4, _translate("lcd_display", "=="))
        self.comboBox_filter_op3.setItemText(5, _translate("lcd_display", "!="))
        self.label_27.setText(_translate("lcd_display", "Filter on/off"))
        self.label_23.setText(_translate("lcd_display", "Filter by Timestamp 2"))
        self.label_7.setText(_translate("lcd_display", "Parameter 1"))
        self.checkBox_filter_cutoff.setText(_translate("lcd_display", "Cut off on/off"))
        self.label_36.setText(_translate("lcd_display", "(data timestap format )"))
        self.label_35.setText(_translate("lcd_display", "(float numbers)"))
        self.label_41.setText(_translate("lcd_display", "First data row"))
        self.checkBox_filter_firstrow.setText(_translate("lcd_display", "start on/off"))
        self.label_45.setText(_translate("lcd_display", "(recomendet for large data)"))
        self.label_42.setText(_translate("lcd_display", "(first row integer)"))
        self.checkbox_filter_5.setText(_translate("lcd_display", "Filter 5 on/off"))
        self.label_40.setText(_translate("lcd_display", "(last row integer)"))
        self.checkbox_filter_t2.setText(_translate("lcd_display", "Time Filter 2 on/off"))
        self.checkBox_filter_repeat.setText(_translate("lcd_display", "repeat Filter on /off"))
        self.label_44.setText(_translate("lcd_display", "Filter repeating lat lon positions"))
        self.checkbox_filter_3.setText(_translate("lcd_display", "Filter 3 on/off"))
        self.label_11.setText(_translate("lcd_display", "If argument"))
        self.label_39.setText(_translate("lcd_display", "Cut of data at row"))
        self.label_17.setText(_translate("lcd_display", "Parameter 4"))
        self.label_26.setText(_translate("lcd_display", "Operator"))
        self.label_48.setText(_translate("lcd_display", "Filter points who jump over"))
        self.label_49.setText(_translate("lcd_display", "[km]"))
        self.checkBox_filter_jumppoints.setText(_translate("lcd_display", "jump Filter on/off"))
        self.bt_applyfilter.setText(_translate("lcd_display", "Apply Filter"))
        self.bt_undofilter.setText(_translate("lcd_display", "Undo Filter"))
        self.label_43.setText(_translate("lcd_display", "(follows sort)"))
        self.checkBox_jump.setText(_translate("lcd_display", " Filter on /off"))
        self.comboBox_Maptype.setItemText(0, _translate("lcd_display", "OpenStreetMap"))
        self.comboBox_Maptype.setItemText(1, _translate("lcd_display", "Stamen Terrain"))
        self.comboBox_Maptype.setItemText(2, _translate("lcd_display", "Stamen Toner"))
        self.label_37.setText(_translate("lcd_display", "(recomendet for large data sets)"))
        self.label_46.setText(_translate("lcd_display", "(recomendet for large data)"))
        self.label_4.setText(_translate("lcd_display", "Tooltips in Markers"))
        self.label_38.setText(_translate("lcd_display", "(or filepath,  dictionarys have to exist)"))
        self.label_47.setText(_translate("lcd_display", "(Integer numbers)"))
        self.label_5.setText(_translate("lcd_display", "Mapname"))
        self.label_6.setText(_translate("lcd_display", "Map Options"))
        self.text_Mapname.setText(_translate("lcd_display", "examplename"))
        self.label_34.setText(_translate("lcd_display", "(just up to 3000 points)"))
        self.bt_Mapping.setText(_translate("lcd_display", "Save Map"))
        self.label_31.setText(_translate("lcd_display", "Keep every ... Marker"))
        self.label_Maptype.setText(_translate("lcd_display", "Maptype"))
        self.checkBox_cluster.setText(_translate("lcd_display", "Cluster Markers"))
        self.checkBox_Marker.setText(_translate("lcd_display", "Markers"))
        self.checkBox_Polyline.setText(_translate("lcd_display", "Polyline between Markers"))
        self.label_13.setText(_translate("lcd_display", "Seperator"))
        self.text_datasave_seperator.setText(_translate("lcd_display", ","))
        self.comboBox_datasave_format.setItemText(0, _translate("lcd_display", ".csv"))
        self.comboBox_datasave_format.setItemText(1, _translate("lcd_display", ".xlsx"))
        self.label_14.setText(_translate("lcd_display", "Filename"))
        self.text_datasave_filename.setText(_translate("lcd_display", "file"))
        self.label_2.setText(_translate("lcd_display", "Fileformat"))
        self.label_24.setText(_translate("lcd_display", "(only for csv)"))
        self.label_12.setText(_translate("lcd_display", "Save Data"))
        self.bt_savefiltered.setText(_translate("lcd_display", "Save Filtered Data"))
        self.checkBox.setText(_translate("lcd_display", "save jumppoints in .xlsx file"))
        self.label_15.setText(_translate("lcd_display", "Current Data"))
        self.label_30.setText(_translate("lcd_display", "Lines of Data:"))
        self.bt_cleardata.setText(_translate("lcd_display", "Clear Data"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    lcd_display = QtWidgets.QMainWindow()
    ui = Ui_lcd_display()
    ui.setupUi(lcd_display)
    lcd_display.show()
    sys.exit(app.exec_())
