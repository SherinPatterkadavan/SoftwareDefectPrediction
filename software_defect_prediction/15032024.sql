/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 8.0.33 : Database - software_defect
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`software_defect` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `software_defect`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=69 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add assign_table',7,'add_assign_table'),
(26,'Can change assign_table',7,'change_assign_table'),
(27,'Can delete assign_table',7,'delete_assign_table'),
(28,'Can view assign_table',7,'view_assign_table'),
(29,'Can add hr_table',8,'add_hr_table'),
(30,'Can change hr_table',8,'change_hr_table'),
(31,'Can delete hr_table',8,'delete_hr_table'),
(32,'Can view hr_table',8,'view_hr_table'),
(33,'Can add login_table',9,'add_login_table'),
(34,'Can change login_table',9,'change_login_table'),
(35,'Can delete login_table',9,'delete_login_table'),
(36,'Can view login_table',9,'view_login_table'),
(37,'Can add notification_table',10,'add_notification_table'),
(38,'Can change notification_table',10,'change_notification_table'),
(39,'Can delete notification_table',10,'delete_notification_table'),
(40,'Can view notification_table',10,'view_notification_table'),
(41,'Can add tl_table',11,'add_tl_table'),
(42,'Can change tl_table',11,'change_tl_table'),
(43,'Can delete tl_table',11,'delete_tl_table'),
(44,'Can view tl_table',11,'view_tl_table'),
(45,'Can add work_table',12,'add_work_table'),
(46,'Can change work_table',12,'change_work_table'),
(47,'Can delete work_table',12,'delete_work_table'),
(48,'Can view work_table',12,'view_work_table'),
(49,'Can add tm_table',13,'add_tm_table'),
(50,'Can change tm_table',13,'change_tm_table'),
(51,'Can delete tm_table',13,'delete_tm_table'),
(52,'Can view tm_table',13,'view_tm_table'),
(53,'Can add result_table',14,'add_result_table'),
(54,'Can change result_table',14,'change_result_table'),
(55,'Can delete result_table',14,'delete_result_table'),
(56,'Can view result_table',14,'view_result_table'),
(57,'Can add report_table',15,'add_report_table'),
(58,'Can change report_table',15,'change_report_table'),
(59,'Can delete report_table',15,'delete_report_table'),
(60,'Can view report_table',15,'view_report_table'),
(61,'Can add doubt_table',16,'add_doubt_table'),
(62,'Can change doubt_table',16,'change_doubt_table'),
(63,'Can delete doubt_table',16,'delete_doubt_table'),
(64,'Can view doubt_table',16,'view_doubt_table'),
(65,'Can add complaint_table',17,'add_complaint_table'),
(66,'Can change complaint_table',17,'change_complaint_table'),
(67,'Can delete complaint_table',17,'delete_complaint_table'),
(68,'Can view complaint_table',17,'view_complaint_table');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user` */

insert  into `auth_user`(`id`,`password`,`last_login`,`is_superuser`,`username`,`first_name`,`last_name`,`email`,`is_staff`,`is_active`,`date_joined`) values 
(1,'pbkdf2_sha256$260000$0NiNw6gitPEBQTlbeEkPzt$ptioqign5cDe4tJwRPFIML/HKny5SPC9bO+BEKynbvM=','2024-03-22 09:33:18.956492',1,'admin','','','admin@gmail.com',1,1,'2024-03-22 04:32:15.798605');

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(7,'sdp','assign_table'),
(17,'sdp','complaint_table'),
(16,'sdp','doubt_table'),
(8,'sdp','hr_table'),
(9,'sdp','login_table'),
(10,'sdp','notification_table'),
(15,'sdp','report_table'),
(14,'sdp','result_table'),
(11,'sdp','tl_table'),
(13,'sdp','tm_table'),
(12,'sdp','work_table'),
(6,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'contenttypes','0001_initial','2024-03-22 04:29:46.965889'),
(2,'auth','0001_initial','2024-03-22 04:29:47.674515'),
(3,'admin','0001_initial','2024-03-22 04:29:47.889431'),
(4,'admin','0002_logentry_remove_auto_add','2024-03-22 04:29:47.897770'),
(5,'admin','0003_logentry_add_action_flag_choices','2024-03-22 04:29:47.912309'),
(6,'contenttypes','0002_remove_content_type_name','2024-03-22 04:29:48.137138'),
(7,'auth','0002_alter_permission_name_max_length','2024-03-22 04:29:48.223382'),
(8,'auth','0003_alter_user_email_max_length','2024-03-22 04:29:48.255043'),
(9,'auth','0004_alter_user_username_opts','2024-03-22 04:29:48.261158'),
(10,'auth','0005_alter_user_last_login_null','2024-03-22 04:29:48.339184'),
(11,'auth','0006_require_contenttypes_0002','2024-03-22 04:29:48.357843'),
(12,'auth','0007_alter_validators_add_error_messages','2024-03-22 04:29:48.370867'),
(13,'auth','0008_alter_user_username_max_length','2024-03-22 04:29:48.455793'),
(14,'auth','0009_alter_user_last_name_max_length','2024-03-22 04:29:48.538194'),
(15,'auth','0010_alter_group_name_max_length','2024-03-22 04:29:48.576381'),
(16,'auth','0011_update_proxy_permissions','2024-03-22 04:29:48.580891'),
(17,'auth','0012_alter_user_first_name_max_length','2024-03-22 04:29:48.678882'),
(18,'sdp','0001_initial','2024-03-22 04:29:49.867357'),
(19,'sessions','0001_initial','2024-03-22 04:29:49.919215');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('1fgh0gbx2x00nqwvoqqppskx30f4f7mr','.eJxVjjsOwjAQRO_iGlleJ7ZsSnrOEM3aaxKIEimfCnF3YikFtPNmnuatOuxb3-2rLN2Q1VWRuvxmjPSSqYL8xPSYdZqnbRlY14o-6arvc5bxdnb_BD3W_lhbJBTKSI03bSoQi-AdPBmGC84aD4oRIhJMNOSJI1OxaNmSawIf0rH-s58vxcY6Hg:1rnbH4:Hey4YACt7P6tDcWtZlTWFPn2KenbJboiGZacR9bBvqM','2024-04-05 09:33:18.956492');

/*Table structure for table `sdp_assign_table` */

DROP TABLE IF EXISTS `sdp_assign_table`;

CREATE TABLE `sdp_assign_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `work_details` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `status` varchar(100) NOT NULL,
  `TM_id` bigint NOT NULL,
  `WORK_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `sdp_assign_table_TM_id_41902e3a_fk_sdp_tm_table_id` (`TM_id`),
  KEY `sdp_assign_table_WORK_id_477c4750_fk_sdp_work_table_id` (`WORK_id`),
  CONSTRAINT `sdp_assign_table_TM_id_41902e3a_fk_sdp_tm_table_id` FOREIGN KEY (`TM_id`) REFERENCES `sdp_tm_table` (`id`),
  CONSTRAINT `sdp_assign_table_WORK_id_477c4750_fk_sdp_work_table_id` FOREIGN KEY (`WORK_id`) REFERENCES `sdp_work_table` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `sdp_assign_table` */

/*Table structure for table `sdp_complaint_table` */

DROP TABLE IF EXISTS `sdp_complaint_table`;

CREATE TABLE `sdp_complaint_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `complaint_details` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `replay` varchar(100) NOT NULL,
  `TM_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `sdp_complaint_table_TM_id_a8187b9b_fk_sdp_tm_table_id` (`TM_id`),
  CONSTRAINT `sdp_complaint_table_TM_id_a8187b9b_fk_sdp_tm_table_id` FOREIGN KEY (`TM_id`) REFERENCES `sdp_tm_table` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `sdp_complaint_table` */

/*Table structure for table `sdp_doubt_table` */

DROP TABLE IF EXISTS `sdp_doubt_table`;

CREATE TABLE `sdp_doubt_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `doubt` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `replay` varchar(100) NOT NULL,
  `TM_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `sdp_doubt_table_TM_id_e0ec4a43_fk_sdp_tm_table_id` (`TM_id`),
  CONSTRAINT `sdp_doubt_table_TM_id_e0ec4a43_fk_sdp_tm_table_id` FOREIGN KEY (`TM_id`) REFERENCES `sdp_tm_table` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `sdp_doubt_table` */

/*Table structure for table `sdp_hr_table` */

DROP TABLE IF EXISTS `sdp_hr_table`;

CREATE TABLE `sdp_hr_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `place` varchar(100) NOT NULL,
  `pin` int NOT NULL,
  `post` varchar(100) NOT NULL,
  `phone_no` bigint NOT NULL,
  `Email` varchar(100) NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `sdp_hr_table_LOGIN_id_a4724208_fk_sdp_login_table_id` (`LOGIN_id`),
  CONSTRAINT `sdp_hr_table_LOGIN_id_a4724208_fk_sdp_login_table_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `sdp_login_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `sdp_hr_table` */

