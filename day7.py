def import_data():
    with open("day7_input.txt") as f:
        line = f.readline()
    data_temp = line.split(',')
    data = [int(x) for x in data_temp]
    return data


def optimize_input_pt1(data):
    max_element = max(data)
    fuel_count_list = []
    for hor_pos in range(max_element):
        fuel_count = 0
        for element in data:
            move = abs(element - hor_pos)
            fuel_count += move
        fuel_count_list.append(fuel_count)
    print(fuel_count_list)  # TEST
    return min(fuel_count_list)


def optimize_input_pt2(data):
    max_element = max(data)
    fuel_count_list = []
    for hor_pos in range(max_element):
        fuel_count = 0
        for element in data:
            move = abs(element - hor_pos)
            for inc in range(0, move):
                fuel_count += 1 + inc
                inc += 1
        fuel_count_list.append(fuel_count)
    print(fuel_count_list)  # TEST
    return min(fuel_count_list)


def main():
    # Part 1
    result = optimize_input_pt1(import_data())
    print(f'Result pt1 = {result}')
    ##
    # Part 2
    result = optimize_input_pt2(import_data())
    print(f'Result pt2 = {result}')


if __name__ == "__main__":
    main()
