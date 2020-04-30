import random
digits = list(range(10)) 
random.shuffle(digits) 
digits=digits[:3] 
print("Welcome code breaker! Let's see if you can guess my 3 digit number")

ran_num=[i for i in digits]

guess = input("What is your guess? ")

guess=[int(i) for i in guess]

while guess != ran_num:
    if guess[0] == ran_num[0] or guess[1] == ran_num[1] or guess[2] == ran_num[2]:
        print('Match you guessed a correct number in the correct position!')
        guess = input("What is your guess? ")
        guess=[int(i) for i in guess]
    elif guess[0]== ran_num[1] or guess[0]== ran_num[2] or guess[1]== ran_num[0] or guess[1]== ran_num[2] or guess[2]== ran_num[0] or guess[2]== ran_num[1]:
        print('Close you have guessed a correct number but in the wrong positon')
        guess = input("What is your guess? ")
        guess=[int(i) for i in guess]
    elif guess[0] == ran_num[0] and guess[1] == ran_num[1] and guess[2] == ran_num[2]:
        print('You guessed it! ')
    else:
        print('Nope you have not guessed any of the numbers correctly!')
        guess = input("What is your guess? ")
        guess=[int(i) for i in guess]
