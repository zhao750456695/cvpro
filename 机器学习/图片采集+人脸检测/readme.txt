
1.�����Ϊ�����֣������� ͼƬ�ɼ�.py��
2.�ɼ����˿����� train.py ����ѵ�����ó�����ģ�ͽ������ơ�
3.ͨ�� �Ž�ϵͳ����ʶ��ϵͳ.py ���л�������ͷ������ʶ��

���ڻ�������ͷ������Ҫ���°�����˳�����С�
�������ݿ⣺���ݿ���studentlist
���ݿ��н��������ű�
���ѧ����Ϣ��studentlist������ ѧ�� ѧԺ רҵ �༶ 
ֻ������һ����Ϣ����Ҫ��֤��������һ�������Ϣ����������ʶ��ʱ��ȥ���ݿ��в�����Ϣ������ƥ�䡣
mysql> CREATE TABLE IF NOT EXISTS `studentlist`(
    ->    `id` INT UNSIGNED AUTO_INCREMENT,
    ->    `name` VARCHAR(100) NOT NULL,
    ->    `studentid` INT NOT NULL,
    ->    `school` VARCHAR(100) NOT NULL,
    ->    `major` VARCHAR(100) NOT NULL,
    ->    `class` VARCHAR(100) NOT NULL,
    ->    PRIMARY KEY ( `id` )
    -> )ENGINE=InnoDB DEFAULT CHARSET=utf8;


�Լ���¼������Ϣ��studentrecord��
����ͷʶ��ɹ�ʱ�������ñ����ݣ�������ѧ�ź�ʱ�䡣
mysql> CREATE TABLE IF NOT EXISTS `studentrecord`(
    ->    `id` INT UNSIGNED AUTO_INCREMENT,
    ->    `name` VARCHAR(100) NOT NULL,
    ->    `studentid` INT NOT NULL,
    ->    `time` VARCHAR(100) NOT NULL,
    ->    PRIMARY KEY ( `id` )
    -> )ENGINE=InnoDB DEFAULT CHARSET=utf8;
