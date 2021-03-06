from dataclasses import dataclass


@dataclass
class Grid:
    grid: list


@dataclass
class Coordinates:
    x_init: int
    y_init: int
    x_end: int
    y_end: int


def diagram_parser():
    with open('day5_input.txt', 'r') as f:
        lines = f.readlines()
    lines_parsed = [line.strip().split('\n') for line in lines]
    output = []
    for line in lines_parsed:
        output.append(line[0])
    return output


def line_parser(diagram: list):
    output = []
    for line in diagram:
        line_split = line.split(' -> ')
        line_temp = []
        for i in line_split:
            numbers = i.split(',')
            for j in numbers:
                line_temp.append(int(j))
        output.append(line_temp)
    return output


def move_x(command):
    coordinates = Coordinates(command[0], command[1], command[2], command[3])
    range1 = min(coordinates.x_init, coordinates.x_end)
    range2 = max(coordinates.x_init, coordinates.x_end)
    for i in range(range1, range2 + 1):
        Grid.grid[coordinates.y_init][i] += 1


def move_y(command):
    coordinates = Coordinates(command[0], command[1], command[2], command[3])
    range1 = min(coordinates.y_init, coordinates.y_end)
    range2 = max(coordinates.y_init, coordinates.y_end)
    for j in range(range1, range2 + 1):
        Grid.grid[j][coordinates.x_init] += 1


def move_diag(command):
    coordinates = Coordinates(command[0], command[1], command[2], command[3])

    if coordinates.x_init < coordinates.x_end:
        x1 = coordinates.x_init
        y1 = coordinates.y_init
        y2 = coordinates.y_end
    else:
        x1 = coordinates.x_end
        y1 = coordinates.y_end
        y2 = coordinates.y_init
    inc = abs(y1 - y2)
    # Case up
    if y2 > y1:
        for i in range(inc + 1):
            Grid.grid[y1 + i][x1 + i] += 1
    # Case down
    else:
        for i in range(inc + 1):
            Grid.grid[y1 - i][x1 + i] += 1


def result_counter() -> int:
    max_index = len(Grid.grid)
    counter = 0
    for i in range(max_index):
        for j in range(max_index):
            if Grid.grid[i][j] > 1:
                counter += 1
    return counter


def main():
    # Sample
    sample_diagram = ['0,9 -> 5,9',
                      '8,0 -> 0,8',
                      '9,4 -> 3,4',
                      '2,2 -> 2,1',
                      '7,0 -> 7,4',
                      '6,4 -> 2,0',
                      '0,9 -> 2,9',
                      '3,4 -> 1,4',
                      '0,0 -> 8,8',
                      '5,5 -> 8,2']
    _MAX_COOR = 1000  # Board dimensions
    diagram = diagram_parser()
    # diagram = sample_diagram
    input_data_temp = line_parser(diagram)
    # Discard non vertical or horizontal lines
    input_data = input_data_temp
    """Remove below loop for Part 2"""
    # for i, command in enumerate(input_data_temp):
    #     if not (command[0] == command[2] or command[1] == command[3]):
    #         input_data.pop(i)

    # Define global initialized grid composed of zeroes
    grid = []
    for i in range(_MAX_COOR):
        line_temp = []
        for j in range(_MAX_COOR):
            line_temp.append(0)
        grid.append(line_temp)

    Grid.grid = grid
    for i, command in enumerate(input_data):
        if command[0] == command[2]:
            move_y(command)
        elif command[1] == command[3]:
            move_x(command)
        else:
            move_diag(command)

    print(f'Result = {result_counter()}')

    # for line in Grid.grid:
    #     print(line)


if __name__ == '__main__':
    main()
