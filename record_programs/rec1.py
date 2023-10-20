print("## Student v o l a t i l e Database Program ##")
masterdb = []

def addtodb():
    global masterdb
    n = int(input("How many students? "))
    for i in range(n):
        num = int(input(f"Enter roll number of student {i+1}: "))
        name = input("Enter student name: ")
        avg = float(input("Enter student average mark: "))
        masterdb += [[num,name,avg]]
def searchdb():
    global masterdb
    st = input("Enter student name or roll number: ")
    if st.isdigit():
        st = int(st)
    for i in range(len(masterdb)):
        if st == masterdb[i][0] or st == masterdb[i][1]:
            print("Found!")
            print(f"Roll number: {masterdb[i][0]}")
            print(f"Name: {masterdb[i][1]}")
            print(f"Average mark: {masterdb[i][2]}")
            break
        else:
            print("Not found!")

while True:
    print()
    print("What would you like to do?")
    print("1. Add student(s) to the database")
    print("2. Search student(s) in the database")
    print("3. Exit")
    choice = int(input("(Enter number) "))
    if choice == 1:
        print()
        addtodb()
    elif choice == 2:
        print()
        searchdb()
    elif choice == 3:
        print("Exiting the program will yeet the database into the abyss.")
        confirm = input("Are you sure you want to exit? (y/N): ")
        if confirm == "y":
            print("Goodbye!")
            break
