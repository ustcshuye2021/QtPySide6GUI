# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'student_new.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpinBox, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(889, 458)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(80, 120, 301, 241))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 50, 53, 16))
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 110, 53, 16))
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 170, 53, 16))
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.chinese = QSpinBox(self.groupBox)
        self.chinese.setObjectName(u"chinese")
        self.chinese.setGeometry(QRect(120, 50, 81, 22))
        self.math = QSpinBox(self.groupBox)
        self.math.setObjectName(u"math")
        self.math.setGeometry(QRect(120, 110, 81, 22))
        self.english = QSpinBox(self.groupBox)
        self.english.setObjectName(u"english")
        self.english.setGeometry(QRect(120, 170, 81, 22))
        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(490, 120, 311, 241))
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 60, 53, 16))
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 140, 53, 16))
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.total = QLineEdit(self.groupBox_2)
        self.total.setObjectName(u"total")
        self.total.setGeometry(QRect(130, 60, 113, 21))
        self.total.setReadOnly(True)
        self.average = QLineEdit(self.groupBox_2)
        self.average.setObjectName(u"average")
        self.average.setGeometry(QRect(130, 140, 113, 21))
        self.average.setReadOnly(True)
        self.btnCalculate = QPushButton(Form)
        self.btnCalculate.setObjectName(u"btnCalculate")
        self.btnCalculate.setGeometry(QRect(310, 400, 101, 41))
        self.btnSave = QPushButton(Form)
        self.btnSave.setObjectName(u"btnSave")
        self.btnSave.setGeometry(QRect(470, 400, 91, 41))
        self.groupBox_3 = QGroupBox(Form)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(80, 10, 721, 81))
        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(40, 36, 51, 16))
        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(422, 30, 51, 20))
        self.name = QLineEdit(self.groupBox_3)
        self.name.setObjectName(u"name")
        self.name.setGeometry(QRect(90, 30, 113, 21))
        self.number = QSpinBox(self.groupBox_3)
        self.number.setObjectName(u"number")
        self.number.setGeometry(QRect(490, 30, 191, 21))
        self.number.setMaximum(10000)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u5b66\u751f\u6210\u7ee9", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u8bed\u6587", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u6570\u5b66", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u82f1\u8bed", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"\u6210\u7ee9\u7edf\u8ba1", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u603b\u6210\u7ee9", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u5e73\u5747\u5206", None))
        self.btnCalculate.setText(QCoreApplication.translate("Form", u"\u8ba1   \u7b97", None))
        self.btnSave.setText(QCoreApplication.translate("Form", u"\u4fdd    \u5b58", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"\u5b66\u751f\u57fa\u672c\u4fe1\u606f ", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u59d3\u540d", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u5b66\u53f7", None))
    # retranslateUi

