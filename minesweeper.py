import random

def create_board(grid_size,num_mines):
    board = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
    display = [["-" for _ in range(grid_size)] for _ in range(grid_size)]
    mine_pos = set()
    while len(mine_pos) < num_mines:
        position = (random.randrange(grid_size - 1), random.randrange(grid_size - 1))
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
    col, row = input("Make move (A:5) - ", ).split(':')
    char_to_int = ord(col.lower()) - ord('a')
    #print(f"char to int is ", char_to_int)
    return int(row), int(char_to_int)

def print_board(display):
    header = '   '
    row_num = 0
    for i in range(0, len(display)):
        header += chr(i + 65) + ' '

    print(header)

    for row in display:
        print(f"{row_num}| " + ' '.join(str(x) for x in row))
        row_num += 1

def reveal(board, display, row, col):
    if display[row][col] == "-":
        display[row][col] = board[row][col]

def play_game(size = 10, mines = 15):
    board, display, pos = create_board(size, mines)
    possible_moves = size ** 2 - mines
    used = set()

    while len(used) < possible_moves:
        print("\033[H\033[2J", end="") # ANSI Escape Codes: https://stackoverflow.com/a/50560686
        print_board(display)
        row, col = get_move(size)
        reveal(board, display, row, col)
        print("\033[H\033[2J", end="") # ANSI Escape Codes: https://stackoverflow.com/a/50560686
        print_board(display)
        #print(f"row is {row} and col is {col}")
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
    play_game(3,3)
