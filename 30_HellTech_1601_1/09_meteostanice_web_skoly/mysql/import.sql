-- 4.2.4 MySQL dump

SET NAMES utf8;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

DROP TABLE IF EXISTS `meteo_actual`;
CREATE TABLE `meteo_actual` (
  `name` varchar(20) NOT NULL,
  `value` varchar(20) NOT NULL,
  PRIMARY KEY  (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

INSERT INTO `meteo_actual` (`name`, `value`) VALUES
('date',	'2016-01-18 16:00:00'),
('temperature',	'20.0'),
('humidity',	'80'),
('light',	'1234'),
('temperature_date',	'2016-01-18 16:00:00'),
('humidity_date',	'2016-01-18 16:00:00'),
('light_date',	'2016-01-18 16:00:00');

DROP TABLE IF EXISTS `meteo_day`;
CREATE TABLE `meteo_day` (
  `date` char(20) NOT NULL,
  `temperature` float NOT NULL,
  `humidity` float NOT NULL,
  `light` float NOT NULL,
  PRIMARY KEY  (`date`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

INSERT INTO `meteo_day` (`date`, `temperature`, `humidity`, `light`) VALUES
('2016-01-18',	20.0,	80,	1234);

DROP TABLE IF EXISTS `meteo_hour`;
CREATE TABLE `meteo_hour` (
  `date` char(20) NOT NULL,
  `temperature` float NOT NULL,
  `temperature_sum` float NOT NULL default '0',
  `temperature_count` int(11) NOT NULL default '0',
  `humidity` float NOT NULL,
  `humidity_sum` int(11) NOT NULL default '0',
  `humidity_count` int(11) NOT NULL default '0',
  `light` float NOT NULL,
  `light_sum` int(11) NOT NULL default '0',
  `light_count` int(11) NOT NULL default '0',
  PRIMARY KEY  (`date`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
