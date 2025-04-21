DROP TABLE IF EXISTS People;

CREATE TABLE People (  
    Id SERIAL PRIMARY KEY,  
    FirstName VARCHAR(100) NOT NULL,  
    LastName VARCHAR(100) NOT NULL,  
    DateOfBirth DATE NOT NULL,  
    Country VARCHAR(100) NOT NULL  
);

-- 1. Додати нову людину  
INSERT INTO People (FirstName, LastName, DateOfBirth, Country)  
VALUES ('Олексій', 'Іваненко', '1990-05-12', 'Україна');   

-- 2. Вивести людей, ім’я яких починається на певну літеру  
SELECT * FROM People  
WHERE FirstName LIKE 'А%';

-- 3. Вивести людей, які народились після певної дати  
SELECT * FROM People  
WHERE DateOfBirth > '2000-01-01';  

-- 4. Вивести скільки людей живе у певній країні  
SELECT Country, COUNT(*) AS NumberOfPeople  
FROM People  
WHERE Country = 'Польща'  
GROUP BY Country;


 
