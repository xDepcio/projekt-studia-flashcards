from ui.ui_createCardDialog import Ui_Dialog
from PySide2.QtWidgets import QDialog, QFileDialog
from utils import (
    extend_cards_storage_from_json,
    extend_cards_storage_from_csv, add_card)
from config import Config as cfg
import os


class CreateCardDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self._setupAddCard()
        self._setupImport()

    def _setupAddCard(self):
        self.ui.btnBox.accepted.connect(self._handleAddCard)

    def _handleAddCard(self):
        origin_name = self.ui.originNameInput.text()
        learn_name = self.ui.learnNameInput.text()
        cat_input = self.ui.categoryInput.text()
        if cat_input.strip() == '':
            categories = None
        else:
            categories_arr = cat_input.split(',')
            categories = [cat.strip().capitalize() for cat in categories_arr]
        pop = self.ui.horizontalSlider.value()/100
        add_card(origin_name, learn_name, categories, pop)
        self.parent().ui.categoriesField.clear()
        self.parent()._setupCategories()

    def _setupImport(self):
        self.ui.btnImport.clicked.connect(self._handleImport)

    def _handleImport(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        options |= QFileDialog.DontConfirmOverwrite
        file_path, _ = QFileDialog.getSaveFileName(
            None,
            "Importuj fiszki",
            "",
            "Text Files (*.txt);;JSON Files (*.json)",
            options=options
        )
        base, ext = os.path.splitext(file_path)
        if ext == '.json':
            extend_cards_storage_from_json(file_path, cfg.CARDS_PATH)
        if ext == '.txt':
            extend_cards_storage_from_csv(file_path, cfg.CARDS_PATH)
        self.parent().ui.categoriesField.clear()
        self.parent()._setupCategories()
        self.close()
