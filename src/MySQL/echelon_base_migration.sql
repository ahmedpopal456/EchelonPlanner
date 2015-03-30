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
-- Table structure for table `app_academicprogram`
--

DROP TABLE IF EXISTS `app_academicprogram`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_academicprogram` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(120) NOT NULL,
  `credits` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_academicprogram`
--

LOCK TABLES `app_academicprogram` WRITE;
/*!40000 ALTER TABLE `app_academicprogram` DISABLE KEYS */;
/*!40000 ALTER TABLE `app_academicprogram` ENABLE KEYS */;
UNLOCK TABLES;

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
  CONSTRAINT `app_course_p_to_course_id_3c5e79fde91bad97_fk_app_course_deptnum` FOREIGN KEY (`to_course_id`) REFERENCES `app_course` (`deptnum`),
  CONSTRAINT `app_course_from_course_id_28a5f31dc21eda46_fk_app_course_deptnum` FOREIGN KEY (`from_course_id`) REFERENCES `app_course` (`deptnum`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_course_prerequisites`
--

LOCK TABLES `app_course_prerequisites` WRITE;
/*!40000 ALTER TABLE `app_course_prerequisites` DISABLE KEYS */;
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
  `building` varchar(120) DEFAULT NULL,
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
  `course_id` varchar(120) DEFAULT NULL,
  `event_id` int(11) DEFAULT NULL,
  `lecture_id` int(11),
  `tutorial_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `event_id` (`event_id`),
  UNIQUE KEY `app_lab_section_4a018e8deeecef8e_uniq` (`section`,`course_id`,`lecture_id`,`tutorial_id`),
  KEY `app_lab_ea134da7` (`course_id`),
  KEY `app_lab_72a11f01` (`lecture_id`),
  KEY `app_lab_b6fbbedb` (`tutorial_id`),
  CONSTRAINT `app_lab_tutorial_id_13e12ea8147acd24_fk_app_tutorial_id` FOREIGN KEY (`tutorial_id`) REFERENCES `app_tutorial` (`id`),
  CONSTRAINT `app_lab_course_id_471223ca08fef175_fk_app_course_deptnum` FOREIGN KEY (`course_id`) REFERENCES `app_course` (`deptnum`),
  CONSTRAINT `app_lab_event_id_7f4e381e5d8f6606_fk_app_event_id` FOREIGN KEY (`event_id`) REFERENCES `app_event` (`id`),
  CONSTRAINT `app_lab_lecture_id_489063728613ca22_fk_app_lecture_id` FOREIGN KEY (`lecture_id`) REFERENCES `app_lecture` (`id`)
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
  `prof` varchar(120) NOT NULL,
  `course_id` varchar(120) DEFAULT NULL,
  `event_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `event_id` (`event_id`),
  UNIQUE KEY `app_lecture_section_551418753ff0cf9e_uniq` (`section`,`course_id`,`session`),
  KEY `app_lecture_ea134da7` (`course_id`),
  CONSTRAINT `app_lecture_event_id_517610aea0a8e987_fk_app_event_id` FOREIGN KEY (`event_id`) REFERENCES `app_event` (`id`),
  CONSTRAINT `app_lecture_course_id_2a298ad762d007d0_fk_app_course_deptnum` FOREIGN KEY (`course_id`) REFERENCES `app_course` (`deptnum`)
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
-- Table structure for table `app_option`
--

DROP TABLE IF EXISTS `app_option`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_option` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(120) NOT NULL,
  `option` int(11) NOT NULL,
  `type` int(11) NOT NULL,
  `academicprogram_id` int(11) NOT NULL,
  `course_id` varchar(120) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app_option_15134093` (`academicprogram_id`),
  KEY `app_option_ea134da7` (`course_id`),
  CONSTRAINT `app_option_course_id_d6436598d0d3885_fk_app_course_deptnum` FOREIGN KEY (`course_id`) REFERENCES `app_course` (`deptnum`),
  CONSTRAINT `app_academicprogram_id_e5240792e7c39c9_fk_app_academicprogram_id` FOREIGN KEY (`academicprogram_id`) REFERENCES `app_academicprogram` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_option`
--

LOCK TABLES `app_option` WRITE;
/*!40000 ALTER TABLE `app_option` DISABLE KEYS */;
/*!40000 ALTER TABLE `app_option` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_professor`
--

DROP TABLE IF EXISTS `app_professor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_professor` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `isEngineer` tinyint(1) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `app_professor_user_id_11f448628b5a55f0_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_professor`
--

LOCK TABLES `app_professor` WRITE;
/*!40000 ALTER TABLE `app_professor` DISABLE KEYS */;
/*!40000 ALTER TABLE `app_professor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_programdirector`
--

DROP TABLE IF EXISTS `app_programdirector`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_programdirector` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `department` varchar(120) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `app_programdirector_user_id_4c0bc69b9d59daad_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_programdirector`
--

LOCK TABLES `app_programdirector` WRITE;
/*!40000 ALTER TABLE `app_programdirector` DISABLE KEYS */;
/*!40000 ALTER TABLE `app_programdirector` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_schedule`
--

DROP TABLE IF EXISTS `app_schedule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_schedule` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_schedule`
--

LOCK TABLES `app_schedule` WRITE;
/*!40000 ALTER TABLE `app_schedule` DISABLE KEYS */;
/*!40000 ALTER TABLE `app_schedule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_schedule_labList`
--

DROP TABLE IF EXISTS `app_schedule_labList`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_schedule_labList` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `schedule_id` int(11) NOT NULL,
  `lab_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `schedule_id` (`schedule_id`,`lab_id`),
  KEY `app_schedule_labList_9bc70bb9` (`schedule_id`),
  KEY `app_schedule_labList_9db8e5d7` (`lab_id`),
  CONSTRAINT `app_schedule_labList_lab_id_9a6b8931583ebdd_fk_app_lab_id` FOREIGN KEY (`lab_id`) REFERENCES `app_lab` (`id`),
  CONSTRAINT `app_schedule_lab_schedule_id_6a8c7b8c34d774e6_fk_app_schedule_id` FOREIGN KEY (`schedule_id`) REFERENCES `app_schedule` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_schedule_labList`
--

LOCK TABLES `app_schedule_labList` WRITE;
/*!40000 ALTER TABLE `app_schedule_labList` DISABLE KEYS */;
/*!40000 ALTER TABLE `app_schedule_labList` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_schedule_lectureList`
--

DROP TABLE IF EXISTS `app_schedule_lectureList`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_schedule_lectureList` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `schedule_id` int(11) NOT NULL,
  `lecture_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `schedule_id` (`schedule_id`,`lecture_id`),
  KEY `app_schedule_lectureList_9bc70bb9` (`schedule_id`),
  KEY `app_schedule_lectureList_72a11f01` (`lecture_id`),
  CONSTRAINT `app_schedule_lectu_lecture_id_4f39cca2085f433e_fk_app_lecture_id` FOREIGN KEY (`lecture_id`) REFERENCES `app_lecture` (`id`),
  CONSTRAINT `app_schedule_lec_schedule_id_1ceec5e8aa8a51a2_fk_app_schedule_id` FOREIGN KEY (`schedule_id`) REFERENCES `app_schedule` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_schedule_lectureList`
--

LOCK TABLES `app_schedule_lectureList` WRITE;
/*!40000 ALTER TABLE `app_schedule_lectureList` DISABLE KEYS */;
/*!40000 ALTER TABLE `app_schedule_lectureList` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_schedule_tutorialList`
--

DROP TABLE IF EXISTS `app_schedule_tutorialList`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_schedule_tutorialList` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `schedule_id` int(11) NOT NULL,
  `tutorial_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `schedule_id` (`schedule_id`,`tutorial_id`),
  KEY `app_schedule_tutorialList_9bc70bb9` (`schedule_id`),
  KEY `app_schedule_tutorialList_b6fbbedb` (`tutorial_id`),
  CONSTRAINT `app_schedule_tut_tutorial_id_25c0ed7d1eac6f9c_fk_app_tutorial_id` FOREIGN KEY (`tutorial_id`) REFERENCES `app_tutorial` (`id`),
  CONSTRAINT `app_schedule_tut_schedule_id_5b0724bb3476f8fe_fk_app_schedule_id` FOREIGN KEY (`schedule_id`) REFERENCES `app_schedule` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_schedule_tutorialList`
--

LOCK TABLES `app_schedule_tutorialList` WRITE;
/*!40000 ALTER TABLE `app_schedule_tutorialList` DISABLE KEYS */;
/*!40000 ALTER TABLE `app_schedule_tutorialList` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_student`
--

DROP TABLE IF EXISTS `app_student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_student` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `homephone` int(11) NOT NULL,
  `cellphone` int(11) NOT NULL,
  `address` varchar(120) NOT NULL,
  `IDNumber` int(11) NOT NULL,
  `academicRecord_id` int(11),
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  UNIQUE KEY `academicRecord_id` (`academicRecord_id`),
  CONSTRAINT `app_student_user_id_448dcbd68c3e33d5_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `app_s_academicRecord_id_3d71955252fdb3b0_fk_app_studentrecord_id` FOREIGN KEY (`academicRecord_id`) REFERENCES `app_studentrecord` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_student`
--

LOCK TABLES `app_student` WRITE;
/*!40000 ALTER TABLE `app_student` DISABLE KEYS */;
/*!40000 ALTER TABLE `app_student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_studentrecord`
--

DROP TABLE IF EXISTS `app_studentrecord`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_studentrecord` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `GPA` double NOT NULL,
  `currentStanding` varchar(120) NOT NULL,
  `currentCredits` double NOT NULL,
  `remainingCredits` double NOT NULL,
  `academicProgram_id` int(11) DEFAULT NULL,
  `mainSchedule_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `app_studentrecord_5f4ad74d` (`academicProgram_id`),
  KEY `app_studentrecord_d09c72f3` (`mainSchedule_id`),
  CONSTRAINT `app_studentr_mainSchedule_id_7fa2e91e7106c2e2_fk_app_schedule_id` FOREIGN KEY (`mainSchedule_id`) REFERENCES `app_schedule` (`id`),
  CONSTRAINT `ap_academicProgram_id_5e0e9298e3bf5e21_fk_app_academicprogram_id` FOREIGN KEY (`academicProgram_id`) REFERENCES `app_academicprogram` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_studentrecord`
--

LOCK TABLES `app_studentrecord` WRITE;
/*!40000 ALTER TABLE `app_studentrecord` DISABLE KEYS */;
/*!40000 ALTER TABLE `app_studentrecord` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_studentrecord_coursesTaken`
--

DROP TABLE IF EXISTS `app_studentrecord_coursesTaken`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_studentrecord_coursesTaken` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `studentrecord_id` int(11) NOT NULL,
  `course_id` varchar(120) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `studentrecord_id` (`studentrecord_id`,`course_id`),
  KEY `app_studentrecord_coursesTaken_e2d76079` (`studentrecord_id`),
  KEY `app_studentrecord_coursesTaken_ea134da7` (`course_id`),
  CONSTRAINT `app_studentreco_course_id_2fcb022bb92ee3fb_fk_app_course_deptnum` FOREIGN KEY (`course_id`) REFERENCES `app_course` (`deptnum`),
  CONSTRAINT `app_stu_studentrecord_id_b295aacd52f3b9e_fk_app_studentrecord_id` FOREIGN KEY (`studentrecord_id`) REFERENCES `app_studentrecord` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_studentrecord_coursesTaken`
--

LOCK TABLES `app_studentrecord_coursesTaken` WRITE;
/*!40000 ALTER TABLE `app_studentrecord_coursesTaken` DISABLE KEYS */;
/*!40000 ALTER TABLE `app_studentrecord_coursesTaken` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_studentrecord_registeredCourses`
--

DROP TABLE IF EXISTS `app_studentrecord_registeredCourses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_studentrecord_registeredCourses` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `studentrecord_id` int(11) NOT NULL,
  `course_id` varchar(120) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `studentrecord_id` (`studentrecord_id`,`course_id`),
  KEY `app_studentrecord_registeredCourses_e2d76079` (`studentrecord_id`),
  KEY `app_studentrecord_registeredCourses_ea134da7` (`course_id`),
  CONSTRAINT `app_studentreco_course_id_3b8ee8d2001decb6_fk_app_course_deptnum` FOREIGN KEY (`course_id`) REFERENCES `app_course` (`deptnum`),
  CONSTRAINT `app_st_studentrecord_id_24314a55b26ae913_fk_app_studentrecord_id` FOREIGN KEY (`studentrecord_id`) REFERENCES `app_studentrecord` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_studentrecord_registeredCourses`
--

LOCK TABLES `app_studentrecord_registeredCourses` WRITE;
/*!40000 ALTER TABLE `app_studentrecord_registeredCourses` DISABLE KEYS */;
/*!40000 ALTER TABLE `app_studentrecord_registeredCourses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_studentrecord_scheduleCache`
--

DROP TABLE IF EXISTS `app_studentrecord_scheduleCache`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_studentrecord_scheduleCache` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `studentrecord_id` int(11) NOT NULL,
  `schedule_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `studentrecord_id` (`studentrecord_id`,`schedule_id`),
  KEY `app_studentrecord_scheduleCache_e2d76079` (`studentrecord_id`),
  KEY `app_studentrecord_scheduleCache_9bc70bb9` (`schedule_id`),
  CONSTRAINT `app_studentrecord_schedule_id_eb83414a8f18fe9_fk_app_schedule_id` FOREIGN KEY (`schedule_id`) REFERENCES `app_schedule` (`id`),
  CONSTRAINT `app_st_studentrecord_id_768407eeb8f12427_fk_app_studentrecord_id` FOREIGN KEY (`studentrecord_id`) REFERENCES `app_studentrecord` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_studentrecord_scheduleCache`
--

LOCK TABLES `app_studentrecord_scheduleCache` WRITE;
/*!40000 ALTER TABLE `app_studentrecord_scheduleCache` DISABLE KEYS */;
/*!40000 ALTER TABLE `app_studentrecord_scheduleCache` ENABLE KEYS */;
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
  `course_id` varchar(120) DEFAULT NULL,
  `event_id` int(11) DEFAULT NULL,
  `lecture_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `event_id` (`event_id`),
  UNIQUE KEY `app_tutorial_section_63e07094458eb625_uniq` (`section`,`course_id`,`lecture_id`),
  KEY `app_tutorial_ea134da7` (`course_id`),
  KEY `app_tutorial_72a11f01` (`lecture_id`),
  CONSTRAINT `app_tutorial_lecture_id_179fc8f31b2578dc_fk_app_lecture_id` FOREIGN KEY (`lecture_id`) REFERENCES `app_lecture` (`id`),
  CONSTRAINT `app_tutorial_course_id_49ec9ddbe6beb27d_fk_app_course_deptnum` FOREIGN KEY (`course_id`) REFERENCES `app_course` (`deptnum`),
  CONSTRAINT `app_tutorial_event_id_75fe3c5360874dec_fk_app_event_id` FOREIGN KEY (`event_id`) REFERENCES `app_event` (`id`)
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
  CONSTRAINT `auth_group_p_permission_id_5ad026a5d9deef9_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permission_group_id_6f02d62fc6a877ba_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
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
  CONSTRAINT `auth__content_type_id_51708a357086f8b0_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=55 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add course',7,'add_course'),(20,'Can change course',7,'change_course'),(21,'Can delete course',7,'delete_course'),(22,'Can add academic program',8,'add_academicprogram'),(23,'Can change academic program',8,'change_academicprogram'),(24,'Can delete academic program',8,'delete_academicprogram'),(25,'Can add option',9,'add_option'),(26,'Can change option',9,'change_option'),(27,'Can delete option',9,'delete_option'),(28,'Can add event',10,'add_event'),(29,'Can change event',10,'change_event'),(30,'Can delete event',10,'delete_event'),(31,'Can add lecture',11,'add_lecture'),(32,'Can change lecture',11,'change_lecture'),(33,'Can delete lecture',11,'delete_lecture'),(34,'Can add tutorial',12,'add_tutorial'),(35,'Can change tutorial',12,'change_tutorial'),(36,'Can delete tutorial',12,'delete_tutorial'),(37,'Can add lab',13,'add_lab'),(38,'Can change lab',13,'change_lab'),(39,'Can delete lab',13,'delete_lab'),(40,'Can add schedule',14,'add_schedule'),(41,'Can change schedule',14,'change_schedule'),(42,'Can delete schedule',14,'delete_schedule'),(43,'Can add program director',15,'add_programdirector'),(44,'Can change program director',15,'change_programdirector'),(45,'Can delete program director',15,'delete_programdirector'),(46,'Can add professor',16,'add_professor'),(47,'Can change professor',16,'change_professor'),(48,'Can delete professor',16,'delete_professor'),(49,'Can add student record',17,'add_studentrecord'),(50,'Can change student record',17,'change_studentrecord'),(51,'Can delete student record',17,'delete_studentrecord'),(52,'Can add student',18,'add_student'),(53,'Can change student',18,'change_student'),(54,'Can delete student',18,'delete_student');
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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$15000$2DuwY0vhxS9o$n6ndOoDVI6dPOHIowVzWXQsTsiFU1TUE90QUu2/JaFc=','2015-03-30 00:43:50',1,'foxtrot','','','sniperjefz@hotmail.com',1,1,'2015-03-30 00:43:50'),(2,'pbkdf2_sha256$15000$NQfdYLnp4hHC$47+joJQJdU6+10r1JqRM0NnHI7RsIxuQ9GgbmgP/uKM=','2015-03-30 00:44:05',1,'root','','','',1,1,'2015-03-30 00:44:05');
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
  CONSTRAINT `auth_user_groups_group_id_2a9d6125d5cd2527_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_22e610f65135a7a8_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
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
  CONSTRAINT `auth_user_u_permission_id_637bf541bc7a8f51_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissi_user_id_14ce4264e26cbd33_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
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
  CONSTRAINT `django_admin_log_user_id_19d4a8d95af315cd_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `djang_content_type_id_1b2cbe83b79b00ac_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
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
  UNIQUE KEY `django_content_type_app_label_2acafebd5b566adc_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'log entry','admin','logentry'),(2,'permission','auth','permission'),(3,'group','auth','group'),(4,'user','auth','user'),(5,'content type','contenttypes','contenttype'),(6,'session','sessions','session'),(7,'course','app','course'),(8,'academic program','app','academicprogram'),(9,'option','app','option'),(10,'event','app','event'),(11,'lecture','app','lecture'),(12,'tutorial','app','tutorial'),(13,'lab','app','lab'),(14,'schedule','app','schedule'),(15,'program director','app','programdirector'),(16,'professor','app','professor'),(17,'student record','app','studentrecord'),(18,'student','app','student');
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
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2015-03-30 00:40:53'),(2,'auth','0001_initial','2015-03-30 00:40:58'),(3,'admin','0001_initial','2015-03-30 00:40:59'),(4,'app','0001_initial','2015-03-30 00:41:35'),(5,'sessions','0001_initial','2015-03-30 00:41:42');
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

-- Dump completed on 2015-03-29 20:45:15
