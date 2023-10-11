# DISCLAIMER: The author of this code, https://github.com/pseudoforceyt can NOT 
# be held responsible for consequences (good or bad,) of memorizing this code.
# The code is tested and known to work, but is not approved by any official.
# Do your own research before diving in!

def create_list():
    Lnew = []
    print("Enter elements of list (Enter for next element, put strings in quotes, Enter blank for end):")
    while True:
        try:
            Lnew += [eval(input("> "))]
        except:
            break
    return Lnew

def shift_left(L):
    Lnew = L.copy()
    for i in range(len(L)):
        Lnew[i-2] = L[i]
    L = Lnew.copy()
    return L

def spedisplay(O):
    for i in O:
        if f'{i}'.isnumeric():
            print(i,i,end=' ')
        else:
            print(f'{i}*',end=' ')

L = []

while True:
    print("What would you like to do?")
    print("1. Shift a list to the left mame")
    print("2. Display the list like a madman mame")
    print("3. Enter/change the list mame")
    print("4. exit mame")
    n = int(input("> "))
    if n == 1:
        L = shift_left(L)
        print("Shifted the list mame\n",L)
    elif n == 2:
        spedisplay(L)
        print("showed mame")
    elif n == 3:
        L = create_list()
        print("List updated mame\n",L)
    elif n == 4:
        print("Varta mame? drrrrrrrrrrrrrrrrrrrrrrrr")
        break
    else:
        print("sariya select pannu mame")    