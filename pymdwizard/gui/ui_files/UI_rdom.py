# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rdom.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_fgdc_attrdomv(object):
    def setupUi(self, fgdc_attrdomv):
        fgdc_attrdomv.setObjectName("fgdc_attrdomv")
        fgdc_attrdomv.resize(354, 442)
        self.verticalLayout = QtWidgets.QVBoxLayout(fgdc_attrdomv)
        self.verticalLayout.setObjectName("verticalLayout")
        self.fgdc_rdom = QtWidgets.QWidget(fgdc_attrdomv)
        self.fgdc_rdom.setObjectName("fgdc_rdom")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.fgdc_rdom)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_19 = QtWidgets.QLabel(self.fgdc_rdom)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)
        self.label_19.setMinimumSize(QtCore.QSize(0, 0))
        self.label_19.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("")
        self.label_19.setScaledContents(False)
        self.label_19.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft
        )
        self.label_19.setWordWrap(False)
        self.label_19.setIndent(0)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_5.addWidget(self.label_19)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.fgdc_rdommin = QtWidgets.QLineEdit(self.fgdc_rdom)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fgdc_rdommin.sizePolicy().hasHeightForWidth())
        self.fgdc_rdommin.setSizePolicy(sizePolicy)
        self.fgdc_rdommin.setMinimumSize(QtCore.QSize(0, 0))
        self.fgdc_rdommin.setMaximumSize(QtCore.QSize(16777215, 20))
        self.fgdc_rdommin.setObjectName("fgdc_rdommin")
        self.horizontalLayout_8.addWidget(self.fgdc_rdommin)
        self.label_20 = QtWidgets.QLabel(self.fgdc_rdom)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)
        self.label_20.setMinimumSize(QtCore.QSize(15, 0))
        self.label_20.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_20.setFont(font)
        self.label_20.setScaledContents(True)
        self.label_20.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label_20.setIndent(0)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_8.addWidget(self.label_20)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.label_21 = QtWidgets.QLabel(self.fgdc_rdom)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy)
        self.label_21.setMinimumSize(QtCore.QSize(0, 0))
        self.label_21.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_21.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft
        )
        self.label_21.setObjectName("label_21")
        self.verticalLayout_5.addWidget(self.label_21)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.fgdc_rdommax = QtWidgets.QLineEdit(self.fgdc_rdom)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fgdc_rdommax.sizePolicy().hasHeightForWidth())
        self.fgdc_rdommax.setSizePolicy(sizePolicy)
        self.fgdc_rdommax.setMinimumSize(QtCore.QSize(0, 0))
        self.fgdc_rdommax.setMaximumSize(QtCore.QSize(16777215, 20))
        self.fgdc_rdommax.setObjectName("fgdc_rdommax")
        self.horizontalLayout_9.addWidget(self.fgdc_rdommax)
        self.label_25 = QtWidgets.QLabel(self.fgdc_rdom)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy)
        self.label_25.setMinimumSize(QtCore.QSize(15, 20))
        self.label_25.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_25.setFont(font)
        self.label_25.setScaledContents(True)
        self.label_25.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label_25.setIndent(0)
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_9.addWidget(self.label_25)
        self.verticalLayout_5.addLayout(self.horizontalLayout_9)
        self.label_22 = QtWidgets.QLabel(self.fgdc_rdom)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy)
        self.label_22.setMinimumSize(QtCore.QSize(0, 0))
        self.label_22.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_22.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft
        )
        self.label_22.setObjectName("label_22")
        self.verticalLayout_5.addWidget(self.label_22)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.fgdc_attrunit = QtWidgets.QLineEdit(self.fgdc_rdom)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.fgdc_attrunit.sizePolicy().hasHeightForWidth()
        )
        self.fgdc_attrunit.setSizePolicy(sizePolicy)
        self.fgdc_attrunit.setMinimumSize(QtCore.QSize(0, 0))
        self.fgdc_attrunit.setMaximumSize(QtCore.QSize(16777215, 20))
        self.fgdc_attrunit.setObjectName("fgdc_attrunit")
        self.horizontalLayout_10.addWidget(self.fgdc_attrunit)
        spacerItem = QtWidgets.QSpacerItem(
            15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_10.addItem(spacerItem)
        self.verticalLayout_5.addLayout(self.horizontalLayout_10)
        self.label_23 = QtWidgets.QLabel(self.fgdc_rdom)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy)
        self.label_23.setMinimumSize(QtCore.QSize(0, 0))
        self.label_23.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_23.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft
        )
        self.label_23.setObjectName("label_23")
        self.verticalLayout_5.addWidget(self.label_23)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.fgdc_attrmres = QtWidgets.QLineEdit(self.fgdc_rdom)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.fgdc_attrmres.sizePolicy().hasHeightForWidth()
        )
        self.fgdc_attrmres.setSizePolicy(sizePolicy)
        self.fgdc_attrmres.setMinimumSize(QtCore.QSize(0, 0))
        self.fgdc_attrmres.setMaximumSize(QtCore.QSize(16777215, 20))
        self.fgdc_attrmres.setObjectName("fgdc_attrmres")
        self.horizontalLayout_11.addWidget(self.fgdc_attrmres)
        spacerItem1 = QtWidgets.QSpacerItem(
            15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_11.addItem(spacerItem1)
        self.verticalLayout_5.addLayout(self.horizontalLayout_11)
        self.verticalLayout.addWidget(self.fgdc_rdom)
        spacerItem2 = QtWidgets.QSpacerItem(
            20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout.addItem(spacerItem2)

        self.retranslateUi(fgdc_attrdomv)
        QtCore.QMetaObject.connectSlotsByName(fgdc_attrdomv)

    def retranslateUi(self, fgdc_attrdomv):
        _translate = QtCore.QCoreApplication.translate
        fgdc_attrdomv.setWindowTitle(_translate("fgdc_attrdomv", "Form"))
        self.label_19.setText(
            _translate("fgdc_attrdomv", "Range Minimum (Numeric or Date)")
        )
        self.fgdc_rdommin.setToolTip(
            _translate(
                "fgdc_attrdomv",
                "Address -- an address line for the address.\n"
                "Type: text\n"
                "Domain: free text\n"
                "Short Name: address",
            )
        )
        self.label_20.setToolTip(_translate("fgdc_attrdomv", "Required"))
        self.label_20.setText(
            _translate(
                "fgdc_attrdomv",
                '<html><head/><body><p align="center"><span style=" font-size:18pt; color:#55aaff;">*</span></p></body></html>',
            )
        )
        self.label_21.setText(
            _translate("fgdc_attrdomv", "Range Maximum (Numeric or Date)")
        )
        self.fgdc_rdommax.setToolTip(
            _translate(
                "fgdc_attrdomv",
                "Address -- an address line for the address.\n"
                "Type: text\n"
                "Domain: free text\n"
                "Short Name: address",
            )
        )
        self.label_25.setToolTip(_translate("fgdc_attrdomv", "Required"))
        self.label_25.setText(
            _translate(
                "fgdc_attrdomv",
                '<html><head/><body><p align="center"><span style=" font-size:18pt; color:#55aaff;">*</span></p></body></html>',
            )
        )
        self.label_22.setText(_translate("fgdc_attrdomv", "Units of Measure"))
        self.fgdc_attrunit.setToolTip(
            _translate(
                "fgdc_attrdomv",
                "Address -- an address line for the address.\n"
                "Type: text\n"
                "Domain: free text\n"
                "Short Name: address",
            )
        )
        self.label_23.setText(_translate("fgdc_attrdomv", "Measurement Resolution"))
        self.fgdc_attrmres.setToolTip(
            _translate(
                "fgdc_attrdomv",
                "City -- the city of the address.\n"
                "Type: text\n"
                "Domain: free text\n"
                "Short Name: city",
            )
        )
