# what is the fewest number of cubes of each color that could have been in the bag to make the game possible?

# Again consider the example games from earlier:

# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
# In game 1, the game could have been played with as few as 4 red, 2 green, and 6 blue cubes. If any color had even one fewer cube, the game would have been impossible.
# Game 2 could have been played with a minimum of 1 red, 3 green, and 4 blue cubes.
# Game 3 must have been played with at least 20 red, 13 green, and 6 blue cubes.
# Game 4 required at least 14 red, 3 green, and 15 blue cubes.
# Game 5 needed no fewer than 6 red, 3 green, and 2 blue cubes in the bag.
# The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together. The power of the minimum set of cubes in game 1 is 48. In games 2-5 it was 12, 1560, 630, and 36, respectively. Adding up these five powers produces the sum 2286.


def check_game(game):
    # save the game number for later
    game_number = game[0]
    game[0] = game[0].split(':')[1]
    red = 0
    green = 0
    blue = 0
    for hand in game:
        
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
                redi = int(cube[0])
                if redi > red:
                    red = redi
                
                # print('Red: ' + str(red))
            elif cube[1] == 'green':
                greeni = int(cube[0])
                if greeni > green:
                    green = greeni
                # print('Green: ' + str(green))
                    
            elif cube[1] == 'blue':
                bluei = int(cube[0])
                if bluei > blue:
                    blue = bluei
                # print('Blue: ' + str(blue))
            else:
                print('error')

    # here i need to know the minimum number of cubes of each color that could have been in the bag to make the game possible
    gn = game_number.split(' ')
    gn = gn[0] + ' ' + gn[1]
    print(str(gn))
    print('Red: ' + str(red))
    print('Green: ' + str(green))
    print('Blue: ' + str(blue))
    # print newline
    print()
    
    # return the power of the game
    power = red * green * blue

    return power
        
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


