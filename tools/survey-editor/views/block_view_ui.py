# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'block.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Block(object):
    def setupUi(self, Block):
        Block.setObjectName("Block")
        Block.resize(1366, 768)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setBold(False)
        font.setWeight(50)
        Block.setFont(font)
        self.gridLayout_4 = QtWidgets.QGridLayout(Block)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame_2 = QtWidgets.QFrame(Block)
        self.frame_2.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setBold(True)
        font.setWeight(75)
        self.frame_2.setFont(font)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.questions_headline = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        self.questions_headline.setFont(font)
        self.questions_headline.setAlignment(QtCore.Qt.AlignCenter)
        self.questions_headline.setObjectName("questions_headline")
        self.gridLayout_2.addWidget(self.questions_headline, 0, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_5.addWidget(self.pushButton_5)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_5.addWidget(self.pushButton_4)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        self.line_3.setFont(font)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_2.addWidget(self.line_3, 3, 0, 1, 1)
        self.time_headline = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setBold(True)
        font.setWeight(75)
        self.time_headline.setFont(font)
        self.time_headline.setAlignment(QtCore.Qt.AlignCenter)
        self.time_headline.setObjectName("time_headline")
        self.gridLayout_2.addWidget(self.time_headline, 4, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.time_field = QtWidgets.QLineEdit(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setBold(True)
        font.setWeight(75)
        self.time_field.setFont(font)
        self.time_field.setText("")
        self.time_field.setPlaceholderText("")
        self.time_field.setObjectName("time_field")
        self.horizontalLayout_2.addWidget(self.time_field)
        self.comboBox = QtWidgets.QComboBox(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setCurrentText("")
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 5, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setBold(True)
        font.setWeight(75)
        self.line.setFont(font)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 6, 0, 1, 1)
        self.settings_headline = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setBold(True)
        font.setWeight(75)
        self.settings_headline.setFont(font)
        self.settings_headline.setAlignment(QtCore.Qt.AlignCenter)
        self.settings_headline.setObjectName("settings_headline")
        self.gridLayout_2.addWidget(self.settings_headline, 7, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.settings_field = QtWidgets.QLineEdit(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setBold(True)
        font.setWeight(75)
        self.settings_field.setFont(font)
        self.settings_field.setText("")
        self.settings_field.setPlaceholderText("")
        self.settings_field.setObjectName("settings_field")
        self.horizontalLayout_3.addWidget(self.settings_field)
        self.comboBox_2 = QtWidgets.QComboBox(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.horizontalLayout_3.addWidget(self.comboBox_2)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 8, 0, 1, 1)
        self.settings_list = QtWidgets.QListView(self.frame_2)
        self.settings_list.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setBold(True)
        font.setWeight(75)
        self.settings_list.setFont(font)
        self.settings_list.setObjectName("settings_list")
        self.gridLayout_2.addWidget(self.settings_list, 9, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.settings_add_button = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setBold(True)
        font.setWeight(75)
        self.settings_add_button.setFont(font)
        self.settings_add_button.setObjectName("settings_add_button")
        self.horizontalLayout_4.addWidget(self.settings_add_button)
        self.settings_delete_button = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setBold(True)
        font.setWeight(75)
        self.settings_delete_button.setFont(font)
        self.settings_delete_button.setObjectName("settings_delete_button")
        self.horizontalLayout_4.addWidget(self.settings_delete_button)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 10, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setBold(True)
        font.setWeight(75)
        self.line_2.setFont(font)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_2.addWidget(self.line_2, 11, 0, 1, 1)
        self.meta_label = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setBold(True)
        font.setWeight(75)
        self.meta_label.setFont(font)
        self.meta_label.setAlignment(QtCore.Qt.AlignCenter)
        self.meta_label.setObjectName("meta_label")
        self.gridLayout_2.addWidget(self.meta_label, 12, 0, 1, 1)
        self.meta_field = QtWidgets.QPlainTextEdit(self.frame_2)
        self.meta_field.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setBold(True)
        font.setWeight(75)
        self.meta_field.setFont(font)
        self.meta_field.setObjectName("meta_field")
        self.gridLayout_2.addWidget(self.meta_field, 13, 0, 1, 1)
        self.meta_save_button = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setBold(True)
        font.setWeight(75)
        self.meta_save_button.setFont(font)
        self.meta_save_button.setObjectName("meta_save_button")
        self.gridLayout_2.addWidget(self.meta_save_button, 14, 0, 1, 1)
        self.question_list = QtWidgets.QListWidget(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        self.question_list.setFont(font)
        self.question_list.setObjectName("question_list")
        self.gridLayout_2.addWidget(self.question_list, 1, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame_2, 1, 0, 2, 1)
        self.frame = QtWidgets.QFrame(Block)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setBold(True)
        font.setWeight(75)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.headline = QtWidgets.QLabel(self.frame)
        self.headline.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.headline.setFont(font)
        self.headline.setAlignment(QtCore.Qt.AlignCenter)
        self.headline.setObjectName("headline")
        self.gridLayout.addWidget(self.headline, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame, 0, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(Block)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setBold(True)
        font.setWeight(75)
        self.frame_3.setFont(font)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.previous_block_button = QtWidgets.QPushButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setBold(True)
        font.setWeight(75)
        self.previous_block_button.setFont(font)
        self.previous_block_button.setObjectName("previous_block_button")
        self.horizontalLayout.addWidget(self.previous_block_button)
        self.back_to_days_button = QtWidgets.QPushButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setBold(True)
        font.setWeight(75)
        self.back_to_days_button.setFont(font)
        self.back_to_days_button.setObjectName("back_to_days_button")
        self.horizontalLayout.addWidget(self.back_to_days_button)
        self.next_block_button = QtWidgets.QPushButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setBold(True)
        font.setWeight(75)
        self.next_block_button.setFont(font)
        self.next_block_button.setObjectName("next_block_button")
        self.horizontalLayout.addWidget(self.next_block_button)
        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame_3, 2, 1, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(Block)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.gridLayout_4.addWidget(self.tabWidget, 0, 1, 2, 1)

        self.retranslateUi(Block)
        self.tabWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Block)

    def retranslateUi(self, Block):
        _translate = QtCore.QCoreApplication.translate
        Block.setWindowTitle(_translate("Block", "Form"))
        self.questions_headline.setText(_translate("Block", "Questions"))
        self.pushButton_5.setText(_translate("Block", "new"))
        self.pushButton_4.setText(_translate("Block", "delete"))
        self.time_headline.setText(_translate("Block", "Time"))
        self.settings_headline.setText(_translate("Block", "Settings"))
        self.settings_add_button.setText(_translate("Block", "add"))
        self.settings_delete_button.setText(_translate("Block", "delete"))
        self.meta_label.setText(_translate("Block", "Meta"))
        self.meta_save_button.setText(_translate("Block", "save"))
        self.headline.setText(_translate("Block", "Block X"))
        self.previous_block_button.setText(_translate("Block", "previous"))
        self.back_to_days_button.setText(_translate("Block", "back to days"))
        self.next_block_button.setText(_translate("Block", "next"))


