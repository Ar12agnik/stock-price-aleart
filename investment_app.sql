-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 16, 2024 at 05:22 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `investment_app`
--

-- --------------------------------------------------------

--
-- Table structure for table `shares_owned`
--

CREATE TABLE `shares_owned` (
  `Sl_no` int(11) NOT NULL,
  `Symbol` varchar(255) NOT NULL,
  `Price` int(11) NOT NULL,
  `No_of_shares` int(11) NOT NULL,
  `Total` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `shares_owned`
--

INSERT INTO `shares_owned` (`Sl_no`, `Symbol`, `Price`, `No_of_shares`, `Total`) VALUES
(1, '', 0, 0, 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `shares_owned`
--
ALTER TABLE `shares_owned`
  ADD PRIMARY KEY (`Sl_no`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `shares_owned`
--
ALTER TABLE `shares_owned`
  MODIFY `Sl_no` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
