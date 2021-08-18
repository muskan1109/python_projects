# Program name: zambales.py

import random

# storing zambales characters in a list
ZAMBALES_CHARS = ["I", "II", "III", "X", "+", "#"]

def one_time(i):
    '''
    This function is called for each time the player throws two dice in a game 
    and returns if a double was thrown. 

    This function is called when the user wants to play a game. To play one game
    fully, this function has to be called 5 times. First it generates 2 random 
    numbers. Then it prints out the characters that corresponds with the numbers
    generated. It also checks if the numbers generated are the same. If they are
    same, it prints out "-- double" next to the charcaters. It also returns 1 if
    the numbers generated are the same, otherwise it returns 0. This value is 
    used to keep track of total number of doubles produced. 

    Parameters
    ----------
    i : int
        This is a counter that tells at exactly which iteration the loop is at. 

    Returns
    -------
    int
        The returned value indicates if a double was made or not. 1 means double
        was made, 0 means double was not made. 
    '''
    face_1 = random.randint(1,6) # random number between 1 and 6
    face_2 = random.randint(1,6) # random number between 1 and 6

    # printing result when the dice is rolled    
    print("[{}] {}, {} {} ".format(i, ZAMBALES_CHARS[face_1 - 1],\
                            ZAMBALES_CHARS[face_2 - 1], 
                            "-- double" if face_1 == face_2 else ""))

    # if user gets a double, 1 is returned (to increment total doubles) 
    return 1 if face_1 == face_2 else 0


def results(num_of_games, total_games_won, total_doubles, name_of_user):
    '''
    This function prints out the statistical results of all the games played.

    This function takes in 4 parameters and prints out the statistical result of
    all the games played by the user. First it prints out the total number of 
    games played by the user. Next, it prints out the total number of games won 
    by the user. After that it prints out the total number of doubles made by 
    the user in all the games and then prints out the average number of doubles 
    made per game. Lastly, it prints out a goodbye statement to the user.

    Parameters
    ----------
    num_of_games : int 
        This parameter is for the total number of games played.

    total_games_won : int
        This parameter is for the total number of games won.

    total_doubles : float
        This parameter is for the total number of doubles made.

    name_of_user : String
        This parameter is for the name of the user. 
    '''

    print("\nResults:\n========")
    print("Total number of games: {}.".format(num_of_games))
    print("Total games won: {}.".format(total_games_won))
    print("Total doubles: {}.".format(total_doubles))
    print("Average doubles per game: {}\n".format(0 if num_of_games == 0 \
                                            else total_doubles / num_of_games))
    print("\nBye, bye {}".format(name_of_user))


def main():
    print("===================\nWelcome to Zambles!\n===================")

    # asking user to enter name
    name_of_user = input("Enter your name: ")

    print("\nGreetings {}\n\nRoll the die 5 times,".format(name_of_user), \
          "see if you can throw a double.\n")

    # num_of_games holds the total number of games played
    # total_doubles holds the total number of doubles made 
    # total_games_won holds total number of games won
    num_of_games = 0; total_doubles = 0; total_games_won = 0

    # infinite loop to run program
    while True:
        
        # ask if user wants to play game
        play_game_answer = input(str(name_of_user) + \
                                 ", do you want to play the game (y/n)? ")

        # checking if user wants to play game 
        if play_game_answer in ['Y', 'y']:
            # increment total number of games by 1
            num_of_games += 1 
            print("\nPLAYING!!!\n\nGame " + str(num_of_games))

            # prev_total_doubles holds the total number of doubles made in all
            # the previous games
            prev_total_doubles = total_doubles

            # for loop to roll the dice 5 times 
            for i in range(1, 6): total_doubles += one_time(i)

            # print number of doubles made in current game
            print("\n{} double{}\n".format(total_doubles - prev_total_doubles, \
                                "" if total_doubles - prev_total_doubles == 1 \
                                    else "s"))

            # checking if any doubles were made in the current game
            # if so increment total_games_won by 1
            if total_doubles != prev_total_doubles:
                total_games_won += 1
            continue
        break # breaking out of infinte while loop if user does not want to play 
   
    # calling results() function to print out results 
    results(num_of_games, total_games_won, total_doubles, name_of_user) 

if __name__ == "__main__":
    main()