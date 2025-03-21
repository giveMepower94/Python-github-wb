# Корректируем игру крестики нолики
# Рисуем игровое поле, используем библиотеку Colorama

from colorama import Fore, Back, Style


def draw_board(board):
    for x in range(len(board)):
        for y in range(len(board)):
            if board[x][y] == " ":
                if y < len(board) - 1:
                    print(Back.YELLOW + board[x][y] + Style.RESET_ALL, "| ", end='')
                else:
                    print(Back.YELLOW + board[x][y] + Style.RESET_ALL, "| ")
            elif board[x][y] == "X":
                if y < len(board) - 1:
                    print(Fore.RED + "X" + Style.RESET_ALL, "| ", end='')
                else:
                    print(Fore.RED + "X" + Style.RESET_ALL, "| ")
            elif board[x][y] == "O":
                if y < len(board) - 1:
                    print(Fore.BLUE + "O" + Style.RESET_ALL, "| ", end='')
                else:
                    print(Fore.BLUE + "O" + Style.RESET_ALL, "| ")
        print("---------")

# Создайте функцию, которая запрашивает ход


def ask_move(player, board):
    while True:
        try:
            x, y = (
                input(f"{player}, Введите x и y координаты (пример 0 0): ").strip().split()
            )
            x, y = int(x), int(y)
            if (0 <= x < len(board)) and (0 <= y < len(board)) and (board[x][y] == " "):
                return (x, y)
            else:
                print(f"Клетка {x} {y} занята или вне диапазона. Попробуйте еще раз.")
        except ValueError:
            print("Некорректный ввод. Введите два числа, разделенные пробелом.")