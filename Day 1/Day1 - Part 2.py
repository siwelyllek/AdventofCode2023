# regex
import re

first_total = 0
total = 0


def to_num(num):
    # Dictionary to pair strings to numbers
    word_dict = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8',
                 'nine': '9'}
    if num in word_dict.keys():
        final_num = word_dict.get(num)
        return final_num
    else:
        return str(num)


# Part 2
def extract_nums(line):
    numbers = re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine',line)
    for item in numbers:
        # Addresses strings tied together
        num = to_num(item)
        new_sub = item[0] + num + item[-1]
        # print(new_sub)
        line = re.sub(item,new_sub,line)
    numbers = re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', line)
    if len(numbers) == 1:
        number = to_num(numbers[0])
        value = int(number + number)
        return value
    else:
        front = to_num(numbers[0])
        back = to_num(numbers[-1])
        value = int(front + back)
        # print(value)
        return value

with open('./Day 1/input.txt','r') as f:
    for line in f:
        total += extract_nums(line)
# Part 2 solution
print(total)