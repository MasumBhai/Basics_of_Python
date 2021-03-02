import math as mathematics
import random
import time
import sys

try:
    print(math.factorial(5))  # it will gve error
except Exception as err:
    print(err)
finally:
    print(mathematics.factorial(5))
    # uncomment it
# help(mathematics)  # here if i pass my_own_module then it will be nice but feeling lazy

""" Python Modules """
import random
import time



def main():
    start_time = time.time();
    print('\nWelcome to the guissing game!!')
    print("Disclaimer: You have been given 5 chances,use wisely")
    random_number = random.randint(1, 50)
    guessing_chance = 5
    total_time = None
    while True:
        guessing_number = int(input('\nEnter your guess(1 to 50): '))
        if guessing_number < random_number:
            print('Please wait for the result....')
            time.sleep(2)
            print('Your number is less than Actual number')
            guessing_chance -= 1
            print('Guessing chance remaining: ', guessing_chance)
        elif guessing_number > random_number:
            print('Please wait for the result')
            time.sleep(2)
            print('Your number is greater than Actual number')
            guessing_chance -= 1
            print('Guessing chance remaining: ', guessing_chance)
        elif guessing_number == random_number:
            # print('\nPlease wait for the result')
            time.sleep(2)
            end_time = time.time()
            total_time = end_time - start_time
            print("\n###########################")
            print('##Congrats##')
            print("No matter what,you lost your precious {} seconds!!Ha Ha..".format(mathematics.ceil(total_time)))
            print("##Victory for developer MasumBhai!!")
            print("###########################\n")
            break
        if guessing_chance == 0:
            time.sleep(2)
            end_time = time.time();
            total_time = end_time - start_time
            print("\n###########################")
            print('##Yes!!Loser!!!##')
            print("Actual number was:", random_number)
            print("Bad Luck,mehhh (just imagine robot movie scene)")
            print("Also you lost your precious {} seconds from your valuable life".format(mathematics.ceil(total_time)))
            print("###########################\n")
            break


if __name__ == "__main__":
    main()
    while True:
        ans = input("Do you want to play again?(Y/N) : ")
        if ans == 'y' or 'Y':
            main();
        elif ans == 'n' or 'N':
            time.sleep(1)
            sys.exit("Terminating programme...")
            break
        else:
            time.sleep(1)
            print("\nWrong choise,try again plz")
