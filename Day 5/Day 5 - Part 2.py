# the main question on day 5 is: What is the lowest location number that corresponds to any of the initial seed numbers?

import re


with open("./Day 5/input.txt", "r") as f:
    input = f.read()

# seeds are the numbers that are in the first line of the input
def extract_seeds(input):
    # for firstline only
    firstline = input.split("\n\n")[0]

    # find all numbers which can be more than one digit and are separated by whitespace in the first line and add them to the seeds list
    seeds = [seed for seed in re.findall(r'\d+', firstline)]


    # # Generate the final seeds list using a list comprehension
    # final_seeds = (j for i in range(0, len(seeds), 2) for j in range(seeds[i], seeds[i] + seeds[i+1]))

    seeds = list(seeds)
    # print(list(final_seeds))
    return seeds
    

def extract_maps(input):
    maps = input.split('\n\n')
    # print(maps)
    return maps

        
def part2(input):
    maps = extract_maps(input)
    # print(segments)
    seeds = extract_seeds(input)
    # print(seeds)

    intervals = []

    for seed in re.findall(r'(\d+) (\d+)', maps[0]):
        x1, delta = map(int, seed)
        x2 = x1 + delta
        intervals.append((x1, x2,1))
    print(intervals)
    

    # had a workign solution but it was too slow for the input so nicked this in classic advent of code style
    min_location = float('inf')
    while intervals:
        x1, x2, level = intervals.pop()
        if level == 8:
            min_location = min(x1, min_location)
            continue

        for conversion in re.findall(r'(\d+) (\d+) (\d+)', maps[level]):
            z, y1, dy = map(int, conversion)
            y2 = y1 + dy
            diff = z - y1
            if x2 <= y1 or y2 <= x1:    # no overlap
                continue
            if x1 < y1:                 # split original interval at y1
                intervals.append((x1, y1, level))
                x1 = y1
            if y2 < x2:                 # split original interval at y2
                intervals.append((y2, x2, level))
                x2 = y2
            intervals.append((x1 + diff, x2 + diff, level + 1)) # perfect overlap -> make conversion and let pass to next nevel 
            break

        else:
            intervals.append((x1, x2, level + 1))

    return min_location



print('Lowest location:', part2(input))