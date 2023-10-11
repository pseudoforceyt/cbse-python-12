# DISCLAIMER: The author of this code, https://github.com/pseudoforceyt can NOT 
# be held responsible for consequences (good or bad,) of memorizing this code.
# The code is tested and known to work, but is not approved by any official.
# Do your own research before diving in!

# Edge cases covered:
# 1. Duplicate of max element: First found index returned
# 2. Max element present in both lists: Index printed from list 1

def max_two(L1,L2):
    arr = L1 + L2
    max_n = max(arr) # if max is not allowed here figure out by yourself what to do
    try:
        index_max = L1.index(max_n)
        return {'max':max_n, 'in_list':1, 'index':index_max}
    except ValueError:
        index_max = L2.index(max_n)
        return {'max':max_n, 'in_list':2, 'index':index_max}

def modify_list(L):
    try:
        Lnew = list(eval(input('enter numbers separated by commas my fren\n> ')))
        L = Lnew.copy()
    except:
        pass
    return L

L1,L2 = [],[]

while True:
    print("ennada pannanum unakku yenda uyira vaangura")
    print("1. list enter pannanum/maathanum\n2. max enga irukku?\n3. exit")
    n = int(input("> "))
    if n == 1:
        L1 = modify_list(L1)
        L2 = modify_list(L2)
        print("senjiten")
    elif n == 2:
        maxinfo = max_two(L1,L2)
        # This print statement does not have jokes, for you to understand properly
        print("The max value element",maxinfo['max'], "is present in List",
              maxinfo['in_list'], "at index position", maxinfo['index'])
    elif n == 3:
        print("hey alexa, play 'poi vaada' from 'dharmadhurai'")
        break


