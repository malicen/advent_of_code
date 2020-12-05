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
Day 2
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
Day 2
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