# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\yoshi\PycharmProjects\Resolve_Script\library\python\yr\tool\softalk2resolve\softalk2resolve.ui',
# licensing of 'C:\Users\yoshi\PycharmProjects\Resolve_Script\library\python\yr\tool\softalk2resolve\softalk2resolve.ui' applies.
#
# Created: Thu Feb  3 03:42:10 2022
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(720, 547)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setOpaqueResize(True)
        self.splitter.setObjectName("splitter")
        self.treeView = QtWidgets.QTreeView(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeView.sizePolicy().hasHeightForWidth())
        self.treeView.setSizePolicy(sizePolicy)
        self.treeView.setMinimumSize(QtCore.QSize(300, 0))
        self.treeView.setDragEnabled(True)
        self.treeView.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.treeView.setObjectName("treeView")
        self.widget = QtWidgets.QWidget(self.splitter)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.softalkwLineEdit = QtWidgets.QLineEdit(self.widget)
        self.softalkwLineEdit.setObjectName("softalkwLineEdit")
        self.horizontalLayout_2.addWidget(self.softalkwLineEdit)
        self.softalkwToolButton = QtWidgets.QToolButton(self.widget)
        self.softalkwToolButton.setObjectName("softalkwToolButton")
        self.horizontalLayout_2.addWidget(self.softalkwToolButton)
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.outLineEdit = QtWidgets.QLineEdit(self.widget)
        self.outLineEdit.setObjectName("outLineEdit")
        self.horizontalLayout.addWidget(self.outLineEdit)
        self.outToolButton = QtWidgets.QToolButton(self.widget)
        self.outToolButton.setObjectName("outToolButton")
        self.horizontalLayout.addWidget(self.outToolButton)
        self.formLayout_2.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.verticalLayout_2.addLayout(self.formLayout_2)
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.groupBox)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.horizontalLayout_4.addWidget(self.plainTextEdit)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.voiceComboBox = QtWidgets.QComboBox(self.groupBox)
        self.voiceComboBox.setMaximumSize(QtCore.QSize(120, 16777215))
        self.voiceComboBox.setObjectName("voiceComboBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.voiceComboBox)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.volumeSpinBox = QtWidgets.QSpinBox(self.groupBox)
        self.volumeSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.volumeSpinBox.setMaximum(100)
        self.volumeSpinBox.setObjectName("volumeSpinBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.volumeSpinBox)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.speedSpinBox = QtWidgets.QSpinBox(self.groupBox)
        self.speedSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.speedSpinBox.setMinimum(1)
        self.speedSpinBox.setMaximum(300)
        self.speedSpinBox.setObjectName("speedSpinBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.speedSpinBox)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.pitchSpinBox = QtWidgets.QSpinBox(self.groupBox)
        self.pitchSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.pitchSpinBox.setMaximum(300)
        self.pitchSpinBox.setObjectName("pitchSpinBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.pitchSpinBox)
        self.horizontalLayout_4.addLayout(self.formLayout)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.logTextEdit = QtWidgets.QTextEdit(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logTextEdit.sizePolicy().hasHeightForWidth())
        self.logTextEdit.setSizePolicy(sizePolicy)
        self.logTextEdit.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.logTextEdit.setReadOnly(True)
        self.logTextEdit.setObjectName("logTextEdit")
        self.verticalLayout.addWidget(self.logTextEdit)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.exportButton = QtWidgets.QPushButton(self.widget)
        self.exportButton.setMinimumSize(QtCore.QSize(100, 40))
        self.exportButton.setObjectName("exportButton")
        self.horizontalLayout_3.addWidget(self.exportButton)
        self.closeButton = QtWidgets.QPushButton(self.widget)
        self.closeButton.setMinimumSize(QtCore.QSize(100, 40))
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout_3.addWidget(self.closeButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 720, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionSave_Voice_Template = QtWidgets.QAction(MainWindow)
        self.actionSave_Voice_Template.setObjectName("actionSave_Voice_Template")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_Voice_Template)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "softalkwの場所", None, -1))
        self.softalkwToolButton.setText(QtWidgets.QApplication.translate("MainWindow", "...", None, -1))
        self.outToolButton.setText(QtWidgets.QApplication.translate("MainWindow", "...", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "保存ディレクトリ", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("MainWindow", "音声設定", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("MainWindow", "声", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("MainWindow", "音量", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("MainWindow", "速度", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("MainWindow", "音程", None, -1))
        self.groupBox_2.setTitle(QtWidgets.QApplication.translate("MainWindow", "ログ", None, -1))
        self.exportButton.setText(QtWidgets.QApplication.translate("MainWindow", "export", None, -1))
        self.closeButton.setText(QtWidgets.QApplication.translate("MainWindow", "close", None, -1))
        self.menuFile.setTitle(QtWidgets.QApplication.translate("MainWindow", "File", None, -1))
        self.actionOpen.setText(QtWidgets.QApplication.translate("MainWindow", "Open", None, -1))
        self.actionOpen.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+O", None, -1))
        self.actionSave.setText(QtWidgets.QApplication.translate("MainWindow", "Save", None, -1))
        self.actionSave.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+S", None, -1))
        self.actionExit.setText(QtWidgets.QApplication.translate("MainWindow", "Exit", None, -1))
        self.actionExit.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+Q", None, -1))
        self.actionSave_Voice_Template.setText(QtWidgets.QApplication.translate("MainWindow", "Save Voice Template", None, -1))

