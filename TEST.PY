from dataclasses import dataclass


@dataclass
class Coordinates:
    x_init: int
    y_init: int
    x_end: int
    y_end: int


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
    inc = abs(y1 - y2) + 2
    # Case up
    if y2 > y1:
        for i in range(inc + 1):
            # Print in diag
            print([x1 + i, y1 + i])
    # Case down
    else:
        for i in range(inc):
            # Print in diag
            print([x1 - i, y1 - i])


def main():
    x1 = 6
    y1 = 2
    x2 = 2
    y2 = 0

    command = [x1, y1, x2, y2]
    move_diag(command)


if __name__ == '__main__':
    main()


