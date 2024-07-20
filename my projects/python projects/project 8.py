import random
def getwin(comp,you):
     if comp==you:
         return None
     elif comp=='p':
        if you=='s':
            return False
        elif you=='r':
            return True
     elif comp=='s':
            if you=='r':
                return False
            elif you=='p':
                return True
     elif comp=='r':
            if you=='s':
                return False
            elif you=='r':
                return True
        
print("compTurn :Paper(p) Scissor(s) Rock(r)?")
randNo=random.randint(1,3)
if randNo==1:
    comp='p'
elif randNo==2:
    comp='s'
elif randNo==3:
    comp='r'

you = input("Your turn:Paper(p) Scissor(s) or Rock(r)?")
a=getwin(comp,you)
if a==None:
    print("the game is tie")
elif a:
    print("You win")
else:
    print("Tou lose")

