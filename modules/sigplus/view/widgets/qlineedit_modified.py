from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QLineEdit


class QLineEditModified(QLineEdit):
    """Provides modifications to a QLineEdit.

    Attributes:
        switching_requested (Signal(str)): sent when the user pressed the key Enter, passes:
            -"n": "Enter" pressed
            -"p": "Shift+Enter" pressed
    """

    switching_requested = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)

    def keyPressEvent(self, event):
        super().keyPressEvent(event)
        if (event.key() == Qt.Key.Key_Return or event.key() == Qt.Key.Key_Enter):
            if event.modifiers() == Qt.KeyboardModifier.ShiftModifier:
                self.switching_requested.emit("p")
            else:
                self.switching_requested.emit("n")