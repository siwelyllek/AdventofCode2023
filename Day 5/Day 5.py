# the main question on day 5 is: What is the lowest location number that corresponds to any of the initial seed numbers?

import re

with open("./Day 5/input.txt", "r") as f:
    input = f.read()

# seeds are the numbers that are in the first line of the input
def extract_seeds(input):
    seeds = []

    # for firstline only
    firstline = input.split("\n\n")[0]

    # find all numbers which can be more than one digit and are seperated by whitespace in the first line and add them to the seeds list
    seeds = re.findall(r'\d+', firstline)
    return seeds
    

def extract_maps(input):
    maps = input.split('\n\n')
    return maps

        
def part1(input):
    maps = extract_maps(input)
    # print(segments)
    seeds = extract_seeds(input)
    # print(seeds)

    min_location = float('inf')
    for x in map(int, seeds):
        for seg in maps[1:]:
            for conversion in re.findall(r'(\d+) (\d+) (\d+)', seg):
                destination, start, delta = map(int, conversion)
                print(destination, start, delta)
                if x in range(start, start + delta):
                    x += destination - start
                    break

        min_location = min(x, min_location)

    return min_location



print('Lowest location:', part1(input))