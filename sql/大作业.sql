-- Database: `movielens`
CREATE DATABASE IF NOT EXISTS `movielens` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `movielens`;


-- 表的结构 tags
DROP TABLE IF EXISTS tag;
CREATE TABLE IF NOT EXISTS tag(
     userid     VARCHAR(20),
     movieid    VARCHAR(20),
     tag        VARCHAR(400),
     timestamp  INT,
     PRIMARY KEY (userid, movieid, tag, timestamp)
  )ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- 表的结构 movie
DROP TABLE IF EXISTS movie;
CREATE TABLE IF NOT EXISTS movie(
     movieid     VARCHAR(20),
     title       VARCHAR(200),
     genres      VARCHAR(400),
     PRIMARY KEY (movieid)
  )ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- 表的结构 rating
DROP TABLE IF EXISTS rating;
CREATE TABLE IF NOT EXISTS rating(
     userid      VARCHAR(20),
     movieid     VARCHAR(20),
     rating      FLOAT,
     timestamp   INT,
     PRIMARY KEY (userid, movieid, timestamp)
  )ENGINE=InnoDB DEFAULT CHARSET=latin1;

--表的结构 link
DROP TABLE IF EXISTS link;
CREATE TABLE IF NOT EXISTS link(
     movieid     VARCHAR(20),
     imdbid      VARCHAR(20),
     tmbdid      VARCHAR(20),
     PRIMARY KEY (movieid)
  )ENGINE=InnoDB DEFAULT CHARSET=latin1;


--表的结构 genome_scores
DROP TABLE IF EXISTS genome_scores;
CREATE TABLE IF NOT EXISTS genome_scores(
     movieid     VARCHAR(20),
     tagid       VARCHAR(20),
     relevance   FLOAT,
     PRIMARY KEY (movieid, tagid)
  )ENGINE=InnoDB DEFAULT CHARSET=latin1;

--表的结构 genome_tags
DROP TABLE IF EXISTS genome_scores;
CREATE TABLE IF NOT EXISTS genome_tags(
     tagid       VARCHAR(20),
     tag         VARCHAR(200),
     PRIMARY KEY (tagid)
  )ENGINE=InnoDB DEFAULT CHARSET=latin1;

--*****************
--数据插入
-- ****************

-- tag
load data infile 'ml-25m/tags.csv'
into table tag
fields terminated by ',' optionally enclosed by '"' escaped by '"'
lines terminated by '\r\n'
(userid, movieid, tag, timestamp);

-- rating
load data infile 'ml-25m/ratings.csv'
into table rating
fields terminated by ',' optionally enclosed by '"' escaped by '"'
lines terminated by '\r\n'
ignore 1 lines
(userid, movieid, rating, timestamp);

-- movie
load data infile 'ml-25m/movies.csv'
into table movie
fields terminated by ',' optionally enclosed by '"' escaped by '"'
lines terminated by '\r\n'
(movieid, title, genres);
  
-- link
load data infile 'ml-25m/links.csv'
into table link
fields terminated by ',' optionally enclosed by '"' escaped by '"'
lines terminated by '\r\n'
(movieid, imdbid, tmbdid);

*******************************************
--一共有多少不同的用户
select count(distinct tag.userId) from tag
union
select count(distinct rating.userId) from rating

--一共有多少不同的电影
select count(distinct movie.title) from movie

--一共有多少不同的电影种类
select count(distinct movie.genres) from movie

--4.一共有多少电影没有外部链接
select count(distinct link.moviedid) from link 
 where link.imdbid is null  
--5.2018年一共有多少人进行过电影评分
select count(distinct rating.userid) from rating 
 where t.timestamp >= TIMESTAMPDIFF(SECOND, '1970-01-01 00:00:00','2018-01-01 00:00:00')
            and t.timestamp < TIMESTAMPDIFF(SECOND, '1970-01-01 00:00:00','2019-01-01 00:00:00')

