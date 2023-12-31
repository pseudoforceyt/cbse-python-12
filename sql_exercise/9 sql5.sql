USE xiia1010;
CREATE TABLE IF NOT EXISTS SPORTS (
    SCODE INT(3) PRIMARY KEY,
    SPORTSNAME VARCHAR(30),
    PARTICIPANTS INT,
    PRIZEMONEY INT,
    SCHEDULEDATE DATE
);
CREATE TABLE IF NOT EXISTS COACH (
    CODE INT PRIMARY KEY,
    NAME VARCHAR(30),
    SCODE INT(3) REFERENCES SPORTS
);
INSERT INTO SPORTS VALUES 
	(101, 'CARROM', 2, 5000, '2012-01-23'), 
    (102, 'BADMINTON', 2, 12000, '2011-12-12'), 
    (103, 'TABLE TENNIS', 4, 8000, '2012-02-14'), 
    (105, 'CHESS', 2, 9000, '2012-01-01'), 
    (108, 'LAWN TENNIS', 4, 25000, '2012-03-09');
INSERT INTO COACH VALUES 
	(1, 'RAVI', 101), 
	(2, 'MOHAN', 108), 
    (3, 'SAMEER', 101), 
    (4, 'SHIKHAR', 103);
SELECT SCODE, COUNT(SCODE) FROM COACH GROUP BY SCODE ORDER BY SCODE DESC;
SELECT SPORTS.*,COACH.NAME FROM SPORTS NATURAL JOIN COACH 
WHERE PRIZEMONEY>9000 AND NAME LIKE '%N';
SELECT SPORTS.*,COACH.NAME FROM SPORTS NATURAL JOIN COACH 
WHERE SCHEDULEDATE BETWEEN '2019-01-01' AND '2019-12-31';
SELECT SUM(PARTICIPANTS) FROM SPORTS;
ALTER TABLE SPORTS DROP PRIZEMONEY;
SELECT * FROM SPORTS;