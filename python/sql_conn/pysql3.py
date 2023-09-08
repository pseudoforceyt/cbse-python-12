import mysql.connector as sqltor


con = sqltor.connect(host="localhost", user="root", passwd="2240026", database="school_stuff")
if con.is_connected():
    print("Connection Established to Database")
cur = con.cursor()

# (i)
cur.execute("CREATE TABLE CELEBRITY(CELEBRITYID CHAR(4) PRIMARY KEY, NAME VARCHAR(45), PHONE CHAR(10), FEECHARGED INT)")
cur.execute("CREATE TABLE EVENT(EVENTID INT PRIMARY KEY, EVENTNAME VARCHAR(45), NUMPERF INT, CELEBRITYID CHAR(4) REFERENCES CELEBRITY)")
con.commit()

# (ii)
cur.execute("INSERT INTO EVENT VALUES (101, 'BIRTHDAY', 10, 'C102'), (102, 'PROMOTION PARTY', 20, 'C103'), (103, 'ENGAGEMENT', 12, 'C102'), (104, 'WEDDING', 15, 'C104'), (105, 'BIRTHDAY', 17, 'C101')")
cur.execute("INSERT INTO CELEBRITY VALUES ('C101', 'FAIZ KHAN', '9910195610', 200000), ('C102', 'SANJAY KUMAR', '8934664481', 250000), ('C103', 'NEERAKHAN KAPOOR', '9811665685', 300000), ('C104', 'REENA BHATIA', '6587775645', 100000)")
con.commit()

# (iii)
cur.execute("SELECT EVENTNAME, NAME, FEECHARGED FROM EVENT NATURAL JOIN CELEBRITY WHERE FEECHARGED>200000")
query3=cur.fetchall()
print(query3)

# (iv)
cur.execute("UPDATE CELEBRITY NATURAL JOIN EVENT SET FEECHARGED = FEECHARGED+10000 WHERE NUMPERF>15")
con.commit()
cur.execute("SELECT * FROM CELEBRITY")
print(cur.fetchall())

# (v)
cur.execute("DELETE FROM CELEBRITY WHERE NAME LIKE 'R%'")
con.commit()

con.close()