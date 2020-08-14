# 1.查询同时存在1课程和2课程的情况

select t1.id, t1.name 
from (
select st.id, st.name, sc.courseId 
from student as st
left join student_course as sc
on st.id =sc.studentId
where sc.studentId="1")t1
inner join(
select st.id,st.name,sc.courseId 
from student as st
left join student_course as sc
on st.id =sc.studentId
where sc.studentId="2")t2
on t1.id = t2.id;

# 2.查询同时存在1课程和2课程的情况
select t1.id, t1.name 
from (
select st.id, st.name, sc.courseId 
from student as st
left join student_course as sc
on st.id =sc.studentId
where sc.studentId="1")t1
inner join(
select st.id,st.name,sc.courseId 
from student as st
left join student_course as sc
on st.id =sc.studentId
where sc.studentId="2")t2
on t1.id = t2.id;

# 3.查询平均成绩大于等于60分的同学的学生编号和学生姓名和平均成绩

select st.name, sc.studentId, sc.score 
from student as st 
inner join student_course as sc
on st.id = sc.studentId
group by 1,2
having avg(sc.score)>=60;
 
# 4.查询在student_course表中不存在成绩的学生信息的SQL语句

select st.name, st.age,st.sex,sc.studentId, sc.score 
from student as st 
left join student_course as sc
on st.id = sc.studentId
where sc.studentId is null;

# 5.查询所有有成绩的SQL

select sc.studentId, sc.score
from student_course as sc
where sc.score is not null;

# 6.查询学过编号为1并且也学过编号为2的课程的同学的信息

select t1.id, t1.name, t1.age, t1.sex
from (
select st.id, st.name, st.age, st.sex,sc.courseId 
from student as st
left join student_course as sc
on st.id =sc.studentId
where sc.courseId="1")t1
inner join(
select st.id,st.name,st.age, st.sex,sc.courseId 
from student as st
left join student_course as sc
on st.id =sc.studentId
where sc.courseId="2")t2
on t1.id = t2.id;

# 7.检索1课程分数小于60，按分数降序排列的学生信息

select st.name, st.age,st.sex
from student as st 
inner join student_course as sc
on st.id = sc.studentId
where sc.courseId="1" and sc.score<60
order by sc.score desc;

# 8.查询每门课程的平均成绩，结果按平均成绩降序排列，平均成绩相同时，按课程编号升序排列

select sc.coureseId,avg(sc.score)
from student_course as sc
group by 1
order by avg(sc.score) desc,sc.courseId;

# 9.查询课程名称为"数学"，且分数低于60的学生姓名和分数

select t1.name, t1.score
from (
select st.name, st.id,sc.score
from student as st 
left join student_course as sc
on st.id = sc.studentId
where sc.score<60) t1
left join(
select sc.studentId
from student_course as sc
left join course as c
on st.courseId = c.id
where c.name="数学")t2
on t1.id =t2.studentId




