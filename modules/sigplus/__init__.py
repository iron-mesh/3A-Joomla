
from .view.main_widget import MainWidget
from .presenter.manager import Manager

Manager.start()

class Sigplus:
    widget = MainWidget.instance()
    name = "Sigplus filler"