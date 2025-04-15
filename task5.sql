CREATE TABLE PERSON (  
    ID SERIAL PRIMARY KEY,  
    FIRST_NAME VARCHAR(20) NOT NULL, -- Не может быть пропуска  
    LAST_NAME VARCHAR(20) NOT NULL UNIQUE, -- Добавлено NOT NULL для LAST_NAME  
    AGE INT CHECK(AGE > 0), -- Убедимся, что AGE больше 0  
    CITY VARCHAR(30) DEFAULT 'ЗАПОРІЖЖЯ', -- Значение по умолчанию для CITY  
    BIRTH_DATE DATE NOT NULL CHECK(BIRTH_DATE > '1925-01-01') -- Дата рождения не может быть до 1925 года  
);  

	