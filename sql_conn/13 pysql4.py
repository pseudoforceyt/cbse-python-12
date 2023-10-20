import mysql.connector as sqltor


def qprint(data):
    for i in data:
        print(i)

con = sqltor.connect(host="localhost", user="root", passwd="mvmsss", database="xiia1010")
if con.is_connected():
    print("Connection Established to Database")
cur = con.cursor()

# (i)
cur.execute("CREATE TABLE EMPLOYEE(EMPNO INT PRIMARY KEY, NAME VARCHAR(45), DESIG VARCHAR(20), SALARY INT, `LEAVE` INT, BONUS INT)")
cur.execute("CREATE TABLE INSURANCE(EMPNO INT REFERENCES EMPLOYEE, LIC BOOL)")
con.commit()
print("1. Created Tables")

# (ii)
print("====== Enter 5 employees' info ======")
for i in range(1, 6):
    print(f"Employee {i} ====")
    empno = int(input("Employee Number: "))
    name = input("Employee Name: ")
    desig = input("Designation: ")
    salary = int(input("Salary: "))
    leave = int(input("Number of leaves taken: "))
    bonus = int(input("Bonus: "))
    cur.execute(f"INSERT INTO EMPLOYEE VALUES \
({empno},'{name}','{desig}',{salary},{leave},{bonus})")
    con.commit()
    lic = input("Has LIC Insurance (true/false): ")
    cur.execute(f"INSERT INTO INSURANCE VALUES ({empno},{lic})")
    con.commit()
    print("========= Entered")
print('============= Complete! =============')

# (iii)
cur.execute("SELECT SUM(SALARY) FROM EMPLOYEE WHERE NAME LIKE 'R%' GROUP BY DESIG")
query3=cur.fetchall()
print("\n3. Total Salary of R% people")
qprint(query3)

# (iv)
cur.execute("SELECT EMPNO, NAME FROM EMPLOYEE NATURAL JOIN INSURANCE WHERE LIC=TRUE")
query4=cur.fetchall()
print("\n4. Employees with LIC Insurance")
qprint(query4)

# (v)
cur.execute("UPDATE EMPLOYEE SET SALARY=SALARY*1.1 WHERE DESIG='CLERK'")
con.commit()
cur.execute("SELECT * FROM EMPLOYEE")
query5=cur.fetchall()
print("\n5. Clerk Updation")
qprint(query4)

con.close()

""" OUTPUT:
Connection Established to Database
1. Created Tables
====== Enter 5 employees' info ======
Employee 1 ====
Employee Number: 90062072
Employee Name: Sasikala K
Designation: Sr Lecturer
Salary: 40000
Number of leaves taken: 4
Bonus: 8000
========= Entered
Employee 2 ====
Employee Number: 10006782
Employee Name: Prakash S
Designation: Clerk
Salary: 27000
Number of leaves taken: 2
Bonus: 5000
========= Entered
Employee 3 ====
Employee Number: 96800072 
Employee Name: Preethi N
Designation: Vice Principal
Salary: 60000
Number of leaves taken: 1
Bonus: 10000
========= Entered
Employee 4 ====
Employee Number: 10002040
Employee Name: Balaji M
Designation: Clerk
Salary: 26000
Number of leaves taken: 2
Bonus: 5000
========= Entered
Employee 5 ====
Employee Number: 10000023
Employee Name: Madhava Charyulu
Designation: Principal
Salary: 100000
Number of leaves taken: 0
Bonus: 12000
========= Entered
============= Complete! =============
=== Enter 5 employees' LIC Status ===
Employee 1 ====
Employee Number: 90062072
Has LIC Insurance (true/false): true
========= Entered
Employee 2 ====
Employee Number: 10006782
Has LIC Insurance (true/false): false
========= Entered
Employee 3 ====
Employee Number: 96800072
Has LIC Insurance (true/false): true
========= Entered
Employee 4 ====
Employee Number: 10002040
Has LIC Insurance (true/false): true
========= Entered
Employee 5 ====
Employee Number: 10000023
Has LIC Insurance (true/false): true
========= Entered
============= Complete! =============

2. Inserted Values

3. Total Salary of R% people

4. Employees with LIC Insurance
(90062072, 'Sasikala K')
(96800072, 'Preethi N')
(10002040, 'Balaji M')
(10000023, 'Madhava Charyulu')

5. Clerk Updation
(90062072, 'Sasikala K')
(96800072, 'Preethi N')
(10002040, 'Balaji M')
(10000023, 'Madhava Charyulu')
"""
