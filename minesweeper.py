import random
import math
import sys

def create_board(grid_size,num_mines):
    board = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
    display = [["-" for _ in range(grid_size)] for _ in range(grid_size)]
    mine_pos = set()
    while len(mine_pos) < num_mines:
        position = (random.randrange(grid_size), random.randrange(grid_size))
        if position not in mine_pos:
            mine_pos.add(position)
            row, col = position
            board[row][col] = "M"
            for neighbor_row in range (max(0, row - 1), min(grid_size, row + 2)):
                for neighbor_col in range(max(0, col - 1), min(grid_size, col + 2)):
                    if board[neighbor_row][neighbor_col] != "M":
                        board[neighbor_row][neighbor_col] += 1

    return board, display, mine_pos

def get_move(grid_size):
    while True:
        move_str = input("Choose coordinates to uncover (ex a5) - ").strip()
        #print("Type 'exit' to quit\n")
        if move_str.lower() == "exit":
            print("\033[H\033[2J", end="") # ANSI Escape Codes: https://stackoverflow.com/a/50560686 
            sys.exit()
        if len(move_str) < 2:
            print("Invalid input. Enter 2 characters or more.")
            continue

        col, row = move_str[0], move_str[1:]

        if not col.isalpha() or not row.isdigit():
            print("Invalid input. First character should be a letter and the rest should be digits.")
            continue

        col_index = ord(col.lower()) - ord('a')
        row_index = int(row)

        if col_index >= grid_size or row_index >= grid_size:
            print("Invalid move. Coordinates out of range.")
            continue

        return row_index, col_index


def print_board(display):
    header = '    '
    row_num = 0

    for i in range(0, len(display)):
        header += chr(i + 65) + ' '
    
    print(header)
    
    for row in display:
        print(f"{row_num:02d}| " + ' '.join(str(x) for x in row))
        row_num += 1

def reveal(board, display, row, col):
    if display[row][col] == "-":
        display[row][col] = board[row][col]
        if board[row][col] == 0:
            for neighbor_row in range(max(0, row - 1), min(len(board), row + 2)):
                for neighbor_col in range(max(0, col - 1), min(len(board), col + 2)):
                    if board[neighbor_row][neighbor_col] != "M":
                        reveal(board, display, neighbor_row, neighbor_col)

def game_setup():
    options = ["3x3", "10x10", "25x25"]
    selected_index = 0
    while True:
        print("\033[H\033[2J", end="") # ANSI Escape Codes: https://stackoverflow.com/a/50560686 
        print("How large of a board would you like to play?")
        print("\nType 'exit' to quit\n")
        for i, option in enumerate(options, 1):
            print(f"{i} {option}")
        choice = input("Choose a number: ").strip()
        
        if choice.lower() == "exit":
            print("\033[H\033[2J", end="") # ANSI Escape Codes: https://stackoverflow.com/a/50560686 
            sys.exit()

        if choice.isdigit():
            choice_num = int(choice)
            if 1 <= choice_num <= len(options):
                return options[choice_num - 1]

def play_game(size = 10, mines = 15):
    setup = game_setup()
    size = int(setup.split("x")[0])
    mines = math.floor(float(size**2) * .15)
    board, display, pos = create_board(size, mines)
    possible_moves = size ** 2 - mines
    used = set()

    while len(used) < possible_moves:
        print("\033[H\033[2J", end="") # ANSI Escape Codes: https://stackoverflow.com/a/50560686
        print_board(display)
        print("\nType 'exit' to quit\n")
        row, col = get_move(size)
        reveal(board, display, row, col)
        print("\033[H\033[2J", end="") # ANSI Escape Codes: https://stackoverflow.com/a/50560686
        print_board(display)
        if (row, col) in pos:
            print("You suck!")
            break
        else:
            used.add((row, col))

    if len(used) == possible_moves:
        print("Mines Cleared!")
    else:
        print("Mine Hit!")

if __name__ == "__main__":
    play_game()
