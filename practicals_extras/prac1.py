# DISCLAIMER: The author of this code, https://github.com/pseudoforceyt can NOT 
# be held responsible for consequences (good or bad,) of memorizing this code.
# The code is tested and known to work, but is not approved by any official.
# Do your own research before diving in!

def create_matrix(m,n):
    matrix = []
    for i in range(m):
        row = []
        for j in range(n):
            row += [int(input(f"Enter number {j+1} of row {i+1}: "))]
        matrix += [row]
    return matrix

def Msum(m1, m2):
    result = []
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
        for i in range(len(m1)):
            op_row = []
            for j in range(len(m1[0])):
                op_row += [m1[i][j] + m2[i][j]]
            result += [op_row]
        return result
    else:
        raise Exception("addition and subtraction is not possible")
def Mdiff(m1, m2):
    result = []
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
        for i in range(len(m1)):
            op_row = []
            for j in range(len(m1[0])):
                op_row += [m1[i][j] - m2[i][j]]
            result += [op_row]
        return result
    else:
        raise Exception("addition and subtraction is not possible")
def Mndiff(m1, m2):
    result = []
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
        for i in range(len(m1)):
            op_row = []
            for j in range(len(m1[0])):
                op_row += [m2[i][j] - m1[i][j]]
            result += [op_row]
        return result
    else:
        raise Exception("addition and subtraction is not possible")

print("Matrix 1: Enter number of")
m,n = int(input("rows:")), int(input("columns:"))
m1 = create_matrix(m,n)

print("Matrix 2: Enter number of")
m,n = int(input("rows:")), int(input("columns:"))
m2 = create_matrix(m,n)

while True:
    print("Choose operation:\n1. Matrix 1 + Matrix 2")
    print("2. Matrix 1 - Matrix 2\n3. Matrix 2 - Matrix 1\n4. Exit\n")
    n = int(input("> "))
    if n == 1:
        S = Msum(m1, m2)
        print("Sum of matrices:\n", S)
    elif n == 2:
        D1 = Mdiff(m1, m2)
        print("(Matrix 1 - Matrix 2):\n", D1)
    elif n == 3:
        D2 = Mndiff(m1, m2)
        print("(Matrix 2 - Matrix 1):\n", D2)
    elif n == 4:
        print('ok tata')
        break