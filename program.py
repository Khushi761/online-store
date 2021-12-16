#Steps 
#1 - Guessing a number between 1 and 100 (range) 
#2 - Ask the user for a number
#3 - Compare both values
#4 - Outputting a sentence according to the value entered by the user
#5 - Repeat the program until the numbers are the same

import random

guess = int(input("I am thinking of a number between 1-100. Can you guess what it is?")) 

amount = random.randint(1,100)  

while guess != amount:
    if guess > amount:
        print("No, the number i am thinking of is higher than", amount,"Can you guess what it is?")
    guess = int(input())

        
        