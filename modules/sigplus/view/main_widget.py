
#  Copyright (c)
#  2026 Ivan Balakirev (www.ironmesh.ru)
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
import os
import re
from enum import Enum

from PySide6.QtCore import Signal, QLocale, QFileInfo
from PySide6.QtGui import QPixmap, Qt
from PySide6.QtWidgets import QWidget, QMessageBox, QFileIconProvider, QListWidgetItem, QVBoxLayout, QLineEdit, QLabel, \
    QSizePolicy
from typing_extensions import Literal

from PyUB.bases import Singleton
from . import lang_consts as lc
from .dialogs.select_locale import SelectLocale
from .forms.ui_main_widget import Ui_Form


class MainWidget(Singleton, QWidget):
    """
    Attributes:
        received_dir_list(Signal(list[str]): Sends list of directory paths that the user dragged and dropped
    """

    class UserRequest(Enum):
        SAVE_DATA = 0
        IMPORT_DATA = 1

    user_request = Signal(UserRequest)
    received_dir_list = Signal(list)

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self._init_widgets()
        self._data = {}
        self.setAcceptDrops(True)

    def set_data(self, data: dict):
        self._data = data

        self.ui.folders_comboBox.blockSignals(True)
        self.ui.folders_comboBox.clear()
        for folder_path in data.keys():
            self.ui.folders_comboBox.addItem(folder_path)
        self.ui.folders_comboBox.setCurrentIndex(0)
        self.ui.folders_comboBox.blockSignals(False)
        self._on_folder_changed()

    def get_data(self) -> dict:
        return self._data

    def _on_folder_changed(self):
        curr_dir = self.ui.folders_comboBox.currentText()
        if not curr_dir:
            return
        self.ui.file_list.blockSignals(True)
        self.ui.file_list.clear()
        icon_provider = QFileIconProvider()
        for filename in self._data[curr_dir].keys():
            file_path = os.path.join(curr_dir, filename)
            new_item = QListWidgetItem(filename)
            new_item.setIcon(icon_provider.icon(QFileInfo(file_path)))
            self.ui.file_list.addItem(new_item)
        self.ui.file_list.setCurrentRow(0)
        self.ui.file_list.blockSignals(False)

        for filename in self._data[curr_dir].keys():
            self.ui.locales_comboBox.blockSignals(True)
            self.ui.locales_comboBox.clear()
            for locale in self._data[curr_dir][filename].keys():
                new_loc = QLocale(locale)
                if new_loc.language() != QLocale.Language.C:
                    language = new_loc.nativeLanguageName()
                    territory = new_loc.nativeTerritoryName()
                    self.ui.locales_comboBox.addItem(f"{language} ({territory})", userData=locale)
                else:
                    self.ui.locales_comboBox.addItem(str(locale), userData=locale)
            self.ui.locales_comboBox.setCurrentIndex(0)
            self.ui.locales_comboBox.blockSignals(False)
            break
        self._on_curr_file_changed()

    def _on_curr_file_changed(self):
        if self.ui.file_list.count() == 0:
            return

        curr_folder = self.ui.folders_comboBox.currentText()
        curr_filename = self.ui.file_list.currentItem().text()
        file_path = os.path.join(curr_folder, curr_filename)
        if os.path.exists(file_path):
            pixmap = QPixmap(file_path)
            pixmap = pixmap.scaled(
                self.ui.image_label.size(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
        else:
            pixmap = QPixmap()
        self.ui.image_label.setPixmap(pixmap)
        self._update_input_widgets()

    def _update_input_widgets(self):
        if not all([
            self.ui.folders_comboBox.count(),
            self.ui.file_list.count(),
            self.ui.locales_comboBox.count()]):
            return

        curr_folder = self.ui.folders_comboBox.currentText()
        curr_filename = self.ui.file_list.currentItem().text()
        locales = []
        if self.ui.show_all_locales_checkBox.isChecked():
            for i in range(self.ui.locales_comboBox.count()):
                locales.append(
                    (self.ui.locales_comboBox.itemText(i), self.ui.locales_comboBox.itemData(i, Qt.UserRole))
                )
        else:
            self.ui.locales_comboBox.setEnabled(True)
            locales.append(
                (self.ui.locales_comboBox.currentText(), self.ui.locales_comboBox.currentData(Qt.UserRole))
            )

        widget = QWidget()
        widget.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum))
        v_layout = QVBoxLayout(widget)
        v_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        n = 0
        first_line_edit = None
        for lang_fullname, locale in locales:
            curr_locale_data = self._data[curr_folder][curr_filename][locale]

            header_lineEdit = QLineEdit()
            header_lineEdit.setPlaceholderText(lc.HEADER())
            header_lineEdit.setProperty("part", "header")
            header_lineEdit.setProperty("loc", locale)
            header_lineEdit.setText(curr_locale_data["header"])
            header_lineEdit.textChanged.connect(self._on_text_changed)
            if n==0:
                first_line_edit = header_lineEdit

            description_lineEdit = QLineEdit()
            description_lineEdit.setPlaceholderText(lc.DESCRIPTION())
            description_lineEdit.setProperty("part", "desc")
            description_lineEdit.setProperty("loc", locale)
            description_lineEdit.setText(curr_locale_data["desc"])
            description_lineEdit.textChanged.connect(self._on_text_changed)

            if self.ui.show_all_locales_checkBox.isChecked():
                label = QLabel(lang_fullname)
                v_layout.addWidget(label)

            v_layout.addWidget(header_lineEdit)
            v_layout.addWidget(description_lineEdit)

            n += 1

        widget.adjustSize()
        self.ui.scrollArea.setWidget(widget)
        first_line_edit.setFocus()

    def _on_text_changed(self, s: str):
        curr_folder = self.ui.folders_comboBox.currentText()
        curr_filename = self.ui.file_list.currentItem().text()
        locale = self.sender().property("loc")
        part = self.sender().property("part")
        self._data[curr_folder][curr_filename][locale][part] = s

    def _init_widgets(self):
        self.ui.edit_locale_btn.setVisible(False)

        self.ui.prev_image_btn.clicked.connect(lambda: self._on_switch_file("up"))
        self.ui.next_image_btn.clicked.connect(lambda: self._on_switch_file("down"))

        self.ui.next_folder_btn.clicked.connect(lambda: self._on_switch_folder("next"))
        self.ui.prev_folder_btn.clicked.connect(lambda: self._on_switch_folder("prev"))

        self.ui.add_folder_btn.clicked.connect(lambda: self.user_request.emit(MainWidget.UserRequest.IMPORT_DATA))
        self.ui.delete_folder_btn.clicked.connect(self._on_delete_folder)
        self.ui.clear_folders_btn.clicked.connect(self._on_delete_all_folders)
        self.ui.add_locale_btn.clicked.connect(self._on_add_locale)
        self.ui.delete_locale_btn.clicked.connect(self._on_delete_locale)
        self.ui.save_btn.clicked.connect(lambda: self.user_request.emit(MainWidget.UserRequest.SAVE_DATA))
        self.ui.locales_comboBox.currentIndexChanged.connect(self._update_input_widgets)
        self.ui.folders_comboBox.currentIndexChanged.connect(self._on_folder_changed)
        self.ui.file_list.currentRowChanged.connect(self._on_curr_file_changed)
        self.ui.show_all_locales_checkBox.stateChanged.connect(self._update_input_widgets)
        self.ui.scrollArea.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.MinimumExpanding))
        self.ui.scrollArea.setWidgetResizable(True)

        self.ui.image_label.setAlignment(Qt.AlignCenter)

    def _on_delete_folder(self):
        if self.ui.folders_comboBox.count() > 0:
            curr_folder = self.ui.folders_comboBox.currentText()
            del self._data[curr_folder]
            self.ui.folders_comboBox.removeItem(self.ui.folders_comboBox.currentIndex())
        if self.ui.folders_comboBox.count() == 0:
            self._clear_widgets()

    def _clear_widgets(self):
        self.ui.folders_comboBox.clear()
        self.ui.file_list.clear()
        self.ui.locales_comboBox.clear()
        if w := self.ui.scrollArea.takeWidget():
            w.deleteLater()
        self.ui.image_label.clear()

    def _on_delete_all_folders(self):
        self._clear_widgets()
        self._data = {}

    def _on_add_locale(self):
        if self.ui.folders_comboBox.count() == 0:
            return

        dialog = SelectLocale(self)
        dialog.setWindowTitle(lc.ADD_LOCALE())
        res = dialog.exec_()
        text = dialog.locale()
        if res and text:
            error = False
            match_obj = re.match(r"^(\w{2})[-_\s](\w{2})$", text)
            if match_obj:
                lang_code = f"{match_obj.group(1)}_{match_obj.group(2)}"
                locale = QLocale(lang_code)
                if locale.language() == QLocale.Language.C:
                    error = True
            else:
                error = True

            if error:
                QMessageBox.warning(self, lc.ERROR(), lc.NOT_CORRECT_LOCALE())
                return

            included_locales = [self.ui.locales_comboBox.itemData(i, Qt.ItemDataRole.UserRole) \
                                for i in range(self.ui.locales_comboBox.count())]
            normalized_locale = \
                f"{QLocale.languageToCode(locale.language())}-{QLocale.territoryToCode(locale.territory())}"

            if normalized_locale in included_locales:
                QMessageBox.warning(self, lc.ERROR(), lc.LOCALE_INCLUDED())
                return

            if self.ui.folders_comboBox.count() > 1:
                ans = QMessageBox.question(self, lc.QUESTION(), lc.ADD_FOR_OTHER(),
                                           buttons=QMessageBox.Yes | QMessageBox.No)
            else:
                ans = QMessageBox.No

            for folder in self._data.keys():
                selected_folder = self.ui.folders_comboBox.currentText()
                if ans != QMessageBox.Yes and selected_folder != folder:
                    continue
                for filename in self._data[folder].keys():
                    if normalized_locale not in self._data[folder][filename]:
                        self._data[folder][filename][normalized_locale] = \
                            {"header": "", "desc": ""}

            add_to_combobox = True
            for i in range(self.ui.locales_comboBox.count()):
                i_data = self.ui.locales_comboBox.itemData(i, Qt.ItemDataRole.UserRole)
                if i_data == normalized_locale:
                    add_to_combobox = False
                    break

            if add_to_combobox:
                language = locale.nativeLanguageName()
                territory = locale.nativeTerritoryName()
                self.ui.locales_comboBox.addItem(f"{language} ({territory})", userData=normalized_locale)
                self._update_input_widgets()

    def _on_delete_locale(self):
        if self.ui.locales_comboBox.count() == 0:
            return

        curr_folder = self.ui.folders_comboBox.currentText()
        curr_locale = self.ui.locales_comboBox.currentData(Qt.UserRole)

        self.ui.locales_comboBox.blockSignals(True)
        self.ui.locales_comboBox.removeItem(self.ui.locales_comboBox.currentIndex())
        self.ui.locales_comboBox.blockSignals(False)

        for file in self._data[curr_folder].values():
            del file[curr_locale]

        if self.ui.locales_comboBox.count() == 0:
            for row in range(self.ui.file_list.count()):
                file = self.ui.file_list.item(row).text()
                self._data[curr_folder][file][None] = {"header": "", "desc": ""}
            self.ui.locales_comboBox.addItem("None", userData=None)
        self._update_input_widgets()

    def _on_switch_file(self, direction: Literal["up", "down"]):
        if self.ui.file_list.count() < 2:
            return

        if direction == "up":
            if self.ui.file_list.currentRow() == 0:
                self.ui.file_list.setCurrentRow(self.ui.file_list.count() - 1)
            else:
                self.ui.file_list.setCurrentRow(self.ui.file_list.currentRow() - 1)
        elif direction == "down":
            if self.ui.file_list.currentRow() == self.ui.file_list.count() - 1:
                self.ui.file_list.setCurrentRow(0)
            else:
                self.ui.file_list.setCurrentRow(self.ui.file_list.currentRow() + 1)

    def _on_switch_folder(self, direction: Literal["next", "prev"]):
        if self.ui.folders_comboBox.count() < 2:
            return

        if direction == "prev":
            if self.ui.folders_comboBox.currentIndex() == 0:
                self.ui.folders_comboBox.setCurrentIndex(self.ui.folders_comboBox.count() - 1)
            else:
                self.ui.folders_comboBox.setCurrentIndex(self.ui.folders_comboBox.currentIndex() - 1)
        elif direction == "next":
            if self.ui.folders_comboBox.currentIndex() == self.ui.folders_comboBox.count() - 1:
                self.ui.folders_comboBox.setCurrentIndex(0)
            else:
                self.ui.folders_comboBox.setCurrentIndex(self.ui.folders_comboBox.currentIndex() + 1)

    def dragEnterEvent(self, event) -> None:
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event) -> None:
        if event.mimeData().hasUrls():
            result = []
            for url in event.mimeData().urls():
                path = url.toLocalFile()
                if os.path.isdir(path):
                    result.append(path)
            if result:
                self.received_dir_list.emit(result)
            event.accept()
        else:
            event.ignore()