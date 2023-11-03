# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'openAIWidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(780, 762)
        Form.setStyleSheet(u"background-color: rgb(36, 36, 36);")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setFamily(u"Artifakt Element")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(10)
        self.label.setFont(font1)
        self.label.setToolTipDuration(-3)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_4.addWidget(self.label)

        self.spinBox_temp = QDoubleSpinBox(Form)
        self.spinBox_temp.setObjectName(u"spinBox_temp")
        self.spinBox_temp.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_temp.setMaximum(2.000000000000000)
        self.spinBox_temp.setSingleStep(0.100000000000000)
        self.spinBox_temp.setValue(0.500000000000000)

        self.horizontalLayout_4.addWidget(self.spinBox_temp)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.textEdit_prompt = QTextEdit(Form)
        self.textEdit_prompt.setObjectName(u"textEdit_prompt")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_prompt.sizePolicy().hasHeightForWidth())
        self.textEdit_prompt.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamily(u"MS Shell Dlg 2")
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        self.textEdit_prompt.setFont(font2)
        self.textEdit_prompt.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.textEdit_prompt.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_prompt.setLineWrapMode(QTextEdit.WidgetWidth)

        self.verticalLayout.addWidget(self.textEdit_prompt)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_submitQuestion = QPushButton(Form)
        self.btn_submitQuestion.setObjectName(u"btn_submitQuestion")
        font3 = QFont()
        font3.setFamily(u"MS Shell Dlg 2")
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(50)
        self.btn_submitQuestion.setFont(font3)
        self.btn_submitQuestion.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(75, 75, 75);")

        self.horizontalLayout.addWidget(self.btn_submitQuestion)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.label_2)

        self.textEdit_response = QTextEdit(Form)
        self.textEdit_response.setObjectName(u"textEdit_response")
        font4 = QFont()
        font4.setFamily(u"Courier")
        font4.setPointSize(12)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setWeight(50)
        self.textEdit_response.setFont(font4)
        self.textEdit_response.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Courier\";")
        self.textEdit_response.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout.addWidget(self.textEdit_response)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.btn_run = QPushButton(Form)
        self.btn_run.setObjectName(u"btn_run")
        self.btn_run.setFont(font3)
        self.btn_run.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(75, 75, 75);")

        self.horizontalLayout_5.addWidget(self.btn_run)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_searchRef = QPushButton(Form)
        self.btn_searchRef.setObjectName(u"btn_searchRef")
        self.btn_searchRef.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(75, 75, 75);")

        self.horizontalLayout_2.addWidget(self.btn_searchRef)

        self.comboBox_version = QComboBox(Form)
        self.comboBox_version.setObjectName(u"comboBox_version")
        self.comboBox_version.setFont(font1)
        self.comboBox_version.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(75, 75, 75);")

        self.horizontalLayout_2.addWidget(self.comboBox_version)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_save = QPushButton(Form)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setFont(font3)
        self.btn_save.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(75, 75, 75);")

        self.horizontalLayout_3.addWidget(self.btn_save)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.btn_close = QPushButton(Form)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setFont(font3)
        self.btn_close.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(75, 75, 75);")

        self.horizontalLayout_3.addWidget(self.btn_close)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Prompt", None))
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("Form", u"Temperature is a parameter that controls the \u201ccreativity\u201d or randomness\n"
"of the text generated by the AI model.  A higher temperature (e.g., 0.7) \n"
"results in more diverse and creative output, while a lower temperature \n"
"(e.g., 0.2) makes the output more deterministic and focused.", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("Form", u"Temperature", None))
#if QT_CONFIG(tooltip)
        self.textEdit_prompt.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.textEdit_prompt.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Using the Unreal 5 Python API ...</span></p></body></html>", None))
        self.btn_submitQuestion.setText(QCoreApplication.translate("Form", u"  Submit Question  ", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Response", None))
        self.textEdit_response.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Courier'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textEdit_response.setPlaceholderText("")
        self.btn_run.setText(QCoreApplication.translate("Form", u"Run Code", None))
        self.btn_searchRef.setText(QCoreApplication.translate("Form", u"  Search Unreal Python API  ", None))
        self.btn_save.setText(QCoreApplication.translate("Form", u"  Save code as .py  ", None))
        self.btn_close.setText(QCoreApplication.translate("Form", u"Close", None))
    # retranslateUi

