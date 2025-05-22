import sys
from PySide6.QtWidgets import QApplication
from game import SeaBattleGame

if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = SeaBattleGame()
    game.show()
    sys.exit(app.exec())