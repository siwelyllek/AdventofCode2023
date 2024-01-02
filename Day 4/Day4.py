def clean_line(line):
    line = line.replace("  ", " ")
    line = line.replace(" ", ",")   
    line = line.replace(",,", ",")
    line = line.replace(",|,", "|")
    line = line.replace("Card,", "Card ")
    line = line.replace(":,", ":")
    return line

def open_file():
    with open("./Day 4/input.txt", "r") as file:
        lines = file.readlines()
        # remove all whitespace and newlines
        lines = [line.strip() for line in lines]
    return lines

# one winning number = 1 points, two winning numbers = 2 points, three winning numbers = 4 points, etc
def calculate_score(winning_numbers):
    if len(winning_numbers) == 0:
        return 0
    else:
        return 2 ** (len(winning_numbers) - 1)


def main():
    score = 0

    lines = open_file()    
    for line in lines:
        winning_numbers = []
        winning_numbers_final = []

        # remove all whitespace and newlines including the ones in the middle of the string
        line = clean_line(line)
        
        # split the string into 3 parts, the card number, the numbers on the card, and the winning numbers
        # the card number is everything before the :
        # the winning numbers are everything between the : and the |
        # the numbers you have are everything after the |
        card_number, numbers = line.split(":")
        numbers = numbers.split("|")
        winning_numbers = numbers[0]
        your_numbers = numbers[1]

        # split the winning numbers into a list
        winning_numbers = winning_numbers.split(",")
        # split your numbers into a list
        your_numbers = your_numbers.split(",")

        # check if you have any winning numbers
        # if you do, add the card number to the list of winning cards
        
        for number in your_numbers:
            if number in winning_numbers:
                winning_numbers_final.append(number)  
        
        score += calculate_score(winning_numbers_final)

    print(score)


    # print(winning_numbers)

if __name__ == "__main__":
    main()