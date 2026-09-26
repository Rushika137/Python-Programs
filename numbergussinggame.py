import random
number=random.randint(1,100)

print("you have 3 chances to guess the number.")

for i in range(3):
    guess=int(input("guess your number:"))
    if guess>number:
        print("its too high")
    elif guess<number:
        print("its too low")
    else: 
        print("you won")
        break

if guess!=number:
 print("you lost")
 print("the number is ",number)
