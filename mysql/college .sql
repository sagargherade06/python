create database colleges;
use colleges; 
create table college(
Cid int primary key,
Cname varchar (50),
city varchar (60),
address varchar (50),
state varchar (20) ); 
create table department(
Did int primary key,
Dname varchar(30),
Cid int,
foreign key (Cid)references college(Cid));

create table professor(
Pid int primary key,
Pname varchar(30),
title varchar(30),
email varchar(40),
Did int,
foreign key(Did) references department(Did)); 
create table student(
Sid int primary key,
Sname varchar(10),
email varchar(30),
Gpa varchar(20));
create table enrollment(
Eid int primary key,
Sid int,
courceid int,
semister varchar(10),
grade int,
foreign key (Courceid) references cources(Courceid));
create table degree(
deggid int primary key ,
deggname varchar(10),
Sid int,
foreign key(Sid)references student(Sid));
show tables;
show databases;
SHOW TABLES;
show tables;
drop table if exists cource;
show tables;
drop table if exists cources;
select *from department;
alter table department drop column cid;
alter table department drop foreign key Cid;
select * from department;
alter table department drop foreign key Did ;
SHOW CREATE TABLE department;
alter table department drop foreign key Did ;
SHOW CREATE TABLE cources;
alter table cources drop foreign key courceid;
show tables;
show create table cources;
ALTER TABLE cources DROP FOREIGN KEY cources_ibfk_1;
select * from cources;
alter table cources drop column Did;

alter table cources drop courceid;
show create table enrollment;
select * from enrollment;
alter table enrolment drop foreign key enrollment_ibfk_1;
show create table enrollment;
alter table enrollment drop foreign key enrollment_ibfk_1;
SHOW TABLES;	
alter table enrollment drop foreign key enrollment_ibfk_1;
select * from enrollment;
select * from cources;
insert into cources(courceid, description) values(101,"english");
select * from enrollment;
insert into enrollment(Eid,Sid,courceid,semister,grade) values(101,103,101,2,3);
select * from enrollment;
alter table enrollment drop column Eid;
Select *  from enrollment;
drop table enrollment;
SELECT * FROM enrollment;
drop table if exists cources;
show databases; 
show create database mysql;

use mysql;
show tables;
select * from db;
use  colleges;
show tables;
select * from department;
drop table department;
show create table department; 
alter table department drop foreign key department_ibfk_1;
DROP TABLE department;
show create table professor;
alter table professor drop foreign key professor_ibfk_1;
drop table department; 
show tables;
drop table professor,degree;
show tables;
select * from student;
alter table student drop column gpa;
select * from student;
alter table student change column Sname fname varchar(60);
select * from student;
ALTER TABLE student ADD COLUMN Lname varchar(30) not null;
ALTER TABLE student 
/*ADD Mno tinyint unsigned  not null,
ADD city varchar(20) not null,*/
ADD age TINYINT default 18;
insert into student values(101,'sagar','sagargherade@2003gmail.com','gherade',8767108476,'baramati',21);
DESCRIBE student;
ALTER TABLE student
ADD CONSTRAINT chk_Mno CHECK (Mno BETWEEN 1 AND 10);
ALTER TABLE student MODIFY Mno TINYINT UNSIGNED; 
insert into student values(101,'sagar','sagargherade@2003gmail.com','gherade',8767108476,'baramati',21);
alter table student modify Mno int ;
insert into student values(101,'sagar','sagargherade@2003gmail.com','gherade',8767108476,'baramati',21);
select * from student;
insert into student(Sid,fname,email,Lname,Mno,city,age)values(101,'sagar','sagargherade@2003gmail.com','gherade',8767108476,'baramati',21);
DESCRIBE student;
ALTER TABLE student MODIFY Mno SMALLINT UNSIGNED;
insert into student(Sid,fname,email,Lname,Mno,city,age)values(101,'sagar','sagargherade@2003gmail.com','gherade',8767108476,'baramati',21);

DESCRIBE student;
ALTER table student MODIFY Mno int;
insert into student(Sid,fname,email,Lname,Mno,city,age)values(101,'sagar','sagargherade@2003gmail.com','gherade',876710476,'baramati',21);

SHOW CREATE TABLE student;
alter table student modify Mno int not null;
insert into student(Sid,fname,email,Lname,Mno,city,age)values(101,'sagar','sagargherade@2003gmail.com','gherade',876710476,'baramati',21);
ALTER TABLE student DROP CHECK chk_Mno;
show create table student;
insert into student(Sid,fname,email,Lname,Mno,city,age)values(101,'sagar','sagargherade@2003gmail.com','gherade',876710476,'baramati',21);
select * from student;
insert into student(Sid,fname,email,Lname,Mno,city,age)
values
(102,'karan','karankadam@gmail.com','kadam',852963,'pune',21),
(103,'ganesh','ganeshkangude@gmail.com','kangude',7865266,'ahilyanagr',21),
(104,'prakash','prakashkangude@gmail.com','kangude',585542,'takali lonar',22),
(105,'mahendra','mahendrabudwant@gmail.com','budhawant','89158522,takali lonar',22),
(106,'aditya','adityafarkande@gmail.com','farkande',74185263,'madhevadgoan',23);
insert into student(Sid,fname,email,Lname,Mno,city,age)
values
(102,'karan','karankadam@gmail.com','kadam',852963,'pune',21),
(103,'ganesh','ganeshkangude@gmail.com','kangude',7865266,'ahilyanagr',21),
(104,'prakash','prakashkangude@gmail.com','kangude',585542,'takali lonar',22),
(105,'mahendra','mahendrabudwant@gmail.com','budhawant',89158522,'takali lonar',22),
(106,'aditya','adityafarkande@gmail.com','farkande',74185263,'madhevadgoan',23);
alter table student add marks int not null;
select * from student;
insert into student(marks)values(52);
update student set marks=95 where age=21;
alter table student modify marks int default 55;
update  student
set marks=95
where age=21;
SET SQL_SAFE_UPDATES = 0;
select * from student;
update student
set marks=80
where age=22;
update student
set marks=85
where age=23;

select * from student;
delete from student where age=18;
select * from student ;
select * from student where marks<90 limit 1;
update student set city='pune' where city='takali lonar' ;
select * from student;
update student set city='baramati' where Sid=106;
select city,fname,age from student where city like 'pune%' group by city,fname,age having age=22;

show create table colleges;
select * from student;
select age,count(marks) from student  where marks in(95) group by fname;
select * from student;
select count(marks) from student  where marks in(95) group by city;
