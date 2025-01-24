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

# Функция для рисования сетки, рисуем вертикальную и горизонтальную линию

def draw_grid():
   screen.fill(WHITE)
   for i in range(1, 3):
       pygame.draw.line(screen, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, WINDOW_SIZE), LINE_WIDTH)
       pygame.draw.line(screen, BLACK, (0, i * CELL_SIZE), (WINDOW_SIZE, i * CELL_SIZE), LINE_WIDTH)


# Функция для рисования крестиков и ноликов
