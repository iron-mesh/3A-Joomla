from abc import ABC, abstractmethod

from PySide6.QtWidgets import QWidget


class AbstractModule(ABC):
    """Abstract base class for a module"""

    @classmethod
    @abstractmethod
    def name(cls) -> str:
        """Returns the name of the module"""
        pass

    @classmethod
    @abstractmethod
    def widget(cls) -> QWidget:
        """Returns the widget of the module"""
        pass

    @classmethod
    @abstractmethod
    def retranslate(cls):
        """Perform a retranslation of the module gui"""
        pass