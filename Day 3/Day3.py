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
                list_of_symbols.append((char, i+1, j))
        
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
                start_j = j
                while j + 1 < len(lines[i]) and lines[i][j + 1].isdigit():
                    j += 1
                    number += lines[i][j]
                list_of_numbers.append((int(number), i+1, start_j))
            j += 1
    # print(len(list_of_numbers))

    return list_of_numbers
        
def main():
    #open file and seperate into lines
    with open("./Day 3/input.txt", "r") as file:
        lines = file.readlines()
        symbols = find_symbols(lines)
        numbers = find_numbers(lines)
        # print(symbols)
        # print(numbers)

        # add all numbers where any part of the number is next to a symbol in all 8 directions to a list that may contain duplicates
    list_of_numbers = []
    for number, x, y in numbers:
        number_length = len(str(number))
        for symbol, sx, sy in symbols:
            for i in range(number_length):
                if (x == sx and abs(y + i - sy) == 1) or (y + i == sy and abs(x - sx) == 1) or (abs(x - sx) == 1 and abs(y + i - sy) == 1):
                    list_of_numbers.append(number)
                    # print((number, x, y))
                    break
    print(sum(list_of_numbers))
            
if __name__ == "__main__":
    main()





   
    
   

    




