import random 
random_integer = random.randint(1, 10)
intguess = input
while not  random_integer == intguess:
    print("Guess a number")
    input(int)
if input(int) == intguess:
    print("correct")
    print(random_integer)
else: 
    print("wrong")
    