insert  into `sdp_hr_table`(`id`,`name`,`place`,`pin`,`post`,`phone_no`,`Email`,`LOGIN_id`) values 
(1,'Shifa','Wayanad',670645,'Mananthavady',7654321890,'shifa2@gmail.com',2),
(2,'sherinpk','Malappuram',676504,'kodur',8113990374,'sherinpkz07@gmail.com',3);

/*Table structure for table `sdp_login_table` */

DROP TABLE IF EXISTS `sdp_login_table`;

CREATE TABLE `sdp_login_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `type` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `sdp_login_table` */

insert  into `sdp_login_table`(`id`,`username`,`password`,`type`) values 
(1,'admin','admin','admin'),
(2,'shifa','123','hr'),
(3,'sherin','123','hr'),
(4,'junaid3@gmail.com','123','TL'),
(5,'sameera','123','TL'),
(6,'vismaya','123','TL'),
(7,'rifa','123','TM'),
(8,'fiza','123','TM'),
(9,'lulu','123','blocked'),
(10,'sithara','123','blocked');

/*Table structure for table `sdp_notification_table` */

DROP TABLE IF EXISTS `sdp_notification_table`;

CREATE TABLE `sdp_notification_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `notifications` varchar(100) NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `sdp_notification_table` */

/*Table structure for table `sdp_report_table` */

