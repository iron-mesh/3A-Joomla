# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainPaVMuS.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize, Qt)
from PySide6.QtGui import (QIcon)
from PySide6.QtWidgets import (QAbstractScrollArea, QCheckBox, QComboBox,
                               QFrame, QHBoxLayout, QLabel, QLayout,
                               QListWidget, QPushButton, QScrollArea,
                               QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1012, 796)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.folders_comboBox = QComboBox(Form)
        self.folders_comboBox.setObjectName(u"folders_comboBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.folders_comboBox.sizePolicy().hasHeightForWidth())
        self.folders_comboBox.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.folders_comboBox)

        self.prev_folder_btn = QPushButton(Form)
        self.prev_folder_btn.setObjectName(u"prev_folder_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.prev_folder_btn.sizePolicy().hasHeightForWidth())
        self.prev_folder_btn.setSizePolicy(sizePolicy2)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoPrevious))
        self.prev_folder_btn.setIcon(icon)
        self.prev_folder_btn.setIconSize(QSize(25, 25))
#if QT_CONFIG(shortcut)
        self.prev_folder_btn.setShortcut(u"Alt+Left")
#endif // QT_CONFIG(shortcut)

        self.horizontalLayout_3.addWidget(self.prev_folder_btn)

        self.next_folder_btn = QPushButton(Form)
        self.next_folder_btn.setObjectName(u"next_folder_btn")
        sizePolicy2.setHeightForWidth(self.next_folder_btn.sizePolicy().hasHeightForWidth())
        self.next_folder_btn.setSizePolicy(sizePolicy2)
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoNext))
        self.next_folder_btn.setIcon(icon1)
        self.next_folder_btn.setIconSize(QSize(25, 25))
#if QT_CONFIG(shortcut)
        self.next_folder_btn.setShortcut(u"Alt+Right")
#endif // QT_CONFIG(shortcut)

        self.horizontalLayout_3.addWidget(self.next_folder_btn)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.add_folder_btn = QPushButton(Form)
        self.add_folder_btn.setObjectName(u"add_folder_btn")
        sizePolicy2.setHeightForWidth(self.add_folder_btn.sizePolicy().hasHeightForWidth())
        self.add_folder_btn.setSizePolicy(sizePolicy2)
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListAdd))
        self.add_folder_btn.setIcon(icon2)
        self.add_folder_btn.setIconSize(QSize(25, 25))

        self.horizontalLayout_3.addWidget(self.add_folder_btn)

        self.delete_folder_btn = QPushButton(Form)
        self.delete_folder_btn.setObjectName(u"delete_folder_btn")
        sizePolicy2.setHeightForWidth(self.delete_folder_btn.sizePolicy().hasHeightForWidth())
        self.delete_folder_btn.setSizePolicy(sizePolicy2)
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListRemove))
        self.delete_folder_btn.setIcon(icon3)
        self.delete_folder_btn.setIconSize(QSize(25, 25))

        self.horizontalLayout_3.addWidget(self.delete_folder_btn)

        self.clear_folders_btn = QPushButton(Form)
        self.clear_folders_btn.setObjectName(u"clear_folders_btn")
        sizePolicy2.setHeightForWidth(self.clear_folders_btn.sizePolicy().hasHeightForWidth())
        self.clear_folders_btn.setSizePolicy(sizePolicy2)
        icon4 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditDelete))
        self.clear_folders_btn.setIcon(icon4)
        self.clear_folders_btn.setIconSize(QSize(25, 25))

        self.horizontalLayout_3.addWidget(self.clear_folders_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.file_list = QListWidget(Form)
        self.file_list.setObjectName(u"file_list")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Ignored)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.file_list.sizePolicy().hasHeightForWidth())
        self.file_list.setSizePolicy(sizePolicy3)
        self.file_list.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)

        self.horizontalLayout.addWidget(self.file_list)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.prev_image_btn = QPushButton(Form)
        self.prev_image_btn.setObjectName(u"prev_image_btn")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.prev_image_btn.sizePolicy().hasHeightForWidth())
        self.prev_image_btn.setSizePolicy(sizePolicy4)
        self.prev_image_btn.setMinimumSize(QSize(50, 0))
        icon5 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoUp))
        self.prev_image_btn.setIcon(icon5)
        self.prev_image_btn.setIconSize(QSize(30, 30))
