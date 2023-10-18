import pickle

def writeinfo(n):
    print(f"==== Entering info of {n} cars ====")
    with open("CARS.DAT", "ab") as f:
        for i in range(n):
            print(f"==== Car {i+1}")
            CarNo = int(input("Car No.: "))
            Carname = input("Car Name: ")
            Mileage = int(input("Mileage: "))
            Price = int(input("Price: "))
            rec = [CarNo, Carname, Mileage, Price]
            pickle.dump(rec, f)
            print("Entered ====")
        print("== Completed! ==")

def toyotainfo():
    print("Toyota Cars:")
    print("No.\tName\tPrice")
    with open("CARS.DAT", "rb") as f:
        found = 0
        while True:
            try:
                rec = pickle.load(f)
                if rec[1].lower() == 'toyota':
                    print(rec[0], rec[1], rec[3], sep = "\t")
            except EOFError:
                f.close()
                if found == 0:
                    print("No records!")

while True:
    print("What do you want to do?")
    print("1. Enter data of cars")
    print("2. Print Toyota cars")
    print("3. Exit")
    ch = int(input("> "))
    if ch == 1:
        n = int(input("Number of cars to enter? "))
        writeinfo(n)
    elif ch == 2:
        toyotainfo()
    elif ch == 3:
        print("tata")
        break
    else:
        print("Select a valid operation!")
