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
    for i in range(coordinates.x_init, coordinates.x_end):
        Grid.grid[coordinates.x_init + i][coordinates.y_init] += 1
        # Grid.grid[coordinates.y_init + i][coordinates.x_init] += 1

        # for line in Grid.grid:
        #     print(line)


def move_y(command):
    coordinates = Coordinates(command[0], command[1], command[2], command[3])


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
    _MAX_COOR = 10
    input_data_temp = line_parser(sample_diagram)
    # Discard non vertical or horizontal lines
    input_data = input_data_temp
    for i, command in enumerate(input_data_temp):
        if not (command[0] == command[2] or command[1] == command[3]):
            input_data.pop(i)

    # Define global initialized grid composed of zeroes
    grid = [[0 for i in range(_MAX_COOR)]] * _MAX_COOR
    Grid.grid = grid
    for i, command in enumerate(input_data):
        if command[0] == command[2]:
            move_y(command)
        if command[1] == command[3]:
            move_x(command)

    for line in Grid.grid:
        print(line)


if __name__ == '__main__':
    main()
