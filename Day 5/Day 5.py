# the main question on day 5 is: What is the lowest location number that corresponds to any of the initial seed numbers?

import re

with open("./Day 5/input-test.txt", "r") as f:
    input = f.read()

# seeds are the numbers that are in the first line of the input
def extract_seeds(input):
    seeds = []

    # for firstline only
    firstline = input.split("\n")[0]

    # find all numbers which can be more than one digit and are seperated by whitespace in the first line and add them to the seeds list
    seeds = re.findall(r'\d+', firstline)
    return seeds
    

def extract_maps(input, first, second):
    maps = []

    # split input into lines
    lines = input.split("\n")

    # in the input find the line that starts with 'first-to-second' and add it to the maps list
    for line in lines:
        if line.startswith(first + "-to-" + second):
            # append the next x lines until the next empty line to the maps list
            for i in range(lines.index(line) + 1, len(lines)):
                if lines[i] == "":
                    break
                else:


                    maps.append(lines[i])
    # turn the maps into a list of lists
    maps = [[int(num) for num in map.split()] for map in maps]

    # print(maps)
    return maps

def process_map(maps):
    # print (map)
    ranges = []
    # for each line in the map
    for line in maps:
        # print(line)
        # if the line is empty then skip it
        if line == []:
            continue
        # if the line is not empty then
        else:
            # set the source_start to the first number in the line
            source_start = line[1]
            # set the source_end to the second number in the line
            source_end = source_start + line[2]
            # set the destination_start to the third number in the line
            destination_start = line[0]
            # set the destination_end to the fourth number in the line
            destination_end = destination_start + line[2]
            
            ranges.append([source_start, source_end, destination_start, destination_end])
    return source_start, source_end, destination_start, destination_end

        
           

def part1(input):
    seeds = extract_seeds(input)
    print('Seeds:',seeds)


    
    maps =[]
    maps.append(extract_maps(input, 'seed', 'soil'))
    maps.append(extract_maps(input, 'soil', 'fertilizer'))
    maps.append(extract_maps(input, 'fertilizer', 'water'))
    # maps.append(extract_maps(input, 'water', 'light'))
    # maps.append(extract_maps(input, 'light', 'temperature'))
    # maps.append(extract_maps(input, 'temperature', 'humidity'))
    # maps.append(extract_maps(input, 'humidity', 'location'))



    new_seeds = seeds.copy()
    for seed in seeds:
        seed = int(seed)
        
        
    # process map isnt working so get this to how you want it then change process map
    for conversion in maps:
        print(conversion,process_map(conversion))
           
                
            
        
            
        # print(destination_start, destination_end, source_start, source_end)
    print(new_seeds)                

    
    # for each seed, check if it is in the range of any of the mappings
   
    # return the lowest location number that corresponds to any of the initial seed numbers
    return min(new_seeds)



print('Lowest location:', part1(input))