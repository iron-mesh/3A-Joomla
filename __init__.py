from typing import Optional

from PySide6.QtWidgets import QWidget, QTabWidget

from PyUB.Types import Plugin
from PyUB.Types.Properties import PropertyContainer
from .common.settings import Settings
from .modules.sigplus import Sigplus


class plugin(Plugin):

    @classmethod
    def gui(cls) -> QWidget:
        qtabwidget = QTabWidget()
        qtabwidget.setTabPosition(QTabWidget.TabPosition.West)

        qtabwidget.addTab(Sigplus.widget, Sigplus.name)

        return qtabwidget

    @classmethod
    def settings(cls) -> Optional[PropertyContainer]:
        return Settings


