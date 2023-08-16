import sys
from PySide6.QtWidgets import QApplication
from authentication.token import TokenDialog

if __name__ == "__main__":
    app = QApplication(sys.argv)
    token_dialog = TokenDialog()
    token_dialog.show()
    sys.exit(app.exec())
