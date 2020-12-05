'''
Day 1
'''
def read_input_1():
    """
    TODO: buy alfred deoderant
    """
    lines = []
    with open("input.txt") as file:
        for line in file.readlines():
            lines.append(int(line.strip()))
    return lines

def find_product_of_two_nums():
    numSet = set()
    nums = read_input_1()
    for num in nums:
        diff = 2020 - num
        if diff in numSet:
            return diff * num
        else:
            numSet.add(num)
    return -1

'''
Day 2 part 1
'''
def find_bad_passwords():
    lines = []
    finalcount = 0
    with open("day2_input.txt") as file:
        for line in file.readlines():
            values = line.split()
            mymin = int(values[0].split('-')[0])
            mymax = int(values[0].split('-')[1])
            myletter = values[1][0]
            string = values[2]
            count = 0
            for c in string:
                if myletter == c:
                    count += 1
            if count >= mymin and count <= mymax:
                finalcount += 1
    return finalcount

'''
Day 2 part 2
'''
def find_bad_passwords_again():
    lines = []
    finalcount = 0
    with open("day2_input.txt") as file:
        for line in file.readlines():
            values = line.split()
            index_1 = int(values[0].split('-')[0]) - 1
            index_2 = int(values[0].split('-')[1]) - 1
            myletter = values[1][0]
            string = values[2]

            count = 0
            if index_1 < len(string) and string[index_1] == myletter:
                count += 1
            if index_2 < len(string) and string[index_2] == myletter:
                count += 1
            if count == 1:
                finalcount += 1
    return finalcount

    '''
    Day 3 part 1
    '''
def read_input_toboggan_sledding():
    matrix = []

    with open("day3_input.txt") as f:
        for line in f.readlines():
            matrix.append(line.strip())
    return matrix

def toboggan_sledding():
    matrix = read_input_toboggan_sledding()

'''
Day 5 part 1
'''
def airplane_tickets_part_1():
    highestId = 0
    with open("day5_input.txt") as file:
        for line in file.readlines():
            front_back = line.strip()[:-3]
            left_right = line.strip()[-3:]

            fb_lo = 0
            fb_hi = 127
            for c in front_back:
                fb_med = (fb_lo + fb_hi) // 2
                if c == 'F':
                    fb_hi = fb_med
                if c == 'B':
                    fb_lo = fb_med + 1
            lr_lo = 0
            lr_hi = 7
            for c in left_right:
                lr_med = (lr_lo + lr_hi) // 2
                if c == 'L':
                    lr_hi = lr_med
                if c == 'R':
                    lr_lo = lr_med + 1
            highestId = max(highestId, (fb_lo * 8) + lr_lo)
    print(highestId)

'''
Day 5 part 2
'''
def airplane_tickets_part_2():
    mylist = []
    highestId = 0
    with open("day5_input.txt") as file:
        for line in file.readlines():
            front_back = line.strip()[:-3]
            left_right = line.strip()[-3:]

            fb_lo = 0
            fb_hi = 127
            for c in front_back:
                fb_med = (fb_lo + fb_hi) // 2
                if c == 'F':
                    fb_hi = fb_med
                if c == 'B':
                    fb_lo = fb_med + 1
            lr_lo = 0
            lr_hi = 7
            for c in left_right:
                lr_med = (lr_lo + lr_hi) // 2
                if c == 'L':
                    lr_hi = lr_med
                if c == 'R':
                    lr_lo = lr_med + 1
            myId = (fb_hi * 8) + lr_hi
            mylist.append(myId)
    mylist.sort()
    prevnum = mylist[0]
    for num in mylist[1:]:
        if num != prevnum + 1:
            return num - 1
        else:
            prevnum = num



