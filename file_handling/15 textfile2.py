def story(lines):
    with open('Story.txt', 'w') as f:
        f.writelines(lines)

def read_four():
    with open('Story.txt', 'r') as f:
        S = f.read().replace("\n", ' ')
        array = []
        for i in S.split():
            if len(i) < 4:
                array += [i]
    return array


n=int(input("How many lines do you want your Story.txt to be? "))
l=[]
for i in range(n):
    l += [input(f"Enter line {i+1}:\n")+'\n']

story(l)
print("Words that have less than 4 letters in your Story.txt:\n", read_four())

