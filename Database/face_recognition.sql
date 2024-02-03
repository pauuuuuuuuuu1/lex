-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 02, 2024 at 04:24 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 7.4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `face_recognition`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id` int(11) NOT NULL,
  `email` varchar(255) NOT NULL,
  `pwd` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id`, `email`, `pwd`) VALUES
(1, 'admin', 'admin123');

-- --------------------------------------------------------

--
-- Table structure for table `attendance`
--

CREATE TABLE `attendance` (
  `Student_ID` varchar(255) NOT NULL,
  `Name` varchar(255) NOT NULL,
  `std_time` varchar(255) NOT NULL,
  `std_date` varchar(255) NOT NULL,
  `status` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `attendance`
--

INSERT INTO `attendance` (`Student_ID`, `Name`, `std_time`, `std_date`, `status`) VALUES
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present'),
('', '1', '', '17/12/2023', 'Present');

-- --------------------------------------------------------

--
-- Table structure for table `regteach`
--

CREATE TABLE `regteach` (
  `id` int(11) NOT NULL,
  `employee_id` varchar(50) NOT NULL,
  `fname` varchar(255) NOT NULL,
  `mname` varchar(255) NOT NULL,
  `lname` varchar(255) NOT NULL,
  `cnum` varchar(11) NOT NULL,
  `email` varchar(255) NOT NULL,
  `department` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `regteach`
--

INSERT INTO `regteach` (`id`, `employee_id`, `fname`, `mname`, `lname`, `cnum`, `email`, `department`, `password`) VALUES
(1, '', 'Elexis', '', 'Falceso', '2147483647', 'admin', '', 'admin'),
(35, '', 'Leanne France', 'Pasco', 'Loyola', '09161550150', 'loyola@gmail.com', 'Elementary', '1231231010'),
(42, '12345', 'asdfghjkl', 'asdf', 'asdfghj', '12345678901', 'marlon@edu.ph', 'Elementary', '123');

-- --------------------------------------------------------

--
-- Table structure for table `stdattendance`
--

CREATE TABLE `stdattendance` (
  `std_id` varchar(255) NOT NULL,
  `std_name` varchar(255) NOT NULL,
  `Email` varchar(255) NOT NULL,
  `std_time` time NOT NULL DEFAULT current_timestamp(),
  `std_date` varchar(255) NOT NULL DEFAULT current_timestamp(),
  `std_attendance` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `stdattendance`
--

INSERT INTO `stdattendance` (`std_id`, `std_name`, `Email`, `std_time`, `std_date`, `std_attendance`) VALUES
('3', 'Jerome Falceso', '4 - Kind', '10:01:06', '2023-12-05', 'Present'),
('3', 'Jerome Falceso', '4 - Kind', '10:01:06', '2023-12-05', 'Present'),
('1', 'Elexis Falceso', '4 - Love', '10:26:59', '2023-12-29', 'Present'),
('2', 'Ephraim Falceso', '4 - Love', '10:28:52', '2023-12-29', 'Present');

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `Student_ID` varchar(255) NOT NULL,
  `Name` varchar(50) NOT NULL,
  `mname` varchar(255) NOT NULL,
  `lname` varchar(255) NOT NULL,
  `Division` varchar(50) NOT NULL,
  `Gender` varchar(50) NOT NULL,
  `DOB` varchar(50) NOT NULL,
  `Address` varchar(50) NOT NULL,
  `Roll_No` varchar(50) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `Teacher_Name` varchar(50) NOT NULL,
  `PhotoSample` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`Student_ID`, `Name`, `mname`, `lname`, `Division`, `Gender`, `DOB`, `Address`, `Roll_No`, `Email`, `Teacher_Name`, `PhotoSample`) VALUES
('1', 'Elexis', 'Fajiculay', 'Falceso', 'Morning', 'Male', '01/21/1998', 'Cavite', '201502011', '4 - Love', 'Jared Alabanza', 'No'),
('2', 'Ephraim', 'Ginez', 'Falceso', 'Afternoon', 'Male', '01/21/1998', 'Cavite', '201502012', '4 - Love', 'Jared Alabanza', 'No'),
('3', 'Mark', 'Ginez', 'Xucker Burg', 'Afternoon', 'Male', '12/06/2023', 'Cavite', '201502012', '4 - Kind', 'Jared Alabanza', 'No'),
('4', 'Mark', 'Ginez', 'Xucker Burg', 'Afternoon', 'Male', '12/06/2023', 'Cavite', '201502012', '3 - Kind', 'Jared Alabanza', 'No');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `regteach`
--
ALTER TABLE `regteach`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `regteach`
--
ALTER TABLE `regteach`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=43;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
