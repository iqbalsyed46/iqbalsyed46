import time
time=int(input("enter the time"))

if (time<12):
    print("good morning")
elif(time>12):
        print("good afternoon")
elif(time<=24):
        print("good evening")
else:
        print("bad evening")