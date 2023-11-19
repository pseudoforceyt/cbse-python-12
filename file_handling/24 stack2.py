def Push():
    for k,v in SCORE.items():
        if v > 49:
            stk.append(k)

def Pop_and_Display():
    if len(stk) > 0:
        print("Pop:",stk.pop())
    else:
        print("Stack empty.")

SCORE = {"KAPIL":40, "SACHIN":55, "SAURAV":80, "RAHUL":35, "YUVRAJ":110}
stk = list()

print("Operations:")
print("\t1. Push players to stack (Score > 49)")
print("\t2. Pop player from stack")
print("\t3. Exit")
while True:
    print("What would you like to do?")
    ch = int(input("> "))

    if ch == 1:
        Push()
        print("Pushed players.")
    elif ch == 2:
        Pop_and_Display()
    elif ch == 3:
        print("Goodbye!")
        break
    else:
        print("Enter a valid choice!")