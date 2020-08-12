create database student_examination_sys

create table student
(id char(4) not null,
 name varchar(100) not null,
  age integer ,
  sex varchar(100),
 primary key(id));

start transaction;
insert into student values ('001','张三','18','男');
insert into student values ('002','李四','20','女');
commit;

create table subject
(id char(4) not null,
 subject varchar(100) not null,
  teacher varchar(100) not null,
  description varchar(100) not null,
 primary key(id));

start transaction;
insert into subject values ('1001','语文','王老师','本次考试比较简单');
insert into subject values ('1002','数学','刘老师','本次考试比较难');
commit;

create table score
(id char(4) not null,
 student_id char(4) not null,
  subject_id char(4) not null,
  score integer not null,
 primary key(id));

start transaction;
insert into score values ('1','001','1001','80');
insert into score values ('2','002','1002','60');
insert into score values ('3','001','1001','70');
insert into score values ('4','002','1002','60.5');
commit;
