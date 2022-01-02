# sample
print('PART 1:')
def split_number(number):
    return [char for char in number]
with open('day3_input.txt','r') as fil:
    lines = fil.readlines()
    lines_parsed = [line.strip().split('\n') for line in lines]
    lines_parsed_2 = []
    for line in lines_parsed:
        lines_parsed_2.append(line[0])
# sample = ['00100',
#           '11110',
#           '10110',
#           '10111',
#           '10101',
#           '01111',
#           '00111',
#           '11100',
#           '10000',
#           '11001',
#           '00010',
#           '01010']
# lines_parsed_2 = sample
sample_char = [split_number(number) for number in lines_parsed_2]

bit_0_count = 0
bit_1_count = 0
gamma = ''
epsylon = ''

for i in range(len(lines_parsed_2[0])):
    for item in sample_char:
        if item[i] == '0':
            bit_0_count +=1
        else:
            bit_1_count +=1
    if bit_0_count > bit_1_count:
        gamma += '0'
        epsylon += ('1')
    else:
        gamma += ('1')
        epsylon += ('0')
    bit_0_count = 0
    bit_1_count = 0
# print(gamma)
gamma_decimal = int(gamma,2)
print(f'Gamma = {gamma_decimal}')
# print(epsylon)
epsylon_decimal = int(epsylon,2)
print(f'Gamma = {epsylon_decimal}')

print(f'Power consumption = {gamma_decimal * epsylon_decimal}')

##
# PART 2
##
print()
print('PART 2:')
data = lines_parsed_2
def zero_or_one(data, index) -> int:
    bit_0_count = 0
    bit_1_count = 0
    for item in data:
        if item[index] == '0':
            bit_0_count +=1
        else:
            bit_1_count +=1
    if bit_0_count > bit_1_count:
        return '0'
    else:
        return '1'

data = sample_char   
index = 0
while len(data)>1:
    first_bit = zero_or_one(data,index) 
    data_temp = []
    for item in data:
        if item[index] == first_bit:
            data_temp.append(item)
    data = data_temp
    index += 1
oxygen = ''
for item in data[0]:
    oxygen += item
print(f'Oxygen = {int (oxygen, 2)}')

data = sample_char   
index = 0
while len(data)>1:
    first_bit = zero_or_one(data,index) 
    data_temp = []
    for item in data:
        if not item[index] == first_bit:
            data_temp.append(item)
    data = data_temp
    index += 1
co2 = ''
for item in data[0]:
    co2 += item
print(f'CO2 = {int (co2, 2)}')

print(f'Life support rating = {int(oxygen,2 ) * int(co2, 2)}')