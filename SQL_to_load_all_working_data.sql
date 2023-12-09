-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: racing-zone_schema
-- ------------------------------------------------------
-- Server version	8.0.34

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `cars`
--

DROP TABLE IF EXISTS `cars`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cars` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `year` varchar(255) DEFAULT NULL,
  `make` varchar(255) DEFAULT NULL,
  `model` varchar(255) DEFAULT NULL,
  `transmission` varchar(255) DEFAULT NULL,
  `horsepower` varchar(255) DEFAULT NULL,
  `weight` varchar(255) DEFAULT NULL,
  `image_path` varchar(255) DEFAULT 'static\corvette_img.jpg',
  `price` varchar(45) DEFAULT NULL,
  `title` varchar(45) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `fk_cars_users_idx` (`user_id`),
  CONSTRAINT `fk_cars_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cars`
--

LOCK TABLES `cars` WRITE;
/*!40000 ALTER TABLE `cars` DISABLE KEYS */;
INSERT INTO `cars` VALUES (3,2,'2020','Ferrari','Enzo','Automatic','800','1500',_binary '2020-Ford-GT-Mk-II-005-2160.jpg','$20,000','Ferrari','a nice red ferrari looking car that needs a little car and it going to run fast.','2023-12-06 21:30:06','2023-12-06 21:30:06'),(4,1,'2018','Cheverolet','Corvette','Automatic','950','1600',_binary 'beautiful-big-tiger-3840x2160_79896-mm-90.jpg','$70,000','Corvette for sale!','LEaving on a trip and don\'t need it going to sell for half price.','2023-12-06 21:31:32','2023-12-06 21:31:32'),(5,1,'2022','Tesla','Model X','Automatic','1000','1800',_binary 'alfa-romeo-c39-formula-1-3840x2160_947944-mm-90.jpg','$40,000','Tesla, need charge','justs needs some charge and its good to go','2023-12-06 21:35:20','2023-12-06 21:35:20'),(6,1,'2013','Maserati','Levante','Manual','780','1250',_binary 'pininfarina-iconica-motion-picture-3840x2160_578494-mm-90.jpg','$55,500','Maserati, moving out!','I am moving to a new town and don\'t want to drive it so im going to sell it on the low!','2023-12-06 21:37:45','2023-12-06 21:37:45'),(8,1,'2022','Tesla','Model X','Automatic','1000','1800',_binary '2020-Ford-GT-Mk-II-005-2160.jpg','$40,000','Tesla, need charge','justs needs some charge and its good to go','2023-12-06 21:35:20','2023-12-06 21:35:20'),(9,2,'1999','nissan','sentra','auto','500','1000',_binary 'beautiful-big-tiger-3840x2160_79896-mm-90.jpg','62456','dfgs','i dont want this car','2023-12-07 16:06:17','2023-12-07 16:06:17');
/*!40000 ALTER TABLE `cars` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `phone_number` varchar(10) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Diego','Millan','dm@gmail.com','7867867867','$2b$12$t4Xlsk8aTJYx5YHl1iBc4ueOD8oSWIKHFOrorAjungsOeGdSC6rQ.','2023-12-06 15:19:08','2023-12-06 15:19:08'),(2,'Natalie','Moron','NM@gmail.com','7864561234','$2b$12$E5EFKKl0lsoIgTA2.yHA2u9/ATU0jsez3NQpzHcB1n6TeDZs7ywC6','2023-12-08 01:46:16','2023-12-08 01:46:16');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-09  2:18:22
