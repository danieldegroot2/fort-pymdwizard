# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Descriptor.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(526, 432)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fgdc_descript = QtWidgets.QGroupBox(Form)
        self.fgdc_descript.setObjectName("fgdc_descript")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.fgdc_descript)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(self.fgdc_descript)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_2 = QtWidgets.QLabel(self.fgdc_descript)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font: italic;")
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.fgdc_abstract = QtWidgets.QPlainTextEdit(self.fgdc_descript)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.fgdc_abstract.setFont(font)
        self.fgdc_abstract.setAcceptDrops(False)
        self.fgdc_abstract.setPlainText("")
        self.fgdc_abstract.setOverwriteMode(True)
        self.fgdc_abstract.setObjectName("fgdc_abstract")
        self.verticalLayout.addWidget(self.fgdc_abstract)
        self.label_6 = QtWidgets.QLabel(self.fgdc_descript)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_3 = QtWidgets.QLabel(self.fgdc_descript)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("font: italic;")
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.fgdc_purpose = QtWidgets.QPlainTextEdit(self.fgdc_descript)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.fgdc_purpose.setFont(font)
        self.fgdc_purpose.setAcceptDrops(False)
        self.fgdc_purpose.setPlainText("")
        self.fgdc_purpose.setOverwriteMode(True)
        self.fgdc_purpose.setObjectName("fgdc_purpose")
        self.verticalLayout.addWidget(self.fgdc_purpose)
        self.label_4 = QtWidgets.QLabel(self.fgdc_descript)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label = QtWidgets.QLabel(self.fgdc_descript)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setStyleSheet("font: italic;")
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.fgdc_supplinf = QtWidgets.QPlainTextEdit(self.fgdc_descript)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.fgdc_supplinf.setFont(font)
        self.fgdc_supplinf.setAcceptDrops(False)
        self.fgdc_supplinf.setPlainText("")
        self.fgdc_supplinf.setOverwriteMode(True)
        self.fgdc_supplinf.setObjectName("fgdc_supplinf")
        self.verticalLayout.addWidget(self.fgdc_supplinf)
        self.horizontalLayout.addWidget(self.fgdc_descript)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.fgdc_descript.setTitle(_translate("Form", "Descriptors"))
        self.label_5.setText(_translate("Form", "Abstract"))
        self.label_2.setText(
            _translate("Form", "Provide a description of the dataset.")
        )
        self.label_6.setText(_translate("Form", "Purpose"))
        self.label_3.setText(
            _translate(
                "Form",
                "Why were the data collected?  What is an appropriate use of the data?",
            )
        )
        self.label_4.setText(_translate("Form", "Supplemental Information"))
        self.label.setText(
            _translate(
                "Form",
                "Use this optional section to add ANY other details or information about the dataset that may be helpful to future users.",
            )
        )


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
