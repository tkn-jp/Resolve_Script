# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\yoshi\PycharmProjects\Resolve_Script\app\resolve\Python\rs_resolve\tool\voice_dropper\voice_dropper.ui',
# licensing of 'C:\Users\yoshi\PycharmProjects\Resolve_Script\app\resolve\Python\rs_resolve\tool\voice_dropper\voice_dropper.ui' applies.
#
# Created: Sun Dec 25 02:56:19 2022
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(379, 469)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.voiceDirLineEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.voiceDirLineEdit.setObjectName("voiceDirLineEdit")
        self.horizontalLayout_2.addWidget(self.voiceDirLineEdit)
        self.voiceDirToolButton = QtWidgets.QToolButton(self.groupBox_3)
        self.voiceDirToolButton.setObjectName("voiceDirToolButton")
        self.horizontalLayout_2.addWidget(self.voiceDirToolButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.statusLabel = QtWidgets.QLabel(self.groupBox_3)
        self.statusLabel.setMinimumSize(QtCore.QSize(0, 0))
        self.statusLabel.setObjectName("statusLabel")
        self.horizontalLayout_3.addWidget(self.statusLabel)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.startButton = QtWidgets.QPushButton(self.groupBox_3)
        self.startButton.setObjectName("startButton")
        self.horizontalLayout_3.addWidget(self.startButton)
        self.stopButton = QtWidgets.QPushButton(self.groupBox_3)
        self.stopButton.setObjectName("stopButton")
        self.horizontalLayout_3.addWidget(self.stopButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.waitTimeSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.waitTimeSpinBox.setDecimals(3)
        self.waitTimeSpinBox.setObjectName("waitTimeSpinBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.waitTimeSpinBox)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.offsetSpinBox = QtWidgets.QSpinBox(self.groupBox)
        self.offsetSpinBox.setMaximum(999999999)
        self.offsetSpinBox.setObjectName("offsetSpinBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.offsetSpinBox)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.videoIndexSpinBox = QtWidgets.QSpinBox(self.groupBox)
        self.videoIndexSpinBox.setMinimum(1)
        self.videoIndexSpinBox.setMaximum(8)
        self.videoIndexSpinBox.setObjectName("videoIndexSpinBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.videoIndexSpinBox)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label)
        self.audioIndexSpinBox = QtWidgets.QSpinBox(self.groupBox)
        self.audioIndexSpinBox.setMinimum(1)
        self.audioIndexSpinBox.setMaximum(8)
        self.audioIndexSpinBox.setObjectName("audioIndexSpinBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.audioIndexSpinBox)
        self.makeScriptCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.makeScriptCheckBox.setObjectName("makeScriptCheckBox")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.makeScriptCheckBox)
        self.useCharaCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.useCharaCheckBox.setObjectName("useCharaCheckBox")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.useCharaCheckBox)
        self.verticalLayout_3.addWidget(self.groupBox)
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
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.importButton = QtWidgets.QPushButton(self.centralwidget)
        self.importButton.setMinimumSize(QtCore.QSize(80, 30))
        self.importButton.setObjectName("importButton")
        self.horizontalLayout.addWidget(self.importButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.minimizeButton = QtWidgets.QToolButton(self.centralwidget)
        self.minimizeButton.setMinimumSize(QtCore.QSize(30, 30))
        self.minimizeButton.setArrowType(QtCore.Qt.DownArrow)
        self.minimizeButton.setObjectName("minimizeButton")
        self.horizontalLayout.addWidget(self.minimizeButton)
        self.closeButton = QtWidgets.QPushButton(self.centralwidget)
        self.closeButton.setMinimumSize(QtCore.QSize(80, 30))
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout.addWidget(self.closeButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.groupBox_3.setTitle(QtWidgets.QApplication.translate("MainWindow", "声フォルダ", None, -1))
        self.voiceDirToolButton.setText(QtWidgets.QApplication.translate("MainWindow", "...", None, -1))
        self.statusLabel.setText(QtWidgets.QApplication.translate("MainWindow", "停止中", None, -1))
        self.startButton.setText(QtWidgets.QApplication.translate("MainWindow", "start", None, -1))
        self.stopButton.setText(QtWidgets.QApplication.translate("MainWindow", "stop", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("MainWindow", "読み込み", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "待ち時間(秒)", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("MainWindow", "間隔(フレーム)", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("MainWindow", "ビデオトラック", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "オーディオトラック", None, -1))
        self.makeScriptCheckBox.setText(QtWidgets.QApplication.translate("MainWindow", "VoiceBin用スクリプトを生成する", None, -1))
        self.useCharaCheckBox.setText(QtWidgets.QApplication.translate("MainWindow", "VoiceBinのキャラクター設定を使って配置", None, -1))
        self.groupBox_2.setTitle(QtWidgets.QApplication.translate("MainWindow", "ログ", None, -1))
        self.importButton.setText(QtWidgets.QApplication.translate("MainWindow", "import", None, -1))
        self.minimizeButton.setToolTip(QtWidgets.QApplication.translate("MainWindow", "最小化", None, -1))
        self.minimizeButton.setText(QtWidgets.QApplication.translate("MainWindow", "...", None, -1))
        self.closeButton.setToolTip(QtWidgets.QApplication.translate("MainWindow", "閉じる", None, -1))
        self.closeButton.setText(QtWidgets.QApplication.translate("MainWindow", "close", None, -1))

from rs.gui.log import LogTextEdit
