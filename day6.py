from dataclasses import dataclass


@dataclass
class Fish:
    NEW_AGE = 8
    RESET_AGE = 6


def import_data():
    with open('day6_input.txt', 'r') as f:
        data = f.readlines()[0]
    return data


def parser(sample):
    sample_temp = sample.split(',')
    return [int(x) for x in sample_temp]


def produce_list(input_data, total_days):
    for k in range(total_days):
        print(k)
        append = 0
        for i, fish in enumerate(input_data):
            # Check if 0
            if fish == 0:
                input_data[i] = Fish.RESET_AGE
                append += 1
            else:
                input_data[i] -= 1
        if not append == 0:
            [input_data.append(Fish.NEW_AGE) for _ in range(append)]
    return input_data


def main():
    sample = '3,4,3,1,2'
    input_data = parser(import_data())
    # input_data = parser(sample)

    total_days = 80
    fish_list = produce_list(input_data, total_days)

    print(f'Result = {len(fish_list)}')


if __name__ == '__main__':
    main()
