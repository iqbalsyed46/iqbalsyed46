import random
randnumber=random.randint(1,100)
userguess=None
guesses=0
while(userguess!=randnumber):
    userguess=int(input("enter the number"))
    guesses+=1
    if (userguess==randnumber):
        print("you guessed right ")
    else:
        if(userguess>randnumber):
            print(' you guessed worong ..please guess samll value')
        else:
            print(" you guessed worong.....please guess large number")
print(f"you guessed the number in {guesses}")