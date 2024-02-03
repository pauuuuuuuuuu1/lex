-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 23, 2023 at 11:25 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
  `fname` varchar(50) NOT NULL,
  `lname` varchar(50) NOT NULL,
  `cnum` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `ssq` varchar(50) NOT NULL,
  `sa` varchar(50) NOT NULL,
  `pwd` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `regteach`
--

INSERT INTO `regteach` (`id`, `fname`, `lname`, `cnum`, `email`, `ssq`, `sa`, `pwd`) VALUES
(1, 'Elexis', 'Falceso', '09505934815', 'admin', 'Your Date of Birth', '1/21/1998', 'admin'),
(2, 'jenesis', 'falceso', '09514781767', 'jenisis@gmail.com', 'Your Nick Name', 'jen', '1231231010'),
(3, 'sad', 'asdsa', 'asdas', 'asdsa', 'Your Date of Birth', 'dsazdas', 'asdsa'),
(4, 'asdas', 'asdas', 'asdsa', 'sadas', 'Your Date of Birth', 'sadas', 'asdsa'),
(5, 'elexis', 'falceso', '09505934815', 'elexis30@gmail.com', 'Your Nick Name', 'iket', '1231231010'),
(6, 'asdas', 'asdas', '262362462486464', 'asdasdasd', 'Your Date of Birth', '212121', 'asdsadas'),
(7, 'asdasd', 'asdas', '297682684648', 'sadasdsa', 'Your Date of Birth', 'sadsad', 'asdasdsadas'),
(8, 'dasdas', 'asdas', 'asdasdas', 'dasdas', 'Your Date of Birth', 'asdsad', '1231231010'),
(9, 'asdas', 'asdas', 'asdas', 'asdasd', 'Your Date of Birth', 'asdsadasd', '1231231010'),
(10, 'asdas', 'asdas', 'asdas', 'asdasd', 'Your Date of Birth', 'asdsadasd', '1231231010'),
(11, 'asdas', 'asdas', 'asdas', 'asdasd', 'Your Date of Birth', 'asdsadasd', '1231231010'),
(13, 'asdas', 'asdas', 'asdas', 'asdasd', 'Your Date of Birth', 'asdsadasd', '1231231010'),
(15, 'dasdas', 'asdas', 'asdasdas', 'dasdas', 'Your Date of Birth', 'asdsad', '1231231010'),
(16, 'asdas', 'asdas', 'asdas', 'asdasd', 'Your Date of Birth', 'asdsadasd', '1231231010'),
(21, 'asdas', 'asdas', 'asdas', 'asdasd', 'Your Date of Birth', 'asdsadasd', '1231231010'),
(22, 'dasdas', 'asdas', 'asdasdas', 'dasdas', 'Your Date of Birth', 'asdsad', '1231231010'),
(23, 'asdas', 'asdas', 'asdas', 'asdasd', 'Your Date of Birth', 'asdsadasd', '1231231010'),
(34, 'asdsa', 'asdsaasdas', 'elexis.falceso@gmail.com', 'Your Nick Name', 'asdasd', '123', '123'),
(35, 'Falceso', '09505934815', 'elexis.falceso@cvsu.edu.ph', 'Your Nick Name', 'iket', '1231231010', '1231231010'),
(36, 'asdas', 'asdasdas', '726878692768', 'qawscawrv', 'Your Nick Name', 'asdasdas', '1231231010'),
(37, 'asdasasdas', 'asdas', '7687236838', 'QAWHRBGAV', 'Your Nick Name', 'iketsss', '1231231010'),
(38, 'dasdsad', 'asdsad', '7638863783927', 'gqarebBQRAWE', 'Your Nick Name', 'iketsss', '1231231010'),
(39, 'asdasd', 'asdsad', '627356.38', 'sadasdsadas', 'Your Nick Name', 'asdasdasd', '123'),
(40, 'asdasd', 'asdasdsa', '83678665378', 'hsafbdvvsdr', 'Your Nick Name', 'asdasdsa', '123'),
(41, 'asdasd', 'asdsadsa', '623876.8', 'fsgavsdf', 'Your Nick Name', 'asdasdas', '123');

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `stdattendance`
--

INSERT INTO `stdattendance` (`std_id`, `std_name`, `Email`, `std_time`, `std_date`, `std_attendance`) VALUES
('2', 'Elexis Falceso', '4 - Kind', '17:07:09', '2023-12-22', 'Present'),
('2', 'Elexis Falceso', '4 - Kind', '17:07:09', '2023-12-22', 'Present'),
('2', 'Elexis Falceso', '4 - Kind', '17:07:09', '2023-12-22', 'Present'),
('2', 'Elexis Falceso', '4 - Kind', '17:07:09', '2023-12-22', 'Present'),
('1', 'Elexis Falceso', '4 - Love', '17:07:09', '2023-12-24', 'Present'),
('2', 'Elexis Falceso', '4 - Kind', '17:07:09', '2023-12-17', 'Present'),
('2', 'Elexis Falceso', '4 - Kind', '17:07:09', '2023-12-23', 'Present'),
('2', 'Elexis Falceso', '4 - Kind', '17:07:09', '2023-11-23', 'Present');

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`Student_ID`, `Name`, `mname`, `lname`, `Division`, `Gender`, `DOB`, `Address`, `Roll_No`, `Email`, `Teacher_Name`, `PhotoSample`) VALUES
('1', 'Elexis', 'Fajiculay', 'Falceso', 'Morning', 'Male', '01/21/1998', 'Cavite', '201502011', '4 - Love', 'Jared Alabanza', 'No');

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=42;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
