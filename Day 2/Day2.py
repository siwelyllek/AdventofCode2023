# given the following rules for a bag of cubes containing 3 colors:

# I would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?
# input.txt contains all the games played. I would like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

# The file contains 1000 lines formatted as follows:
# Game 1: 7 red, 8 blue; 6 blue, 6 red, 2 green; 2 red, 6 green, 8 blue; 9 green, 2 red, 4 blue; 6 blue, 4 green

max_red = 12
max_green = 13
max_blue = 14


def check_max(color, max_color):
    if color > max_color:
        return False
    else:
        return True

def check_game(game):
    # save the game number for later
    game_number = game[0]
    game[0] = game[0].split(':')[1]
    
    for hand in game:
        red = 0
        green = 0
        blue = 0
        hand = hand.split(',')
        # trim whitespace
        hand = [x.strip() for x in hand]
        # print(hand)
        # check each set of cubes and see if it is valid
        for cube in hand:
            # trim whitespace
            cube = cube.strip()
            cube = cube.split(' ')
            # trim whitespace
            cube = [x.strip() for x in cube]

            if cube[1] == 'red':
                red = int(cube[0])
                # print(red)
            elif cube[1] == 'green':
                green = int(cube[0])
                # print(green)
            elif cube[1] == 'blue':
                blue = int(cube[0])
                # print(blue)
            else:
                print('error')

# if any of the colors are greater than their max, return for that whole game
        if not check_max(red, max_red):
            return False
        if not check_max(green, max_green):
            return False
        if not check_max(blue, max_blue):
            return False
        
    # not sure if the 52 is correct or not as it might just be calculating based on the first hand
    # spliut the game number and return the sum of the game numbers
    game_number = game_number.split(' ')
    game_number = game_number[1]
    # remove the colon
    game_number = game_number[:-1]
    game_number = int(game_number)
    # print(game_number)
    return game_number
    

def check_games(games):
    possible_games = []
    for game in games:
            possible_games.append(check_game(game))
    return possible_games


def main():
    games = []
    with open('./Day 2/input.txt', 'r') as f:
        for line in f:
            game = line.split(';')
            
            games.append(game)
            
    # print(games)
    possible_games = check_games(games)
    
    # sum the possible games
    print(sum(possible_games))
    

if __name__ == '__main__':
    main()








