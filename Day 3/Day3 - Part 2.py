# input.txt has 140 lines by 140 characters
# i need to determine which numbers are next to a symbol. '.' does not count as a symbol

import re

def find_symbols(lines):
#remove \n from each line
    list_of_symbols = []
    for i in range(len(lines)):
        lines[i] = lines[i].replace("\n", "")
        


         # find all non-digit and non-dot characters
        for j, char in enumerate(lines[i]):
            if re.match(r'[^0-9.]', char):
                # append the symbol along with its coordinates (i, j)
                list_of_symbols.append((char, i, j))
        
    # print(list_of_symbols)
    return list_of_symbols

def find_numbers(lines):
    #remove \n from each line
    list_of_numbers = []
    for i in range(len(lines)):
        lines[i] = lines[i].replace("\n", "")
        j = 0
        while j < len(lines[i]):
            if lines[i][j].isdigit():
                number = lines[i][j]
                coords = [(i, j)]  # start a new list of coordinates for this number
                while j + 1 < len(lines[i]) and lines[i][j + 1].isdigit():
                    j += 1
                    number += lines[i][j]
                    coords.append((i, j))  # add this coordinate to the list
                list_of_numbers.append((int(number), coords))
            j += 1
    return list_of_numbers
        
def main():
    #open file and seperate into lines
    with open("./Day 3/input.txt", "r") as file:
        lines = file.readlines()
        symbols = find_symbols(lines)
        numbers = find_numbers(lines)
        # print(symbols)
        print(numbers)

   # find all '*' symbols where they are next to exactly two numbers in all 8 directions
    gear_ratios = []
    for symbol, sx, sy in symbols:
        if symbol == '*':  # check if the symbol is '*'
            adjacent_numbers = []
            for number, coords in numbers:
                for x, y in coords:
                    if (abs(x - sx) <= 1 and abs(y - sy) <= 1):
                        if number not in adjacent_numbers:
                            adjacent_numbers.append(number)
            if len(adjacent_numbers) == 2:
                gear_ratio = adjacent_numbers[0] * adjacent_numbers[1]
                gear_ratios.append(gear_ratio)
    print(sum(gear_ratios))
            
if __name__ == "__main__":
    main()





   
    
   

    




