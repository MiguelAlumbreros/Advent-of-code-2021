from dataclasses import dataclass


@dataclass
class BoardDimensions:
    board_dim_x: int = 5
    board_dim_y: int = 5


def import_data() -> list:
    with open('day4_input.txt', 'r') as fil:
        lines = fil.readlines()
    lines_parsed = [line.strip().split('\n') for line in lines]
    # Parse number draw list
    draw_temp = lines_parsed[0][0].split(',')
    for i in range(len(draw_temp)):
        draw_temp[i] = int(draw_temp[i])

    # Parse matrices
    boards_temp = []
    matrix_temp = []
    for i in range(2, len(lines)):
        line_temp = lines[i].split(' ')
        line_output = []
        if not line_temp[0] == '\n':
            for element in line_temp:
                if not element == '':
                    line_output.append(int(element))
            # line_output[-1] = line_output[-1].split('\n')[0]
        else:
            line_output = ['']
        if not line_output[0] == '':
            matrix_temp.append(line_output)
        else:
            boards_temp.append(matrix_temp)
            matrix_temp = []
    return draw_temp, boards_temp


def board_check(boards_temp: list, draw_temp: list):
    boards_checked = boards_temp
    for draw in draw_temp:
        for board_index, board in enumerate(boards_temp):
            for i in range(BoardDimensions.board_dim_x):
                for j in range(BoardDimensions.board_dim_y):
                    if board[i][j] == draw:
                        boards_checked[board_index][i][j] = 'x'
                    winning_board_x = check_if_row(boards_checked)
                    if winning_board_x:
                        return winning_board_x, board, draw
                    winning_board_y = check_if_column(boards_checked)
                    if winning_board_y:
                        return winning_board_y, board, draw


def check_if_row(boards_checked: list) -> int:
    row_x_counter = 0
    for board_index, board in enumerate(boards_checked):
        for i in range(BoardDimensions.board_dim_x):
            for j in range(BoardDimensions.board_dim_y):
                if board[i][j] == 'x':
                    row_x_counter += 1
                    if row_x_counter == BoardDimensions.board_dim_x:
                        print('>> ROW!')
                        return (board_index)
            row_x_counter = 0


def check_if_column(boards_checked: list) -> int:
    coulumn_x_counter = 0
    for board_index, board in enumerate(boards_checked):
        for i in range(BoardDimensions.board_dim_x):
            for j in range(BoardDimensions.board_dim_y):
                if board[j][i] == 'x':
                    coulumn_x_counter += 1
                    if coulumn_x_counter == BoardDimensions.board_dim_x:
                        print('>> COLUMN!')
                        return (board_index)
            coulumn_x_counter = 0


def main():
    # # Sample
    # sample_draw = [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24,
    #                10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1]
    # sample_boards = [[[22, 13, 17, 11, 0], [8, 2, 23, 4, 24], [1, 9, 14, 16, 7], [6, 10, 3, 18, 5], [1, 12, 20, 15, 19]], [[3, 15, 0, 2, 22], [9, 18, 13, 17, 5], [
    #     9, 8, 7, 25, 23], [0, 11, 10, 24, 4], [4, 21, 16, 12, 6]], [[14, 21, 17, 24, 4], [10, 16, 15, 9, 19], [18, 8, 23, 26, 20], [22, 11, 13, 6, 5], [2, 0, 12, 3, 7]]]

    # Import data

    draw_temp, boards_temp = import_data()
    # boards_temp = sample_boards
    # draw_temp = sample_draw

    winning_board_index, winning_board, winning_draw = board_check(
        boards_temp, draw_temp)
    print(winning_board_index)
    board_summation = 0
    for i in range(BoardDimensions.board_dim_x):
        for j in range(BoardDimensions.board_dim_y):
            if type(winning_board[i][j]) is int:
                board_summation += winning_board[i][j]
    print(f'Winning board sum = {board_summation}')
    print(f'Winning draw = {winning_draw}')
    print(f'Result = {board_summation * winning_draw}')


if __name__ == '__main__':
    main()
