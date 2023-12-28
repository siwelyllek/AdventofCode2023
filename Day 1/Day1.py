# Open the input file
with open('./Day 1/input.txt', 'r') as file:
    total_sum = 0

    # Read each line from the file
    for line in file:
        line = line.strip()

        #find the first instance of a number in the string for the line
        first_digit = line[line.find(next(filter(str.isdigit, line)))]

        #find the last instance of a number in the string for the line
        #reverse the string to find the last instance
        line = line[::-1]
        last_digit = line[line.find(next(filter(str.isdigit, line)))]

        # concatenate  the first and last digits into a string
        first_digit = str(first_digit)
        last_digit = str(last_digit)
        line_sum = first_digit + last_digit
        
        # convert the string to an integer
        line_sum = int(line_sum)

        # add the integer to the total sum
        total_sum += line_sum

        

    # Print the final sum
    print("Total sum:", total_sum)
