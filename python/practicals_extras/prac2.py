# DISCLAIMER: The author of this code, https://github.com/pseudoforceyt can NOT 
# be held responsible for consequences (good or bad,) of memorizing this code.
# The code is tested and known to work, but is not approved by any official.
# Do your own research before diving in!

def double_up(L):
    for i in range(len(L)-1,0,-1):
        if L[i] == 0 or L[i-1] % L[i] == 0:
            L[i] *= 2
    return L

def invert_case(S):
    flag = False
    invert_S = S
    for i in S:
        if i.lower() in "aeiou":
            flag = True
            break
    if flag:
        invert_S = ''
        # this shit can be reduced to a single line if swapcase() use is allowed
        # invert_S = S.swapcase()
        for i in S:
            if i.isupper():
                invert_S += i.lower()
            elif i.islower():
                invert_S += i.upper()
            else:
                invert_S += i
    return invert_S

while True:
    print('wut wud u like to do my fren?')
    print('1. i wanna give you a list which you will modify and give me back')
    print('2. i wanna give you a string which you will invert the case of and give')
    print('3. get lost ra stupedu fello')
    n = int(input('> '))
    if n == 1:
        L = list(eval(input('enter numbers separated by commas my fren\n> ')))
        double_up(L)
        print('heres ur modified list my fren\n',L)
    elif n == 2:
        S = input('enter a string my fren\n> ')
        invert_S = invert_case(S)
        print('heres ur case inverted string my fren\n',invert_S)
    elif n == 3:
        print('im closing ur program without warning for the rudeness')
        break # dan heng go BREAK

