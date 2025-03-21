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
