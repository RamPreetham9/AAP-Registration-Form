-- MySQL dump 10.13  Distrib 5.7.24, for osx11.1 (x86_64)
--
-- Host: localhost    Database: aapDB
-- ------------------------------------------------------
-- Server version	9.1.0

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
-- Table structure for table `assemblies`
--

DROP TABLE IF EXISTS `assemblies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `assemblies` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `parliament_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `parliament_id` (`parliament_id`),
  CONSTRAINT `assemblies_ibfk_1` FOREIGN KEY (`parliament_id`) REFERENCES `parliaments` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=575 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `assemblies`
--

LOCK TABLES `assemblies` WRITE;
/*!40000 ALTER TABLE `assemblies` DISABLE KEYS */;
INSERT INTO `assemblies` VALUES (1,'Achanta',15),(2,'Addanki',5),(3,'Adoni',12),(4,'Allagadda',14),(5,'Alur',12),(6,'Amadalavalasa',21),(7,'Amalapuram',1),(8,'Anakapalle',2),(9,'Anantapur Urban',3),(10,'Anaparthy',19),(11,'Araku Valley',4),(12,'Atmakur',17),(13,'Avanigadda',13),(14,'Badvel',10),(15,'Banaganapalle',14),(16,'Bapatla',5),(17,'Bhimavaram',15),(18,'Bhimili',24),(19,'Bobbili',25),(20,'Chandragiri',6),(21,'Cheepurupalli',25),(22,'Chilakaluripet',16),(23,'Chintalapudi',7),(24,'Chirala',5),(25,'Chittoor',6),(26,'Chodavaram',2),(27,'Darsi',18),(28,'Denduluru',7),(29,'Dharmavaram',9),(30,'Dhone',14),(31,'Elamanchili',2),(32,'Eluru',7),(33,'Etcherla',25),(34,'Gajapathinagaram',25),(35,'Gajuwaka',24),(36,'Gangadhara Nellore',6),(37,'Gannavaram',1),(38,'Gannavaram',13),(39,'Giddalur',18),(40,'Gopalapuram',19),(41,'Gudivada',13),(42,'Gudur',22),(43,'Guntakal',3),(44,'Guntur East',8),(45,'Guntur West',8),(46,'Gurajala',16),(47,'Hindupur',9),(48,'Ichchapuram',21),(49,'Jaggampeta',11),(50,'Jaggayyapeta',23),(51,'Jammalamadugu',10),(52,'Kadapa',10),(53,'Kadiri',9),(54,'Kaikalur',7),(55,'Kakinada City',11),(56,'Kakinada Rural',11),(57,'Kalyandurg',3),(58,'Kamalapuram',10),(59,'Kandukur',17),(60,'Kanigiri',18),(61,'Kavali',17),(62,'Kodumur',12),(63,'Kodur',20),(64,'Kondapi',18),(65,'Kothapeta',1),(66,'Kovur',17),(67,'Kovvur',19),(68,'Kuppam',6),(69,'Kurnool',12),(70,'Kurupam',4),(71,'Macherla',16),(72,'Machilipatnam',13),(73,'Madakasira',9),(74,'Madanapalle',20),(75,'Madugula',2),(76,'Mandapeta',1),(77,'Mangalagiri',8),(78,'Mantralayam',12),(79,'Markapuram',18),(80,'Mummidivaram',1),(81,'Mydukur',10),(82,'Mylavaram',23),(83,'Nagari',6),(84,'Nandigama',23),(85,'Nandikotkur',14),(86,'Nandyal',14),(87,'Narasannapeta',21),(88,'Narasapuram',15),(89,'Narasaraopet',16),(90,'Narsipatnam',2),(91,'Nellimarla',25),(92,'Nellore City',17),(93,'Nellore Rural',17),(94,'Nidadavole',19),(95,'Nuzvid',7),(96,'Ongole',18),(97,'Paderu',4),(98,'Palakollu',15),(99,'Palakonda',4),(100,'Palamaner',6),(101,'Palasa',21),(102,'Pamarru',13),(103,'Panyam',14),(104,'Parchur',5),(105,'Parvathipuram',4),(106,'Pathapatnam',21),(107,'Pattikonda',12),(108,'Payakaraopet',2),(109,'Pedakurapadu',16),(110,'Pedana',13),(111,'Peddapuram',11),(112,'Penamaluru',13),(113,'Pendurthi',2),(114,'Penukonda',9),(115,'Pileru',20),(116,'Pithapuram',11),(117,'Polavaram',7),(118,'Ponnuru',8),(119,'Prathipadu',11),(120,'Prathipadu',8),(121,'Proddatur',10),(122,'Pulivendla',10),(123,'Punganur',20),(124,'Puthalapattu',6),(125,'Puttaparthi',9),(126,'Rajahmundry City',19),(127,'Rajahmundry Rural',19),(128,'Rajam',25),(129,'Rajampet',20),(130,'Rajanagaram',19),(131,'Ramachandrapuram',1),(132,'Rampachodavaram',4),(133,'Raptadu',9),(134,'Rayachoti',20),(135,'Rayadurg',3),(136,'Razole',1),(137,'Repalle',5),(138,'Salur',4),(139,'Santhanuthalapadu',5),(140,'Sarvepalli',22),(141,'Sathyavedu',22),(142,'Sattenapalle',16),(143,'Singanamala',3),(144,'Srikakulam',21),(145,'Srikalahasti',22),(146,'Srisailam',14),(147,'Srungavarapukota',24),(148,'Sullurpeta',22),(149,'Tadepalligudem',15),(150,'Tadikonda',8),(151,'Tadipatri',3),(152,'Tanuku',15),(153,'Tekkali',21),(154,'Tenali',8),(155,'Thamballapalle',20),(156,'Tirupati',22),(157,'Tiruvuru',23),(158,'Tuni',11),(159,'Udayagiri',17),(160,'Undi',15),(161,'Unguturu',7),(162,'Uravakonda',3),(163,'Vemuru',5),(164,'Venkatagiri',22),(165,'Vijayawada Central',23),(166,'Vijayawada East',23),(167,'Vijayawada West',23),(168,'Vinukonda',16),(169,'Visakhapatnam East',24),(170,'Visakhapatnam North',24),(171,'Visakhapatnam South',24),(172,'Visakhapatnam West',24),(173,'Vizianagaram',25),(174,'Yemmiganur',12),(175,'Yerragondapalem',18);
/*!40000 ALTER TABLE `assemblies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cities`
--

DROP TABLE IF EXISTS `cities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cities` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `district_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `district_id` (`district_id`),
  CONSTRAINT `cities_ibfk_1` FOREIGN KEY (`district_id`) REFERENCES `districts` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cities`
--

LOCK TABLES `cities` WRITE;
/*!40000 ALTER TABLE `cities` DISABLE KEYS */;
/*!40000 ALTER TABLE `cities` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `districts`
--

DROP TABLE IF EXISTS `districts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `districts` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `districts`
--

LOCK TABLES `districts` WRITE;
/*!40000 ALTER TABLE `districts` DISABLE KEYS */;
INSERT INTO `districts` VALUES (1,'Alluri Sitharama Raju'),(2,'Anakapalli'),(3,'Parvathipuram Manyam'),(4,'Srikakulam'),(5,'Visakhapatnam'),(6,'Vizianagaram'),(7,'Bapatla'),(8,'Dr. B. R. Ambedkar Konaseema'),(9,'East Godavari'),(10,'Eluru'),(11,'Guntur'),(12,'Kakinada'),(13,'Krishna'),(14,'NTR'),(15,'Palnadu'),(16,'Prakasam'),(17,'Sri Potti Sriramulu Nellore'),(18,'West Godavari'),(19,'Anantapur'),(20,'Annamayya'),(21,'Chittoor'),(22,'YSR (Kadapa)'),(23,'Kurnool'),(24,'Nandyal'),(25,'Sri Sathya Sai'),(26,'Tirupati');
/*!40000 ALTER TABLE `districts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `election_participation`
--

DROP TABLE IF EXISTS `election_participation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `election_participation` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `interested_positions` varchar(255) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `election_participation_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `election_participation`
--

LOCK TABLES `election_participation` WRITE;
/*!40000 ALTER TABLE `election_participation` DISABLE KEYS */;
/*!40000 ALTER TABLE `election_participation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mandals`
--

DROP TABLE IF EXISTS `mandals`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mandals` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `assembly_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `assembly_id` (`assembly_id`),
  CONSTRAINT `mandals_ibfk_1` FOREIGN KEY (`assembly_id`) REFERENCES `assemblies` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mandals`
--

LOCK TABLES `mandals` WRITE;
/*!40000 ALTER TABLE `mandals` DISABLE KEYS */;
/*!40000 ALTER TABLE `mandals` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `parliaments`
--

DROP TABLE IF EXISTS `parliaments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `parliaments` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `parliaments`
--

LOCK TABLES `parliaments` WRITE;
/*!40000 ALTER TABLE `parliaments` DISABLE KEYS */;
INSERT INTO `parliaments` VALUES (1,'Amalapuram'),(2,'Anakapalle'),(3,'Anantapur'),(4,'Araku'),(5,'Bapatla'),(6,'Chittoor'),(7,'Eluru'),(8,'Guntur'),(9,'Hindupur'),(10,'Kadapa'),(11,'Kakinada'),(12,'Kurnool'),(13,'Machilipatnam'),(14,'Nandyal'),(15,'Narasapuram'),(16,'Narasaraopet'),(17,'Nellore'),(18,'Ongole'),(19,'Rajahmundry'),(20,'Rajampet'),(21,'Srikakulam'),(22,'Tirupati'),(23,'Vijayawada'),(24,'Visakhapatnam'),(25,'Vizianagaram');
/*!40000 ALTER TABLE `parliaments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `unique_member_id` varchar(50) NOT NULL,
  `full_name` varchar(100) NOT NULL,
  `mobile_number` varchar(15) NOT NULL,
  `country_code` varchar(5) DEFAULT NULL,
  `password` varchar(255) NOT NULL,
  `voter_district` varchar(100) DEFAULT NULL,
  `voter_parliament` varchar(100) DEFAULT NULL,
  `voter_assembly` varchar(100) DEFAULT NULL,
  `voter_city` varchar(100) DEFAULT NULL,
  `voter_mandal` varchar(100) DEFAULT NULL,
  `voter_ward` varchar(50) DEFAULT NULL,
  `date_of_birth` date DEFAULT NULL,
  `profile_picture` varchar(255) DEFAULT NULL,
  `leader_id` int DEFAULT NULL,
  `otp` varchar(6) DEFAULT NULL,
  `otp_expiration` datetime DEFAULT NULL,
  `verified` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique_member_id` (`unique_member_id`),
  UNIQUE KEY `mobile_number` (`mobile_number`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (18,'UID-75667','raj','9652066986','+91','$2b$12$hBVESVk9t9afkIEPBkNWeeI1ERBvl9zS.TXwMfw9a0cslQcLG5QFC','Alluri Sitharama Raju','','','','','','2024-12-05','',NULL,NULL,NULL,1);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `volunteering`
--

DROP TABLE IF EXISTS `volunteering`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `volunteering` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `participation_methods` varchar(255) DEFAULT NULL,
  `likes_about_party` text,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `volunteering_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `volunteering`
--

LOCK TABLES `volunteering` WRITE;
/*!40000 ALTER TABLE `volunteering` DISABLE KEYS */;
/*!40000 ALTER TABLE `volunteering` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-04 19:03:45
