-- Створення таблиці Faculties
CREATE TABLE Faculties (
    Id SERIAL PRIMARY KEY,
    Name VARCHAR(100) NOT NULL UNIQUE,
    Financing NUMERIC(10,2) NOT NULL CHECK (Financing >= 0) DEFAULT 0,
    Dean VARCHAR(255) NOT NULL
);


-- Створення таблиці Departments
CREATE TABLE Departments (
    Id SERIAL PRIMARY KEY,
    Financing NUMERIC(10,2) NOT NULL CHECK (Financing >= 0) DEFAULT 0,
    Name VARCHAR(100) NOT NULL UNIQUE,
    FacultyId INT NOT NULL REFERENCES Faculties(Id)
);

-- Створення таблиці Groups
CREATE TABLE "Groups" (
    Id SERIAL PRIMARY KEY,
    Name VARCHAR(10) NOT NULL UNIQUE,
    Year INT NOT NULL CHECK (Year >= 1 AND Year <= 5),
    Rating INT NOT NULL CHECK (Rating >= 0 AND Rating <= 5),
    DepartmentId INT NOT NULL REFERENCES Departments(Id)
);

-- Створення таблиці Teachers
CREATE TABLE Teachers (
    Id SERIAL PRIMARY KEY,
    Name VARCHAR NOT NULL,
    Surname VARCHAR NOT NULL,
    Position VARCHAR NOT NULL,
    Salary NUMERIC(10,2) NOT NULL CHECK (Salary > 0),
    Premium NUMERIC(10,2) NOT NULL CHECK (Premium >= 0) DEFAULT 0,
    EmploymentDate DATE NOT NULL CHECK (EmploymentDate >= '1996-06-01'),
    IsAssistant BOOLEAN NOT NULL DEFAULT FALSE,
    IsProfessor BOOLEAN NOT NULL DEFAULT FALSE
);

-- Створення таблиці Curators
CREATE TABLE Curators (
    Id SERIAL PRIMARY KEY,
    Name VARCHAR NOT NULL,
    Surname VARCHAR NOT NULL
);

-- Створення таблиці GroupsCurators
CREATE TABLE GroupsCurators (
    Id SERIAL PRIMARY KEY,
    CuratorId INT NOT NULL REFERENCES Curators(Id),
    GroupId INT NOT NULL REFERENCES "Groups"(Id)
);

-- Створення таблиці Subjects
CREATE TABLE Subjects (
    Id SERIAL PRIMARY KEY,
    Name VARCHAR(100) NOT NULL UNIQUE
);

-- Створення таблиці Lectures
CREATE TABLE Lectures (
    Id SERIAL PRIMARY KEY,
    LectureRoom VARCHAR NOT NULL,
    SubjectId INT NOT NULL REFERENCES Subjects(Id),
    TeacherId INT NOT NULL REFERENCES Teachers(Id)
);

-- Створення таблиці GroupsLectures
CREATE TABLE GroupsLectures (
    Id SERIAL PRIMARY KEY,
    GroupId INT NOT NULL REFERENCES "Groups"(Id),
    LectureId INT NOT NULL REFERENCES Lectures(Id)
);


-- 1. Виведіть усі можливі пари рядків викладачів і груп.  
SELECT   
    t.Name AS TeacherName,   
    t.Surname AS TeacherSurname,   
    g.Name AS GroupName  
FROM Teachers t  
CROSS JOIN "Groups" g;  

-- 2. Виведіть назви факультетів, фонд фінансування кафедр яких перевищує фонд фінансування факультету.  
SELECT   
    f.Name AS FacultyName  
FROM Faculties f  
JOIN Departments d ON d.FacultyId = f.Id  
WHERE d.Financing > f.Financing;  

-- 3. Виведіть прізвища кураторів груп і назви груп, які вони курирують.  
SELECT   
    c.Surname AS CuratorSurname,   
    g.Name AS GroupName  
FROM GroupsCurators gc  
JOIN Curators c ON gc.CuratorId = c.Id  
JOIN "Groups" g ON gc.GroupId = g.Id;  

-- 4. Виведіть імена та прізвища викладачів, які читають лекції у групі «P107».  
SELECT DISTINCT   
    t.Name,   
    t.Surname  
FROM GroupsLectures gl  
JOIN "Groups" g ON gl.GroupId = g.Id  
JOIN Lectures l ON gl.LectureId = l.Id  
JOIN Teachers t ON l.TeacherId = t.Id  
WHERE g.Name = 'P107';  

-- 5. Виведіть прізвища викладачів і назви факультетів, на яких вони читають лекції.  
SELECT DISTINCT   
    t.Surname,   
    f.Name AS FacultyName  
FROM Lectures l  
JOIN Teachers t ON l.TeacherId = t.Id  
JOIN GroupsLectures gl ON l.Id = gl.LectureId  
JOIN "Groups" g ON gl.GroupId = g.Id  
JOIN Departments d ON g.DepartmentId = d.Id  
JOIN Faculties f ON d.FacultyId = f.Id;  

-- 6. Виведіть назви кафедр і назви груп, які до них належать.  
SELECT   
    d.Name AS DepartmentName,   
    g.Name AS GroupName  
FROM Departments d  
JOIN "Groups" g ON g.DepartmentId = d.Id;  

-- 7. Виведіть назви предметів, які викладає викладач «Samantha Adams».  
SELECT DISTINCT   
    s.Name AS SubjectName  
FROM Teachers t  
JOIN Lectures l ON t.Id = l.TeacherId  
JOIN Subjects s ON l.SubjectId = s.Id  
WHERE t.Name = 'Samantha' AND t.Surname = 'Adams';  

-- 8. Виведіть назви кафедр, на яких викладається дисципліна «Database Theory».  
SELECT DISTINCT   
    d.Name AS DepartmentName  
FROM Subjects s  
JOIN Lectures l ON s.Id = l.SubjectId  
JOIN GroupsLectures gl ON l.Id = gl.LectureId  
JOIN "Groups" g ON gl.GroupId = g.Id  
JOIN Departments d ON g.DepartmentId = d.Id  
WHERE s.Name = 'Database Theory';  

-- 9. Виведіть назви груп, що належать до факультету «Computer Science».  
SELECT   
    g.Name AS GroupName  
FROM "Groups" g  
JOIN Departments d ON g.DepartmentId = d.Id  
JOIN Faculties f ON d.FacultyId = f.Id  
WHERE f.Name = 'Computer Science';  

-- 10. Виведіть назви груп 5-го курсу, а також назви факультетів, до яких вони належать.  
SELECT   
    g.Name AS GroupName,   
    f.Name AS FacultyName  
FROM "Groups" g  
JOIN Departments d ON g.DepartmentId = d.Id  
JOIN Faculties f ON d.FacultyId = f.Id  
WHERE g.Year = 5;  

-- 11. Виведіть повні імена викладачів і лекції, які вони читають (назви предметів та груп). Зробіть відбір по тим лекціям, які проходять в аудиторії «B103».  
SELECT DISTINCT   
    t.Name AS TeacherName,  
    t.Surname AS TeacherSurname,  
    s.Name AS SubjectName,  
    g.Name AS GroupName  
FROM Lectures l  
JOIN Teachers t ON l.TeacherId = t.Id  
JOIN Subjects s ON l.SubjectId = s.Id  
JOIN GroupsLectures gl ON l.Id = gl.LectureId  
JOIN "Groups" g ON gl.GroupId = g.Id  
WHERE l.LectureRoom = 'B103';  
