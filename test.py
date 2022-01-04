def diagram_parser():
    with open('day5_input.txt', 'r') as f:
        lines = f.readlines()
    lines_parsed = [line.strip().split('\n') for line in lines]
    output = []
    for line in lines_parsed:
        output.append(line[0])
    return output

diagram_parser()