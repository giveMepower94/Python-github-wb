import pygame
import sys

# Инициализация Pygame
pygame.init()

# Определение размеров окна и клеток
WINDOW_SIZE = 300
CELL_SIZE = WINDOW_SIZE // 3
LINE_WIDTH = 15

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Создание окна
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption('Крестики-нолики')

# Инициализация игрового поля
board = [['' for _ in range(3)] for _ in range(3)]