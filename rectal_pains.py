def read_input():
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
    nums = read_input()
    for num in nums:
        diff = 2020 - num
        if diff in numSet:
            return diff * num
        else:
            numSet.add(num)
    return -1