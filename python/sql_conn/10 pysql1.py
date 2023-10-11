import mysql.connector as sqltor

mycon=sqltor.connect(host='localhost', user='root', passwd='mvmsss', database='xiia1010')
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
for i in query1:
    print(i)
print("\n4. Updation of Salary\n")
for i in query2:
    print(i)
print("\n5. Highest Salary Department Wise:\n")
for i in query3:
    print(i)
mycon.close()

""" OUTPUT:
Connection Established to Database
Successfully
1. Created Table
2. Inserted given values


3. Teachers belonging to Delhi:

(1, 'JUGAL', 34, 'COMPUTER SCIENCE', datetime.date(2017, 10, 1), 12000, 'M', 'DELHI')
(3, 'SANDEEP', 32, 'MATHEMATICS', datetime.date(2016, 12, 12), 30000, 'M', 'DELHI')
(5, 'RAKESH', 42, 'MATHEMATICS', datetime.date(2007, 9, 5), 25000, 'M', 'DELHI')

4. Updation of Salary

(1, 'JUGAL', 34, 'COMPUTER SCIENCE', datetime.date(2017, 10, 1), 13200, 'M', 'DELHI')
(2, 'SHARMILA', 31, 'HISTORY', datetime.date(2008, 3, 24), 20000, 'F', 'RAJPUR')
(3, 'SANDEEP', 32, 'MATHEMATICS', datetime.date(2016, 12, 12), 30000, 'M', 'DELHI')
(4, 'SANGEETA', 35, 'HISTORY', datetime.date(2014, 7, 1), 40000, 'F', 'CHENNAI')
(5, 'RAKESH', 42, 'MATHEMATICS', datetime.date(2007, 9, 5), 25000, 'M', 'DELHI')

5. Highest Salary Department Wise:

('COMPUTER SCIENCE', 13200)
('HISTORY', 40000)
('MATHEMATICS', 30000)
"""