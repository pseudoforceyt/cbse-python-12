
USE HarshathM;
CREATE TABLE STATIONARY(S_ID varchar(5) primary key, S_NAME varchar(20), COMPANY varchar(20), PRICE int);
CREATE TABLE CONSUMER(C_ID varchar(5) primary key, C_NAME varchar(20), ADDRESS varchar(20), S_ID char(4) REFERENCES STATIONARY);

INSERT INTO STATIONARY VALUES ("DP01", "Dot Pen", "ABC", 10), ("PL02", "Pencil", "XYZ", 6), ("ER05", "Eraser", "XYZ", 7), ("PL01", "Pencil", "CAM", 5), ("GP02", "Gel Pen", "ABC", 15);
INSERT INTO CONSUMER VALUES ('01', "Good Learner", "Delhi", "PL01"), ('06', "Write Well", "Mumbai", "GP02"), ('12', "Topper", "Delhi", "PL02"), ('15', "Write & Draw", "Delhi", "PL02"), ('16', "Motivation", "Bangalore", "PL01");

SELECT DISTINCT COMPANY FROM STATIONARY;
SELECT * FROM STATIONARY WHERE PRICE BETWEEN 8 and 15;
SELECT C_NAME, ADDRESS, COMPANY, PRICE FROM STATIONARY natural join CONSUMER; 
