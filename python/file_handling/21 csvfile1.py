import csv

def enter(n, w):
    for c in range(1,n+1):
        print(f"Student {c}")
        Rno = int(input("Roll no.: "))
        Name = input("Name: ")
        print("Marks out of 100:")
        English = float(input("English marks: "))
        cs = float(input("CS marks: "))
        Maths = float(input("Maths marks: "))
        Physics = float(input("Physics marks: "))
        Chemistry = float(input("Chemistry marks: "))
        Average = (English + cs + Maths + Physics + Chemistry)/5
        w.writerow([Rno, Name, English, cs, Maths, Physics, Chemistry, Average])
        print("Entered.")
    print("Complete.")

def showtoppers(f):
    print("\nRno\tName\t\t\tEnglish\tCS\tMaths\tPhysics\tChemistry\tAverage")
    r = csv.reader(f)
    r = next(r)
    for i in r:
        if i[-1] > 85:
            print(f"\n{i[0]}\t{i[1]}\t\t\t{i[2]}\t{i[3]}\t{i[4]}\t{i[5]}\t{i[6]}\t{i[7]}")


f = open("Student.csv", "w+", newline='')
w = csv.writer(f)
header = ["Rno", "Name", "English", "CS", "Maths", "Physics", "Chemistry", "Average"]
w.writerow(header)

while True:
    print("What would you like to do?")
    print("1. Enter student record")
    print("2. Display students with average > 85")
    print("3. Exit")

    ch = int(input("> "))
    if ch == 1:
        n = int(input("How many records? "))
        enter(n, w)

    elif ch == 2:
        print("Students with avg > 85:")
        showtoppers(f)
        
    elif ch == 3:
        print("Goodbye!")
        break

    else:
        print("Enter a valid choice!\n\n")