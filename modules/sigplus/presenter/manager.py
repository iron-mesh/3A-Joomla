import os
import re
from typing import Optional

from PySide6.QtGui import QImageReader
from PySide6.QtWidgets import QFileDialog, QTreeView, QAbstractItemView, QMessageBox

from PyUB.utils import retranslate_nested_langconstants
from ..view import lang_consts as lc
from ..view.main_widget import MainWidget
from ....common.settings import Settings


class Manager:

    @classmethod
    def start(cls):
        cls._widget = MainWidget()
        cls._widget.user_request.connect(cls._user_request_handler)
        cls._widget.received_dir_list.connect(cls._import_data)

    @classmethod
    def _user_request_handler(cls, action: MainWidget.UserRequest):
        match action:
            case MainWidget.UserRequest.IMPORT_DATA:
                cls._import_data()
            case MainWidget.UserRequest.SAVE_DATA:
                cls._export_data()


    @classmethod
    def _import_data(cls, from_dirs: list[str] = []):
        if not from_dirs:
            selected_folders = set(cls._select_multiple_folders())
        else:
            selected_folders = set(from_dirs)
        if not selected_folders:
            return

        available_filetypes = [i.toStdString() for i in QImageReader.supportedImageFormats()]
        if Settings.add_subfolders_m1.value:
            for folder in selected_folders.copy():
                for root, dirs, files in os.walk(folder):
                    selected_folders = selected_folders.union(os.path.join(root, d) for d in dirs)

        if Settings.ignore_empty_folders_m1.value:
            for folder in selected_folders.copy():
                if any(entry.name.split(".")[-1] in available_filetypes for entry in os.scandir(folder) if entry.is_file()):
                    continue
                selected_folders.remove(folder)

        data = {}
        for folder_path in selected_folders:
            data[folder_path] = {}
            filename_list = []
            parsed_files = {}
            for entry in os.scandir(folder_path):
                if not entry.is_file():
                    continue
                if entry.name.split(".")[-1] in available_filetypes:
                    filename_list.append(entry.name)
                elif entry.name.split(".")[-1] == "txt":
                    parsed_data = cls._parse_file(entry.path)
                    if parsed_data:
                        parsed_files[parsed_data["locale"]] = parsed_data["files"]

            if None in parsed_files:
                deleting_key = set(parsed_files.keys())
                deleting_key.discard(None)
                for key in deleting_key:
                    del parsed_files[key]

            if not parsed_files: # create fictive file if empty
                parsed_files[None] = {}

            for filename in filename_list:
                data[folder_path][filename] = {}
                for locale, files in parsed_files.items():
                    data[folder_path][filename][locale] = {}
                    if filename in files:
                        data[folder_path][filename][locale]["header"] = files[filename].get("header", "")
                        data[folder_path][filename][locale]["desc"] = files[filename].get("desc", "")
                    else:
                        data[folder_path][filename][locale]["header"] = ""
                        data[folder_path][filename][locale]["desc"] = ""
        cls._widget.set_data(cls._widget.get_data() | data)

    @classmethod
    def _export_data(cls):
        data = cls._widget.get_data()

        created_files = 0
        modified_files = 0

        for folder_path in data.keys():
            files_content = {}
            for file_name in data[folder_path].keys():
                for locale in data[folder_path][file_name].keys():
                    if locale not in files_content:
                        files_content[locale] = []
                    header = data[folder_path][file_name][locale]["header"]
                    description = data[folder_path][file_name][locale]["desc"]
                    if header or description:
                        files_content[locale].append("|".join(
                            [file_name,
                             header,
                             description]
                        ))

            for locale, content in files_content.items():
                if not content:
                    continue

                if locale is None:
                    filename = "labels.txt"
                else:
                    filename = f"labels.{locale}.txt"
                file_path = os.path.join(folder_path, filename)
                try:
                    file_exists = os.path.exists(file_path)
                    with open(file_path, "w", encoding="utf-8") as file:
                        file.write("\n".join(content))
                    if file_exists:
                        modified_files += 1
                    else:
                        created_files += 1
                except Exception as e:
                    QMessageBox.warning(cls._widget, lc.ERROR(), lc.CANNOT_SAVE_LABEL_FILE().format(path=file_path))

        QMessageBox.information(cls._widget, lc.REPORT(),
                                lc.SAVING_REPORT().format(modified=modified_files, created=created_files))


    @classmethod
    def _parse_file(cls, path: str) -> Optional[dict]:
        """
            Read text file and returns dict with data
                Example:
                {
                    "locale": "en_GB,
                    "files": {
                    "filename": {"header": "Header image", "desc": "Description image"},
                    }
                }

            Returns:
                dict: parsed data
                None: if cannot read file
        """
        file_name = os.path.basename(path)
        re_pattern = re.compile(r"labels\.(\w\w-\w\w)\.txt")
        if not re_pattern.match(file_name) and file_name != "labels.txt":
            return None
        result = {}
        match_obj = re_pattern.search(file_name)
        if match_obj and match_obj.group(1):
            locale = match_obj.group(1)
        else:
            locale = None

        result["locale"] = locale
        result["files"] = {}

        try:
            with open(path, "r", encoding="utf-8") as file:
                for line in file.readlines():
                    parts = line.split("|")
                    if len(parts) >= 2:
                        fname = parts[0].strip()
                        result["files"] [fname] = {}
                        result["files"] [fname] ["header"] = parts[1].strip()
                        result["files"] [fname] ["desc"] = parts[2].strip() if len(parts) >= 3 else ""
            return result
        except Exception as e:
            QMessageBox.warning(cls._widget, lc.ERROR(), lc.CANNOT_LOAD_LABEL_FILE().format(path=path))
            return None

    @classmethod
    def _select_multiple_folders(cls) -> list[str]:
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.FileMode.Directory)
        dialog.setOption(QFileDialog.Option.ShowDirsOnly, True)
        dialog.setOption(QFileDialog.Option.DontUseNativeDialog, True)
        tree_view = dialog.findChild(QTreeView)
        if tree_view:
            tree_view.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)

        if dialog.exec():
            selected_folders = dialog.selectedFiles()
            return selected_folders
        return []

    @classmethod
    def retranslate(cls):
        retranslate_nested_langconstants(lc)
        cls._widget.retranslate()
