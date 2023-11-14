import csv


def enter(n):
    f = open("Emp.csv", "a", newline='')
    w = csv.writer(f)
    for i in range(1, n+1):
        print(f"Employee {i} ====")
        Eno = int(input("Employee Number: "))
        Name = input("Employee Name: ")
        Designation = input("Designation: ")
        Department = input("Department: ")
        Salary = int(input("Salary: "))
        w.writerow([Eno, Name, Designation, Department, Salary])
        print("Entered.")
    print("Complete.")
    f.close()

def sales_managers():
    f = open("Emp.csv", "r", newline='')
    r = csv.reader(f)
    next(r)
    print("Sales managers' data")
    print("Name, Salary")
    for i in r:
        if i[2] == "Manager" and i[3] == "Sales":
            print(i[1], i[-1], sep = ', ')
    f.close()

f = open("Emp.csv", "w", newline='')
w = csv.writer(f)
header = ["Eno", "Name", "Designation", "Department", "Salary"]
w.writerow(header)
f.close()

enter(int(input("How many employees to enter: ")))
sales_managers()