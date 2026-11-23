from classes.class_game import Game
import io
import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Game()
    ex.show()
    sys.exit(app.exec())