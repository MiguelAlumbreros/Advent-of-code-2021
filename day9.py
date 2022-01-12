def import_data():
    with open("day9_input.txt", "r") as f:
        lines = f.readlines()
    lines_parsed = [line.split('\n')[0] for line in lines]
    data = []
    for line in lines_parsed:
        digit_list = [int(digit) for digit in line]
        data.append(digit_list)
    return data


def is_minimum(data, number, y_index, x_index):
    max_y = len(data) - 1
    max_x = len(data[0]) - 1

    # Top left corner
    if y_index == 0 and x_index == 0:
        if number < data[y_index + 1][x_index] and number < data[y_index][x_index + 1]:
            return True
        return False
    # Top right corner
    if y_index == 0 and x_index == max_x:
        if number < data[y_index + 1][x_index] and number < data[y_index][x_index - 1]:
            return True
        return False
    # Bottom left corner
    if y_index == max_y and x_index == 0:
        if number < data[y_index - 1][x_index] and number < data[y_index][x_index + 1]:
            return True
        return False
    # Bottom right corner
    if y_index == max_y and x_index == max_x:
        if number < data[y_index - 1][x_index] and number < data[y_index][x_index - 1]:
            return True
        return False

    # Top
    if y_index == 0:
        if number < data[y_index][x_index - 1] \
                and number < data[y_index][x_index + 1] \
                and number < data[y_index + 1][x_index]:
            return True
        return False
    # Bottom
    if y_index == max_y:
        if number < data[y_index][x_index - 1] \
                and number < data[y_index][x_index + 1] \
                and number < data[y_index - 1][x_index]:
            return True
        return False
    # Left
    if x_index == 0:
        if number < data[y_index - 1][x_index] \
                and number < data[y_index + 1][x_index] \
                and number < data[y_index][x_index + 1]:
            return True
        return False
    # Right
    if x_index == max_x:
        if number < data[y_index - 1][x_index] \
                and number < data[y_index + 1][x_index] \
                and number < data[y_index][x_index - 1]:
            return True
        return False
    # Inner
    if number < data[y_index - 1][x_index] \
            and number < data[y_index + 1][x_index] \
            and number < data[y_index][x_index - 1] \
            and number < data[y_index][x_index + 1]:
        return True
    return False


def main():
    data = import_data()
    count = 0
    for y_index, y in enumerate(data):
        for x_index, number in enumerate(y):
            if is_minimum(data, number, y_index, x_index):
                count += number + 1
    print(f'Part 1: Reusult = {count}')


if __name__ == "__main__":
    main()
