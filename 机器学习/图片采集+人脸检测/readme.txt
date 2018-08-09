
1.程序分为三部分，先运行 图片采集.py。
2.采集完了可运行 train.py 进行训练，该程序会把模型进行腌制。
3.通过 门禁系统人脸识别系统.py 进行基于摄像头的人脸识别

由于基于摄像头，你需要重新按以上顺序运行。
关于数据库：数据库名studentlist
数据库中建立了两张表：
存放学生信息的studentlist：姓名 学号 学院 专业 班级 
只输入了一条信息，若要验证请再输入一条你的信息，这样人脸识别时会去数据库中查找信息，进行匹配。
mysql> CREATE TABLE IF NOT EXISTS `studentlist`(
    ->    `id` INT UNSIGNED AUTO_INCREMENT,
    ->    `name` VARCHAR(100) NOT NULL,
    ->    `studentid` INT NOT NULL,
    ->    `school` VARCHAR(100) NOT NULL,
    ->    `major` VARCHAR(100) NOT NULL,
    ->    `class` VARCHAR(100) NOT NULL,
    ->    PRIMARY KEY ( `id` )
    -> )ENGINE=InnoDB DEFAULT CHARSET=utf8;


以及记录进出信息的studentrecord：
摄像头识别成功时，会插入该表数据：姓名，学号和时间。
mysql> CREATE TABLE IF NOT EXISTS `studentrecord`(
    ->    `id` INT UNSIGNED AUTO_INCREMENT,
    ->    `name` VARCHAR(100) NOT NULL,
    ->    `studentid` INT NOT NULL,
    ->    `time` VARCHAR(100) NOT NULL,
    ->    PRIMARY KEY ( `id` )
    -> )ENGINE=InnoDB DEFAULT CHARSET=utf8;
