--(Завдання_1)

CREATE DATABASE Academy;  

-- Створення таблиці Кафедри (Departments1)  
CREATE TABLE Departments(  
    Id SERIAL PRIMARY KEY,  
    Financing MONEY NOT NULL CHECK (Financing >= 0) DEFAULT 0,  
    Name VARCHAR(100) NOT NULL UNIQUE  
);  

-- Створення таблиці Факультети (Faculties)  
CREATE TABLE Faculties(  
    Id SERIAL PRIMARY KEY,  
    Dean VARCHAR(255) NOT NULL,  
    Name VARCHAR(100) NOT NULL UNIQUE  
);  

-- Створення таблиці Групи (Groups)  
CREATE TABLE Groups(  
    Id SERIAL PRIMARY KEY,  
    Name VARCHAR(10) NOT NULL UNIQUE,  
    Rating INT NOT NULL CHECK (Rating >= 0 AND Rating <= 5),  
    Year INT NOT NULL CHECK (Year >= 1 AND Year <= 5)  
);  

-- Створення таблиці Викладачі (Teachers)  
CREATE TABLE Teachers(  
    Id SERIAL PRIMARY KEY,  
    EmploymentDate DATE NOT NULL CHECK (EmploymentDate >= '1996-06-01'),  
    IsAssistant BOOLEAN NOT NULL DEFAULT FALSE,  
    IsProfessor BOOLEAN NOT NULL DEFAULT FALSE,  
    Name VARCHAR NOT NULL,  
    Position VARCHAR NOT NULL,  
    Premium MONEY NOT NULL CHECK (Premium >= '0') DEFAULT 0,  
    Salary MONEY NOT NULL CHECK (Salary > '0'),  
    Surname VARCHAR NOT NULL  
);  

--(Завдання_2)
--1.Вивести таблицю кафедр у зворотному порядку.
SELECT * FROM Departments ORDER BY Id DESC; 

--2.Вивести назви груп та їх рейтинги.
SELECT Name AS "Group Name", Rating AS "Group Rating" FROM Groups;

--3.Вивести прізвища викладачів, відсоток ставки від надбавки та відсоток ставки від зарплати.
SELECT Surname,   
       (Premium / Salary) * 100 AS "Percentage of Premium from Salary",  
       (Premium / (Salary + Premium)) * 100 AS "Percentage of Salary from Total"   
FROM Teachers; 

--4.Вивести таблицю факультетів у форматі: «The dean of faculty [faculty] is [dean]».
SELECT CONCAT('The dean of faculty ', Name, ' is ', Dean) AS "Faculty Information" FROM Faculties; 

--5.Вивести прізвища професорів зі ставкою, яка перевищує 1050.
SELECT Surname FROM Teachers WHERE IsProfessor = TRUE AND Salary > 1050; 

--6.Вивести назви кафедр з фондом фінансування менше 11000 або більшим за 25000.
SELECT Name FROM Departments WHERE Financing < 11000 OR Financing > 25000;

--7.Вивести назви факультетів, окрім факультету «Computer Science».
SELECT Name FROM Faculties WHERE Name <> 'Computer Science'; 

--8.Вивести прізвища та посади викладачів, які не є професорами.
SELECT Surname, Position FROM Teachers WHERE IsProfessor = FALSE;

--9.Вивести прізвища, посади, ставки та надбавки асистентів з надбавкою у діапазоні від 160 до 550.
SELECT Surname, Position, Salary, Premium FROM Teachers   
WHERE IsAssistant = TRUE AND Premium BETWEEN 160 AND 550;

--10.Вивести прізвища та ставки асистентів.
SELECT Surname, Salary FROM Teachers WHERE IsAssistant = TRUE;  

--11.Вивести прізвища та посади викладачів, які прийняті на роботу до 01.01.2000.
SELECT Surname, Position FROM Teachers WHERE EmploymentDate < '2000-01-01';  

--12.Вивести назви кафедр, які в алфавітному порядку розміщені до кафедри «Software Development».
SELECT Name AS "Name of Department" FROM Departments   
WHERE Name < 'Software Development'   
ORDER BY Name; 

--13.Вивести прізвища асистентів зі зарплатою не більше 1200.
SELECT Surname FROM Teachers   
WHERE IsAssistant = TRUE AND (Salary + Premium) <= 1200;  

--14.Вивести назви груп 5-го курсу з рейтингом у діапазоні від 2 до 4.
SELECT Name FROM Groups   
WHERE Year = 5 AND Rating BETWEEN 2 AND 4;  

--15.Вивести прізвища асистентів зі ставкою менше 550 або надбавкою менше 200.
SELECT Surname FROM Teachers   
WHERE IsAssistant = TRUE AND (Salary < 550 OR Premium < 200);  