DROP TABLE IF EXISTS `sdp_report_table`;

CREATE TABLE `sdp_report_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `report` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `status` varchar(100) NOT NULL,
  `ASSIGN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `sdp_report_table_ASSIGN_id_8a52cf7a_fk_sdp_assign_table_id` (`ASSIGN_id`),
  CONSTRAINT `sdp_report_table_ASSIGN_id_8a52cf7a_fk_sdp_assign_table_id` FOREIGN KEY (`ASSIGN_id`) REFERENCES `sdp_assign_table` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `sdp_report_table` */

/*Table structure for table `sdp_result_table` */

DROP TABLE IF EXISTS `sdp_result_table`;

CREATE TABLE `sdp_result_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `prediction_result` varchar(100) NOT NULL,
  `allocation` varchar(100) NOT NULL,
  `ASSIGN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `sdp_result_table_ASSIGN_id_0fc22a01_fk_sdp_assign_table_id` (`ASSIGN_id`),
  CONSTRAINT `sdp_result_table_ASSIGN_id_0fc22a01_fk_sdp_assign_table_id` FOREIGN KEY (`ASSIGN_id`) REFERENCES `sdp_assign_table` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `sdp_result_table` */

/*Table structure for table `sdp_tl_table` */

DROP TABLE IF EXISTS `sdp_tl_table`;

