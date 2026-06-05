from PySide6.QtWidgets import QWidget

from .presenter.manager import Manager
from .view.main_widget import MainWidget
from ...common.bases import AbstractModule

Manager.start()

class SigplusFiller(AbstractModule):
    @classmethod
    def name(self) -> str:
        return "Sigplus filler"

    @classmethod
    def widget(cls) -> QWidget:
        return MainWidget.instance()

    @classmethod
    def retranslate(cls):
        Manager.retranslate()