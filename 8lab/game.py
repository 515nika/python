from PySide6.QtWidgets import QMainWindow, QMessageBox, QVBoxLayout, QPushButton, QLabel, QWidget, QGridLayout
from PySide6.QtCore import Qt
import random
from exceptions import ShipPlacementError, InvalidCoordinateError

class SeaBattleGame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Морской бой")
        self.setGeometry(100, 100, 800, 600)
        
        self.player_board = [[0 for _ in range(10)] for _ in range(10)]
        self.computer_board = [[0 for _ in range(10)] for _ in range(10)]
        self.ships = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]  # Размеры кораблей
        self.game_over = False  # Флаг окончания игры
        
        self.init_ui()
        self.place_ships(self.player_board)
        self.place_ships(self.computer_board)
    
    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        self.label = QLabel("Ваш ход! Кликайте по правому полю.")
        layout.addWidget(self.label)
        
        # Сетка для игровых полей
        grid_layout = QGridLayout()
        layout.addLayout(grid_layout)
        
        # Левое поле (игрок)
        self.player_grid = QGridLayout()
        grid_layout.addLayout(self.player_grid, 0, 0)
        
        # Правое поле (компьютер)
        self.computer_grid = QGridLayout()
        grid_layout.addLayout(self.computer_grid, 0, 1)
        
        # Заполняем поля кнопками
        for i in range(10):
            for j in range(10):
                btn_player = QPushButton()
                btn_player.setFixedSize(30, 30)
                self.player_grid.addWidget(btn_player, i, j)
                
                btn_computer = QPushButton()
                btn_computer.setFixedSize(30, 30)
                btn_computer.clicked.connect(lambda _, x=i, y=j: self.player_turn(x, y))
                self.computer_grid.addWidget(btn_computer, i, j)
    
    def place_ships(self, board):
        for ship_size in self.ships:
            placed = False
            while not placed:
                try:
                    x, y = random.randint(0, 9), random.randint(0, 9)
                    horizontal = random.choice([True, False])
                    
                    if horizontal:
                        if y + ship_size > 10:
                            raise ShipPlacementError
                    else:
                        if x + ship_size > 10:
                            raise ShipPlacementError
                    
                    # Проверяем, нет ли рядом других кораблей
                    for i in range(max(0, x-1), min(10, x + (ship_size if not horizontal else 1) + 1)):
                        for j in range(max(0, y-1), min(10, y + (ship_size if horizontal else 1) + 1)):
                            if board[i][j] == 1:
                                raise ShipPlacementError
                    
                    # Размещаем корабль
                    for k in range(ship_size):
                        if horizontal:
                            board[x][y + k] = 1
                        else:
                            board[x + k][y] = 1
                    
                    placed = True
                
                except ShipPlacementError:
                    continue
    
    def check_win(self, board):
        """Проверяет, остались ли непотопленные корабли."""
        for row in board:
            if 1 in row:  # Если есть хотя бы одна клетка с кораблём (1)
                return False
        return True  # Все корабли потоплены
    
    def end_game(self, player_won):
        """Завершает игру и выводит сообщение."""
        self.game_over = True
        for i in range(10):
            for j in range(10):
                self.computer_grid.itemAtPosition(i, j).widget().setEnabled(False)
        
        if player_won:
            QMessageBox.information(self, "Победа!", "Вы победили! 🎉")
        else:
            QMessageBox.information(self, "Поражение", "Компьютер победил. 😢")
    
    def player_turn(self, x, y):
        if self.game_over:
            return
        
        try:
            if x < 0 or x > 9 or y < 0 or y > 9:
                raise InvalidCoordinateError
            
            if self.computer_board[x][y] == 1:  # Попадание
                self.computer_board[x][y] = 2
                self.computer_grid.itemAtPosition(x, y).widget().setText("💥")
                self.computer_grid.itemAtPosition(x, y).widget().setStyleSheet("background-color: red")
                self.label.setText("Попадание! Стреляйте ещё.")
                
                if self.check_win(self.computer_board):
                    self.end_game(True)  # Игрок победил
            
            elif self.computer_board[x][y] == 0:  # Промах
                self.computer_board[x][y] = -1
                self.computer_grid.itemAtPosition(x, y).widget().setText("•")
                self.computer_grid.itemAtPosition(x, y).widget().setStyleSheet("background-color: blue")
                self.label.setText("Промах! Ход компьютера.")
                self.computer_turn()
        
        except InvalidCoordinateError:
            QMessageBox.warning(self, "Ошибка", "Недопустимые координаты!")
    
    def computer_turn(self):
        if self.game_over:
            return
        
        x, y = random.randint(0, 9), random.randint(0, 9)
        
        # Компьютер стреляет только в непроверенные клетки
        while self.player_board[x][y] in (-1, 2):
            x, y = random.randint(0, 9), random.randint(0, 9)
        
        if self.player_board[x][y] == 1:  # Попадание
            self.player_board[x][y] = 2
            self.player_grid.itemAtPosition(x, y).widget().setText("💥")
            self.player_grid.itemAtPosition(x, y).widget().setStyleSheet("background-color: red")
            
            if self.check_win(self.player_board):
                self.end_game(False)  # Компьютер победил
        
        else:  # Промах
            self.player_board[x][y] = -1
            self.player_grid.itemAtPosition(x, y).widget().setText("•")
            self.player_grid.itemAtPosition(x, y).widget().setStyleSheet("background-color: blue")