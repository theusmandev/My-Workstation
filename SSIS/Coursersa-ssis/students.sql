create database ssis_learning
create table students
(Name varchar(20),
Age int
)


insert into students
values
('usman',23),
('hamza',24)

select * from students






INSERT INTO students (Name, Age)
SELECT 'usman', 23
UNION ALL
SELECT 'hamza', 24;
