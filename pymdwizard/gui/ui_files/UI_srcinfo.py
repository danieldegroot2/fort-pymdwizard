# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'srcinfo.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(805, 177)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.fgdc_srcinfo = QtWidgets.QGroupBox(Form)
        self.fgdc_srcinfo.setObjectName("fgdc_srcinfo")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.fgdc_srcinfo)
        self.verticalLayout_4.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_14 = QtWidgets.QLabel(self.fgdc_srcinfo)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_11.addWidget(self.label_14)
        self.fgdc_srccitea = QtWidgets.QLineEdit(self.fgdc_srcinfo)
        self.fgdc_srccitea.setObjectName("fgdc_srccitea")
        self.horizontalLayout_11.addWidget(self.fgdc_srccitea)
        self.label_4 = QtWidgets.QLabel(self.fgdc_srcinfo)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(15, 0))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label_4.setIndent(0)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_11.addWidget(self.label_4)
        self.verticalLayout_4.addLayout(self.horizontalLayout_11)
        self.fgdc_srccite = QtWidgets.QWidget(self.fgdc_srcinfo)
        self.fgdc_srccite.setObjectName("fgdc_srccite")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.fgdc_srccite)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_4.addWidget(self.fgdc_srccite)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(9)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.fgdc_srctime = QtWidgets.QWidget(self.fgdc_srcinfo)
        self.fgdc_srctime.setObjectName("fgdc_srctime")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.fgdc_srctime)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_8 = QtWidgets.QLabel(self.fgdc_srctime)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("font: bold;")
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.label_36 = QtWidgets.QLabel(self.fgdc_srctime)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_36.sizePolicy().hasHeightForWidth())
        self.label_36.setSizePolicy(sizePolicy)
        self.label_36.setStyleSheet("font: italic;")
        self.label_36.setObjectName("label_36")
        self.verticalLayout.addWidget(self.label_36)
        self.fgdc_srccurr = QtWidgets.QComboBox(self.fgdc_srctime)
        self.fgdc_srccurr.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.fgdc_srccurr.setEditable(True)
        self.fgdc_srccurr.setObjectName("fgdc_srccurr")
        self.fgdc_srccurr.addItem("")
        self.fgdc_srccurr.setItemText(0, "")
        self.fgdc_srccurr.addItem("")
        self.fgdc_srccurr.addItem("")
        self.fgdc_srccurr.addItem("")
        self.fgdc_srccurr.addItem("")
        self.verticalLayout.addWidget(self.fgdc_srccurr)
        self.horizontalLayout_3.addWidget(self.fgdc_srctime)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setSpacing(3)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_15 = QtWidgets.QLabel(self.fgdc_srcinfo)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_13.addWidget(self.label_15)
        self.label_16 = QtWidgets.QLabel(self.fgdc_srcinfo)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setMinimumSize(QtCore.QSize(15, 0))
        self.label_16.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_16.setFont(font)
        self.label_16.setScaledContents(True)
        self.label_16.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label_16.setIndent(0)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_13.addWidget(self.label_16)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_13.addItem(spacerItem)
        self.verticalLayout_16.addLayout(self.horizontalLayout_13)
        self.srccontr_layout = QtWidgets.QHBoxLayout()
        self.srccontr_layout.setObjectName("srccontr_layout")
        self.fgdc_srccontr = GrowingTextEdit(self.fgdc_srcinfo)
        self.fgdc_srccontr.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow
        )
        self.fgdc_srccontr.setObjectName("fgdc_srccontr")
        self.srccontr_layout.addWidget(self.fgdc_srccontr)
        self.verticalLayout_16.addLayout(self.srccontr_layout)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_16.addItem(spacerItem1)
        self.horizontalLayout_12.addLayout(self.verticalLayout_16)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setSpacing(3)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_17 = QtWidgets.QLabel(self.fgdc_srcinfo)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_14.addWidget(self.label_17)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.fgdc_typesrc = QtWidgets.QComboBox(self.fgdc_srcinfo)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fgdc_typesrc.sizePolicy().hasHeightForWidth())
        self.fgdc_typesrc.setSizePolicy(sizePolicy)
        self.fgdc_typesrc.setEditable(True)
        self.fgdc_typesrc.setObjectName("fgdc_typesrc")
        self.fgdc_typesrc.addItem("")
        self.horizontalLayout_15.addWidget(self.fgdc_typesrc)
        self.label_18 = QtWidgets.QLabel(self.fgdc_srcinfo)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        self.label_18.setMinimumSize(QtCore.QSize(15, 0))
        self.label_18.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_18.setFont(font)
        self.label_18.setScaledContents(True)
        self.label_18.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label_18.setIndent(0)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_15.addWidget(self.label_18)
        self.verticalLayout_14.addLayout(self.horizontalLayout_15)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSpacing(3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_19 = QtWidgets.QLabel(self.fgdc_srcinfo)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_6.addWidget(self.label_19)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_20 = QtWidgets.QLabel(self.fgdc_srcinfo)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)
        self.label_20.setMinimumSize(QtCore.QSize(15, 0))
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_16.addWidget(self.label_20)
        self.fgdc_srcscale = QtWidgets.QLineEdit(self.fgdc_srcinfo)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.fgdc_srcscale.sizePolicy().hasHeightForWidth()
        )
        self.fgdc_srcscale.setSizePolicy(sizePolicy)
        self.fgdc_srcscale.setObjectName("fgdc_srcscale")
        self.horizontalLayout_16.addWidget(self.fgdc_srcscale)
        self.verticalLayout_6.addLayout(self.horizontalLayout_16)
        self.verticalLayout_14.addLayout(self.verticalLayout_6)
        spacerItem2 = QtWidgets.QSpacerItem(
            20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_14.addItem(spacerItem2)
        self.horizontalLayout_12.addLayout(self.verticalLayout_14)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_12)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_7.addWidget(self.fgdc_srcinfo)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.fgdc_srcinfo.setTitle(_translate("Form", "Source Input"))
        self.label_14.setText(
            _translate("Form", "Abbreviation / Short Name for the Input Data")
        )
        self.label_4.setToolTip(_translate("Form", "Required"))
        self.label_4.setText(
            _translate(
                "Form",
                '<html><head/><body><p><span style=" font-size:18pt; color:#55aaff;">*</span></p></body></html>',
            )
        )
        self.label_8.setWhatsThis(
            _translate(
                "Form",
                "<html><head/><body><p>currentness what's this....</p><p>fakls;dfhjl;sakdjfl</p></body></html>",
            )
        )
        self.label_8.setText(_translate("Form", "Currentness Reference"))
        self.label_36.setText(
            _translate("Form", "Type directly in box below for items not in list.")
        )
        self.fgdc_srccurr.setItemText(1, _translate("Form", "ground condition"))
        self.fgdc_srccurr.setItemText(2, _translate("Form", "observed"))
        self.fgdc_srccurr.setItemText(3, _translate("Form", "publication date"))
        self.fgdc_srccurr.setItemText(4, _translate("Form", "See Supplemental Info"))
        self.label_15.setText(_translate("Form", "Contribution of this Source Input"))
        self.label_16.setToolTip(_translate("Form", "Required"))
        self.label_16.setText(
            _translate(
                "Form",
                '<html><head/><body><p><span style=" font-size:22pt; color:#55aaff;">*</span></p></body></html>',
            )
        )
        self.label_17.setText(_translate("Form", "Type of Resource"))
        self.fgdc_typesrc.setItemText(0, _translate("Form", "Digital and/or Hardcopy"))
        self.label_18.setToolTip(_translate("Form", "Required"))
        self.label_18.setText(
            _translate(
                "Form",
                '<html><head/><body><p><span style=" font-size:18pt; color:#55aaff;">*</span></p></body></html>',
            )
        )
        self.label_19.setText(_translate("Form", "Source Scale"))
        self.label_20.setText(_translate("Form", "1:"))
        self.fgdc_srcscale.setPlaceholderText(_translate("Form", "24000"))


from growingtextedit import GrowingTextEdit
