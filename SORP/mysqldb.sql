-- MySQL dump 10.13  Distrib 5.7.22, for Linux (x86_64)
--
-- Host: localhost    Database: sorp
-- ------------------------------------------------------
-- Server version	5.7.22-0ubuntu0.16.04.1

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
INSERT INTO `auth_group` VALUES (1,'Admin'),(4,'Administraion Staff'),(7,'Department Staff'),(6,'Hostel Staff'),(5,'Library Staff'),(3,'Registration Staff'),(2,'Student');
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=127 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
INSERT INTO `auth_group_permissions` VALUES (1,1,1),(2,1,2),(3,1,3),(4,1,4),(5,1,5),(6,1,6),(7,1,7),(8,1,8),(9,1,9),(10,1,10),(11,1,11),(12,1,12),(13,1,13),(14,1,14),(15,1,15),(16,1,16),(17,1,17),(18,1,18),(19,1,19),(20,1,20),(21,1,21),(22,1,22),(23,1,23),(24,1,24),(25,1,25),(26,1,26),(27,1,27),(28,1,28),(29,1,29),(30,1,30),(31,1,31),(32,1,32),(33,1,33),(34,1,34),(35,1,35),(36,1,36),(37,1,37),(38,1,38),(39,1,39),(40,1,40),(41,1,41),(42,1,42),(43,1,43),(44,1,44),(45,1,45),(46,1,46),(47,1,47),(48,1,48),(49,1,49),(50,1,50),(51,1,51),(52,2,1),(53,2,2),(54,2,3),(55,2,10),(56,2,11),(57,2,12),(58,2,13),(59,2,14),(60,2,15),(61,2,16),(62,2,17),(63,2,18),(64,2,22),(65,2,23),(66,2,24),(67,3,1),(68,3,2),(69,3,3),(70,3,4),(71,3,5),(72,3,6),(73,3,7),(74,3,8),(75,3,9),(76,3,10),(77,3,11),(78,3,12),(79,3,13),(80,3,14),(81,3,15),(82,3,16),(83,3,17),(84,3,18),(85,3,19),(86,3,20),(87,3,21),(88,3,22),(89,3,23),(90,3,24),(91,3,25),(92,3,26),(93,3,27),(94,3,28),(95,3,29),(96,3,30),(97,3,31),(98,3,32),(99,3,33),(100,3,37),(101,3,38),(102,3,39),(103,4,10),(104,4,11),(105,4,12),(106,5,10),(107,5,11),(108,5,12),(109,6,10),(110,6,11),(111,6,12),(113,7,1),(114,7,2),(115,7,3),(117,7,4),(118,7,5),(119,7,6),(120,7,10),(121,7,11),(122,7,12),(123,7,25),(124,7,26),(125,7,27),(126,7,31),(112,7,32),(116,7,33);
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add result',1,'add_result'),(2,'Can change result',1,'change_result'),(3,'Can delete result',1,'delete_result'),(4,'Can add ug branch',2,'add_ugbranch'),(5,'Can change ug branch',2,'change_ugbranch'),(6,'Can delete ug branch',2,'delete_ugbranch'),(7,'Can add documents',3,'add_documents'),(8,'Can change documents',3,'change_documents'),(9,'Can delete documents',3,'delete_documents'),(10,'Can add due',4,'add_due'),(11,'Can change due',4,'change_due'),(12,'Can delete due',4,'delete_due'),(13,'Can add student first fee status',5,'add_studentfirstfeestatus'),(14,'Can change student first fee status',5,'change_studentfirstfeestatus'),(15,'Can delete student first fee status',5,'delete_studentfirstfeestatus'),(16,'Can add document info',6,'add_documentinfo'),(17,'Can change document info',6,'change_documentinfo'),(18,'Can delete document info',6,'delete_documentinfo'),(19,'Can add board',7,'add_board'),(20,'Can change board',7,'change_board'),(21,'Can delete board',7,'delete_board'),(22,'Can add student info',8,'add_studentinfo'),(23,'Can change student info',8,'change_studentinfo'),(24,'Can delete student info',8,'delete_studentinfo'),(25,'Can add ug class',9,'add_ugclass'),(26,'Can change ug class',9,'change_ugclass'),(27,'Can delete ug class',9,'delete_ugclass'),(28,'Can add category',10,'add_category'),(29,'Can change category',10,'change_category'),(30,'Can delete category',10,'delete_category'),(31,'Can add subjects',11,'add_subjects'),(32,'Can change subjects',11,'change_subjects'),(33,'Can delete subjects',11,'delete_subjects'),(34,'Can add log entry',12,'add_logentry'),(35,'Can change log entry',12,'change_logentry'),(36,'Can delete log entry',12,'delete_logentry'),(37,'Can add user',13,'add_user'),(38,'Can change user',13,'change_user'),(39,'Can delete user',13,'delete_user'),(40,'Can add permission',14,'add_permission'),(41,'Can change permission',14,'change_permission'),(42,'Can delete permission',14,'delete_permission'),(43,'Can add group',15,'add_group'),(44,'Can change group',15,'change_group'),(45,'Can delete group',15,'delete_group'),(46,'Can add content type',16,'add_contenttype'),(47,'Can change content type',16,'change_contenttype'),(48,'Can delete content type',16,'delete_contenttype'),(49,'Can add session',17,'add_session'),(50,'Can change session',17,'change_session'),(51,'Can delete session',17,'delete_session');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$100000$sKcHq3lyG5HJ$7SZFjP1vx0mVXgGu2A3e/BxBfZcTP6DRU7/yHlJERac=','2018-07-18 12:27:35.785272',1,'archit','Archit','Jain','architjain.delhi@gmail.com',1,1,'2018-07-18 11:57:45.000000'),(2,'pbkdf2_sha256$100000$bcNrScOGLvxM$9HGAPAuv8BHhofwkADbde7o7PqHFF66+Vk5o3Dthf24=',NULL,1,'admin','Jagdish','Verma','jagdish@nith.ac.in',1,1,'2018-07-18 12:02:56.000000');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
INSERT INTO `auth_user_groups` VALUES (2,1,1),(1,2,1);
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2018-07-18 11:58:20.821621','1','Admin',1,'[{\"added\": {}}]',15,1),(2,'2018-07-18 11:59:17.800072','2','Student',1,'[{\"added\": {}}]',15,1),(3,'2018-07-18 11:59:46.669214','3','Registration Staff',1,'[{\"added\": {}}]',15,1),(4,'2018-07-18 12:00:30.257758','4','Administraion Staff',1,'[{\"added\": {}}]',15,1),(5,'2018-07-18 12:00:57.068254','5','Library Staff',1,'[{\"added\": {}}]',15,1),(6,'2018-07-18 12:01:13.160727','6','Hostel Staff',1,'[{\"added\": {}}]',15,1),(7,'2018-07-18 12:02:04.315143','7','Department Staff',1,'[{\"added\": {}}]',15,1),(8,'2018-07-18 12:02:56.624453','2','admin',1,'[{\"added\": {}}]',13,1),(9,'2018-07-18 12:03:22.506280','2','admin',2,'[{\"changed\": {\"fields\": [\"first_name\", \"last_name\", \"email\", \"is_staff\", \"is_superuser\", \"groups\"]}}]',13,1),(10,'2018-07-18 12:03:40.909762','1','archit',2,'[{\"changed\": {\"fields\": [\"first_name\", \"last_name\", \"groups\"]}}]',13,1),(11,'2018-07-18 12:08:55.479797','CBSE','CBSE',1,'[{\"added\": {}}]',7,1),(12,'2018-07-18 12:10:26.658004','ICSE','ICSE',1,'[{\"added\": {}}]',7,1),(13,'2018-07-18 12:12:14.240709','OP','OP',1,'[{\"added\": {}}]',10,1),(14,'2018-07-18 12:12:29.716625','OBC','OBC',1,'[{\"added\": {}}]',10,1),(15,'2018-07-18 12:12:43.073083','SC','SC',1,'[{\"added\": {}}]',10,1),(16,'2018-07-18 12:12:54.577071','SC','SC',2,'[{\"changed\": {\"fields\": [\"full_name\"]}}]',10,1),(17,'2018-07-18 12:14:14.625331','ST','ST',1,'[{\"added\": {}}]',10,1),(18,'2018-07-18 12:14:24.329178','OPPwD','OPPwD',1,'[{\"added\": {}}]',10,1),(19,'2018-07-18 12:14:37.344150','OBCPwD','OBCPwD',1,'[{\"added\": {}}]',10,1),(20,'2018-07-18 12:14:51.867960','SCPwD','SCPwD',1,'[{\"added\": {}}]',10,1),(21,'2018-07-18 12:15:28.572065','STPwd','STPwd',1,'[{\"added\": {}}]',10,1),(22,'2018-07-18 12:16:13.593357','1','Provisional Admission Letter',1,'[{\"added\": {}}]',3,1),(23,'2018-07-18 12:16:20.114515','2','Four Colored Photographs',1,'[{\"added\": {}}]',3,1),(24,'2018-07-18 12:16:51.278443','3','JEE (MAIN) Score Card',1,'[{\"added\": {}}]',3,1),(25,'2018-07-18 12:16:55.678781','4','JEE (MAIN) Admit Card',1,'[{\"added\": {}}]',3,1),(26,'2018-07-18 12:17:32.250427','5','Class 10th (High School) Board Mark Sheet/Certificate',1,'[{\"added\": {}}]',3,1),(27,'2018-07-18 12:17:43.893198','6','Class 12th Marksheet and Pass Certificate',1,'[{\"added\": {}}]',3,1),(28,'2018-07-18 12:17:49.680215','7','Conduct/Character Certificate',1,'[{\"added\": {}}]',3,1),(29,'2018-07-18 12:17:52.862761','8','Migration/Transfer Certificate',1,'[{\"added\": {}}]',3,1),(30,'2018-07-18 12:17:56.691243','9','Photo ID Proof',1,'[{\"added\": {}}]',3,1),(31,'2018-07-18 12:18:08.349604','10','Category Certificate (OBC/SC/ST)',1,'[{\"added\": {}}]',3,1),(32,'2018-07-18 12:18:19.069824','11','Undertaking (for OBC-NCL Candidates only)',1,'[{\"added\": {}}]',3,1),(33,'2018-07-18 12:18:26.457316','12','Medical Fitness Certificate',1,'[{\"added\": {}}]',3,1),(34,'2018-07-18 12:18:35.559490','13','Certificate of Person with Disability',1,'[{\"added\": {}}]',3,1),(35,'2018-07-18 12:18:40.858049','14','Income Certificate',1,'[{\"added\": {}}]',3,1),(36,'2018-07-18 12:18:54.010348','15','Undertaking by student (Institutional)',1,'[{\"added\": {}}]',3,1),(37,'2018-07-18 12:19:00.853012','16','Affidavit (for Study Gap)',1,'[{\"added\": {}}]',3,1),(38,'2018-07-18 12:19:09.407033','17','Affidavit by Student [ Anti-Ragging ]',1,'[{\"added\": {}}]',3,1),(39,'2018-07-18 12:19:13.661394','18','Affidavit by Parent/Guardian [ Anti-Ragging ]',1,'[{\"added\": {}}]',3,1),(40,'2018-07-18 12:20:15.561372','B.Tech.','B.Tech.',1,'[{\"added\": {}}]',9,1),(41,'2018-07-18 12:20:28.134250','B.Arch.','B.Arch.',1,'[{\"added\": {}}]',9,1),(42,'2018-07-18 12:20:39.128813','Dual Degree','Dual Degree',1,'[{\"added\": {}}]',9,1),(43,'2018-07-18 12:21:06.076748','CE','Civil Engineering',1,'[{\"added\": {}}]',2,1),(44,'2018-07-18 12:21:20.298485','EE','Electrical Engineering',1,'[{\"added\": {}}]',2,1),(45,'2018-07-18 12:21:38.371948','ME','Mechanical Engineering',1,'[{\"added\": {}}]',2,1),(46,'2018-07-18 12:21:56.729880','ECE','Electronics and Communication Engineering',1,'[{\"added\": {}}]',2,1),(47,'2018-07-18 12:22:10.266076','CSE','Computer Science and Engineering',1,'[{\"added\": {}}]',2,1),(48,'2018-07-18 12:22:29.035561','Archi','Architecture',1,'[{\"added\": {}}]',2,1),(49,'2018-07-18 12:22:59.214819','CHE','Chemical Engineering',1,'[{\"added\": {}}]',2,1),(50,'2018-07-18 12:23:15.798491','CMSE','Centre for Material Science and Engineering',1,'[{\"added\": {}}]',2,1),(51,'2018-07-18 12:23:53.795064','CSE (DUAL)','Computer Science and Engineering (DUAL)',1,'[{\"added\": {}}]',2,1),(52,'2018-07-18 12:24:13.690477','ECE (DUAL)','Electronics and Communication Engineering (DUAL)',1,'[{\"added\": {}}]',2,1),(53,'2018-07-18 12:24:32.970252','CSE (IIIT Una)','Computer Science and Engineering (IIIT Una)',1,'[{\"added\": {}}]',2,1),(54,'2018-07-18 12:24:54.574332','ECE (IIIT Una)','Electronics and Communication Engineering (IIIT Una)',1,'[{\"added\": {}}]',2,1),(55,'2018-07-18 12:25:11.989889','IT (IIIT Una)','Information Technology (IIIT Una)',1,'[{\"added\": {}}]',2,1),(56,'2018-07-18 12:25:34.241367','CSE (IIIT Una)','Computer Science and Engineering (IIIT Una)',2,'[{\"changed\": {\"fields\": [\"code\"]}}]',2,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (12,'admin','logentry'),(15,'auth','group'),(14,'auth','permission'),(13,'auth','user'),(16,'contenttypes','contenttype'),(17,'sessions','session'),(7,'sorp_app','board'),(10,'sorp_app','category'),(6,'sorp_app','documentinfo'),(3,'sorp_app','documents'),(4,'sorp_app','due'),(1,'sorp_app','result'),(5,'sorp_app','studentfirstfeestatus'),(8,'sorp_app','studentinfo'),(11,'sorp_app','subjects'),(2,'sorp_app','ugbranch'),(9,'sorp_app','ugclass');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2018-07-18 11:54:25.989005'),(2,'auth','0001_initial','2018-07-18 11:54:35.247564'),(3,'admin','0001_initial','2018-07-18 11:54:37.124868'),(4,'admin','0002_logentry_remove_auto_add','2018-07-18 11:54:37.170079'),(5,'contenttypes','0002_remove_content_type_name','2018-07-18 11:54:38.509067'),(6,'auth','0002_alter_permission_name_max_length','2018-07-18 11:54:38.645492'),(7,'auth','0003_alter_user_email_max_length','2018-07-18 11:54:38.778937'),(8,'auth','0004_alter_user_username_opts','2018-07-18 11:54:38.837934'),(9,'auth','0005_alter_user_last_login_null','2018-07-18 11:54:39.635783'),(10,'auth','0006_require_contenttypes_0002','2018-07-18 11:54:39.669955'),(11,'auth','0007_alter_validators_add_error_messages','2018-07-18 11:54:39.717680'),(12,'auth','0008_alter_user_username_max_length','2018-07-18 11:54:40.039368'),(13,'auth','0009_alter_user_last_name_max_length','2018-07-18 11:54:40.162378'),(14,'sessions','0001_initial','2018-07-18 11:54:40.731527'),(15,'sorp_app','0001_initial','2018-07-18 11:55:03.930229'),(16,'sorp_app','0002_auto_20180718_1743','2018-07-18 12:14:00.289554');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sorp_app_board`
--

DROP TABLE IF EXISTS `sorp_app_board`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sorp_app_board` (
  `id` smallint(6) NOT NULL,
  `name` varchar(16) NOT NULL,
  `full_name` varchar(128) NOT NULL,
  PRIMARY KEY (`name`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sorp_app_board`
--

LOCK TABLES `sorp_app_board` WRITE;
/*!40000 ALTER TABLE `sorp_app_board` DISABLE KEYS */;
INSERT INTO `sorp_app_board` VALUES (1,'CBSE','Central Board of Secondary Education'),(2,'ICSE','Indian Secondary of Secondary Education');
/*!40000 ALTER TABLE `sorp_app_board` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sorp_app_category`
--

DROP TABLE IF EXISTS `sorp_app_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sorp_app_category` (
  `id` smallint(6) NOT NULL,
  `name` varchar(16) NOT NULL,
  `full_name` varchar(64) NOT NULL,
  PRIMARY KEY (`name`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sorp_app_category`
--

LOCK TABLES `sorp_app_category` WRITE;
/*!40000 ALTER TABLE `sorp_app_category` DISABLE KEYS */;
INSERT INTO `sorp_app_category` VALUES (2,'OBC','Other Backward Class'),(6,'OBCPwD','Other Backward Class and Person with Disability'),(1,'OP','Open/General'),(5,'OPPwD','Open and Person with Disability'),(3,'SC','Scheduled Caste'),(7,'SCPwD','Scheduled Caste and Person with Disability'),(4,'ST','Scheduled Tribe'),(8,'STPwd','Scheduled Tribe and Person with Disability');
/*!40000 ALTER TABLE `sorp_app_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sorp_app_documentinfo`
--

DROP TABLE IF EXISTS `sorp_app_documentinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sorp_app_documentinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `submitted` varchar(3) NOT NULL,
  `document_id` int(11) NOT NULL,
  `student_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `sorp_app_documentinf_document_id_80c5261b_fk_sorp_app_` (`document_id`),
  KEY `sorp_app_documentinf_student_id_ce107bea_fk_sorp_app_` (`student_id`),
  CONSTRAINT `sorp_app_documentinf_document_id_80c5261b_fk_sorp_app_` FOREIGN KEY (`document_id`) REFERENCES `sorp_app_documents` (`id`),
  CONSTRAINT `sorp_app_documentinf_student_id_ce107bea_fk_sorp_app_` FOREIGN KEY (`student_id`) REFERENCES `sorp_app_studentinfo` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sorp_app_documentinfo`
--

LOCK TABLES `sorp_app_documentinfo` WRITE;
/*!40000 ALTER TABLE `sorp_app_documentinfo` DISABLE KEYS */;
/*!40000 ALTER TABLE `sorp_app_documentinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sorp_app_documents`
--

DROP TABLE IF EXISTS `sorp_app_documents`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sorp_app_documents` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `doc_name` varchar(512) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sorp_app_documents`
--

LOCK TABLES `sorp_app_documents` WRITE;
/*!40000 ALTER TABLE `sorp_app_documents` DISABLE KEYS */;
INSERT INTO `sorp_app_documents` VALUES (1,'Provisional Admission Letter'),(2,'Four Colored Photographs'),(3,'JEE (MAIN) Score Card'),(4,'JEE (MAIN) Admit Card'),(5,'Class 10th (High School) Board Mark Sheet/Certificate'),(6,'Class 12th Marksheet and Pass Certificate'),(7,'Conduct/Character Certificate'),(8,'Migration/Transfer Certificate'),(9,'Photo ID Proof'),(10,'Category Certificate (OBC/SC/ST)'),(11,'Undertaking (for OBC-NCL Candidates only)'),(12,'Medical Fitness Certificate'),(13,'Certificate of Person with Disability'),(14,'Income Certificate'),(15,'Undertaking by student (Institutional)'),(16,'Affidavit (for Study Gap)'),(17,'Affidavit by Student [ Anti-Ragging ]'),(18,'Affidavit by Parent/Guardian [ Anti-Ragging ]');
/*!40000 ALTER TABLE `sorp_app_documents` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sorp_app_due`
--

DROP TABLE IF EXISTS `sorp_app_due`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sorp_app_due` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `library_due` decimal(10,4) NOT NULL,
  `hostel_due` decimal(10,4) NOT NULL,
  `academic_due` decimal(10,4) NOT NULL,
  `roll_no` varchar(16) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `roll_no` (`roll_no`),
  CONSTRAINT `sorp_app_due_roll_no_73509948_fk_sorp_app_studentinfo_roll_no` FOREIGN KEY (`roll_no`) REFERENCES `sorp_app_studentinfo` (`roll_no`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sorp_app_due`
--

LOCK TABLES `sorp_app_due` WRITE;
/*!40000 ALTER TABLE `sorp_app_due` DISABLE KEYS */;
/*!40000 ALTER TABLE `sorp_app_due` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sorp_app_result`
--

DROP TABLE IF EXISTS `sorp_app_result`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sorp_app_result` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `semester` smallint(6) NOT NULL,
  `sgpi` decimal(4,2) NOT NULL,
  `cgpi` decimal(4,2) NOT NULL,
  `roll_no` varchar(16) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `sorp_app_result_roll_no_ea38c496_fk_sorp_app_studentinfo_roll_no` (`roll_no`),
  CONSTRAINT `sorp_app_result_roll_no_ea38c496_fk_sorp_app_studentinfo_roll_no` FOREIGN KEY (`roll_no`) REFERENCES `sorp_app_studentinfo` (`roll_no`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sorp_app_result`
--

LOCK TABLES `sorp_app_result` WRITE;
/*!40000 ALTER TABLE `sorp_app_result` DISABLE KEYS */;
/*!40000 ALTER TABLE `sorp_app_result` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sorp_app_studentfirstfeestatus`
--

DROP TABLE IF EXISTS `sorp_app_studentfirstfeestatus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sorp_app_studentfirstfeestatus` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fee_josaa_amount` int(10) unsigned NOT NULL,
  `fee_josaa_date` date NOT NULL,
  `fee_NITH_amount` int(10) unsigned NOT NULL,
  `fee_nith_date` date NOT NULL,
  `fee_nith_receipt_no` varchar(32) NOT NULL,
  `fee_total` int(10) unsigned NOT NULL,
  `student_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `student_id` (`student_id`),
  CONSTRAINT `sorp_app_studentfirs_student_id_1b824fab_fk_sorp_app_` FOREIGN KEY (`student_id`) REFERENCES `sorp_app_studentinfo` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sorp_app_studentfirstfeestatus`
--

LOCK TABLES `sorp_app_studentfirstfeestatus` WRITE;
/*!40000 ALTER TABLE `sorp_app_studentfirstfeestatus` DISABLE KEYS */;
/*!40000 ALTER TABLE `sorp_app_studentfirstfeestatus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sorp_app_studentinfo`
--

DROP TABLE IF EXISTS `sorp_app_studentinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sorp_app_studentinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `reg_staff` varchar(50) NOT NULL,
  `img` varchar(100) NOT NULL,
  `year_of_admission` smallint(6) NOT NULL,
  `active_status` tinyint(1) NOT NULL,
  `ug_sem` smallint(6) NOT NULL,
  `date_of_admission` date NOT NULL,
  `institute` varchar(16) NOT NULL,
  `name_eng` varchar(64) NOT NULL,
  `name_hindi` varchar(64) NOT NULL,
  `email` varchar(254) NOT NULL,
  `gender` varchar(8) NOT NULL,
  `dob` date NOT NULL,
  `religion` varchar(16) NOT NULL,
  `contact` varchar(16) NOT NULL,
  `aadhar_no` varchar(16) NOT NULL,
  `area` varchar(16) NOT NULL,
  `b_country` varchar(32) NOT NULL,
  `b_state` varchar(32) NOT NULL,
  `nearest_rs` varchar(64) NOT NULL,
  `corr_addr` varchar(256) NOT NULL,
  `perm_addr` varchar(256) NOT NULL,
  `jee_roll_no` bigint(20) NOT NULL,
  `jee_score` int(10) unsigned NOT NULL,
  `jee_ai_rank` int(10) unsigned NOT NULL,
  `jee_cat_rank` int(10) unsigned DEFAULT NULL,
  `int_country` varchar(32) NOT NULL,
  `int_state` varchar(32) NOT NULL,
  `12th Percentage` decimal(5,3) NOT NULL,
  `10+2 Pass Year` int(11) NOT NULL,
  `12th School type` varchar(16) NOT NULL,
  `12th School Area` varchar(8) NOT NULL,
  `12th School name` varchar(64) NOT NULL,
  `hosteler` tinyint(1) NOT NULL,
  `hostel_name` varchar(16) DEFAULT NULL,
  `entry_no` int(10) unsigned NOT NULL,
  `reg_no` varchar(64) NOT NULL,
  `roll_no` varchar(16) NOT NULL,
  `father_name` varchar(64) NOT NULL,
  `father_contact` varchar(16) NOT NULL,
  `father_email` varchar(254) NOT NULL,
  `mother_name` varchar(64) NOT NULL,
  `mother_contact` varchar(16) NOT NULL,
  `mother_email` varchar(254) NOT NULL,
  `guardian_name` varchar(64) NOT NULL,
  `guardian_contact` varchar(16) NOT NULL,
  `guardian_email` varchar(254) NOT NULL,
  `family_income` int(10) unsigned NOT NULL,
  `fee_waiver` varchar(64) NOT NULL,
  `Admitted Category` varchar(16) NOT NULL,
  `Main Category` varchar(16) NOT NULL,
  `12th Board` varchar(16) NOT NULL,
  `UGBranch` varchar(32) NOT NULL,
  `UGClass` varchar(16) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `aadhar_no` (`aadhar_no`),
  UNIQUE KEY `entry_no` (`entry_no`),
  UNIQUE KEY `reg_no` (`reg_no`),
  UNIQUE KEY `roll_no` (`roll_no`),
  UNIQUE KEY `user_id` (`user_id`),
  KEY `sorp_app_studentinfo_Admitted Category_d7fa56fe_fk_sorp_app_` (`Admitted Category`),
  KEY `sorp_app_studentinfo_Main Category_e42fce98_fk_sorp_app_` (`Main Category`),
  KEY `sorp_app_studentinfo_12th Board_1429c4be_fk_sorp_app_board_name` (`12th Board`),
  KEY `sorp_app_studentinfo_UGBranch_7191284b_fk_sorp_app_ugbranch_name` (`UGBranch`),
  KEY `sorp_app_studentinfo_UGClass_9558ff8b_fk_sorp_app_ugclass_name` (`UGClass`),
  CONSTRAINT `sorp_app_studentinfo_12th Board_1429c4be_fk_sorp_app_board_name` FOREIGN KEY (`12th Board`) REFERENCES `sorp_app_board` (`name`),
  CONSTRAINT `sorp_app_studentinfo_Admitted Category_d7fa56fe_fk_sorp_app_` FOREIGN KEY (`Admitted Category`) REFERENCES `sorp_app_category` (`name`),
  CONSTRAINT `sorp_app_studentinfo_Main Category_e42fce98_fk_sorp_app_` FOREIGN KEY (`Main Category`) REFERENCES `sorp_app_category` (`name`),
  CONSTRAINT `sorp_app_studentinfo_UGBranch_7191284b_fk_sorp_app_ugbranch_name` FOREIGN KEY (`UGBranch`) REFERENCES `sorp_app_ugbranch` (`name`),
  CONSTRAINT `sorp_app_studentinfo_UGClass_9558ff8b_fk_sorp_app_ugclass_name` FOREIGN KEY (`UGClass`) REFERENCES `sorp_app_ugclass` (`name`),
  CONSTRAINT `sorp_app_studentinfo_user_id_209aa733_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sorp_app_studentinfo`
--

LOCK TABLES `sorp_app_studentinfo` WRITE;
/*!40000 ALTER TABLE `sorp_app_studentinfo` DISABLE KEYS */;
/*!40000 ALTER TABLE `sorp_app_studentinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sorp_app_subjects`
--

DROP TABLE IF EXISTS `sorp_app_subjects`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sorp_app_subjects` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `year_onwards` smallint(6) NOT NULL,
  `semester` int(11) NOT NULL,
  `sub_code` varchar(16) NOT NULL,
  `sub_name` varchar(256) NOT NULL,
  `sub_L` smallint(6) NOT NULL,
  `sub_T` smallint(6) NOT NULL,
  `sub_P` smallint(6) NOT NULL,
  `sub_C` smallint(6) NOT NULL,
  `branch` varchar(32) NOT NULL,
  `class` varchar(16) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `sorp_app_subjects_branch_8d466ba5_fk_sorp_app_ugbranch_name` (`branch`),
  KEY `sorp_app_subjects_class_d188d3f1_fk_sorp_app_ugclass_name` (`class`),
  CONSTRAINT `sorp_app_subjects_branch_8d466ba5_fk_sorp_app_ugbranch_name` FOREIGN KEY (`branch`) REFERENCES `sorp_app_ugbranch` (`name`),
  CONSTRAINT `sorp_app_subjects_class_d188d3f1_fk_sorp_app_ugclass_name` FOREIGN KEY (`class`) REFERENCES `sorp_app_ugclass` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sorp_app_subjects`
--

LOCK TABLES `sorp_app_subjects` WRITE;
/*!40000 ALTER TABLE `sorp_app_subjects` DISABLE KEYS */;
/*!40000 ALTER TABLE `sorp_app_subjects` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sorp_app_ugbranch`
--

DROP TABLE IF EXISTS `sorp_app_ugbranch`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sorp_app_ugbranch` (
  `id` smallint(6) NOT NULL,
  `name` varchar(32) NOT NULL,
  `full_name` varchar(128) NOT NULL,
  `code` varchar(16) NOT NULL,
  `section` varchar(8) NOT NULL,
  PRIMARY KEY (`name`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sorp_app_ugbranch`
--

LOCK TABLES `sorp_app_ugbranch` WRITE;
/*!40000 ALTER TABLE `sorp_app_ugbranch` DISABLE KEYS */;
INSERT INTO `sorp_app_ugbranch` VALUES (6,'Archi','Architecture','6','A'),(1,'CE','Civil Engineering','1','A'),(7,'CHE','Chemical Engineering','7','A'),(8,'CMSE','Centre for Material Science and Engineering','8','A'),(5,'CSE','Computer Science and Engineering','5','A'),(9,'CSE (DUAL)','Computer Science and Engineering (DUAL)','MI5','A'),(11,'CSE (IIIT Una)','Computer Science and Engineering (IIIT Una)','IIITU1','1'),(4,'ECE','Electronics and Communication Engineering','4','A'),(10,'ECE (DUAL)','Electronics and Communication Engineering (DUAL)','MI4','A'),(12,'ECE (IIIT Una)','Electronics and Communication Engineering (IIIT Una)','IIITU2','2'),(2,'EE','Electrical Engineering','2','A'),(13,'IT (IIIT Una)','Information Technology (IIIT Una)','IIITU3','3'),(3,'ME','Mechanical Engineering','3','A');
/*!40000 ALTER TABLE `sorp_app_ugbranch` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sorp_app_ugclass`
--

DROP TABLE IF EXISTS `sorp_app_ugclass`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sorp_app_ugclass` (
  `id` smallint(6) NOT NULL,
  `name` varchar(16) NOT NULL,
  `full_name` varchar(64) NOT NULL,
  PRIMARY KEY (`name`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sorp_app_ugclass`
--

LOCK TABLES `sorp_app_ugclass` WRITE;
/*!40000 ALTER TABLE `sorp_app_ugclass` DISABLE KEYS */;
INSERT INTO `sorp_app_ugclass` VALUES (2,'B.Arch.','Bachelor of Architecture'),(1,'B.Tech.','Bachelor of Technology'),(3,'Dual Degree','Dual Degree');
/*!40000 ALTER TABLE `sorp_app_ugclass` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-07-18 18:02:51
