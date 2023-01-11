from ui_createCardDialog import Ui_Dialog
from PySide2.QtWidgets import QDialog


class CreateCardDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
