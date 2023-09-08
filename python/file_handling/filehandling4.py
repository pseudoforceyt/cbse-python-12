def linehealth():
    with open('Exam.txt', 'r') as f:
        S = f.readlines()
        array = []
        for i in S:
            if i.[-7:-1:].lower() == 'health':
                array += [i]
    return array


print(linehealth())
