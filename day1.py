file = open('day1_input.txt','r')
lines = file.readlines()
lines_parsed = []
for line in lines: lines_parsed.append(int(line))

prev = lines_parsed[0]
counter = 0
for line in lines_parsed[1:]:
    if line > prev: 
        counter+=1
    prev = line
print(counter)

###
# PART 2
###
# Sample input

sample = [199,
          200,
          208,
          210,
          200,
          207,
          240,
          269,
          260,
          263]
# lines_parsed = sample

max_index = len(lines_parsed)

counter_pt2 = 0
# sum_1 = lines_parsed[0] + lines_parsed[1] + lines_parsed[2]
for i, line in enumerate(lines_parsed[:max_index-3]):
    sum_1 = line + lines_parsed[i+1] + lines_parsed[i+2]
    # print(f'first numer: {sum_1}')
    check = False
    sum_2 = lines_parsed[i+1] + lines_parsed[i+2] + lines_parsed[i+3]
    # print(f'second numer: {sum_2}')
    if sum_2 > sum_1:
        counter_pt2+=1
        check = True
    # if check:
    #     print('LARGER')
    # print(f'count:{counter_pt2}')
    # print()    
print(counter_pt2)