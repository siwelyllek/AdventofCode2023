import re
import math

with open("./Day 6/input.txt", "r") as f:
    input = f.read()

# input.txt describes 3 races
#     This document describes three races:

# The first race lasts 7 milliseconds. The record distance in this race is 9 millimeters.
# The second race lasts 15 milliseconds. The record distance in this race is 40 millimeters.
# The third race lasts 30 milliseconds. The record distance in this race is 200 millimeters.

# using regex extract the time and distances of the races (they are seperated by spaces)
def extract_race_details(input):
    lines = input.strip().split("\n")
    # using regex find all the numbers in the first line and add them to the times list
    times = re.findall(r'\d+', lines[0])
    # using regex find all the numbers in the second line and add them to the distances list
    distances = re.findall(r'\d+', lines[1])

    # make times and distances ints
    times = [int(i) for i in times]
    distances = [int(i) for i in distances]

    race_details = list(zip(times, distances))
    return race_details

def part1(input):
    races = extract_race_details(input)
    results = []

    for race in races:
        time, record_distance = race
        holding_times = []
        for i in range(1, time + 1):
            speed = i
            distance = speed * (time - i)
            if distance > record_distance:
                holding_times.append(i)
        results.append(holding_times)

    # count the number of items in each list
    results = [len(i) for i in results]
    # multiply them together
    results = math.prod(results) 
        
    return results

    





print('Races', part1(input))
