# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'idinfo.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_fgdc_idinfo(object):
    def setupUi(self, fgdc_idinfo):
        fgdc_idinfo.setObjectName("fgdc_idinfo")
        fgdc_idinfo.resize(1108, 845)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(fgdc_idinfo)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.widget = QtWidgets.QWidget(fgdc_idinfo)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(0, 25))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(10, 2, 2, 2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(15, 0))
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setTextFormat(QtCore.Qt.RichText)
        self.label_5.setScaledContents(False)
        self.label_5.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label_5.setIndent(0)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        spacerItem = QtWidgets.QSpacerItem(
            321,
            20,
            QtWidgets.QSizePolicy.MinimumExpanding,
            QtWidgets.QSizePolicy.Minimum,
        )
        self.horizontalLayout.addItem(spacerItem)
        self.widget1 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget1.sizePolicy().hasHeightForWidth())
        self.widget1.setSizePolicy(sizePolicy)
        self.widget1.setMinimumSize(QtCore.QSize(100, 0))
        self.widget1.setObjectName("widget1")
        self.layoutWidget = QtWidgets.QWidget(self.widget1)
        self.layoutWidget.setGeometry(QtCore.QRect(3, 1, 110, 22))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setContentsMargins(5, 0, 5, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
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
        self.label_4.setTextFormat(QtCore.Qt.RichText)
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft
        )
        self.label_4.setIndent(0)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(79, 0))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setTextFormat(QtCore.Qt.RichText)
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.label_3.setIndent(0)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.horizontalLayout.addWidget(self.widget1)
        self.verticalLayout_9.addWidget(self.widget)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.idinfo_scroll_area = QtWidgets.QScrollArea(fgdc_idinfo)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.idinfo_scroll_area.sizePolicy().hasHeightForWidth()
        )
        self.idinfo_scroll_area.setSizePolicy(sizePolicy)
        self.idinfo_scroll_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.idinfo_scroll_area.setFrameShadow(QtWidgets.QFrame.Plain)
        self.idinfo_scroll_area.setWidgetResizable(True)
        self.idinfo_scroll_area.setObjectName("idinfo_scroll_area")
        self.idinfo_main_widget = QtWidgets.QWidget()
        self.idinfo_main_widget.setGeometry(QtCore.QRect(0, 0, 1086, 792))
        self.idinfo_main_widget.setObjectName("idinfo_main_widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.idinfo_main_widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.fgdc_citation = QtWidgets.QWidget(self.idinfo_main_widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.fgdc_citation.sizePolicy().hasHeightForWidth()
        )
        self.fgdc_citation.setSizePolicy(sizePolicy)
        self.fgdc_citation.setObjectName("fgdc_citation")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.fgdc_citation)
        self.verticalLayout_6.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum
        )
        self.verticalLayout_6.addItem(spacerItem1)
        self.verticalLayout_2.addWidget(self.fgdc_citation)
        self.two_column = QtWidgets.QWidget(self.idinfo_main_widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.two_column.sizePolicy().hasHeightForWidth())
        self.two_column.setSizePolicy(sizePolicy)
        self.two_column.setObjectName("two_column")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.two_column)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.two_column_left = QtWidgets.QWidget(self.two_column)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.two_column_left.sizePolicy().hasHeightForWidth()
        )
        self.two_column_left.setSizePolicy(sizePolicy)
        self.two_column_left.setObjectName("two_column_left")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.two_column_left)
        self.verticalLayout_5.setContentsMargins(0, 3, 3, 3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(
            20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_5.addItem(spacerItem2)
        self.horizontalLayout_4.addWidget(self.two_column_left)
        self.two_column_right = QtWidgets.QWidget(self.two_column)
        self.two_column_right.setObjectName("two_column_right")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.two_column_right)
        self.verticalLayout_4.setContentsMargins(3, 3, 0, 3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem3 = QtWidgets.QSpacerItem(
            20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_4.addItem(spacerItem3)
        self.horizontalLayout_4.addWidget(self.two_column_right)
        self.verticalLayout_2.addWidget(self.two_column)
        self.help_crossref = QtWidgets.QWidget(self.idinfo_main_widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.help_crossref.sizePolicy().hasHeightForWidth()
        )
        self.help_crossref.setSizePolicy(sizePolicy)
        self.help_crossref.setObjectName("help_crossref")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.help_crossref)
        self.verticalLayout_8.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        spacerItem4 = QtWidgets.QSpacerItem(
            20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum
        )
        self.verticalLayout_8.addItem(spacerItem4)
        self.verticalLayout_2.addWidget(self.help_crossref)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.idinfo_scroll_area.setWidget(self.idinfo_main_widget)
        self.horizontalLayout_2.addWidget(self.idinfo_scroll_area)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_9.addLayout(self.verticalLayout)

        self.retranslateUi(fgdc_idinfo)
        QtCore.QMetaObject.connectSlotsByName(fgdc_idinfo)

    def retranslateUi(self, fgdc_idinfo):
        _translate = QtCore.QCoreApplication.translate
        fgdc_idinfo.setWindowTitle(_translate("fgdc_idinfo", "Form"))
        self.label_5.setToolTip(_translate("fgdc_idinfo", "Required"))
        self.label_5.setText(
            _translate(
                "fgdc_idinfo",
                '<html><head/><body><p><span style=" font-size:9pt; font-style:italic; color:#55aaff;">Provide general Information about the dataset.</span></p></body></html>',
            )
        )
        self.label_4.setToolTip(_translate("fgdc_idinfo", "Required"))
        self.label_4.setText(
            _translate(
                "fgdc_idinfo",
                '<html><head/><body><p><span style=" font-size:15pt; color:#55aaff;">*</span></p></body></html>',
            )
        )
        self.label_3.setToolTip(_translate("fgdc_idinfo", "Required"))
        self.label_3.setText(
            _translate(
                "fgdc_idinfo",
                '<html><head/><body><p><span style=" font-size:9pt; font-style:italic; color:#55aaff;">= Required</span></p></body></html>',
            )
        )
