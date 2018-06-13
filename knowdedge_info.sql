# Host: localhost  (Version: 5.5.20)
# Date: 2018-06-13 21:14:17
# Generator: MySQL-Front 5.3  (Build 4.52)

/*!40101 SET NAMES utf8 */;

#
# Structure for table "knowdedge_info"
#

DROP TABLE IF EXISTS `knowdedge_info`;
CREATE TABLE `knowdedge_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `createtime` varchar(30) DEFAULT NULL,
  `systemid` varchar(30) DEFAULT NULL,
  `issue` varchar(1000) DEFAULT '',
  `causes` varchar(300) DEFAULT '',
  `solution` varchar(500) DEFAULT '',
  `ps` varchar(255) DEFAULT '',
  `status` varchar(11) DEFAULT '0',
  `annex` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=244 DEFAULT CHARSET=utf8;

#
# Data for table "knowdedge_info"
#

