1.zhihupachong.py���������������Ҫ����urllib�⣬��ȡ����֪���ʴ�
2.zhihu2017121604210.sql�洢��ץȡ��֪���ʴ����лش����������15�������ң�
3.���ݿ�ṹ�ǣ�
�洢�������Ŀ��url���ӡ�������id

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


�洢�ش����Ŀ��url���ӡ�������id

```
CREATE TABLE IF NOT EXISTS `answer`(
   `id` INT UNSIGNED AUTO_INCREMENT,
   `author` VARCHAR(100) NOT NULL,
   `content` text NOT NULL,
   `askid` INT(32) NOT NULL,
   PRIMARY KEY ( `id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

�洢��������֡�tid������

```
CREATE TABLE IF NOT EXISTS `topic_in`(
   `id` INT UNSIGNED AUTO_INCREMENT,
   `name` text NOT NULL,
   `tid` VARCHAR(100) NOT NULL,
   `class` text NOT NULL,
   PRIMARY KEY ( `id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

