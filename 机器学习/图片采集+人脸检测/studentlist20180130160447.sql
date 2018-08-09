-- MySQL dump 10.13  Distrib 5.5.53, for Win32 (AMD64)
--
-- Host: localhost    Database: studentlist
-- ------------------------------------------------------
-- Server version	5.5.53

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `studentlist`
--

DROP TABLE IF EXISTS `studentlist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `studentlist` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `studentid` int(11) NOT NULL,
  `school` varchar(100) NOT NULL,
  `major` varchar(100) NOT NULL,
  `class` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `studentlist`
--

LOCK TABLES `studentlist` WRITE;
/*!40000 ALTER TABLE `studentlist` DISABLE KEYS */;
INSERT INTO `studentlist` VALUES (1,'zhaojie',1301210566,'ghm','Accounting','4');
/*!40000 ALTER TABLE `studentlist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `studentrecord`
--

DROP TABLE IF EXISTS `studentrecord`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `studentrecord` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `studentid` int(11) NOT NULL,
  `time` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `studentrecord`
--

LOCK TABLES `studentrecord` WRITE;
/*!40000 ALTER TABLE `studentrecord` DISABLE KEYS */;
INSERT INTO `studentrecord` VALUES (1,'hh',23,'2018-01-30 13:06:47'),(2,'zhaojie',1301210566,'2018-01-30 13:12:10'),(3,'zhaojie',1301210566,'2018-01-30 14:59:18'),(4,'zhaojie',1301210566,'2018-01-30 14:59:23'),(5,'zhaojie',1301210566,'2018-01-30 14:59:33'),(6,'zhaojie',1301210566,'2018-01-30 15:17:58'),(7,'zhaojie',1301210566,'2018-01-30 15:18:04'),(8,'zhaojie',1301210566,'2018-01-30 15:37:19'),(9,'zhaojie',1301210566,'2018-01-30 15:37:24'),(10,'zhaojie',1301210566,'2018-01-30 15:46:01'),(11,'zhaojie',1301210566,'2018-01-30 15:46:06');
/*!40000 ALTER TABLE `studentrecord` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-01-30 16:04:49
