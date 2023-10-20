import csv


def enter(n, w):
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

def sales_managers(f):
    r = csv.reader(f)
    r = next(r)
    print("Name, Salary")
    for i in r:
        if i[2] == "Manager" and i[3] == "Sales":
            print(i[1], i[-1], sep = ', ')


f = open("Emp.csv", "w+", newline='')
w = csv.writer(f)
header = ["Eno", "Name", "Designation", "Department", "Salary"]
w.writerow(header)

enter(int(input("How many employees to enter: ")), w)
sales_managers(f)