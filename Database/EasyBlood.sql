-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 22, 2019 at 01:55 PM
-- Server version: 10.1.37-MariaDB
-- PHP Version: 7.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `easyblood`
--

-- --------------------------------------------------------

--
-- Table structure for table `donors`
--

CREATE TABLE `donors` (
  `ID` int(11) NOT NULL,
  `UserName` varchar(150) NOT NULL,
  `E_Mail` varchar(150) NOT NULL,
  `Phone` varchar(100) DEFAULT NULL,
  `City` varchar(150) DEFAULT NULL,
  `BloodGroup` varchar(50) DEFAULT NULL,
  `Wight` double DEFAULT NULL,
  `Age` int(11) DEFAULT NULL,
  `Gender` varchar(50) DEFAULT NULL,
  `DataOfLastDonation` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `donors_cities`
--

CREATE TABLE `donors_cities` (
  `ID_City` int(11) NOT NULL,
  `City` varchar(100) DEFAULT NULL,
  `ID_Donor` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `donors_schedule`
--

CREATE TABLE `donors_schedule` (
  `ID_Schedule` int(11) NOT NULL,
  `Status` tinyint(1) DEFAULT NULL,
  `DataOfLastDonation` date DEFAULT NULL,
  `ID_Donor` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `needys`
--

CREATE TABLE `needys` (
  `ID_Needy` int(11) NOT NULL,
  `Name` varchar(150) NOT NULL,
  `City` varchar(150) DEFAULT NULL,
  `Age` double DEFAULT NULL,
  `BloodGroup` varchar(50) DEFAULT NULL,
  `Hospital` varchar(100) DEFAULT NULL,
  `ID_Donor` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `donors`
--
ALTER TABLE `donors`
  ADD PRIMARY KEY (`ID`),
  ADD UNIQUE KEY `UserName` (`UserName`);

--
-- Indexes for table `donors_cities`
--
ALTER TABLE `donors_cities`
  ADD PRIMARY KEY (`ID_City`),
  ADD KEY `ID_Donor` (`ID_Donor`);

--
-- Indexes for table `donors_schedule`
--
ALTER TABLE `donors_schedule`
  ADD PRIMARY KEY (`ID_Schedule`),
  ADD KEY `ID_Donor` (`ID_Donor`);

--
-- Indexes for table `needys`
--
ALTER TABLE `needys`
  ADD PRIMARY KEY (`ID_Needy`),
  ADD UNIQUE KEY `Name` (`Name`),
  ADD KEY `ID_Donor` (`ID_Donor`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `donors_cities`
--
ALTER TABLE `donors_cities`
  ADD CONSTRAINT `donors_cities_ibfk_1` FOREIGN KEY (`ID_Donor`) REFERENCES `donors` (`ID`);

--
-- Constraints for table `donors_schedule`
--
ALTER TABLE `donors_schedule`
  ADD CONSTRAINT `donors_schedule_ibfk_1` FOREIGN KEY (`ID_Donor`) REFERENCES `donors` (`ID`);

--
-- Constraints for table `needys`
--
ALTER TABLE `needys`
  ADD CONSTRAINT `needys_ibfk_1` FOREIGN KEY (`ID_Donor`) REFERENCES `donors` (`ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
