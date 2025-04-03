CREATE TABLE GRADE_STUDENTS (
	STUDENT_ID SERIAL PRIMARY KEY,
	NAME_STUDENT VARCHAR(100),
	CITY VARCHAR(30),
	COUNTRY VARCHAR(30),
	BIRTH_DAY DATE,
	EMAIL VARCHAR(30),
	TEL VARCHAR(30),
	GROUP_NAME VARCHAR(50),
	AVG_GRADE FLOAT,
	SUBJECT_MIN VARCHAR(50),
	SUBJECT_MAX VARCHAR(50)	
)

INSERT INTO GRADE_STUDENTS (NAME_STUDENT, CITY, COUNTRY, BIRTH_DAY, EMAIL, TEL, GROUP_NAME, AVG_GRADE, SUBJECT_MIN, SUBJECT_MAX)  
VALUES  
('John Smith', 'New York', 'USA', '2001-05-12', 'john.smith@email.com', '+1-555-1234', 'Math Group A', 3.5, 'History', 'Math'),  
('Emma Johnson', 'Los Angeles', 'USA', '2002-08-24', 'emma.johnson@email.com', '+1-555-5678', 'Science Group B', 4.2, 'Biology', 'Physics'),  
('Liam Brown', 'London', 'UK', '2000-02-17', 'liam.brown@email.com', '+44-20-1234', 'Engineering Group C', 3.8, 'English', 'Chemistry'),  
('Olivia Williams', 'Toronto', 'Canada', '2003-06-30', 'olivia.williams@email.com', '+1-416-9876', 'Business Group D', 4.5, 'Economics', 'Finance'),  
('Noah Miller', 'Berlin', 'Germany', '1999-09-10', 'noah.miller@email.com', '+49-30-4321', 'Computer Science Group E', 3.9, 'Art', 'Computer Science'),  
('Sophia Davis', 'Paris', 'France', '2001-11-05', 'sophia.davis@email.com', '+33-1-5678', 'Medicine Group F', 4.7, 'Philosophy', 'Biology'),  
('Mason Wilson', 'Sydney', 'Australia', '2002-04-15', 'mason.wilson@email.com', '+61-2-8765', 'Law Group G', 3.6, 'Geography', 'Law'),  
('Isabella Martinez', 'Madrid', 'Spain', '2000-12-22', 'isabella.martinez@email.com', '+34-91-5432', 'Art Group H', 4.1, 'Math', 'Art'),  
('Ethan Taylor', 'Rome', 'Italy', '1998-07-29', 'ethan.taylor@email.com', '+39-06-2345', 'History Group I', 3.7, 'Physics', 'History'),  
('Ava Anderson', 'Amsterdam', 'Netherlands', '2001-10-08', 'ava.anderson@email.com', '+31-20-6789', 'Psychology Group J', 4.3, 'Chemistry', 'Psychology')

-- --Завдання 1
-- Створіть наступні запити для бази даних з оцінками 
-- студентів із попереднього практичного завдання:
-- ■ Показати ПІБ усіх студентів з мінімальною оцінкою
-- у вказаному діапазоні.
-- ■ Показати інформацію про студентів, яким виповни-
-- лося 20 років.
-- ■ Показати інформацію про студентів з віком, у вказа-
-- ному діапазоні.
-- ■ Показати інформацію про студентів із конкретним
-- ім’ям. Наприклад, показати студентів з ім’ям Борис.
-- ■ Показати інформацію про студентів, в номері яких
-- є три сімки.
-- ■ Показати електронні адреси студентів, що почина-
-- ються з конкретної літери.

-- ■ Показати ПІБ усіх студентів з мінімальною оцінкою
-- у вказаному діапазоні.

SELECT *
FROM GRADE_STUDENTS 
WHERE AVG_GRADE > 4 AND AVG_GRADE < 5 

-- ■ Показати інформацію про студентів, яким виповни-
-- лося 20 років.

SELECT EXTRACT(YEAR FROM AGE(BIRTH_DAY))
FROM GRADE_STUDENTS 

SELECT *
FROM GRADE_STUDENTS 
WHERE EXTRACT(YEAR FROM AGE(BIRTH_DAY)) > 25

-- ■ Показати інформацію про студентів з віком, у вказа-
-- ному діапазоні.

SELECT *
FROM GRADE_STUDENTS 
WHERE EXTRACT(YEAR FROM AGE(BIRTH_DAY)) BETWEEN 24 AND 27

-- ■ Показати інформацію про студентів із конкретним
-- ім’ям. Наприклад, показати студентів з ім’ям Борис.

SELECT *
FROM GRADE_STUDENTS 
WHERE NAME_STUDENT LIKE 'Liam %'

-- ■ Показати інформацію про студентів, в номері яких
-- є три сімки.

SELECT *
FROM GRADE_STUDENTS 
WHERE TEL LIKE '%4%4%4%'

-- ■ Показати електронні адреси студентів, що почина-
-- ються з конкретної літери.

SELECT *
FROM GRADE_STUDENTS 
WHERE EMAIL LIKE 'a%'