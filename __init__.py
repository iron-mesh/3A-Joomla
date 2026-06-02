from PySide6.QtWidgets import QWidget, QTabWidget

from PyUB.Types import Plugin
from .modules.sigplus import Sigplus


class plugin(Plugin):

    @classmethod
    def gui(cls) -> QWidget:
        qtabwidget = QTabWidget()
        qtabwidget.setTabPosition(QTabWidget.TabPosition.South)

        qtabwidget.addTab(Sigplus.widget, Sigplus.name)

        return qtabwidget
