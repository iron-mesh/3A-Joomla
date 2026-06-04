import re

from PySide6.QtCore import QLocale, Qt
from PySide6.QtWidgets import QDialog

from .. import lang_consts
from ..forms.ui_select_locale_dialog import Ui_Dialog


class SelectLocale(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        ignoring_attrs = {"C", "AnyLanguage"}
        for lang in QLocale.Language:
            if lang.name in ignoring_attrs:
                continue
            self.ui.language_comboBox.addItem(lang.name, lang)
        self._update_country_list()
        self._update_locale()

        self.ui.language_comboBox.currentIndexChanged.connect(self._update_country_list)
        self.ui.language_comboBox.currentIndexChanged.connect(self._update_locale)
        self.ui.territory_comboBox.currentIndexChanged.connect(self._update_locale)
        self.ui.locale_lineEdit.textChanged.connect(self._on_locale_changed)

        self.ui.label.setText(lang_consts.LOCALE())
        self.ui.label_2.setText(lang_consts.LANGUAGE())
        self.ui.label_3.setText(lang_consts.COUNTRY())

    def _update_country_list(self):
        locales = QLocale.matchingLocales(self.ui.language_comboBox.currentData(Qt.ItemDataRole.UserRole),
                                          QLocale.Script.AnyScript,
                                          QLocale.Country.AnyCountry)
        self.ui.territory_comboBox.blockSignals(True)
        self.ui.territory_comboBox.clear()
        for locale in locales:
            self.ui.territory_comboBox.addItem(QLocale.territoryToString(locale.country()), locale.country())
        self.ui.territory_comboBox.blockSignals(False)

    def _update_locale(self):
        locales = QLocale.matchingLocales(self.ui.language_comboBox.currentData(Qt.ItemDataRole.UserRole),
                                          QLocale.Script.AnyScript,
                                          self.ui.territory_comboBox.currentData(Qt.ItemDataRole.UserRole))
        self.ui.locale_lineEdit.blockSignals(True)
        self.ui.locale_lineEdit.setText(locales[0].name())
        self.ui.locale_lineEdit.selectAll()
        self.ui.locale_lineEdit.blockSignals(False)

    def _on_locale_changed(self, text):
        match_obj = re.match(r"^\w{2}-\w{2}$", text)
        if not match_obj:
            return

        locale = QLocale(text)
        if locale.language() == QLocale.Language.C:
            return

        lang_index = self.ui.language_comboBox.findData(locale.language(), Qt.ItemDataRole.UserRole)
        if lang_index >= 0:
            self.ui.language_comboBox.blockSignals(True)
            self.ui.language_comboBox.setCurrentIndex(lang_index)
            self.ui.language_comboBox.blockSignals(False)
            self._update_country_list()

            country_index = self.ui.territory_comboBox.findData(locale.country(), Qt.ItemDataRole.UserRole)
            if country_index >= 0:
                self.ui.territory_comboBox.blockSignals(True)
                self.ui.territory_comboBox.setCurrentIndex(country_index)
                self.ui.territory_comboBox.blockSignals(False)

    def locale(self):
        return self.ui.locale_lineEdit.text()