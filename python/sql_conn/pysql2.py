import mysql.connector as sqltor

con = sqltor.connect(host="localhost", user="root", passwd="2240026", database="school_stuff")
if con.is_connected():
    print("Connection Established to Database")
cur = con.cursor()

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

# (iv)
cur.execute("SELECT COUNT(GENDER) FROM STUDENT WHERE GENDER='M' AND STREAM='COMMERCE'")
query4=cur.fetchall()

# (v)
cur.execute("DELETE FROM STUDENT WHERE AVERAGE<40")
con.commit()
cur.execute("SELECT * FROM STUDENT")
query5 = cur.fetchall()

con.close()
