# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DataQuality.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_fgdc_dataqual(object):
    def setupUi(self, fgdc_dataqual):
        fgdc_dataqual.setObjectName("fgdc_dataqual")
        fgdc_dataqual.resize(966, 356)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(fgdc_dataqual)
        self.verticalLayout_2.setContentsMargins(2, -1, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(fgdc_dataqual)
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
        self.label_5.setMinimumSize(QtCore.QSize(510, 0))
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
        self.verticalLayout_2.addWidget(self.widget)
        self.idinfo_scroll_area = QtWidgets.QScrollArea(fgdc_dataqual)
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
        self.dataqual_main_widget = QtWidgets.QWidget()
        self.dataqual_main_widget.setGeometry(QtCore.QRect(0, 0, 955, 307))
        self.dataqual_main_widget.setObjectName("dataqual_main_widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.dataqual_main_widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.two_column = QtWidgets.QWidget(self.dataqual_main_widget)
        self.two_column.setObjectName("two_column")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.two_column)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.two_column_left = QtWidgets.QWidget(self.two_column)
        self.two_column_left.setObjectName("two_column_left")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.two_column_left)
        self.verticalLayout_5.setContentsMargins(18, 3, 3, 3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout.addWidget(self.two_column_left)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding
        )
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.fgdc_lineage = QtWidgets.QWidget(self.two_column)
        self.fgdc_lineage.setObjectName("fgdc_lineage")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.fgdc_lineage)
        self.verticalLayout_4.setContentsMargins(3, 3, 0, 3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_6.addWidget(self.fgdc_lineage)
        spacerItem2 = QtWidgets.QSpacerItem(
            20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding
        )
        self.verticalLayout_6.addItem(spacerItem2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)
        self.bottom_layout = QtWidgets.QHBoxLayout()
        self.bottom_layout.setSpacing(0)
        self.bottom_layout.setObjectName("bottom_layout")
        spacerItem3 = QtWidgets.QSpacerItem(
            20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.bottom_layout.addItem(spacerItem3)
        self.verticalLayout_7.addLayout(self.bottom_layout)
        self.verticalLayout_3.addWidget(self.two_column)
        self.idinfo_scroll_area.setWidget(self.dataqual_main_widget)
        self.verticalLayout_2.addWidget(self.idinfo_scroll_area)

        self.retranslateUi(fgdc_dataqual)
        QtCore.QMetaObject.connectSlotsByName(fgdc_dataqual)

    def retranslateUi(self, fgdc_dataqual):
        _translate = QtCore.QCoreApplication.translate
        fgdc_dataqual.setWindowTitle(_translate("fgdc_dataqual", "Form"))
        self.label_5.setToolTip(_translate("fgdc_dataqual", "Required"))
        self.label_5.setText(
            _translate(
                "fgdc_dataqual",
                '<html><head/><body><p><span style=" font-style:italic; color:#55aaff;">Provide information about the accuracy of the dataset and details about how it was produced.</span></p></body></html>',
            )
        )
        self.label_4.setToolTip(_translate("fgdc_dataqual", "Required"))
        self.label_4.setText(
            _translate(
                "fgdc_dataqual",
                '<html><head/><body><p><span style=" font-size:15pt; color:#55aaff;">*</span></p></body></html>',
            )
        )
        self.label_3.setToolTip(_translate("fgdc_dataqual", "Required"))
        self.label_3.setText(
            _translate(
                "fgdc_dataqual",
                '<html><head/><body><p><span style=" font-size:9pt; font-style:italic; color:#55aaff;">= Required</span></p></body></html>',
            )
        )
