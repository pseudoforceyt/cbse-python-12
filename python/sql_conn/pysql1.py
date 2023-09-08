import mysql.connector as sqltor

def prettyprint(L):
    print("\n\t%-10s"%"Tid.","%-15s"%"Name","%-9s"%"Age","%-25s"%"Department","%-0s"%"DateofJoin","%-15s"%"Salary","%-10s"%"Gender","%-15s"%"Place")
    for row in L:
        print("\t%-10s"%row[0],"%-15s"%row[1],"%-9s"%row[2],"%-25s"%row[3],"%-20s"%row[4],"%-15s"%row[5],"%-10s"%row[6],"%-15s"%row[7])
def highest_salary(L):
    print("\n\t%-25s"%"Department","%-15s"%"Highest Salary")
    for row in L:
        print("\t%-25s"%row[0],"%-15s"%row[1])

mycon=sqltor.connect(host='localhost', user='root', passwd='2240026', database='school_stuff')
if mycon.is_connected():
    print("Connection Established to Database")
cur=mycon.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS TEACHER(T_ID INT PRIMARY KEY, NAME VARCHAR(35), AGE INT, DEPARTMENT VARCHAR(30), DATE_OF_JOIN DATE, SALARY INT, GENDER CHAR(1), PLACE VARCHAR(20))")
cur.execute("INSERT INTO TEACHER VALUES (1, 'JUGAL', 34, 'COMPUTER SCIENCE', '2017-10-01', 12000, 'M', 'DELHI'), (2, 'SHARMILA', 31, 'HISTORY', '2008-03-24', 20000, 'F', 'RAJPUR'), (3, 'SANDEEP', 32, 'MATHEMATICS', '2016-12-12', 30000, 'M', 'DELHI'), (4, 'SANGEETA', 35, 'HISTORY', '2014-07-01', 40000, 'F', 'CHENNAI'), (5, 'RAKESH', 42, 'MATHEMATICS', '2007-09-05', 25000, 'M', 'DELHI')")
mycon.commit()
print("Successfully\n1. Created Table\n2. Inserted given values\n")
cur.execute("SELECT * FROM TEACHER WHERE PLACE='DELHI'")
query1=cur.fetchall()
cur.execute("UPDATE TEACHER SET SALARY=SALARY*1.1 WHERE DATE_OF_JOIN BETWEEN '2017-01-01' AND '2018-12-31'")
mycon.commit()
cur.execute("SELECT * FROM TEACHER")
query2=cur.fetchall()
cur.execute("SELECT DEPARTMENT, MAX(SALARY) FROM TEACHER GROUP BY DEPARTMENT")
query3=cur.fetchall()
print("\n3. Teachers belonging to Delhi:\n")
prettyprint(query1)
print("\n4. Updation of Salary\n")
prettyprint(query2)
print("\n5. Highest Salary Department Wise:\n")
highest_salary(query3)
mycon.close()
