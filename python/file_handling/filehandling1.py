def createfile(lines):
    with open('Replace.txt', 'w') as f:
        f.writelines(lines)

def copy_a():
    with open('Replace.txt', 'r') as f:
        with open('New.txt', 'w') as fn:
            acl = []
            for line in f:
                if 'a' in line.lower():
                    acl += [line]
            fn.writelines(acl)

n=int(input("Enter no. of lines to write to Replace.txt"))
l=[]
for i in range(n):
    l += [input(f"Enter line {i+1}:\n")+'\n']

createfile(l)
copy_a()

with open('New.txt','r') as file:
    print(file.read())