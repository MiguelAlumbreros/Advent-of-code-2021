from dataclasses import dataclass


@dataclass
class NumberMappings:
    number_0: int = 6
    number_1: int = 2
    number_2: int = 5
    number_3: int = 5
    number_4: int = 4
    number_5: int = 5
    number_6: int = 6
    number_7: int = 3
    number_8: int = 7
    number_9: int = 6


@dataclass
class NumberChecks:
    number_0: bool = False
    number_1: bool = False
    number_2: bool = False
    number_3: bool = False
    number_4: bool = False
    number_5: bool = False
    number_6: bool = False
    number_7: bool = False
    number_8: bool = False
    number_9: bool = False


def import_data():
    with open("day8_input.txt") as f:
        lines = f.readlines()
    lines_parsed = [line.split('\n') for line in lines]
    data_signal_parameters = []
    data_output_value = []
    for line in lines_parsed:
        signal_parameters = []
        output_value = []
        delimeter = False

        line_temp = line[0].split()
        for item in line_temp:
            if not delimeter:
                signal_parameters.append(item)
            elif delimeter:
                output_value.append(item)
            if item == '|':
                delimeter = True

        data_signal_parameters.append(signal_parameters)
        data_output_value.append(output_value)

    # Remove delimiter
    for item in data_signal_parameters:
        for index, item_in_list in enumerate(item):
            if item_in_list == '|':
                item.pop(index)
    result = zip(data_signal_parameters, data_output_value)

    return result


def count_unique_digits(data):
    count = 0
    unique_numbers_lenghts = [2, 4, 3, 7]
    for item in data:
        data_output_value = item[1]
        for item_in_list in data_output_value:
            for unique in unique_numbers_lenghts:
                if len(item_in_list) == unique:
                    count += 1
                    break
    return count


def main():
    data = import_data()
    result = count_unique_digits(data)
    print(result)


if __name__ == "__main__":
    main()
