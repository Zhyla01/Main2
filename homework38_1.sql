--(Завдання_1)

CREATE TABLE veg_table_and_fruit (
    id SERIAL PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    type VARCHAR(100) CHECK (LOWER(type) IN ('овоч', 'фрукт')) NOT NULL,
    color VARCHAR(100),
    calories INT,
    description TEXT
);

INSERT INTO veg_table_and_fruit (name, type, color, calories, description) VALUES  
    ('Огірок', 'овоч', 'зелений', 16, 'Хрусткий і соковитий овоч, популярний у салатах та як закуска.'),  
    ('Морква', 'овоч', 'помаранчевий', 41, 'Солодкий коренеплід, багатий вітамінами, часто вживається сирим або вареним.'),  
    ('Броколі', 'овоч', 'зелений', 34, 'Зелене овоче з великими головками, багате на вітаміни та антиоксиданти.'),  
    ('Яблуко', 'фрукт', 'червоний', 52, 'Солодкий та хрусткий плід, популярний у всьому світі, вживається свіжим або в десертах.'),  
    ('Банан', 'фрукт', 'жовтий', 89, 'Солодкий фрукт, багатий на калій, часто використовується у сніданках та десертах.');  

-- Оновлення типів даних (необхідно тільки в разі некоректних типів)
UPDATE veg_table_and_fruit
SET type = 'фрукт'
WHERE type NOT IN ('овоч', 'фрукт');

-- Вибір овочів з калоріями менше 200
SELECT * FROM veg_table_and_fruit WHERE type = 'овоч' AND calories < 200;  

-- Вибір фруктів з калоріями між 30 і 300
SELECT * FROM veg_table_and_fruit WHERE type = 'фрукт' AND calories BETWEEN 30 AND 300;  

-- Вибір овочів, у назві яких є "кавуста"
SELECT * FROM veg_table_and_fruit WHERE type = 'овоч' AND name ILIKE '%кавуста%';  

-- Вибір овочів і фруктів з описом, що містить "гемоглобін"
SELECT * FROM veg_table_and_fruit WHERE description ILIKE '%гемоглобін%' AND type = 'овоч'  
UNION  
SELECT * FROM veg_table_and_fruit WHERE description ILIKE '%гемоглобін%' AND type = 'фрукт';  

-- Вибір за кольором
SELECT * FROM veg_table_and_fruit WHERE color IN ('жовтий', 'червоний');


--(Завдання_2)

-- Підрахунок кількості елементів у таблиці
SELECT COUNT(*) FROM veg_table_and_fruit;  

-- Підрахунок кількості фруктів
SELECT COUNT(*) FROM veg_table_and_fruit WHERE type = 'фрукт';  

-- Підрахунок кількості овочів і фруктів певного кольору
SELECT COUNT(*) FROM veg_table_and_fruit WHERE color = 'заданий_колір' AND type = 'овоч'  
UNION ALL  
SELECT COUNT(*) FROM veg_table_and_fruit WHERE color = 'заданий_колір' AND type = 'фрукт';  

-- Підрахунок кількості овочів і фруктів за кожним кольором
SELECT color, COUNT(*) as count FROM veg_table_and_fruit WHERE type = 'овоч' GROUP BY color  
UNION ALL  
SELECT color, COUNT(*) as count FROM veg_table_and_fruit WHERE type = 'фрукт' GROUP BY color;  

-- Колір з найменшою кількістю елементів
SELECT color FROM (  
    SELECT color, COUNT(*) as count FROM veg_table_and_fruit WHERE type = 'овоч'  
    GROUP BY color  
    UNION ALL  
    SELECT color, COUNT(*) as count FROM veg_table_and_fruit WHERE type = 'фрукт'  
    GROUP BY color  
) AS combined  
ORDER BY count ASC  
LIMIT 1;  

-- Колір з найбільшою кількістю елементів
SELECT color FROM (  
    SELECT color, COUNT(*) as count FROM veg_table_and_fruit WHERE type = 'овоч'  
    GROUP BY color  
    UNION ALL  
    SELECT color, COUNT(*) as count FROM veg_table_and_fruit WHERE type = 'фрукт'  
    GROUP BY color  
) AS combined  
ORDER BY count DESC  
LIMIT 1;  

-- Мінімальна кількість калорій серед всіх овочів і фруктів
SELECT MIN(calories) FROM veg_table_and_fruit;

-- Максимальна кількість калорій серед всіх овочів і фруктів
SELECT MAX(calories) FROM veg_table_and_fruit;

-- Середнє значення калорій серед всіх овочів і фруктів
SELECT AVG(calories) FROM veg_table_and_fruit;

-- Овоч з мінімальними калоріями
SELECT * FROM veg_table_and_fruit WHERE type = 'овоч' ORDER BY calories ASC LIMIT 1;  

-- Овоч з максимальними калоріями
SELECT * FROM veg_table_and_fruit WHERE type = 'овоч' ORDER BY calories DESC LIMIT 1;  

-- Фрукт з мінімальними калоріями
SELECT * FROM veg_table_and_fruit WHERE type = 'фрукт' ORDER BY calories ASC LIMIT 1;  

-- Фрукт з максимальними калоріями
SELECT * FROM veg_table_and_fruit WHERE type = 'фрукт' ORDER BY calories DESC LIMIT 1;  
