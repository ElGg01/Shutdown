from PySide6.QtWidgets import QApplication
from controllers.main_window import MainShutdownWindow

if __name__ == '__main__':
    app = QApplication()
    window = MainShutdownWindow()
    window.show()

    app.exec()