from typing import Optional

from PySide6.QtWidgets import QWidget, QTabWidget

from PyUB.Types import Plugin, Helper
from PyUB.Types.Properties import PropertyContainer
from PyUB.utils import retranslate_nested_langconstants
from .common import lang_consts
from .common.bases import AbstractModule
from .common.settings import Settings


class plugin(Plugin):
    modules: list[AbstractModule] = []

    @classmethod
    def gui(cls) -> QWidget:
        qtabwidget = QTabWidget()
        qtabwidget.setTabPosition(QTabWidget.TabPosition.West)

        from .modules.sigplus import SigplusFiller
        cls.modules = [SigplusFiller]

        for module in cls.modules:
            qtabwidget.addTab(module.widget(), module.name())

        Helper().plugin_language_changing.connect(cls.retranslate)

        return qtabwidget

    @classmethod
    def settings(cls) -> Optional[PropertyContainer]:
        return Settings

    @classmethod
    def retranslate(cls):
        retranslate_nested_langconstants(lang_consts)
        for module in cls.modules:
            module.retranslate()


