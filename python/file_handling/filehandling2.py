def kuttystory(lines):
    with open('Story.txt', 'w') as f:
        f.writelines(lines)

def read_four():
    with open('Story.txt', 'r') as f:
        L=f.readlines().replace('\n',' ').split()
        for word in L:
            if len(word) >= 4:
                L.remove(word)
    return L

n=int(input("Tell me a kutty story, ill write it in story.txt. First tell me number of lines of the kutty story: "))
l=[]
for i in range(n):
    l += [input(f"Enter line {i+1} of your kutty story:\n")+'\n']
kuttystory(l)

print("Words with less than 4 characters in your kutty story:")
print(read_four())