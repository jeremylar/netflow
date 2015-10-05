CREATE DATABASE `netflow`;
USE `netflow`;

CREATE TABLE IF NOT EXISTS `netflowFL` (
		`id` int(11) NOT NULL AUTO_INCREMENT,
		`timeofflow` datetime NOT NULL,
		`sourceip` varchar(15) NULL,
		`sourceport` int(10) NULL,
		`destinationip` varchar(15) NULL,
		`destinationport` int(10) NULL,
		`bytes` float(15) NOT NULL,
		`packets` int(10) NOT NULL,
		`totaloutput` int(5) NOT NULL,
		`protocol` varchar(10) NULL,
		PRIMARY KEY (`id`)
	) ENGINE=MyISAM DEFAULT CHARSET=utf8;
	
	CREATE TABLE IF NOT EXISTS `netflowBX` (
		`id` int(11) NOT NULL AUTO_INCREMENT,
		`timeofflow` datetime NOT NULL,
		`sourceip` varchar(15) NULL,
		`sourceport` int(10) NULL,
		`destinationip` varchar(15) NULL,
		`destinationport` int(10) NULL,
		`bytes` float(15) NOT NULL,
		`packets` int(10) NOT NULL,
		`totaloutput` int(5) NOT NULL,
		`protocol` varchar(10) NULL,
		PRIMARY KEY (`id`)
	) ENGINE=MyISAM DEFAULT CHARSET=utf8;
	
	CREATE TABLE IF NOT EXISTS `netflowBY` (
		`id` int(11) NOT NULL AUTO_INCREMENT,
		`timeofflow` datetime NOT NULL,
		`sourceip` varchar(15) NULL,
		`sourceport` int(10) NULL,
		`destinationip` varchar(15) NULL,
		`destinationport` int(10) NULL,
		`bytes` float(15) NOT NULL,
		`packets` int(10) NOT NULL,
		`totaloutput` int(5) NOT NULL,
		`protocol` varchar(10) NULL,
		PRIMARY KEY (`id`)
	) ENGINE=MyISAM DEFAULT CHARSET=utf8;
	
	CREATE TABLE IF NOT EXISTS `netflowMN` (
		`id` int(11) NOT NULL AUTO_INCREMENT,
		`timeofflow` datetime NOT NULL,
		`sourceip` varchar(15) NULL,
		`sourceport` int(10) NULL,
		`destinationip` varchar(15) NULL,
		`destinationport` int(10) NULL,
		`bytes` float(15) NOT NULL,
		`packets` int(10) NOT NULL,
		`totaloutput` int(5) NOT NULL,
		`protocol` varchar(10) NULL,
		PRIMARY KEY (`id`)
	) ENGINE=MyISAM DEFAULT CHARSET=utf8;
	
TRUNCATE `netflowFL`;
TRUNCATE `netflowBX`;
TRUNCATE `netflowBY`;
TRUNCATE `netflowMN`;