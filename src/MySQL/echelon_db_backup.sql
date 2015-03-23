CREATE DATABASE  IF NOT EXISTS `echelon` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `echelon`;
-- MySQL dump 10.13  Distrib 5.5.41, for debian-linux-gnu (x86_64)
--
-- Host: bbbtimmy.noip.me    Database: echelon
-- ------------------------------------------------------
-- Server version	5.5.41-0+wheezy1

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
-- Table structure for table `app_course`
--

DROP TABLE IF EXISTS `app_course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_course` (
  `name` varchar(120) NOT NULL,
  `department` varchar(120) NOT NULL,
  `number` int(11) NOT NULL,
  `deptnum` varchar(120) NOT NULL,
  `type` varchar(120) DEFAULT NULL,
  `credits` double NOT NULL,
  `yearSpan` varchar(120) DEFAULT NULL,
  PRIMARY KEY (`deptnum`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_course`
--

LOCK TABLES `app_course` WRITE;
/*!40000 ALTER TABLE `app_course` DISABLE KEYS */;
INSERT INTO `app_course` VALUES ('FLIGHT CONTROL SYSTEMS','AERO',480,'AERO480',NULL,3,'14-15'),('AVIONIC NAVIGATION SYSTEMS','AERO',482,'AERO482',NULL,3,'14-15'),('RECREATION/LEISURE IN CANADA','AHSC',242,'AHSC242',NULL,3,'14-15'),('INTRODUCTION TO CULTURE','ANTH',202,'ANTH202',NULL,3,'14-15'),('TECHNOLOGY & CONTEMP. ART','ARTH',353,'ARTH353',NULL,3,'14-15'),('ELEMENTARY GENETICS','BIOL',206,'BIOL206',NULL,3,'14-15'),('BIODIVERSITY AND ECOLOGY','BIOL',226,'BIOL226',NULL,3,'14-15'),('MOLECULAR & GENERAL GENETICS','BIOL',261,'BIOL261',NULL,3,'14-15'),('DISCOVERING BIOTECHNOLOGY','CHEM',209,'CHEM209',NULL,3,'14-15'),('INTRO ANALYTICAL CHEMISTRY I','CHEM',217,'CHEM217',NULL,3,'14-15'),('INTRO - ORGANIC CHEMISTRY I','CHEM',221,'CHEM221',NULL,3,'14-15'),('PHYS.CHEM I:THERMODYNAMICS','CHEM',234,'CHEM234',NULL,3,'14-15'),('INTRO CLASSICAL ARCHAEOLOGY','CLAS',266,'CLAS266',NULL,3,'14-15'),('INTRO TO REAL-TIME SYSTEMS','COEN',320,'COEN320',NULL,3,'14-15'),('MATH. FOR COMPUTER SCIENCE','COMP',232,'COMP232',NULL,3,'14-15'),('OBJ-ORIENTED PROGRAMMING I','COMP',248,'COMP248',NULL,3,'14-15'),('OBJ-ORIENTED PROGRAMMING II','COMP',249,'COMP249',NULL,3,'14-15'),('INTRO/THEORETICAL COMP SCI','COMP',335,'COMP335',NULL,3,'14-15'),('ADVANCED PROGRAM DESIGN, C++','COMP',345,'COMP345',NULL,4,'14-15'),('OPERATING SYSTEMS','COMP',346,'COMP346',NULL,4,'14-15'),('PRIN./PROGRAMMING LANGUAGES','COMP',348,'COMP348',NULL,3,'14-15'),('DATA STRUCTURES + ALGORITHMS','COMP',352,'COMP352',NULL,3,'14-15'),('DATABASES','COMP',353,'COMP353',NULL,4,'14-15'),('ELEMENTARY NUMERICAL METHODS','COMP',361,'COMP361',NULL,3,'14-15'),('COMPUTER GRAPHICS','COMP',371,'COMP371',NULL,4,'14-15'),('INTRO. TO GAME DEVELOPMENT','COMP',376,'COMP376',NULL,4,'14-15'),('MULTICORE PROGRAMMING','COMP',426,'COMP426',NULL,4,'14-15'),('PARALLEL PROGRAMMING','COMP',428,'COMP428',NULL,4,'14-15'),('COMPILER DESIGN','COMP',442,'COMP442',NULL,4,'14-15'),('DATA COMM + COMP NETWORKS','COMP',445,'COMP445',NULL,4,'14-15'),('DESIGN+ANALYSIS/ALGORITHMS','COMP',465,'COMP465',NULL,3,'14-15'),('ARTIFICIAL INTELLIGENCE','COMP',472,'COMP472',NULL,4,'14-15'),('PATTERN RECOGNITION','COMP',473,'COMP473',NULL,4,'14-15'),('INTELLIGENT SYSTEMS','COMP',474,'COMP474',NULL,4,'14-15'),('ADVANCED GAME DEVELOPMENT','COMP',476,'COMP476',NULL,4,'14-15'),('ANIMATION FOR COMPUTER GAMES','COMP',477,'COMP477',NULL,4,'14-15'),('IMAGE PROCESSING','COMP',478,'COMP478',NULL,4,'14-15'),('INFO. RETRIEVAL & WEB SEARCH','COMP',479,'COMP479',NULL,4,'14-15'),('MASS COMMUNICATION','COMS',360,'COMS360',NULL,3,'14-15'),('INTRODUCTION-MICROECONOMICS','ECON',201,'ECON201',NULL,3,'14-15'),('INTRODUCTION-MACROECONOMICS','ECON',203,'ECON203',NULL,3,'14-15'),('INTRO TO PHILOSOPHY OF EDUC','EDUC',230,'EDUC230',NULL,3,'14-15'),('PRINCIPLES OF ELEC. ENGG.','ELEC',275,'ELEC275',NULL,3,'14-15'),('TECH. WRITING + COMMUNIC N.','ENCS',282,'ENCS282',NULL,3,'14-15'),('INN.&CRITICL; THKNG SCI&TECH;','ENCS',483,'ENCS483',NULL,3,'14-15'),('PROFESS L. PRACTICE+RESPONS.','ENGR',201,'ENGR201',NULL,1.5,'14-15'),('SUSTAIN.DEV.+ENVIRO.STEWART.','ENGR',202,'ENGR202',NULL,1.5,'14-15'),('APP.ORDINARY DIFF.EQUATIONS','ENGR',213,'ENGR213',NULL,3,'14-15'),('APPLIED ADVANCED CALCULUS','ENGR',233,'ENGR233',NULL,3,'14-15'),('ENGR.MGMT.PRINCIP.+ECONOMICS','ENGR',301,'ENGR301',NULL,3,'14-15'),('PROBABILITY+STATISTICS/ENGR.','ENGR',371,'ENGR371',NULL,3,'14-15'),('NUMERICAL METHODS IN ENGR','ENGR',391,'ENGR391',NULL,3,'14-15'),('IMPACT/TECHNOLOGY ON SOCIETY','ENGR',392,'ENGR392',NULL,3,'14-15'),('SPECIAL TECHNICAL REPORT','ENGR',411,'ENGR411',NULL,1.5,'14-15'),('INTRO CULTURE FRANCOPHONE','FLIT',230,'FLIT230',NULL,3,'14-15'),('ENGLISH-CANADIAN FILM','FMST',214,'FMST214',NULL,3,'14-15'),('LE CINEMA QUEBECOIS','FMST',215,'FMST215',NULL,3,'14-15'),('CANADIAN ENVIRONM TAL ISSUES','GEOG',203,'GEOG203',NULL,3,'14-15'),('GLOBAL ENVIRONMENTAL ISSUES','GEOG',204,'GEOG204',NULL,3,'14-15'),('GEOGRAPHY OF GLOBAL CHANGE','GEOG',210,'GEOG210',NULL,3,'14-15'),('PLACE, SPACE AND IDENTITY','GEOG',220,'GEOG220',NULL,3,'14-15'),('INTRO:EUROPEAN HIST TO 1789','HIST',201,'HIST201',NULL,3,'14-15'),('INTRO:EUROPEAN 1789-PRESENT','HIST',202,'HIST202',NULL,3,'14-15'),('CANADA: POST-CONFEDERATION','HIST',205,'HIST205',NULL,3,'14-15'),('FILM IN HISTORY','HIST',281,'HIST281',NULL,3,'14-15'),('THE 20TH C: GLOBAL HISTORY','HIST',283,'HIST283',NULL,3,'14-15'),('INTROINFOLITERACYSKILLS','INST',250,'INST250',NULL,3,'14-15'),('LANG & MIND: CHOMSKYAN PROG','LING',222,'LING222',NULL,3,'14-15'),('SOCIOLINGUISTICS','LING',300,'LING300',NULL,3,'14-15'),('PROBLEMS OF PHILOSOPHY','PHIL',201,'PHIL201',NULL,3,'14-15'),('CRITICAL THINKING','PHIL',210,'PHIL210',NULL,3,'14-15'),('INTRO TO  ETHICS','PHIL',232,'PHIL232',NULL,3,'14-15'),('BIOMEDICAL ETHICS','PHIL',235,'PHIL235',NULL,3,'14-15'),('MODERN TO POSTMODERN','PHIL',275,'PHIL275',NULL,3,'14-15'),('CONTEMPORARY ETHICAL THEORY','PHIL',330,'PHIL330',NULL,3,'14-15'),('OPTICS','PHYS',252,'PHYS252',NULL,3,'14-15'),('ELECTRICITY & MAGNETISM I','PHYS',253,'PHYS253',NULL,3,'14-15'),('THERMODYNAMICS','PHYS',334,'PHYS334',NULL,3,'14-15'),('ELECTRICITY & MAGNETISM II','PHYS',354,'PHYS354',NULL,3,'14-15'),('INTRO TO POLITICAL SCIENCE','POLI',202,'POLI202',NULL,3,'14-15'),('RELIGIONS OF THE WEST','RELI',214,'RELI214',NULL,3,'14-15'),('RELIGIONS OF ASIA','RELI',215,'RELI215',NULL,3,'14-15'),('SELF/OTHER: ID\'TY & ETHICS','RELI',310,'RELI310',NULL,3,'14-15'),('JUSTICE & SOCIAL CONFLICT','RELI',312,'RELI312',NULL,3,'14-15'),('PUBLIC POLICY &INTEREST;','SCPA',201,'SCPA201',NULL,3,'14-15'),('ECON FOR PUB POL&COM; DEV','SCPA',215,'SCPA215',NULL,3,'14-15'),('INTRODUCTION TO SOCIETY','SOCI',203,'SOCI203',NULL,3,'14-15'),('SYSTEM HARDWARE','SOEN',228,'SOEN228',NULL,4,'14-15'),('WEB PROGRAMMING','SOEN',287,'SOEN287',NULL,3,'14-15'),('SYSTEM HARDWARE LAB','SOEN',298,'SOEN298',NULL,1.5,'14-15'),('INFORMATION SYSTEMS SECURITY','SOEN',321,'SOEN321',NULL,3,'14-15'),('INTRO TO FML MTHDS FOR SOEN','SOEN',331,'SOEN331',NULL,3,'14-15'),('SOFTWARE PROCESS','SOEN',341,'SOEN341',NULL,3,'14-15'),('SW REQUIREMENTS + SPECS.','SOEN',342,'SOEN342',NULL,3,'14-15'),('S.W. ARCHITECURE & DESIGN I','SOEN',343,'SOEN343',NULL,3,'14-15'),('S.W. ARCHITECURE & DESIGN II','SOEN',344,'SOEN344',NULL,3,'14-15'),('S.W. TESTING, VERIF & QA','SOEN',345,'SOEN345',NULL,3,'14-15'),('USER INTERFACE DESIGN','SOEN',357,'SOEN357',NULL,3,'14-15'),('MGMT+QUALITY CTRL./SW DEV.','SOEN',384,'SOEN384',NULL,3,'14-15'),('CONTROL SYSTEMS+APPLICATIONS','SOEN',385,'SOEN385',NULL,3,'14-15'),('WEB-BASED ENTER. APP DESIGN','SOEN',387,'SOEN387',NULL,3,'14-15'),('SOFTWARE ENGR. TEAM PROJECT','SOEN',390,'SOEN390',NULL,3,'14-15'),('EMBEDDED SYSTEMS/SOFTWARE','SOEN',422,'SOEN422',NULL,4,'14-15'),('DISTRIBUTED SYSTEMS','SOEN',423,'SOEN423',NULL,4,'14-15'),('WEB SERVICES & APPLICATIONS','SOEN',487,'SOEN487',NULL,4,'14-15'),('CAPSTONE SW ENGR DESIGN PROJ','SOEN',490,'SOEN490',NULL,4,'14-15'),('INTRO. TO BIBLICAL STUDIES','THEO',202,'THEO202',NULL,3,'14-15'),('INTRO.TO CHRISTIAN ETHICS','THEO',204,'THEO204',NULL,3,'14-15'),('RELG. PLURALISM/SECULAR CULT','THEO',233,'THEO233',NULL,3,'14-15'),('INTRO TO HIST. PERSP. IN WS','WSDB',290,'WSDB290',NULL,3,'14-15'),('INTRO CONT.  PERSP.  IN WS','WSDB',291,'WSDB291',NULL,3,'14-15');
/*!40000 ALTER TABLE `app_course` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_course_prerequisites`
--

DROP TABLE IF EXISTS `app_course_prerequisites`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_course_prerequisites` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `from_course_id` varchar(120) NOT NULL,
  `to_course_id` varchar(120) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `from_course_id` (`from_course_id`,`to_course_id`),
  KEY `app_course_prerequisites_fd68de27` (`from_course_id`),
  KEY `app_course_prerequisites_faf76fb8` (`to_course_id`),
  CONSTRAINT `app_course_prerequis_to_course_id_7634c99e_fk_app_course_deptnum` FOREIGN KEY (`to_course_id`) REFERENCES `app_course` (`deptnum`),
  CONSTRAINT `app_course_prerequ_from_course_id_60c80d08_fk_app_course_deptnum` FOREIGN KEY (`from_course_id`) REFERENCES `app_course` (`deptnum`)
) ENGINE=InnoDB AUTO_INCREMENT=72 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_course_prerequisites`
--

LOCK TABLES `app_course_prerequisites` WRITE;
/*!40000 ALTER TABLE `app_course_prerequisites` DISABLE KEYS */;
INSERT INTO `app_course_prerequisites` VALUES (68,'AERO480','SOEN385'),(69,'AERO482','ENGR371'),(70,'AERO482','SOEN385'),(71,'COEN320','COMP346'),(27,'COMP249','COMP248'),(28,'COMP335','COMP232'),(29,'COMP335','COMP249'),(40,'COMP345','COMP352'),(31,'COMP346','COMP352'),(30,'COMP346','SOEN228'),(32,'COMP348','COMP249'),(33,'COMP352','COMP232'),(34,'COMP352','COMP249'),(41,'COMP353','COMP352'),(37,'COMP361','COMP232'),(38,'COMP361','COMP249'),(42,'COMP371','COMP352'),(43,'COMP426','COMP346'),(44,'COMP428','COMP346'),(45,'COMP442','COMP335'),(46,'COMP442','COMP352'),(47,'COMP445','COMP346'),(48,'COMP465','COMP335'),(49,'COMP465','COMP352'),(50,'COMP472','COMP352'),(51,'COMP473','COMP352'),(52,'COMP474','COMP352'),(59,'COMP476','COMP361'),(58,'COMP476','COMP376'),(60,'COMP476','ENGR391'),(62,'COMP477','COMP361'),(61,'COMP477','COMP371'),(63,'COMP477','ENGR391'),(53,'COMP478','COMP352'),(54,'COMP479','ENGR371'),(1,'ELEC275','ENGR213'),(2,'ENGR371','ENGR213'),(36,'ENGR391','COMP248'),(35,'ENGR391','ENGR213'),(3,'ENGR392','ENCS282'),(4,'ENGR392','ENGR201'),(57,'ENGR411','ENCS282'),(39,'PHIL330','PHIL232'),(5,'SOEN287','COMP248'),(6,'SOEN321','COMP346'),(7,'SOEN331','COMP232'),(8,'SOEN331','COMP249'),(9,'SOEN341','COMP352'),(10,'SOEN341','ENCS282'),(11,'SOEN342','SOEN341'),(12,'SOEN343','SOEN341'),(13,'SOEN343','SOEN342'),(14,'SOEN344','SOEN343'),(15,'SOEN345','SOEN341'),(16,'SOEN345','SOEN343'),(17,'SOEN357','SOEN342'),(18,'SOEN384','ENCS282'),(19,'SOEN385','ENGR213'),(20,'SOEN385','ENGR233'),(64,'SOEN387','COMP353'),(66,'SOEN387','SOEN287'),(65,'SOEN387','SOEN341'),(21,'SOEN390','SOEN344'),(22,'SOEN390','SOEN357'),(55,'SOEN422','COMP346'),(56,'SOEN423','COMP346'),(67,'SOEN487','SOEN387'),(23,'SOEN490','SOEN342'),(24,'SOEN490','SOEN343'),(25,'SOEN490','SOEN344'),(26,'SOEN490','SOEN390');
/*!40000 ALTER TABLE `app_course_prerequisites` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_event`
--

DROP TABLE IF EXISTS `app_event`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_event` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `days` varchar(120) NOT NULL,
  `starttime` time NOT NULL,
  `endtime` time NOT NULL,
  `building` varchar(120) NOT NULL,
  `room` int(11) NOT NULL,
  `location` varchar(120) NOT NULL,
  `semester` varchar(120) NOT NULL,
  `yearSpan` varchar(120) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_event`
--

LOCK TABLES `app_event` WRITE;
/*!40000 ALTER TABLE `app_event` DISABLE KEYS */;
/*!40000 ALTER TABLE `app_event` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_lab`
--

DROP TABLE IF EXISTS `app_lab`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_lab` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `section` varchar(120) NOT NULL,
  `course_id` varchar(120) NOT NULL,
  `lecture_id` int(11) NOT NULL,
  `tutorial_id` int(11),
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_lab_section_625131db_uniq` (`section`,`course_id`,`lecture_id`,`tutorial_id`),
  KEY `app_lab_ea134da7` (`course_id`),
  KEY `app_lab_72a11f01` (`lecture_id`),
  KEY `app_lab_b6fbbedb` (`tutorial_id`),
  CONSTRAINT `app_lab_tutorial_id_5b0293ab_fk_app_tutorial_id` FOREIGN KEY (`tutorial_id`) REFERENCES `app_tutorial` (`id`),
  CONSTRAINT `app_lab_course_id_1644a22d_fk_app_course_deptnum` FOREIGN KEY (`course_id`) REFERENCES `app_course` (`deptnum`),
  CONSTRAINT `app_lab_lecture_id_5f442b5e_fk_app_lecture_id` FOREIGN KEY (`lecture_id`) REFERENCES `app_lecture` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_lab`
--

LOCK TABLES `app_lab` WRITE;
/*!40000 ALTER TABLE `app_lab` DISABLE KEYS */;
/*!40000 ALTER TABLE `app_lab` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_lecture`
--

DROP TABLE IF EXISTS `app_lecture`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_lecture` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `section` varchar(120) NOT NULL,
  `session` varchar(120) NOT NULL,
  `isOnline` tinyint(1) NOT NULL,
  `event` time NOT NULL,
  `course_id` varchar(120) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_lecture_section_69b0720e_uniq` (`section`,`course_id`),
  KEY `app_lecture_ea134da7` (`course_id`),
  CONSTRAINT `app_lecture_course_id_44de2ab2_fk_app_course_deptnum` FOREIGN KEY (`course_id`) REFERENCES `app_course` (`deptnum`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_lecture`
--

LOCK TABLES `app_lecture` WRITE;
/*!40000 ALTER TABLE `app_lecture` DISABLE KEYS */;
/*!40000 ALTER TABLE `app_lecture` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_tutorial`
--

DROP TABLE IF EXISTS `app_tutorial`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_tutorial` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `section` varchar(120) NOT NULL,
  `course_id` varchar(120) NOT NULL,
  `lecture_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_tutorial_section_780f6f26_uniq` (`section`,`course_id`,`lecture_id`),
  KEY `app_tutorial_ea134da7` (`course_id`),
  KEY `app_tutorial_72a11f01` (`lecture_id`),
  CONSTRAINT `app_tutorial_lecture_id_58bbe8e0_fk_app_lecture_id` FOREIGN KEY (`lecture_id`) REFERENCES `app_lecture` (`id`),
  CONSTRAINT `app_tutorial_course_id_1650f675_fk_app_course_deptnum` FOREIGN KEY (`course_id`) REFERENCES `app_course` (`deptnum`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_tutorial`
--

LOCK TABLES `app_tutorial` WRITE;
/*!40000 ALTER TABLE `app_tutorial` DISABLE KEYS */;
/*!40000 ALTER TABLE `app_tutorial` ENABLE KEYS */;
UNLOCK TABLES;

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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
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
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_0e939a4f` (`group_id`),
  KEY `auth_group_permissions_8373b171` (`permission_id`),
  CONSTRAINT `auth_group_permission_group_id_6a73295befdf3d06_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_group__permission_id_41019b8511f30c61_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
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
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_417f1b1c` (`content_type_id`),
  CONSTRAINT `auth__content_type_id_78b0d12cfe9cfbee_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=55 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(40,'Can add course',14,'add_course'),(41,'Can change course',14,'change_course'),(42,'Can delete course',14,'delete_course'),(43,'Can add lecture',15,'add_lecture'),(44,'Can change lecture',15,'change_lecture'),(45,'Can delete lecture',15,'delete_lecture'),(46,'Can add tutorial',16,'add_tutorial'),(47,'Can change tutorial',16,'change_tutorial'),(48,'Can delete tutorial',16,'delete_tutorial'),(49,'Can add lab',17,'add_lab'),(50,'Can change lab',17,'change_lab'),(51,'Can delete lab',17,'delete_lab'),(52,'Can add event',18,'add_event'),(53,'Can change event',18,'change_event'),(54,'Can delete event',18,'delete_event');
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
  `last_login` datetime NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$15000$VhTmrZcSGSl2$UiIveGXkAqbOfgT1rQpRU0UmhMSyhXidhFrwpTNySg8=','2015-03-22 22:58:22',1,'foxtrot','','','sniperjefz@hotmail.com',1,1,'2015-02-15 23:01:36'),(3,'pbkdf2_sha256$15000$H2sO9WqJX0yQ$6j6eGRMrF7evRP+9l3pd1YxwFHyajtaeIz/LFLVFD0s=','2015-03-23 21:26:06',1,'root','','','',1,1,'2015-02-26 01:00:04');
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
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_e8701ad4` (`user_id`),
  KEY `auth_user_groups_0e939a4f` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_7aeb9d00d1d19f8f_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_48d8aa830435280c_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
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
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_e8701ad4` (`user_id`),
  KEY `auth_user_user_permissions_8373b171` (`permission_id`),
  CONSTRAINT `auth_user_user_permissi_user_id_62435a95d3f27026_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `auth_user_u_permission_id_2d74ae2dc57d2962_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
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
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_417f1b1c` (`content_type_id`),
  KEY `django_admin_log_e8701ad4` (`user_id`),
  CONSTRAINT `django_admin_log_user_id_44ff872c38b2c95b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_content_type_id_d695a21803a3786_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
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
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_22818de001b4a693_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'log entry','admin','logentry'),(2,'permission','auth','permission'),(3,'group','auth','group'),(4,'user','auth','user'),(5,'content type','contenttypes','contenttype'),(6,'session','sessions','session'),(14,'course','app','course'),(15,'lecture','app','lecture'),(16,'tutorial','app','tutorial'),(17,'lab','app','lab'),(18,'event','app','event');
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
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (2,'auth','0001_initial','2015-02-15 22:52:39'),(3,'admin','0001_initial','2015-02-15 22:52:40'),(4,'sessions','0001_initial','2015-02-15 22:52:40'),(9,'contenttypes','0001_initial','2015-03-16 19:25:26'),(13,'app','0001_initial','2015-03-23 22:28:43');
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
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('10nl8qdcybgxra5b6konfua5x5cy20nj','MDI2NjJhMWZkYzFjNDk5ZDkzZWQxMzQ2ZGY0ZTE2ZDY2MDliZDJhMjp7fQ==','2015-04-05 22:33:09'),('2c49etizbfysj5bme7triaqsiefd2xp7','MDI2NjJhMWZkYzFjNDk5ZDkzZWQxMzQ2ZGY0ZTE2ZDY2MDliZDJhMjp7fQ==','2015-04-05 22:33:19'),('3yi6hedd8dove2zmcuop2clislb7a5nw','MWExOTFkNWM5NzExMjMyZjBlN2ViZDQxYjlkMjBjYmNhYWM0YzBlYjp7Il9hdXRoX3VzZXJfaWQiOjMsIl9hdXRoX3VzZXJfaGFzaCI6ImU0OWNlNjNiNmI2YWY5MjkzOWM4NmJiODhiMzU0Y2VmNjljZGU4M2EiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCJ9','2015-03-17 13:56:49'),('481f9es812mgbjmg4lue4elmhvitqtop','OTAzNDdjZDYwNDU2YzZiZDMxZjMzYTdmMDUwM2ZkNDdlNzhlODUxYTp7Il9hdXRoX3VzZXJfaGFzaCI6ImU0OWNlNjNiNmI2YWY5MjkzOWM4NmJiODhiMzU0Y2VmNjljZGU4M2EiLCJfYXV0aF91c2VyX2lkIjozLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCJ9','2015-04-06 20:42:27'),('4tszuky9iunvhule1tf9551bx3y0fiek','MTNjOWMwMzk5NjI4NDVmYjgyOTkyNGFmNWJmYzc0MjgxYmYzZDk3Zjp7Il9hdXRoX3VzZXJfaGFzaCI6ImE3NjdlYjUyZGZmZDc2OTU3ZmY3ODJlYzlkMzlhNjVkOGU2MDdlODEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9','2015-04-05 22:58:22'),('508rwz0d9nn5c93jltx3nac8siszapho','ZGY1YjgxMmZjNTI1N2YzNjQ4N2EyZTA4MjU0ZGQwYmY2ODRiNjRiYjp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiZTQ5Y2U2M2I2YjZhZjkyOTM5Yzg2YmI4OGIzNTRjZWY2OWNkZTgzYSIsIl9hdXRoX3VzZXJfaWQiOjN9','2015-04-06 21:25:13'),('76ks8cxnhpt67198sdf53s4yfvctzwgw','MDI2NjJhMWZkYzFjNDk5ZDkzZWQxMzQ2ZGY0ZTE2ZDY2MDliZDJhMjp7fQ==','2015-03-18 14:56:38'),('8m6i3gb5o9emdqi8nfwkpcmc3ifcfjg7','ZWJhNjg0OGQwYzQ2YTNmOTZmNzdkNzBhZWM5NTcxMmJkMDg1ODJiNTp7Il9hdXRoX3VzZXJfaWQiOjMsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiZTQ5Y2U2M2I2YjZhZjkyOTM5Yzg2YmI4OGIzNTRjZWY2OWNkZTgzYSJ9','2015-04-06 18:47:10'),('8wcpop83810h005w26aw1nvi6ksdd971','MDI2NjJhMWZkYzFjNDk5ZDkzZWQxMzQ2ZGY0ZTE2ZDY2MDliZDJhMjp7fQ==','2015-04-04 18:39:11'),('alsd3vietc3u51pjni10fk7gz3bu188w','ZGY1YjgxMmZjNTI1N2YzNjQ4N2EyZTA4MjU0ZGQwYmY2ODRiNjRiYjp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiZTQ5Y2U2M2I2YjZhZjkyOTM5Yzg2YmI4OGIzNTRjZWY2OWNkZTgzYSIsIl9hdXRoX3VzZXJfaWQiOjN9','2015-03-12 01:00:31'),('b88agqxhdmmdo616gthzewp4tiudgkcm','MDI2NjJhMWZkYzFjNDk5ZDkzZWQxMzQ2ZGY0ZTE2ZDY2MDliZDJhMjp7fQ==','2015-03-25 23:51:13'),('c4uwtbk5otd0t1yfzdmdjjbqql5cpqrv','MDI2NjJhMWZkYzFjNDk5ZDkzZWQxMzQ2ZGY0ZTE2ZDY2MDliZDJhMjp7fQ==','2015-03-18 14:32:36'),('ctnbcozlm6yky8zs9jorfv2l9be6xt6z','MDI2NjJhMWZkYzFjNDk5ZDkzZWQxMzQ2ZGY0ZTE2ZDY2MDliZDJhMjp7fQ==','2015-04-04 04:25:36'),('eo5z1doy9peiql9qs9niswaezr2c2n7z','N2E5YzRiZDczOTQxNzRiM2VkNWM2Y2I0YTc2NWNjMmM3NzMyMTJhMDp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MywiX2F1dGhfdXNlcl9oYXNoIjoiZTQ5Y2U2M2I2YjZhZjkyOTM5Yzg2YmI4OGIzNTRjZWY2OWNkZTgzYSJ9','2015-03-17 14:20:14'),('ernlsgim6umyv51nanvowdnewv66xdfv','ZWJhNjg0OGQwYzQ2YTNmOTZmNzdkNzBhZWM5NTcxMmJkMDg1ODJiNTp7Il9hdXRoX3VzZXJfaWQiOjMsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiZTQ5Y2U2M2I2YjZhZjkyOTM5Yzg2YmI4OGIzNTRjZWY2OWNkZTgzYSJ9','2015-04-06 15:39:23'),('fujj5rlux2ntkapjdj4sjtreqz0joehj','OTAzNDdjZDYwNDU2YzZiZDMxZjMzYTdmMDUwM2ZkNDdlNzhlODUxYTp7Il9hdXRoX3VzZXJfaGFzaCI6ImU0OWNlNjNiNmI2YWY5MjkzOWM4NmJiODhiMzU0Y2VmNjljZGU4M2EiLCJfYXV0aF91c2VyX2lkIjozLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCJ9','2015-03-21 19:25:45'),('fyqmzb03d4chypethp0itwvig2lw3sgf','ZGY2NjI1MTViZTM1Y2U2ODYxN2QzMDg3NzAwZDczOTg1YTUyZTRlMDp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYTc2N2ViNTJkZmZkNzY5NTdmZjc4MmVjOWQzOWE2NWQ4ZTYwN2U4MSIsIl9hdXRoX3VzZXJfaWQiOjJ9','2015-03-01 23:03:40'),('j0gwsrft6blvpks2dzdf9hv7yae0r8nd','MDI2NjJhMWZkYzFjNDk5ZDkzZWQxMzQ2ZGY0ZTE2ZDY2MDliZDJhMjp7fQ==','2015-04-06 12:14:03'),('jd3uwyuxkm5xtjd2g9hf267zr8tif8sv','ZGY1YjgxMmZjNTI1N2YzNjQ4N2EyZTA4MjU0ZGQwYmY2ODRiNjRiYjp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiZTQ5Y2U2M2I2YjZhZjkyOTM5Yzg2YmI4OGIzNTRjZWY2OWNkZTgzYSIsIl9hdXRoX3VzZXJfaWQiOjN9','2015-04-04 05:55:23'),('jwoymscv5hvc7216b5xgv25apspo1mk7','MDI2NjJhMWZkYzFjNDk5ZDkzZWQxMzQ2ZGY0ZTE2ZDY2MDliZDJhMjp7fQ==','2015-03-18 14:25:27'),('lpwr3hwdkthyf06crgp1xlmbqerr8h5d','MDI2NjJhMWZkYzFjNDk5ZDkzZWQxMzQ2ZGY0ZTE2ZDY2MDliZDJhMjp7fQ==','2015-04-04 03:28:01'),('mj59kvlyewpx6r3wztv19ld5jq2hjhnm','OTAzNDdjZDYwNDU2YzZiZDMxZjMzYTdmMDUwM2ZkNDdlNzhlODUxYTp7Il9hdXRoX3VzZXJfaGFzaCI6ImU0OWNlNjNiNmI2YWY5MjkzOWM4NmJiODhiMzU0Y2VmNjljZGU4M2EiLCJfYXV0aF91c2VyX2lkIjozLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCJ9','2015-04-04 19:08:53'),('nss57z158txp87ukmadss644dcwb47d1','ZGY1YjgxMmZjNTI1N2YzNjQ4N2EyZTA4MjU0ZGQwYmY2ODRiNjRiYjp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiZTQ5Y2U2M2I2YjZhZjkyOTM5Yzg2YmI4OGIzNTRjZWY2OWNkZTgzYSIsIl9hdXRoX3VzZXJfaWQiOjN9','2015-04-02 17:41:45'),('pnrvhu24dnn100x2cec23j63pvpwgqwt','MDI2NjJhMWZkYzFjNDk5ZDkzZWQxMzQ2ZGY0ZTE2ZDY2MDliZDJhMjp7fQ==','2015-03-18 14:29:23'),('powep144jjyse1fqlu98f10ozskhbiyj','MWExOTFkNWM5NzExMjMyZjBlN2ViZDQxYjlkMjBjYmNhYWM0YzBlYjp7Il9hdXRoX3VzZXJfaWQiOjMsIl9hdXRoX3VzZXJfaGFzaCI6ImU0OWNlNjNiNmI2YWY5MjkzOWM4NmJiODhiMzU0Y2VmNjljZGU4M2EiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCJ9','2015-04-04 17:38:14'),('qdrt12a8e6i2z851ojtwasulxwuldwii','ZGY1YjgxMmZjNTI1N2YzNjQ4N2EyZTA4MjU0ZGQwYmY2ODRiNjRiYjp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiZTQ5Y2U2M2I2YjZhZjkyOTM5Yzg2YmI4OGIzNTRjZWY2OWNkZTgzYSIsIl9hdXRoX3VzZXJfaWQiOjN9','2015-04-06 20:43:39'),('r8fiyfh9hd5xlesz1jaxsolzqv23lqi3','MDI2NjJhMWZkYzFjNDk5ZDkzZWQxMzQ2ZGY0ZTE2ZDY2MDliZDJhMjp7fQ==','2015-03-18 14:27:32'),('uucpqj4nbjgy96wx0rwh3bxkickrhoeu','MDI2NjJhMWZkYzFjNDk5ZDkzZWQxMzQ2ZGY0ZTE2ZDY2MDliZDJhMjp7fQ==','2015-04-04 05:57:43'),('vmaad8diyuu075ujfdzkwjaroiprbkld','OTAzNDdjZDYwNDU2YzZiZDMxZjMzYTdmMDUwM2ZkNDdlNzhlODUxYTp7Il9hdXRoX3VzZXJfaGFzaCI6ImU0OWNlNjNiNmI2YWY5MjkzOWM4NmJiODhiMzU0Y2VmNjljZGU4M2EiLCJfYXV0aF91c2VyX2lkIjozLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCJ9','2015-04-06 21:26:06'),('vwpe67cg1wyugtexw1mlfqou0kzshwvd','ZGY1YjgxMmZjNTI1N2YzNjQ4N2EyZTA4MjU0ZGQwYmY2ODRiNjRiYjp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiZTQ5Y2U2M2I2YjZhZjkyOTM5Yzg2YmI4OGIzNTRjZWY2OWNkZTgzYSIsIl9hdXRoX3VzZXJfaWQiOjN9','2015-03-19 01:53:41'),('wml5zzdb4cg8wdlq8268fwseh398boyt','MDI2NjJhMWZkYzFjNDk5ZDkzZWQxMzQ2ZGY0ZTE2ZDY2MDliZDJhMjp7fQ==','2015-04-04 03:28:02'),('x6v9fo1uv75uny1yx8j6mzdx4bsl8h17','MDI2NjJhMWZkYzFjNDk5ZDkzZWQxMzQ2ZGY0ZTE2ZDY2MDliZDJhMjp7fQ==','2015-04-05 22:33:09'),('xwge1newk7p28koisgt60ej1wv34d8gc','MDI2NjJhMWZkYzFjNDk5ZDkzZWQxMzQ2ZGY0ZTE2ZDY2MDliZDJhMjp7fQ==','2015-03-16 21:53:17'),('ynkqmc796cw97z9k1uax6hjfxpjd6xi9','ZWJhNjg0OGQwYzQ2YTNmOTZmNzdkNzBhZWM5NTcxMmJkMDg1ODJiNTp7Il9hdXRoX3VzZXJfaWQiOjMsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiZTQ5Y2U2M2I2YjZhZjkyOTM5Yzg2YmI4OGIzNTRjZWY2OWNkZTgzYSJ9','2015-04-05 22:04:00'),('zkzrlm6113nzqx0hsuroylyj9i2lncwz','MDI2NjJhMWZkYzFjNDk5ZDkzZWQxMzQ2ZGY0ZTE2ZDY2MDliZDJhMjp7fQ==','2015-04-04 05:07:47'),('zwr5fho2lddvnyp17r6wmgb30y5gp3xs','MWExOTFkNWM5NzExMjMyZjBlN2ViZDQxYjlkMjBjYmNhYWM0YzBlYjp7Il9hdXRoX3VzZXJfaWQiOjMsIl9hdXRoX3VzZXJfaGFzaCI6ImU0OWNlNjNiNmI2YWY5MjkzOWM4NmJiODhiMzU0Y2VmNjljZGU4M2EiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCJ9','2015-04-06 12:16:38');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-03-23 19:09:17
