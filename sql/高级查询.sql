create database student_examination_sys;
use student_examination_sys;
--student表
create table  student  
(id     varchar(5)  not null,
 name   varchar(10),
 age    int,
 sex    varchar(1)
);

--subject表
create table  subject  
(id           int  not null,
 subject      varchar(10),
 teacher      varchar(10),
 description  varchar(20)
);

--score表
create table  score  
(id           int  not null,
 student_id   varchar(5),
 subject_id   int,
 score        float
);

insert into student(id,name,age,sex)
values( '001','张三',18,'男'),('002','李四',20,'女');
insert into subject(id,subject,teacher,description)
values( 1001,'语文','王老师','本次考试比较简单'),(1002,'数学','刘老师','本次考试比较难');
insert into score(id,student_id,subject_id,score)
values( 1,'001',1001,80),(2,'002',1001,75),(3,'001',1002,70),(4,'002',1002,60.5);

delimiter //
create procedure calc_student_stat()
create temporary table student_stat_temp as
begin
select t.student_id, t.subject_id ,t.score,t1.avg_score,t2.total_score,t.score/t2.total_score as score_rate,t3.teacher
from score as t 
left join
(select subject_id,avg(score) as avg_score
from score 
group by subject_id) t1
on t.subject_id =t1.subject_id
left join 
(select student_id,sum(score) as total_score
from score
group by student_id)t2
on t.student_id=t2.student_id
left join
(select id,teacher
from subject)t3
on t.subject_id =t3.id
end;
//
delimiter;
call calc_student_stat();












