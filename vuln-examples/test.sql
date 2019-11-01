--
-- Table structure for table `testtable`
--

DROP TABLE IF EXISTS `testtable`;
CREATE TABLE `testtable` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `firstname` varchar(30) DEFAULT NULL,
  `lastname` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `testtable`
--

LOCK TABLES `testtable` WRITE;
INSERT INTO `testtable` VALUES (1,'Elek','Teszt'),(2,'Elemér','Lapos'),(3,'Buda','Nemoda');
UNLOCK TABLES;