CREATE TABLE `sdp_tl_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `place` varchar(100) NOT NULL,
  `post` varchar(100) NOT NULL,
  `pin` int NOT NULL,
  `phone_no` bigint NOT NULL,
  `email` varchar(100) NOT NULL,
  `HR_id` bigint NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `sdp_tl_table_HR_id_3b750187_fk_sdp_hr_table_id` (`HR_id`),
  KEY `sdp_tl_table_LOGIN_id_635f7392_fk_sdp_login_table_id` (`LOGIN_id`),
  CONSTRAINT `sdp_tl_table_HR_id_3b750187_fk_sdp_hr_table_id` FOREIGN KEY (`HR_id`) REFERENCES `sdp_hr_table` (`id`),
  CONSTRAINT `sdp_tl_table_LOGIN_id_635f7392_fk_sdp_login_table_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `sdp_login_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `sdp_tl_table` */

insert  into `sdp_tl_table`(`id`,`name`,`place`,`post`,`pin`,`phone_no`,`email`,`HR_id`,`LOGIN_id`) values 
(1,'Junaid','Malappuram','Perithalmanna',679322,9876543211,'',2,4),
(2,'sameera','Malappuram','Tirur',676101,9967854321,'',2,5),
(3,'vismaya','Wayanad','Mananthavady',670645,7558068332,'',1,6);

/*Table structure for table `sdp_tm_table` */

DROP TABLE IF EXISTS `sdp_tm_table`;

CREATE TABLE `sdp_tm_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `place` varchar(100) NOT NULL,
  `post` varchar(100) NOT NULL,
  `pin` int NOT NULL,
  `phone_no` bigint NOT NULL,
  `email` varchar(100) NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  `TL_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `sdp_tm_table_LOGIN_id_2dfdd4fd_fk_sdp_login_table_id` (`LOGIN_id`),
  KEY `sdp_tm_table_TL_id_5a58d326_fk_sdp_tl_table_id` (`TL_id`),
  CONSTRAINT `sdp_tm_table_LOGIN_id_2dfdd4fd_fk_sdp_login_table_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `sdp_login_table` (`id`),
  CONSTRAINT `sdp_tm_table_TL_id_5a58d326_fk_sdp_tl_table_id` FOREIGN KEY (`TL_id`) REFERENCES `sdp_tl_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `sdp_tm_table` */

insert  into `sdp_tm_table`(`id`,`name`,`place`,`post`,`pin`,`phone_no`,`email`,`LOGIN_id`,`TL_id`) values 
(1,'Rifa','Malappuram','Alathoorpadi',676517,8765432190,'rifa@gmail.com',7,3),
(2,'fizaa','Kozhikode','Mankavu',678122,9988770543,'fiza@gmail.com',8,2),
(3,'lulu bayan','malappuram','wandoor',679328,9747092196,'lulubayanishak@gmail.com',9,2),
(4,'Sithara','malappuram','Areekode',673639,8590702430,'sitharaaneestk@gmail.com',10,1);

/*Table structure for table `sdp_work_table` */

DROP TABLE IF EXISTS `sdp_work_table`;

CREATE TABLE `sdp_work_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `work_name` varchar(100) NOT NULL,
  `description` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `deadline` date NOT NULL,
  `status` varchar(100) NOT NULL,
  `HR_id` bigint NOT NULL,
  `TL_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `sdp_work_table_HR_id_6914a60c_fk_sdp_hr_table_id` (`HR_id`),
  KEY `sdp_work_table_TL_id_931eb825_fk_sdp_tl_table_id` (`TL_id`),
  CONSTRAINT `sdp_work_table_HR_id_6914a60c_fk_sdp_hr_table_id` FOREIGN KEY (`HR_id`) REFERENCES `sdp_hr_table` (`id`),
  CONSTRAINT `sdp_work_table_TL_id_931eb825_fk_sdp_tl_table_id` FOREIGN KEY (`TL_id`) REFERENCES `sdp_tl_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `sdp_work_table` */

insert  into `sdp_work_table`(`id`,`work_name`,`description`,`date`,`deadline`,`status`,`HR_id`,`TL_id`) values 
(1,'testing','dsd','2024-03-22','2024-03-29','pending',1,1);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
