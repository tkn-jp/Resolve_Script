# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\yoshi\PycharmProjects\Resolve_Script\app\resolve\Python\rs_resolve\tool\voice_bin_assistant\voice_bin_assistant.ui',
# licensing of 'C:\Users\yoshi\PycharmProjects\Resolve_Script\app\resolve\Python\rs_resolve\tool\voice_bin_assistant\voice_bin_assistant.ui' applies.
#
# Created: Wed Dec  7 07:14:41 2022
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(546, 756)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.importWaitSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.importWaitSpinBox.setObjectName("importWaitSpinBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.importWaitSpinBox)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.offsetSpinBox = QtWidgets.QSpinBox(self.groupBox)
        self.offsetSpinBox.setObjectName("offsetSpinBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.offsetSpinBox)
        self.referTrackCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.referTrackCheckBox.setObjectName("referTrackCheckBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.referTrackCheckBox)
        self.verticalLayout_6.addWidget(self.groupBox)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textPlusCheckBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.textPlusCheckBox.setObjectName("textPlusCheckBox")
        self.horizontalLayout.addWidget(self.textPlusCheckBox)
        self.tatieCheckBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.tatieCheckBox.setObjectName("tatieCheckBox")
        self.horizontalLayout.addWidget(self.tatieCheckBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.tatieWaitSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.tatieWaitSpinBox.setObjectName("tatieWaitSpinBox")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.tatieWaitSpinBox)
        self.verticalLayout_4.addLayout(self.formLayout_2)
        self.verticalLayout_6.addWidget(self.groupBox_3)
        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy)
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setMinimumSize(QtCore.QSize(30, 0))
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.videoListView = QtWidgets.QListView(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.videoListView.sizePolicy().hasHeightForWidth())
        self.videoListView.setSizePolicy(sizePolicy)
        self.videoListView.setMinimumSize(QtCore.QSize(0, 0))
        self.videoListView.setBaseSize(QtCore.QSize(0, 0))
        self.videoListView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.videoListView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.videoListView.setObjectName("videoListView")
        self.verticalLayout_2.addWidget(self.videoListView)
        self.horizontalLayout_2.addWidget(self.groupBox_4)
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy)
        self.groupBox_5.setMinimumSize(QtCore.QSize(30, 0))
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.audioListView = QtWidgets.QListView(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.audioListView.sizePolicy().hasHeightForWidth())
        self.audioListView.setSizePolicy(sizePolicy)
        self.audioListView.setMinimumSize(QtCore.QSize(0, 0))
        self.audioListView.setBaseSize(QtCore.QSize(1, 0))
        self.audioListView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.audioListView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.audioListView.setObjectName("audioListView")
        self.verticalLayout_3.addWidget(self.audioListView)
        self.horizontalLayout_2.addWidget(self.groupBox_5)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.copyTextButton = QtWidgets.QPushButton(self.groupBox_6)
        self.copyTextButton.setObjectName("copyTextButton")
        self.horizontalLayout_4.addWidget(self.copyTextButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.updateTrackButton = QtWidgets.QPushButton(self.groupBox_6)
        self.updateTrackButton.setObjectName("updateTrackButton")
        self.horizontalLayout_4.addWidget(self.updateTrackButton)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.verticalLayout_6.addWidget(self.groupBox_6)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.logTextEdit = LogTextEdit(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logTextEdit.sizePolicy().hasHeightForWidth())
        self.logTextEdit.setSizePolicy(sizePolicy)
        self.logTextEdit.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.logTextEdit.setReadOnly(True)
        self.logTextEdit.setObjectName("logTextEdit")
        self.verticalLayout.addWidget(self.logTextEdit)
        self.verticalLayout_6.addWidget(self.groupBox_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.importButton = QtWidgets.QPushButton(self.centralwidget)
        self.importButton.setMinimumSize(QtCore.QSize(100, 40))
        self.importButton.setObjectName("importButton")
        self.horizontalLayout_3.addWidget(self.importButton)
        self.tatieButton = QtWidgets.QPushButton(self.centralwidget)
        self.tatieButton.setMinimumSize(QtCore.QSize(100, 40))
        self.tatieButton.setObjectName("tatieButton")
        self.horizontalLayout_3.addWidget(self.tatieButton)
        self.closeButton = QtWidgets.QPushButton(self.centralwidget)
        self.closeButton.setMinimumSize(QtCore.QSize(100, 40))
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout_3.addWidget(self.closeButton)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("MainWindow", "読み込み", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "待ち時間", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "間隔(フレーム)", None, -1))
        self.referTrackCheckBox.setText(QtWidgets.QApplication.translate("MainWindow", "ビデオトラックを参照する", None, -1))
        self.groupBox_3.setTitle(QtWidgets.QApplication.translate("MainWindow", "TEXT+ 立ち絵", None, -1))
        self.textPlusCheckBox.setText(QtWidgets.QApplication.translate("MainWindow", "TEXT+", None, -1))
        self.tatieCheckBox.setText(QtWidgets.QApplication.translate("MainWindow", "立ち絵", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("MainWindow", "待ち時間", None, -1))
        self.groupBox_6.setTitle(QtWidgets.QApplication.translate("MainWindow", "トラック選択", None, -1))
        self.groupBox_4.setTitle(QtWidgets.QApplication.translate("MainWindow", "ビデオ トラック", None, -1))
        self.groupBox_5.setTitle(QtWidgets.QApplication.translate("MainWindow", "オーディオ トラック", None, -1))
        self.copyTextButton.setText(QtWidgets.QApplication.translate("MainWindow", "TEXT+ コピー", None, -1))
        self.updateTrackButton.setText(QtWidgets.QApplication.translate("MainWindow", "トラック 更新", None, -1))
        self.groupBox_2.setTitle(QtWidgets.QApplication.translate("MainWindow", "ログ", None, -1))
        self.importButton.setText(QtWidgets.QApplication.translate("MainWindow", "読み込み(wav)", None, -1))
        self.tatieButton.setText(QtWidgets.QApplication.translate("MainWindow", "TEXT+ 立ち絵", None, -1))
        self.closeButton.setText(QtWidgets.QApplication.translate("MainWindow", "close", None, -1))

from rs.gui.log import LogTextEdit