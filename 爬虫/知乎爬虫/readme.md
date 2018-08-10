1.zhihupachong.py是爬虫的主程序，主要用了urllib库，爬取的是知乎问答；
2.zhihu2017121604210.sql存储了抓取的知乎问答，其中回答的数据量是15万条左右；
3.数据库结构是：
存储问题的题目、url链接、描述、id

```
CREATE TABLE IF NOT EXISTS `ask`(
   `id` INT UNSIGNED AUTO_INCREMENT,
   `title` VARCHAR(100) NOT NULL,
   `link` VARCHAR(100) NOT NULL,
   `detail` VARCHAR(100) NOT NULL,
   `aid` INT(32) NOT NULL,
   PRIMARY KEY ( `id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
```


存储回答的题目、url链接、描述、id

```
CREATE TABLE IF NOT EXISTS `answer`(
   `id` INT UNSIGNED AUTO_INCREMENT,
   `author` VARCHAR(100) NOT NULL,
   `content` text NOT NULL,
   `askid` INT(32) NOT NULL,
   PRIMARY KEY ( `id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

存储话题的名字、tid、大类

```
CREATE TABLE IF NOT EXISTS `topic_in`(
   `id` INT UNSIGNED AUTO_INCREMENT,
   `name` text NOT NULL,
   `tid` VARCHAR(100) NOT NULL,
   `class` text NOT NULL,
   PRIMARY KEY ( `id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

