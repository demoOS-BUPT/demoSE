-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: 2018-04-24 07:13:53
-- 服务器版本： 5.7.19
-- PHP Version: 5.6.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `air`
--

-- --------------------------------------------------------

--
-- 表的结构 `operate`
--

DROP TABLE IF EXISTS `operate`;
CREATE TABLE IF NOT EXISTS `operate` (
  `id` int(5) NOT NULL AUTO_INCREMENT,
  `operate` varchar(20) NOT NULL COMMENT '操作',
  `user` varchar(20) NOT NULL COMMENT 'client&server',
  `ip` varchar(20) NOT NULL COMMENT 'ip地址',
  `time` timestamp NOT NULL COMMENT '时间戳',
  `currentTemp` double DEFAULT NULL COMMENT '当前温度',
  `finalTemp` double DEFAULT NULL COMMENT '目标温度',
  `wind` int(5) DEFAULT NULL COMMENT '风速',
  `totalMoney` double DEFAULT NULL COMMENT '总金额',
  `perMoney` double DEFAULT NULL COMMENT '每秒金额',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