#if QT_CONFIG(shortcut)
        self.prev_image_btn.setShortcut(u"Alt+Up")
#endif // QT_CONFIG(shortcut)

        self.verticalLayout_2.addWidget(self.prev_image_btn)

        self.next_image_btn = QPushButton(Form)
        self.next_image_btn.setObjectName(u"next_image_btn")
        sizePolicy4.setHeightForWidth(self.next_image_btn.sizePolicy().hasHeightForWidth())
        self.next_image_btn.setSizePolicy(sizePolicy4)
        self.next_image_btn.setMinimumSize(QSize(50, 0))
        icon6 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoDown))
        self.next_image_btn.setIcon(icon6)
        self.next_image_btn.setIconSize(QSize(30, 30))
#if QT_CONFIG(shortcut)
        self.next_image_btn.setShortcut(u"Alt+Down")
#endif // QT_CONFIG(shortcut)

        self.verticalLayout_2.addWidget(self.next_image_btn)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.image_label = QLabel(Form)
        self.image_label.setObjectName(u"image_label")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Ignored)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.image_label.sizePolicy().hasHeightForWidth())
        self.image_label.setSizePolicy(sizePolicy5)
        self.image_label.setMinimumSize(QSize(0, 0))
        self.image_label.setScaledContents(False)
        self.image_label.setWordWrap(False)

        self.horizontalLayout.addWidget(self.image_label)

        self.horizontalSpacer_3 = QSpacerItem(0, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.locales_comboBox = QComboBox(Form)
        self.locales_comboBox.setObjectName(u"locales_comboBox")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.locales_comboBox.sizePolicy().hasHeightForWidth())
        self.locales_comboBox.setSizePolicy(sizePolicy6)
        self.locales_comboBox.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContents)

        self.horizontalLayout_4.addWidget(self.locales_comboBox)

        self.add_locale_btn = QPushButton(Form)
        self.add_locale_btn.setObjectName(u"add_locale_btn")
        sizePolicy2.setHeightForWidth(self.add_locale_btn.sizePolicy().hasHeightForWidth())
        self.add_locale_btn.setSizePolicy(sizePolicy2)
        self.add_locale_btn.setIcon(icon2)
        self.add_locale_btn.setIconSize(QSize(25, 25))

        self.horizontalLayout_4.addWidget(self.add_locale_btn)

        self.edit_locale_btn = QPushButton(Form)
        self.edit_locale_btn.setObjectName(u"edit_locale_btn")
        sizePolicy2.setHeightForWidth(self.edit_locale_btn.sizePolicy().hasHeightForWidth())
        self.edit_locale_btn.setSizePolicy(sizePolicy2)
        icon7 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MailMessageNew))
        self.edit_locale_btn.setIcon(icon7)
        self.edit_locale_btn.setIconSize(QSize(25, 25))

        self.horizontalLayout_4.addWidget(self.edit_locale_btn)

        self.delete_locale_btn = QPushButton(Form)
        self.delete_locale_btn.setObjectName(u"delete_locale_btn")
        sizePolicy2.setHeightForWidth(self.delete_locale_btn.sizePolicy().hasHeightForWidth())
        self.delete_locale_btn.setSizePolicy(sizePolicy2)
        self.delete_locale_btn.setIcon(icon3)
        self.delete_locale_btn.setIconSize(QSize(25, 25))

        self.horizontalLayout_4.addWidget(self.delete_locale_btn)

        self.show_all_locales_checkBox = QCheckBox(Form)
        self.show_all_locales_checkBox.setObjectName(u"show_all_locales_checkBox")

        self.horizontalLayout_4.addWidget(self.show_all_locales_checkBox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 7, 0, 7)
        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy7)
        self.scrollArea.setMinimumSize(QSize(0, 0))
        self.scrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea.setFrameShadow(QFrame.Shadow.Raised)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 992, 69))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollArea)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.save_btn = QPushButton(Form)
        self.save_btn.setObjectName(u"save_btn")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.save_btn.sizePolicy().hasHeightForWidth())
        self.save_btn.setSizePolicy(sizePolicy8)

        self.horizontalLayout_2.addWidget(self.save_btn)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addLayout(self.verticalLayout_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
#if QT_CONFIG(tooltip)
        self.folders_comboBox.setToolTip(QCoreApplication.translate("Form", u"Selected folders", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.prev_folder_btn.setToolTip(QCoreApplication.translate("Form", u"Previous folder (Alt + \u2b05)", None))
#endif // QT_CONFIG(tooltip)
        self.prev_folder_btn.setText("")
#if QT_CONFIG(tooltip)
        self.next_folder_btn.setToolTip(QCoreApplication.translate("Form", u"Next folder (Alt + \u27a1)", None))
#endif // QT_CONFIG(tooltip)
        self.next_folder_btn.setText("")
#if QT_CONFIG(tooltip)
        self.add_folder_btn.setToolTip(QCoreApplication.translate("Form", u"Add folder(s)", None))
#endif // QT_CONFIG(tooltip)
        self.add_folder_btn.setText("")
#if QT_CONFIG(tooltip)
        self.delete_folder_btn.setToolTip(QCoreApplication.translate("Form", u"Delete folder", None))
#endif // QT_CONFIG(tooltip)
        self.delete_folder_btn.setText("")
#if QT_CONFIG(tooltip)
        self.clear_folders_btn.setToolTip(QCoreApplication.translate("Form", u"Delete all folders", None))
#endif // QT_CONFIG(tooltip)
        self.clear_folders_btn.setText("")
#if QT_CONFIG(tooltip)
        self.file_list.setToolTip(QCoreApplication.translate("Form", u"Image list", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.prev_image_btn.setToolTip(QCoreApplication.translate("Form", u"Previous image (Alt + \u2b06)", None))
#endif // QT_CONFIG(tooltip)
        self.prev_image_btn.setText("")
#if QT_CONFIG(tooltip)
        self.next_image_btn.setToolTip(QCoreApplication.translate("Form", u"Next image  (Alt + \u2b07)", None))
#endif // QT_CONFIG(tooltip)
        self.next_image_btn.setText("")
#if QT_CONFIG(tooltip)
        self.image_label.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.image_label.setText("")
#if QT_CONFIG(tooltip)
        self.locales_comboBox.setToolTip(QCoreApplication.translate("Form", u"Language list", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.add_locale_btn.setToolTip(QCoreApplication.translate("Form", u"Add language", None))
#endif // QT_CONFIG(tooltip)
        self.add_locale_btn.setText("")
#if QT_CONFIG(tooltip)
        self.edit_locale_btn.setToolTip(QCoreApplication.translate("Form", u"Delete language", None))
#endif // QT_CONFIG(tooltip)
        self.edit_locale_btn.setText("")
#if QT_CONFIG(tooltip)
        self.delete_locale_btn.setToolTip(QCoreApplication.translate("Form", u"Delete language", None))
#endif // QT_CONFIG(tooltip)
        self.delete_locale_btn.setText("")
        self.show_all_locales_checkBox.setText(QCoreApplication.translate("Form", u"Show All Languages", None))
#if QT_CONFIG(tooltip)
        self.save_btn.setToolTip(QCoreApplication.translate("Form", u"Save data into files.", None))
#endif // QT_CONFIG(tooltip)
        self.save_btn.setText(QCoreApplication.translate("Form", u"Save", None))
    # retranslateUi

