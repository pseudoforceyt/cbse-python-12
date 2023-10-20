import mysql.connector as sqltor

con = sqltor.connect(host="localhost", user="root", passwd="mvmsss", database="xiia1010")
if con.is_connected():
    print("Connection Established to Database")
cur = con.cursor()

def qprint(data):
    for i in data:
        print(i)

# (i)
cur.execute("CREATE TABLE STUDENT(ADMNO INT PRIMARY KEY, SNAME VARCHAR(35), GENDER CHAR(1), DOB DATE, STREAM VARCHAR(15), AVERAGE INT)")
con.commit()

# (ii)
print("====== Enter 5 students' info ======")
for i in range(1, 6):
    print(f"Student {i} ====")
    admno = int(input("Admission Number: "))
    sname = input("Student Name: ")
    gender = input("Enter Gender (M/F/N): ")
    dob = input("Date of Birth (YYYY/MM/DD): ")
    stream = input("Stream: ")
    avg = int(input("Average Mark: "))
    cur.execute(f"INSERT INTO STUDENT VALUES ({admno},'{sname}','{gender}','{dob}','{stream}',{avg})")
    con.commit()
    print("======== Entered")
print('============= Complete! ============')

# (iii)
cur.execute("UPDATE STUDENT SET AVERAGE=AVERAGE+5 WHERE STREAM='SCIENCE'")
con.commit()
cur.execute("SELECT * FROM STUDENT")
query3 = cur.fetchall()
print("1. Table Created\n2. Values Inserted\n3. Mark update\n")
qprint(query3)

# (iv)
cur.execute("SELECT COUNT(GENDER) FROM STUDENT WHERE GENDER='M' AND STREAM='COMMERCE'")
query4=cur.fetchall()
print("\n4. Male commerce students\n")
qprint(query4)

# (v)
cur.execute("DELETE FROM STUDENT WHERE AVERAGE<40")
con.commit()
cur.execute("SELECT * FROM STUDENT")
query5 = cur.fetchall()
print("\n5. Deletion\n")
qprint(query5)

con.close()

""" OUTPUT:
Connection Established to Database
====== Enter 5 students' info ======
Student 1 ====
Admission Number: 5023573
Student Name: Ilamparithi M
Enter Gender (M/F/N): M
Date of Birth (YYYY/MM/DD): 2006/08/10
Stream: SCIENCE
Average Mark: 95
======== Entered
Student 2 ====
Admission Number: 5030722
Student Name: Hemayutika R
Enter Gender (M/F/N): F
Date of Birth (YYYY/MM/DD): 2006/06/21 
Stream: COMMERCE
Average Mark: 16
======== Entered
Student 3 ====
Admission Number: 5161699
Student Name: Sri Avneesh A
Enter Gender (M/F/N): M
Date of Birth (YYYY/MM/DD): 2006/07/08
Stream: SCIENCE
Average Mark: 94
======== Entered
Student 4 ====
Admission Number: 5293317
Student Name: Sajeer M
Enter Gender (M/F/N): M
Date of Birth (YYYY/MM/DD): 2005/05/10
Stream: COMMERCE
Average Mark: 67
======== Entered
Student 5 ====
Admission Number: 5375029
Student Name: Krishnapriya RB
Enter Gender (M/F/N): F
Date of Birth (YYYY/MM/DD): 2007/01/10
Stream: SCIENCE
Average Mark: 31
======== Entered
============= Complete! ============
1. Table Created
2. Values Inserted
3. Mark update

(5023573, 'Ilamparithi M', 'M', datetime.date(2006, 8, 10), 'SCIENCE', 100)
(5030722, 'Hemayutika R', 'F', datetime.date(2006, 06, 21), 'COMMERCE', 16)
(5161699, 'Sri Avneesh A', 'M', datetime.date(2006, 7, 8), 'SCIENCE', 99)
(5293317, 'Sajeer M', 'M', datetime.date(2005, 5, 10), 'COMMERCE', 67)
(5375029, 'KRISHNAPRIYA RB', 'F', datetime.date(2007, 1, 10), 'SCIENCE', 36)

4. Male commerce students

(1,)

5. Deletion

(5023573, 'Ilamparithi M', 'M', datetime.date(2006, 8, 10), 'SCIENCE', 100)
(5161698, 'Sri Avneesh A', 'M', datetime.date(2006, 7, 8), 'SCIENCE', 99)
(5293317, 'Sajeer M', 'M', datetime.date(2005, 5, 10), 'COMMERCE', 67)
"""
