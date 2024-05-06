import random

def create_board(grid_size,num_mines):
    board = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
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

    return board, mine_pos

def print_board(board):
    for row in board:
        print(' '.join(str(x) for x in row))



if __name__ == "__main__":
    print("\033[H\033[2J", end="") # ANSI Escape Codes: https://stackoverflow.com/a/50560686
    board, pos = create_board(10,10)
    print_board(board)
