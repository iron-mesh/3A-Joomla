# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'select_locale_dialogvQHzUO.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QFormLayout, QLabel, QLineEdit,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setWindowModality(Qt.WindowModality.NonModal)
        Dialog.resize(232, 126)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.formLayout = QFormLayout(Dialog)
        self.formLayout.setObjectName(u"formLayout")
        self.locale_lineEdit = QLineEdit(Dialog)
        self.locale_lineEdit.setObjectName(u"locale_lineEdit")
        self.locale_lineEdit.setInputMask(u"AA-AA;#")
        self.locale_lineEdit.setPlaceholderText(u"")
        self.locale_lineEdit.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.locale_lineEdit)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setText(u"Locale")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setText(u"Language")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.language_comboBox = QComboBox(Dialog)
        self.language_comboBox.setObjectName(u"language_comboBox")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.language_comboBox)

        self.territory_comboBox = QComboBox(Dialog)
        self.territory_comboBox.setObjectName(u"territory_comboBox")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.territory_comboBox)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.buttonBox)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setText(u"Territory")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_3)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
    # retranslateUi

