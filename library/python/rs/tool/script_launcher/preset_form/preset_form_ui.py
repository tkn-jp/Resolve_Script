# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\yoshi\PycharmProjects\Resolve_Script\library\python\rs\tool\script_launcher\preset_form\preset_form.ui',
# licensing of 'C:\Users\yoshi\PycharmProjects\Resolve_Script\library\python\rs\tool\script_launcher\preset_form\preset_form.ui' applies.
#
# Created: Fri Jun 17 14:49:24 2022
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(514, 608)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.splitter_2 = QtWidgets.QSplitter(Form)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.groupBox = QtWidgets.QGroupBox(self.splitter_2)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.splitter = QtWidgets.QSplitter(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.dirListView = QtWidgets.QListView(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dirListView.sizePolicy().hasHeightForWidth())
        self.dirListView.setSizePolicy(sizePolicy)
        self.dirListView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.dirListView.setObjectName("dirListView")
        self.fileListView = QtWidgets.QListView(self.splitter)
        self.fileListView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.fileListView.setObjectName("fileListView")
        self.verticalLayout_4.addWidget(self.splitter)
        self.widget = QtWidgets.QWidget(self.splitter_2)
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.makeButton = DragButton(self.widget)
        self.makeButton.setMinimumSize(QtCore.QSize(100, 100))
        self.makeButton.setObjectName("makeButton")
        self.verticalLayout_2.addWidget(self.makeButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.closeButton = QtWidgets.QPushButton(self.widget)
        self.closeButton.setMinimumSize(QtCore.QSize(100, 40))
        self.closeButton.setObjectName("closeButton")
        self.verticalLayout_2.addWidget(self.closeButton)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.groupBox_2 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.filterListView = QtWidgets.QListView(self.groupBox_2)
        self.filterListView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.filterListView.setObjectName("filterListView")
        self.verticalLayout.addWidget(self.filterListView)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.filterNameLineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.filterNameLineEdit.setObjectName("filterNameLineEdit")
        self.horizontalLayout.addWidget(self.filterNameLineEdit)
        self.addFilterButton = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addFilterButton.sizePolicy().hasHeightForWidth())
        self.addFilterButton.setSizePolicy(sizePolicy)
        self.addFilterButton.setMinimumSize(QtCore.QSize(0, 0))
        self.addFilterButton.setMaximumSize(QtCore.QSize(40, 16777215))
        self.addFilterButton.setObjectName("addFilterButton")
        self.horizontalLayout.addWidget(self.addFilterButton)
        self.renameButton = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.renameButton.sizePolicy().hasHeightForWidth())
        self.renameButton.setSizePolicy(sizePolicy)
        self.renameButton.setMinimumSize(QtCore.QSize(40, 0))
        self.renameButton.setMaximumSize(QtCore.QSize(70, 16777215))
        self.renameButton.setObjectName("renameButton")
        self.horizontalLayout.addWidget(self.renameButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.editFilterButton = QtWidgets.QPushButton(self.groupBox_2)
        self.editFilterButton.setObjectName("editFilterButton")
        self.verticalLayout.addWidget(self.editFilterButton)
        self.horizontalLayout_3.addWidget(self.groupBox_2)
        self.verticalLayout_3.addWidget(self.splitter_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("Form", "Setting File", None, -1))
        self.makeButton.setText(QtWidgets.QApplication.translate("Form", "Drag", None, -1))
        self.closeButton.setText(QtWidgets.QApplication.translate("Form", "close", None, -1))
        self.groupBox_2.setTitle(QtWidgets.QApplication.translate("Form", "Filter", None, -1))
        self.addFilterButton.setText(QtWidgets.QApplication.translate("Form", "add", None, -1))
        self.renameButton.setText(QtWidgets.QApplication.translate("Form", "rename", None, -1))
        self.editFilterButton.setText(QtWidgets.QApplication.translate("Form", "edit", None, -1))

from rs.tool.script_launcher.preset_form import DragButton