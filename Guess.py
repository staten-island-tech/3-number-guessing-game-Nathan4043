
#
# import random 
# random_integer = random.randint(1, 10)
# intguess = input
# while not  random_integer == intguess:
#     print("Guess a number")
#     input(int)
# if input(int) == intguess:
#     print("correct")
#     print(random_integer)
# else: 
#     print("wrong") 

# import random 
# random_integer = random.randint(1, 10)
# while True:
#     intguess=int(input("Guess a number 1-10"))
#     if int(input) == intguess:
#         print("correct")
#         print(random_integer)
#     else: 
#         print("wrong")

# import random 
# random_integer = random.randint(1, 10)
# while True:
#     intguess=int(input("Guess a number 1-10:"))
#     if  random_integer == intguess:
#         print("correct")
#         print(random_integer)
#         break
#     else: 
#         print("wrong")

# import random 
# random_integer = random.randint(1, 10)
# while True:
#     intguess=int(input("Guess a number 1-10:"))
#     if  random_integer == intguess:
#         print("correct")
#         print(random_integer)
#         break
#     else: 
#         print("wrong")

# import random 
# random_integer = random.randint(1, 10)
# Guess=0
# while True:
#     Guess=int(input("Guess Number"))
#     if random_integer > Guess:
#         print("is less than")
#     if random_integer < Guess:
#         print("is greater than")
#     if random_integer == Guess:
#         print("Correct!")
#         break

import random 
random_integer = random.randint(1, 10)
Guess=0
history = []
while True:
    Guess=int(input("Guess Number"))
    history.append (Guess)
    if random_integer > Guess:
        print("is less than")
    else:
        print("wrong")
        print(history)
    if random_integer < Guess:
        print("is greater than")
    else:
        print("wrong")
        print(history)
    if random_integer == Guess:
        print("Correct!")
        print("History",history)
        break




