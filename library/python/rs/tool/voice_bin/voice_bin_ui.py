# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\yoshi\PycharmProjects\Resolve_Script\library\python\rs\tool\voice_bin\voice_bin.ui',
# licensing of 'C:\Users\yoshi\PycharmProjects\Resolve_Script\library\python\rs\tool\voice_bin\voice_bin.ui' applies.
#
# Created: Sat Jun 25 17:49:02 2022
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(402, 537)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setObjectName("tabWidget")
        self.stTab = QtWidgets.QWidget()
        self.stTab.setObjectName("stTab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.stTab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.treeView = QtWidgets.QTreeView(self.stTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeView.sizePolicy().hasHeightForWidth())
        self.treeView.setSizePolicy(sizePolicy)
        self.treeView.setMinimumSize(QtCore.QSize(350, 0))
        self.treeView.setDragEnabled(True)
        self.treeView.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.treeView.setObjectName("treeView")
        self.verticalLayout.addWidget(self.treeView)
        self.tabWidget.addTab(self.stTab, "")
        self.textTab = QtWidgets.QWidget()
        self.textTab.setObjectName("textTab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.textTab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.dragButton = DragButton(self.textTab)
        self.dragButton.setMinimumSize(QtCore.QSize(100, 100))
        self.dragButton.setObjectName("dragButton")
        self.horizontalLayout_3.addWidget(self.dragButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_2.addItem(spacerItem1)
        self.charaButton = QtWidgets.QPushButton(self.textTab)
        self.charaButton.setObjectName("charaButton")
        self.verticalLayout_2.addWidget(self.charaButton)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.wavTreeView = QtWidgets.QTreeView(self.textTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wavTreeView.sizePolicy().hasHeightForWidth())
        self.wavTreeView.setSizePolicy(sizePolicy)
        self.wavTreeView.setMinimumSize(QtCore.QSize(350, 0))
        self.wavTreeView.setDragEnabled(True)
        self.wavTreeView.setObjectName("wavTreeView")
        self.verticalLayout_4.addWidget(self.wavTreeView)
        self.tabWidget.addTab(self.textTab, "")
        self.verticalLayout_3.addWidget(self.tabWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.folderLineEdit = QtWidgets.QLineEdit(Form)
        self.folderLineEdit.setObjectName("folderLineEdit")
        self.horizontalLayout_2.addWidget(self.folderLineEdit)
        self.folderToolButton = QtWidgets.QToolButton(Form)
        self.folderToolButton.setObjectName("folderToolButton")
        self.horizontalLayout_2.addWidget(self.folderToolButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.closeButton = QtWidgets.QPushButton(Form)
        self.closeButton.setMinimumSize(QtCore.QSize(100, 40))
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout.addWidget(self.closeButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.stTab), QtWidgets.QApplication.translate("Form", "字幕", None, -1))
        self.dragButton.setText(QtWidgets.QApplication.translate("Form", " Apply", None, -1))
        self.charaButton.setText(QtWidgets.QApplication.translate("Form", "キャラクター設定", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.textTab), QtWidgets.QApplication.translate("Form", "テキスト+", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "声フォルダ: ", None, -1))
        self.folderToolButton.setText(QtWidgets.QApplication.translate("Form", "...", None, -1))
        self.closeButton.setText(QtWidgets.QApplication.translate("Form", "close", None, -1))

from rs.tool.voice_bin.drag_button import DragButton
