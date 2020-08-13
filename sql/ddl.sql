-- **数据库级别：**  
--  显示所有数据库  
show databases;
--  进入某个数据库  
use student_sys;
--  创建一个数据库  
create database student_sys;
--  创建指定字符集的数据库  
create database student_sys character set utf8;
--  显示数据库的创建信息   
show create database student_sys;
--  修改数据库的编码  
alter database student_sys character set gb2312;
--  删除一个数据库   
drop database student_sys;
-- **表级别**
--  修改表名
rename table student to student1;
--  修改字段的数据类型
alter table student1 modify name varchar(100);
--  修改字段名
alter table student1 change name name1;
--  添加字段
alter table student1 add interst int;
--  删除字段
alter table student1 drop interst;
--  修改表的存储引擎
alter table student1 engine=MyISAM;
--  删除表的外键约束
alter table student1 drop foreign key fk_name;
--  删除一张表
drop table student1