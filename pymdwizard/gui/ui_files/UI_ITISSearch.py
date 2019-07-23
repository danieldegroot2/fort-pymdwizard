# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ITISSearch.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ItisSearchWidget(object):
    def setupUi(self, ItisSearchWidget):
        ItisSearchWidget.setObjectName("ItisSearchWidget")
        ItisSearchWidget.resize(1010, 608)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(ItisSearchWidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.splitter = QtWidgets.QSplitter(ItisSearchWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setFrameShape(QtWidgets.QFrame.Box)
        self.splitter.setFrameShadow(QtWidgets.QFrame.Raised)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, 5, 5, 7)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_search_term = QtWidgets.QLabel(self.layoutWidget)
        self.label_search_term.setObjectName("label_search_term")
        self.horizontalLayout.addWidget(self.label_search_term)
        self.search_term = QtWidgets.QLineEdit(self.layoutWidget)
        self.search_term.setObjectName("search_term")
        self.horizontalLayout.addWidget(self.search_term)
        self.button_search = QtWidgets.QPushButton(self.layoutWidget)
        self.button_search.setObjectName("button_search")
        self.horizontalLayout.addWidget(self.button_search)
        self.label_search_type = QtWidgets.QLabel(self.layoutWidget)
        self.label_search_type.setAccessibleName("")
        self.label_search_type.setObjectName("label_search_type")
        self.horizontalLayout.addWidget(self.label_search_type)
        self.combo_search_type = QtWidgets.QComboBox(self.layoutWidget)
        self.combo_search_type.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.combo_search_type.setObjectName("combo_search_type")
        self.combo_search_type.addItem("")
        self.combo_search_type.addItem("")
        self.horizontalLayout.addWidget(self.combo_search_type)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_search_results = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_search_results.setFont(font)
        self.label_search_results.setObjectName("label_search_results")
        self.horizontalLayout_6.addWidget(self.label_search_results)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_6.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.table_results = QtWidgets.QTableView(self.layoutWidget)
        self.table_results.setLineWidth(1)
        self.table_results.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table_results.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table_results.setSortingEnabled(True)
        self.table_results.setObjectName("table_results")
        self.table_results.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.table_results)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_2.addItem(spacerItem1)
        self.button_add_taxon = QtWidgets.QPushButton(self.layoutWidget)
        self.button_add_taxon.setObjectName("button_add_taxon")
        self.horizontalLayout_2.addWidget(self.button_add_taxon)
        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.splitter)
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.layout_include = QtWidgets.QVBoxLayout(self.horizontalLayoutWidget)
        self.layout_include.setContentsMargins(0, 0, 0, 0)
        self.layout_include.setSpacing(0)
        self.layout_include.setObjectName("layout_include")
        self.frame_include = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.frame_include.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_include.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_include.setObjectName("frame_include")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_include)
        self.verticalLayout_6.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.layout_include2 = QtWidgets.QVBoxLayout()
        self.layout_include2.setSpacing(0)
        self.layout_include2.setObjectName("layout_include2")
        self.label_include_item = QtWidgets.QLabel(self.frame_include)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_include_item.setFont(font)
        self.label_include_item.setObjectName("label_include_item")
        self.layout_include2.addWidget(self.label_include_item)
        self.table_include = QtWidgets.QTableView(self.frame_include)
        self.table_include.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.table_include.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table_include.setSortingEnabled(True)
        self.table_include.setObjectName("table_include")
        self.table_include.verticalHeader().setVisible(False)
        self.layout_include2.addWidget(self.table_include)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_7.addItem(spacerItem3)
        self.button_remove_selected = QtWidgets.QPushButton(self.frame_include)
        self.button_remove_selected.setObjectName("button_remove_selected")
        self.horizontalLayout_7.addWidget(self.button_remove_selected)
        spacerItem4 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_7.addItem(spacerItem4)
        self.layout_include2.addLayout(self.horizontalLayout_7)
        self.verticalLayout_6.addLayout(self.layout_include2)
        self.layout_include.addWidget(self.frame_include)
        self.verticalLayout_2.addWidget(self.splitter)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem5 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_3.addItem(spacerItem5)
        self.button_gen_fgdc = QtWidgets.QPushButton(ItisSearchWidget)
        self.button_gen_fgdc.setObjectName("button_gen_fgdc")
        self.horizontalLayout_3.addWidget(self.button_gen_fgdc)
        self.check_include_common = QtWidgets.QCheckBox(ItisSearchWidget)
        self.check_include_common.setObjectName("check_include_common")
        self.horizontalLayout_3.addWidget(self.check_include_common)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(ItisSearchWidget)
        self.combo_search_type.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(ItisSearchWidget)

    def retranslateUi(self, ItisSearchWidget):
        _translate = QtCore.QCoreApplication.translate
        ItisSearchWidget.setWindowTitle(_translate("ItisSearchWidget", "ITIS Search"))
        self.label_search_term.setText(_translate("ItisSearchWidget", "Search Term:"))
        self.search_term.setToolTip(
            _translate("ItisSearchWidget", "terms to search ITIS for")
        )
        self.button_search.setToolTip(
            _translate("ItisSearchWidget", "Perform search of ITIS")
        )
        self.button_search.setText(_translate("ItisSearchWidget", "Search ITIS"))
        self.label_search_type.setToolTip(
            _translate(
                "ItisSearchWidget",
                "The type of ITIS search to perform (Scientific or Common name)",
            )
        )
        self.label_search_type.setText(_translate("ItisSearchWidget", "Search Type:"))
        self.combo_search_type.setToolTip(
            _translate("ItisSearchWidget", "Search ITIS on common or scientific name")
        )
        self.combo_search_type.setItemText(
            0, _translate("ItisSearchWidget", "Common name")
        )
        self.combo_search_type.setItemText(
            1, _translate("ItisSearchWidget", "Scientific name")
        )
        self.label_search_results.setToolTip(
            _translate(
                "ItisSearchWidget",
                "Results from the ITIS common or scientific name search",
            )
        )
        self.label_search_results.setText(
            _translate("ItisSearchWidget", "Search Results:")
        )
        self.button_add_taxon.setToolTip(
            _translate(
                "ItisSearchWidget",
                "Add the selected item above to the list of include species (right)",
            )
        )
        self.button_add_taxon.setText(_translate("ItisSearchWidget", "Add Selection"))
        self.label_include_item.setToolTip(
            _translate(
                "ItisSearchWidget", "List of taxons to include in the taxonomy section"
            )
        )
        self.label_include_item.setText(
            _translate("ItisSearchWidget", "Items to include:")
        )
        self.button_remove_selected.setToolTip(
            _translate("ItisSearchWidget", "Remove selected items from list above")
        )
        self.button_remove_selected.setText(
            _translate("ItisSearchWidget", "Remove Selection")
        )
        self.button_gen_fgdc.setToolTip(
            _translate(
                "ItisSearchWidget",
                "Create a FGDC taxonomy section with the items in the above list",
            )
        )
        self.button_gen_fgdc.setText(
            _translate("ItisSearchWidget", "Generate Taxonomy Section")
        )
        self.check_include_common.setToolTip(
            _translate(
                "ItisSearchWidget",
                "Include common names in FGDC taxonomy section (optional elements)",
            )
        )
        self.check_include_common.setText(
            _translate("ItisSearchWidget", "Include Common Names")
        )
