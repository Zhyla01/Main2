--(Завдання_1)
CREATE DATABASE Birds;  
--(Завдання_2)
ALTER DATABASE Birds RENAME TO Cats
--(Завдання_3)
DROP DATABASE IF EXISTS
Cats
--(Завдання_4)
CREATE DATABASE fruits_and_vegetables;  

CREATE TABLE vegetables_and_fruits (  
    id SERIAL PRIMARY KEY,  
    name VARCHAR(100) NOT NULL,  
    type VARCHAR(50) CHECK (type IN ('овоч', 'фрут')) NOT NULL,  
    color VARCHAR(50),  
    calories INT,  
    description TEXT  
);  

 INSERT INTO vegetables_and_fruits (name, type, color, calories, description)  
VALUES ('Помідор', 'овоч', 'червоний', 18, 'Солодкий овоч, часто використовується в салатах.'); 

SELECT * FROM vegetables_and_fruits; 

--(Завдання_5)
SELECT * FROM vegetables_and_fruits;  

SELECT * FROM vegetables_and_fruits WHERE type = 'vegetable';  

SELECT * FROM vegetables_and_fruits WHERE type = 'fruit';  

SELECT name FROM vegetables_and_fruits;  

SELECT DISTINCT color FROM vegetables_and_fruits;  

SELECT * FROM vegetables_and_fruits WHERE type = 'fruit' AND color = 'вказаний_колір';  

SELECT * FROM vegetables_and_fruits WHERE type = 'vegetable' AND color = 'вказаний_колір';  