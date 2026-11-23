from PyQt6.QtWidgets import QApplication, QMainWindow


class Game(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(640, 494)