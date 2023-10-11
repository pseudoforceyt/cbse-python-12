USE xiia1010;

CREATE TABLE PAYLEVEL(
  PLEVEL CHAR(4) PRIMARY KEY,
  PAY INT NOT NULL,
  ALLOWANCE INT NOT NULL);
CREATE TABLE WORKERS(
  ECODE INT PRIMARY KEY,
  NAME VARCHAR(20) NOT NULL,
  DESIG VARCHAR(20) NOT NULL,
  PLEVEL CHAR(4) NOT NULL REFERENCES PAYLEVEL,
  DOJ DATE NOT NULL,
  DOB DATE NOT NULL);
INSERT INTO PAYLEVEL VALUES
  ('P001',26000,12000),
  ('P002',22000,10000),
  ('P003',12000,6000);
INSERT INTO WORKERS VALUES
  (11,'RadheShyam','Supervisor','P001','2004-09-12','1981-08-23'),
  (12,'Chandernath','Operator','P003','2010-02-22','1987-07-12'),
  (13,'Fizza','Operator','P003','2009-06-14','1983-10-14'),
  (14,'Ameen','Mechanic','P002','2006-08-21','1981-03-13'),
  (15,'Sanya','Clerk','P002','2005-12-19','1983-06-09'),
  (18,'Sarsa','Supervisor','P001','2010-01-20','1982-02-01');

SELECT * FROM WORKERS ORDER BY DOJ DESC;
SELECT NAME,DESIG FROM WORKERS WHERE PLEVEL='P001' OR PLEVEL='P002';
SELECT COUNT(*) FROM WORKERS,PAYLEVEL WHERE WORKERS.PLEVEL=PAYLEVEL.PLEVEL AND PAY+ALLOWANCE>=30000;
UPDATE PAYLEVEL SET ALLOWANCE=ALLOWANCE+1000 WHERE PAY>=20000;
SELECT DESIG,COUNT(*) FROM WORKERS GROUP BY DESIG;

# https://bin.bloom.host/raduxaxato.sql