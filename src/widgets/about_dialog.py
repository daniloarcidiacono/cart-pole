from PyQt5.QtWidgets import QDialog

from src.ui.about_dialog_ui import Ui_AboutDialog


class AboutDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Init the UI
        self.ui = Ui_AboutDialog()
        self.ui.setupUi(self)