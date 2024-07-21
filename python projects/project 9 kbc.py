print("........................WELCOME TO THE .....................\nKOAN BANEGA KARODPAHTI")
q1=["Question no.1 :- what is the capital of india"]
print(q1)
ans=["your options are  :""(a) delhi","(b) culcutta" ,"(c)mumbai","(d)hyderabad"]
print(ans)
ans1=input("choose the options :")

if (ans1=="a"):
    print("your ans is correct\n you have won! 1000 rupees")
else:
    print("your ans is wrong\nsoory...... you are out of the game")


q2=["Question no 2\n  :-  who is the richest actor in the world"]
print(q2)
ans2=["your options are :-""(a)iqbal","(b)robert d juinor","(c)awaiz","(d)adnan"]
print(ans2)
b=input("choose the option :")
if (b=="a"):
    print("your ans is correct \n you have won ! 2000 rupees")

else:
    print("your ans is wrong/nsorry.... you are out from the game")


q3=["Question no 3:-\nwho is the richest person in Asia"]
print(q3)
ans3=["your options are  :-""(a)ambani","(b)iqbal","(c)awaiz","(d)bezos"]
print(ans3)
c=input("choose the option :")
if (c=="b"):
    print("you have answered right!\n you have won!  5000/- rupees")
else:
    print("your ans is wrong\n soory...you are out from the game....")

list=[ans1,b,c]

if (list=="a"=="a"=="b"):
    print("................you are the winner of KBC 2023...............")

else:
    print("you are a looser")