file = open('day2_input.txt', 'r')
lines = file.readlines()
lines_parsed = []
for line in lines:
    lines_parsed.append(line.split())

x_pos = 0
z_pos = 0

for line in lines_parsed:
    if line[0] == 'forward':
        x_pos += int(line[1])
    if line[0] == 'up':
        z_pos -= int(line[1])
    if line[0] == 'down':
        z_pos += int(line[1])
print(f'x = {x_pos} , z = {z_pos}')
print(x_pos * z_pos)

##
# PART 2
##

x_pos = 0
z_pos = 0
aim = 0

for line in lines_parsed:
    if line[0] == 'forward':
        x_pos += int(line[1])
        z_pos += aim * int(line[1])
    if line[0] == 'up':
        aim -= int(line[1])
    if line[0] == 'down':
        aim += int(line[1])
print(f'x = {x_pos} , z = {z_pos} , aim =  {aim}')
print(x_pos * z_pos)
