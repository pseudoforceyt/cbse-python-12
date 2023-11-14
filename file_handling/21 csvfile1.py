import csv

def enter(n):
    f = open("Student.csv", "a", newline='')
    w = csv.writer(f)
    for c in range(1,n+1):
        print(f"Student {c}")
        Rno = int(input("Roll no.: "))
        Name = input("Name: ")
        print("Marks out of 100:")
        print("English, CS, Maths, Physics, Chemistry (Comma separated)")
        E, CS, M, P, C = tuple(eval(input('> ')))
        Average = (E + CS + M + P + C)/5
        print("Average:", Average)
        w.writerow([Rno, Name, E, CS, M, P, C, Average])
        print("Entered.")
    print("Complete.")
    f.close()

def showtoppers():
    f = open("Student.csv", "r", newline='')
    r = csv.reader(f)
    try:
        next(r)
        print("\nRno\tName\t\t\tEnglish\tCS\tMaths\tPhysics\tChemistry\tAverage")
        for i in r:
            if float(i[-1]) > 85:
                print(f"\n{i[0]}\t{i[1]}\t\t\t{i[2]}\t{i[3]}\t{i[4]}\t{i[5]}\t{i[6]}\t{i[7]}")
    except StopIteration:
        print("No records")
    f.close()

f = open("Student.csv", "w", newline='')
w = csv.writer(f)
header = ["Rno", "Name", "English", "CS", "Maths", "Physics", "Chem", "Average"]
w.writerow(header)
f.close()

while True:
    print("What would you like to do?")
    print("1. Enter student record")
    print("2. Display students with average > 85")
    print("3. Exit")

    ch = int(input("> "))
    if ch == 1:
        n = int(input("How many records? "))
        enter(n)

    elif ch == 2:
        print("Students with avg > 85:")
        showtoppers()
        
    elif ch == 3:
        f.close()
        print("Goodbye!")
        break

    else:
        print("Enter a valid choice!\n\n")