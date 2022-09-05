#random number guess for the user
import random

def guess (x):
    random_number = random.randint(1,x)
    guess =0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print ('Sorry too low, Try again')
        elif guess> random_number:
            print ('Sorry, Too high, Try again')
    
    print (f'Congrats,You have got the right number: {random_number}')
            
guess(10)



#random number guess for the system
def computer_guess (x):
    min_range = 1
    max_range = x
    feedback = ''
    while feedback != 'c':
        if min_range != max_range:
            guess_num = random.randint(min_range,max_range)
        else:
            guess_num = min_range
        feedback = input(f'Is {guess_num} too high (h) or Too min_range (l) or correct(c)')
        if feedback == 'h': 
            max_range = guess_num -1
        elif feedback == 'l':
            min_range = guess_num+1
    print (f'Hoo! Comp has guessed your number {guess_num} right!!')

computer_guess(100)

