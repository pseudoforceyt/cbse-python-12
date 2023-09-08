import mysql.connector as sqltor


con = sqltor.connect(host="localhost", user="root", passwd="2240026", database="school_stuff")
if con.is_connected():
    print("Connection Established to Database")
cur = con.cursor()

# (i)
cur.execute("CREATE TABLE EMPLOYEE(EMPNO INT PRIMARYKEY, NAME VARCHAR(45), DESIG VARCHAR(20), SALARY INT, LEAVE INT, BONUS INT)")
cur.execute("CREATE TABLE INSURANCE(EMPNO INT REFERENCES EMPLOYEE, LIC BOOL)")
con.commit()

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
    cur.execute(f"INSERT INTO EMPLOYEE VALUES ({empno},'{name}','{desig}',{salary},{leave},{bonus})")
    con.commit()
    print("========= Entered")
print('============= Complete! =============')

print("=== Enter 5 employees' LIC Status ===")
for i in range(1, 6):
    print(f"Employee {i} ====")
    empno = int(input("Employee Number: "))
    lic = input("Has LIC Insurance (true/false): ")
    cur.execute(f"INSERT INTO INSURANCE VALUES ({empno},{lic})")
    con.commit()
    print("========= Entered")
print('============= Complete! =============')

# (iii)
cur.execute("SELECT SUM(SALARY) FROM EMPLOYEE WHERE NAME LIKE 'R%' GROUP BY DESIG")
query3=cur.fetchall()
print(query3)

# (iv)
cur.execute("SELECT EMPNO, NAME FROM EMPLOYEE NATURAL JOIN INSURANCE WHERE LIC=TRUE")
query4=cur.fetchall()
print(query4)

# (v)
cur.execute("UPDATE EMPLOYEE SET SALARY=SALARY*1.1 WHERE DESIG='CLERK'")
con.commit()

con.close()