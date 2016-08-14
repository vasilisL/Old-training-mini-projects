#Guessing game

import random

user_name = raw_input("What is your name?? ")
number = random.randint(1, 100)
previous_guesses = []
max_tries = raw_input("How hardcore player are you %s? on a scale of 1-10 with 1 being the most hardcore " % user_name)

while True:
    try:
        int(max_tries)
        break
    except:
        print "That is not a number..."
        print "Are you trying to cheat???Very well mr %s you will get just 1 shot to pick the correct number!!!" % user_name
        max_tries = 1

if int(max_tries) not in range(1, 11):
    print "Lol trying to cheat???Very well mr %s you will get just 1 shot to pick the correct number!!!" % user_name
    max_tries = 1


def guessing_game(max_tries, number):
    tries = 0
    while tries < int(max_tries):
        print "Tries left: ", int(max_tries) - tries
        user_guess = raw_input("Can you guess the number i have in my mind %s it is somewhere between 1 and 100??? " % user_name)
        while True:
            try:
                int(user_guess)
                break
            except:
                print "That is not even a number.."
                user_guess = raw_input("Pick a number... ")

        if user_guess in previous_guesses:
            print "You allready said that number!"
            tries -= 1
        else:
            previous_guesses.append(user_guess)

        if int(user_guess) == number:
            print "Wow nice guess %s !!!!" % user_name
            break

        elif int(user_guess) < 1 or int(user_guess) > 100:
            print "Lol i allready told you %s the number is between 1 and 100.. you just wasted a try.." % user_name
            tries += 1

        elif int(user_guess) > number:
            if int(user_guess) - number < 3:
                print "close... you need to go a bit lower..."
            else:
                print "Too high"
            tries += 1

        elif int(user_guess) < number:
            if number - int(user_guess) < 3:
                print "close... you need to go a bit higher"
            else:
                print "Too low..."
            tries += 1
    else:
        print "You loose.. number was", number


guessing_game(max_tries, number)
