# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'basic_dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from swing_utils import fakestr


class Ui_BasicDialog(object):
    def setupUi(self, BasicDialog):
        if not BasicDialog.objectName():
            BasicDialog.setObjectName(u"BasicDialog")
        BasicDialog.setWindowModality(Qt.ApplicationModal)
        BasicDialog.resize(380, 260)
        
        self.verticalLayout_2 = QVBoxLayout(BasicDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        
        self.labelLevelSequence = QLabel(BasicDialog)
        self.labelLevelSequence.setObjectName(u"labelLevelSequence")
        self.verticalLayout.addWidget(self.labelLevelSequence)

        self.comboBoxLevelSequence = QComboBox()
        self.comboBoxLevelSequence.setObjectName(u"comboBoxLevelSequence")
        self.verticalLayout.addWidget(self.comboBoxLevelSequence)

        self.labelMap = QLabel(BasicDialog)
        self.labelMap.setObjectName(u"labelMap")
        self.verticalLayout.addWidget(self.labelMap)

        self.comboBoxMap = QComboBox()
        self.comboBoxMap.setObjectName(u"comboBoxMap")
        self.verticalLayout.addWidget(self.comboBoxMap)

        self.labelPreset = QLabel(BasicDialog)
        self.labelPreset.setObjectName(u"labelPreset")
        self.verticalLayout.addWidget(self.labelPreset)

        self.comboBoxPreset = QComboBox()
        self.comboBoxPreset.setObjectName(u"comboBoxPreset")
        self.verticalLayout.addWidget(self.comboBoxPreset)

        self.labelOutputFolder = QLabel()
        self.labelOutputFolder.setObjectName(u"labelOutputFolder")
        self.verticalLayout.addWidget(self.labelOutputFolder)

        self.lineEditOutputFolder = QLineEdit(BasicDialog)
        self.lineEditOutputFolder.setObjectName(u"lineEditOutputFolder")
        self.verticalLayout.addWidget(self.lineEditOutputFolder)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.buttonBox = QDialogButtonBox(BasicDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)


        self.retranslateUi(BasicDialog)
        self.buttonBox.accepted.connect(BasicDialog.accept)
        self.buttonBox.rejected.connect(BasicDialog.reject)

        QMetaObject.connectSlotsByName(BasicDialog)
    # setupUi

    def retranslateUi(self, BasicDialog):
        BasicDialog.setWindowTitle(fakestr(u"MRQ Renderer", None))
        self.labelLevelSequence.setText(fakestr(u"Level Sequence", None))
        self.labelMap.setText(fakestr(u"Map", None))
        self.labelPreset.setText(fakestr(u"Preset", None))
        self.labelOutputFolder.setText(fakestr(u"Output Folder:", None))
    # retranslateUi

