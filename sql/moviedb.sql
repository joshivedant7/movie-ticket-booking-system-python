-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 05, 2025 at 10:43 AM
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
-- Database: `dbfm1`
--

-- --------------------------------------------------------

--
-- Table structure for table `booking`
--

CREATE TABLE `booking` (
  `Booking_ID` varchar(10) NOT NULL,
  `No_of_Tickets` int(11) NOT NULL,
  `Total_Cost` int(11) NOT NULL,
  `Card_Number` varchar(19) DEFAULT NULL,
  `Name_on_card` varchar(21) DEFAULT NULL,
  `User_ID` varchar(5) DEFAULT NULL,
  `Show_ID` varchar(10) DEFAULT NULL,
  `Gold_Seats` varchar(100) DEFAULT NULL,
  `Silver_Seats` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `booking`
--

INSERT INTO `booking` (`Booking_ID`, `No_of_Tickets`, `Total_Cost`, `Card_Number`, `Name_on_card`, `User_ID`, `Show_ID`, `Gold_Seats`, `Silver_Seats`) VALUES
('BK10000010', 7, 2550, '1100946878185874', 'Amit Sinha', '100', 'SHT0110001', NULL, NULL),
('BK10000015', 4, 1400, '1303333985175724', 'Amit Sinha', '100', 'SHT0120001', NULL, NULL),
('BK10000061', 2, 700, '8128533653062472', 'Amit Sinha', '100', 'SHT0140001', NULL, NULL),
('BK10000074', 4, 1510, '9023681909771241', 'Amit Sinha', '100', 'SHT0210001', NULL, NULL),
('BK12900241', 4, 1550, '7773009689264956', 'Nusaiba Mehrunisa', '129', 'SHT0140002', NULL, NULL),
('BK12900252', 5, 1625, '5737832323108177', 'Nusaiba Mehrunisa', '129', 'SHT0210002', NULL, NULL),
('BK12900300', 5, 1835, '7287414689069330', 'Nusaiba Mehrunisa', '129', 'SHT0230002', NULL, NULL),
('BK12900364', 2, 700, '4851717238812172', 'Nusaiba Mehrunisa', '129', 'SHT0330002', NULL, NULL),
('BK12900388', 1, 350, '7669318050714955', 'Nusaiba Mehrunisa', '129', 'SHT0120003', NULL, NULL),
('BK12900409', 8, 3000, '5007201049284827', 'Nusaiba Mehrunisa', '129', 'SHT0130003', NULL, NULL),
('BK12900442', 8, 3020, '1739448502528726', 'Nusaiba Mehrunisa', '129', 'SHT0210003', NULL, NULL),
('BK12900451', 6, 1950, '1636514608656449', 'Nusaiba Mehrunisa', '129', 'SHT0220003', NULL, NULL),
('BK12900542', 6, 2325, '8771653099213057', 'Nusaiba Mehrunisa', '129', 'SHT0330003', NULL, NULL),
('BK12900601', 4, 1450, '7265583888327070', 'Nusaiba Mehrunisa', '129', 'SHT0140004', NULL, NULL),
('BK12900679', 5, 1625, '6171784724412878', 'Nusaiba Mehrunisa', '129', 'SHT0240004', NULL, NULL),
('BK12900703', 6, 2325, '5008917050886373', 'Nusaiba Mehrunisa', '129', 'SHT0320004', NULL, NULL),
('BK12900719', 8, 3025, '7995196046327721', 'Nusaiba Mehrunisa', '129', 'SHT0330004', NULL, NULL),
('BK12900750', 3, 1100, '7254476829661451', 'Nusaiba Mehrunisa', '129', 'SHT0120005', NULL, NULL),
('BK12900785', 3, 1050, '1289904611045987', 'Nusaiba Mehrunisa', '129', 'SHT0140005', NULL, NULL),
('BK12900794', 1, 325, '2412254834479036', 'Nusaiba Mehrunisa', '129', 'SHT0210005', NULL, NULL),
('BK12900852', 5, 1625, '9350935719531095', 'Nusaiba Mehrunisa', '129', 'SHT0240005', NULL, NULL),
('BK12900863', 11, 4300, '1394299703587144', 'Nusaiba Mehrunisa', '129', 'SHT0310005', NULL, NULL),
('BK12900883', 2, 700, '4384450769792069', 'Nusaiba Mehrunisa', '129', 'SHT0330005', NULL, NULL),
('BK12900909', 7, 2550, '6641261247091598', 'Nusaiba Mehrunisa', '129', 'SHT0110006', NULL, NULL),
('BK12900928', 8, 3000, '2501517711981934', 'Nusaiba Mehrunisa', '129', 'SHT0120006', NULL, NULL),
('BK12900932', 1, 350, '3291333255592962', 'Nusaiba Mehrunisa', '129', 'SHT0130006', NULL, NULL),
('BK12900972', 8, 2740, '6394112527920165', 'Nusaiba Mehrunisa', '129', 'SHT0210006', NULL, NULL),
('BK12900997', 1, 325, '6374129051942085', 'Nusaiba Mehrunisa', '129', 'SHT0230006', NULL, NULL),
('BK12901015', 5, 1625, '1483699589977073', 'Nusaiba Mehrunisa', '129', 'SHT0240006', NULL, NULL),
('BK12901039', 4, 1400, '7291808395469025', 'Nusaiba Mehrunisa', '129', 'SHT0310006', NULL, NULL),
('BK12901082', 6, 2100, '8981508904574621', 'Nusaiba Mehrunisa', '129', 'SHT0110007', NULL, NULL),
('BK12901099', 3, 1050, '2127899327897420', 'Nusaiba Mehrunisa', '129', 'SHT0130007', NULL, NULL),
('BK12901165', 9, 3345, '4446803128339370', 'Nusaiba Mehrunisa', '129', 'SHT0220007', NULL, NULL),
('BK12901189', 5, 1905, '9456680324446186', 'Nusaiba Mehrunisa', '129', 'SHT0240007', NULL, NULL),
('BK12901265', 5, 1900, '9192561724342123', 'Nusaiba Mehrunisa', '129', 'SHT0120008', NULL, NULL),
('BK12901271', 2, 700, '4236229836310363', 'Nusaiba Mehrunisa', '129', 'SHT0130008', NULL, NULL),
('BK12901315', 5, 1625, '4534076455886342', 'Nusaiba Mehrunisa', '129', 'SHT0210008', NULL, NULL),
('BK12901360', 3, 1115, '4934424291798021', 'Nusaiba Mehrunisa', '129', 'SHT0230008', NULL, NULL),
('BK12901376', 3, 1045, '3055767552152728', 'Nusaiba Mehrunisa', '129', 'SHT0240008', NULL, NULL),
('BK12901383', 3, 1050, '6469764221771770', 'Nusaiba Mehrunisa', '129', 'SHT0310008', NULL, NULL),
('BK12901402', 8, 3025, '8301976072521191', 'Nusaiba Mehrunisa', '129', 'SHT0320008', NULL, NULL),
('BK12901424', 3, 1050, '1317863962369737', 'Nusaiba Mehrunisa', '129', 'SHT0110009', NULL, NULL),
('BK12901465', 3, 1050, '5710087254707505', 'Nusaiba Mehrunisa', '129', 'SHT0130009', NULL, NULL),
('BK12901502', 8, 2740, '7552903278029418', 'Nusaiba Mehrunisa', '129', 'SHT0210009', NULL, NULL),
('BK12901574', 4, 1400, '7026039349669550', 'Nusaiba Mehrunisa', '129', 'SHT0320009', NULL, NULL),
('BK12901575', 2, 700, '635536220245698', 'Tirthal Patel', '135', 'SHT0130009', '1111111111111111', '00111111111111111111111111111');

-- --------------------------------------------------------

--
-- Table structure for table `movie`
--

CREATE TABLE `movie` (
  `Movie_ID` varchar(5) NOT NULL,
  `Name` varchar(30) NOT NULL,
  `Language` varchar(10) DEFAULT NULL,
  `Genre` varchar(20) DEFAULT NULL,
  `Target_Audience` varchar(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `movie`
--

INSERT INTO `movie` (`Movie_ID`, `Name`, `Language`, `Genre`, `Target_Audience`) VALUES
('001', 'Hichki', 'Hindi', 'Drama/Comedy', 'U/A'),
('002', 'Pacific Rim Uprising', 'English', 'Fantasy/SciFi', 'U/A'),
('003', 'Strangers : Prey at night', 'English', 'Horror', 'U/A'),
('004', 'Tomb Raider', 'English', 'Fantasy/Action', 'A'),
('005', 'Midnight Sun', 'English', 'Romance', 'R'),
('006', 'Peter Rabbit', 'English', 'Fantasy/Adventure', 'U/A'),
('007', 'Black Panther', 'English', 'Fantasy/SciFi', 'U/A'),
('008', 'Maze Runner: The Death Cure', 'English', 'Fantasy/SciFi', 'U/A'),
('009', 'Insidious: The Last Key', 'English', 'Horror', 'U/A'),
('010', 'Blackmail', 'Hindi', 'Comedy', 'U/A'),
('011', 'Parmanu: The Story of Pokhran', 'Hindi', 'Drama/Thriller', 'U/A'),
('012', '3 Storeys', 'Hindi', 'Drama', 'U/A'),
('013', 'Rajaratha', 'Tamil', 'Comedy', 'U/A'),
('014', 'Yogi Duniya', 'Tamil', 'Drama/Thriller', 'U/A'),
('015', 'Kurukshetra', 'Tamil', 'Fantasy/History', 'U/A'),
('016', 'Mersal', 'Tamil', 'Romance/Comedy', 'U/A');

-- --------------------------------------------------------

--
-- Table structure for table `screen`
--

CREATE TABLE `screen` (
  `Screen_ID` varchar(5) NOT NULL,
  `Theatre_ID` varchar(5) DEFAULT NULL,
  `No_Row_Gold` int(11) DEFAULT NULL,
  `No_Col_Gold` int(11) DEFAULT NULL,
  `Availability_Gold` text DEFAULT NULL,
  `No_Row_Silver` int(11) DEFAULT NULL,
  `No_Col_Silver` int(11) DEFAULT NULL,
  `Availability_Silver` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `screen`
--

INSERT INTO `screen` (`Screen_ID`, `Theatre_ID`, `No_Row_Gold`, `No_Col_Gold`, `Availability_Gold`, `No_Row_Silver`, `No_Col_Silver`, `Availability_Silver`) VALUES
('T011', 'T01', 2, 8, '1100111000010110', 5, 6, '101011110101010100111001011000'),
('T012', 'T01', 2, 8, '1100111000010110', 5, 6, '001011110001010100111001011010'),
('T013', 'T01', 2, 8, '1111111101001100', 5, 6, '001101000001101110111001011100'),
('T014', 'T01', 2, 8, '1101100001110110', 5, 6, '001100110001000011001011010111'),
('T021', 'T02', 2, 8, '11110000111100001111', 5, 6, '101011110101010100111001011010'),
('T022', 'T02', 2, 8, '11110000111100001111', 5, 6, '101011110101010100111001011010'),
('T023', 'T02', 2, 8, '1111111001001010', 5, 6, '111101101001101110101001011100'),
('T024', 'T02', 2, 8, '1101110001110110', 5, 6, '001101011000010011001011110111'),
('T031', 'T03', 2, 8, '1111111011011000', 5, 6, '110111010111001101010110011110'),
('T032', 'T03', 2, 8, '1100111001110110', 5, 6, '101000110101010100111001011010'),
('T033', 'T03', 2, 8, '1100110000110110', 5, 6, '101011110101010100111001011010'),
('T041', 'T04', 6, 3, '111111111111111111', 6, 3, '111111111111111111'),
('T042', 'T04', 6, 3, '111111111111111111', 6, 3, '111111111111111111'),
('T043', 'T04', 6, 3, '111111111111111111', 6, 3, '111111111111111111'),
('T044', 'T04', 6, 3, '111111111111111111', 6, 3, '111111111111111111');

-- --------------------------------------------------------

--
-- Table structure for table `show_table`
--

CREATE TABLE `show_table` (
  `Show_ID` varchar(10) NOT NULL,
  `Show_Time` time NOT NULL,
  `Show_Date` date NOT NULL,
  `Seats_Remaining_Gold` int(11) NOT NULL CHECK (`Seats_Remaining_Gold` >= 0),
  `Seats_Remaining_Silver` int(11) NOT NULL CHECK (`Seats_Remaining_Silver` >= 0),
  `Class_Cost_Gold` int(11) NOT NULL,
  `Class_Cost_Silver` int(11) NOT NULL,
  `Screen_ID` varchar(5) NOT NULL,
  `Movie_ID` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `show_table`
--

INSERT INTO `show_table` (`Show_ID`, `Show_Time`, `Show_Date`, `Seats_Remaining_Gold`, `Seats_Remaining_Silver`, `Class_Cost_Gold`, `Class_Cost_Silver`, `Screen_ID`, `Movie_ID`) VALUES
('SHT0110001', '09:00:00', '0004-04-18', 20, 60, 400, 350, 'T011', '001'),
('SHT0110002', '04:20:00', '0004-04-18', 20, 60, 400, 350, 'T011', '012'),
('SHT0110003', '07:30:00', '0004-04-18', 20, 60, 400, 350, 'T011', '007'),
('SHT0110004', '09:00:00', '0004-04-18', 20, 60, 400, 350, 'T011', '002'),
('SHT0110005', '04:20:00', '0004-04-18', 20, 60, 400, 350, 'T011', '013'),
('SHT0110006', '07:30:00', '0004-04-18', 20, 60, 400, 350, 'T011', '008'),
('SHT0310009', '07:30:00', '0006-04-18', 20, 50, 425, 350, 'T031', '001'),
('SHT0320001', '09:00:00', '0004-04-18', 20, 50, 425, 350, 'T032', '010'),
('SHT0320002', '04:20:00', '0004-04-18', 20, 50, 425, 350, 'T032', '005'),
('SHT0320003', '07:30:00', '0004-04-18', 20, 50, 425, 350, 'T032', '016'),
('SHT0320004', '09:00:00', '0004-04-18', 20, 50, 425, 350, 'T032', '011'),
('SHT0320005', '04:20:00', '0004-04-18', 20, 50, 425, 350, 'T032', '006'),
('SHT0320006', '07:30:00', '0004-04-18', 20, 50, 425, 350, 'T032', '001'),
('SHT0320007', '09:00:00', '0005-04-18', 20, 50, 425, 350, 'T032', '012'),
('SHT0320008', '04:20:00', '0006-04-18', 20, 50, 425, 350, 'T032', '007'),
('SHT0320009', '07:30:00', '0006-04-18', 20, 50, 425, 350, 'T032', '002'),
('SHT0330001', '09:00:00', '0004-04-18', 20, 50, 425, 350, 'T033', '011'),
('SHT0330002', '04:20:00', '0004-04-18', 20, 50, 425, 350, 'T033', '006'),
('SHT0330003', '07:30:00', '0004-04-18', 20, 50, 425, 350, 'T033', '001'),
('SHT0330004', '09:00:00', '0004-04-18', 20, 50, 425, 350, 'T033', '012'),
('SHT0330005', '04:20:00', '0004-04-18', 20, 50, 425, 350, 'T033', '007'),
('SHT0330006', '07:30:00', '0004-04-18', 20, 50, 425, 350, 'T033', '002'),
('SHT0330007', '09:00:00', '0005-04-18', 20, 50, 425, 350, 'T033', '013'),
('SHT0330008', '04:20:00', '0006-04-18', 20, 50, 425, 350, 'T033', '008'),
('SHT0330009', '07:30:00', '0006-04-18', 20, 50, 425, 350, 'T033', '003');

-- --------------------------------------------------------

--
-- Table structure for table `theatre`
--

CREATE TABLE `theatre` (
  `Theatre_ID` varchar(5) NOT NULL,
  `Name_of_Theatre` varchar(30) NOT NULL,
  `No_of_Screens` int(11) DEFAULT NULL,
  `Area` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `theatre`
--

INSERT INTO `theatre` (`Theatre_ID`, `Name_of_Theatre`, `No_of_Screens`, `Area`) VALUES
('T01', 'PVR Cinemas', 4, 'Koramangala, Bangalore'),
('T02', 'INOX Movies', 4, 'Katpadi, Vellore'),
('T03', 'Cinepolis', 3, 'Meera Marg, Gurgaon'),
('T04', 'Raj Hans', 4, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `ticket`
--

CREATE TABLE `ticket` (
  `Ticket_ID` varchar(20) NOT NULL,
  `Booking_ID` varchar(10) DEFAULT NULL,
  `Class` varchar(3) NOT NULL,
  `Price` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `ticket`
--

INSERT INTO `ticket` (`Ticket_ID`, `Booking_ID`, `Class`, `Price`) VALUES
('G0001SHT0110009', 'BK10101438', 'GLD', 400),
('G0001SHT0120002', 'BK11200209', 'GLD', 400),
('G0001SHT0120004', 'BK12700578', 'GLD', 400),
('G0001SHT0120005', 'BK10800754', 'GLD', 400),
('G0001SHT0120006', 'BK12900928', 'GLD', 400),
('G0001SHT0120007', 'BK11801097', 'GLD', 400),
('S0064SHT0220006', 'BK12600979', 'SLV', 325),
('S0064SHT0220007', 'BK11801151', 'SLV', 325),
('S0064SHT0220008', 'BK12301321', 'SLV', 325),
('S0064SHT0220009', 'BK11401507', 'SLV', 325),
('S0064SHT0230001', 'BK10200100', 'SLV', 325),
('S0064SHT0230002', 'BK10800283', 'SLV', 325),
('S0064SHT0230003', 'BK12700465', 'SLV', 325),
('S0064SHT0230004', 'BK12700645', 'SLV', 325),
('S0064SHT0230005', 'BK11700825', 'SLV', 325),
('S0064SHT0230006', 'BK11500996', 'SLV', 325),
('S0064SHT0230007', 'BK10901169', 'SLV', 325),
('S0064SHT0230008', 'BK11001341', 'SLV', 325),
('S0064SHT0230009', 'BK10101523', 'SLV', 325),
('S0064SHT0240001', 'BK12300118', 'SLV', 325),
('S0064SHT0240002', 'BK10300301', 'SLV', 325),
('S0064SHT0240003', 'BK11600484', 'SLV', 325),
('S0064SHT0240004', 'BK11300662', 'SLV', 325),
('S0064SHT0240005', 'BK12700842', 'SLV', 325),
('S0064SHT0240006', 'BK11001011', 'SLV', 325),
('S0064SHT0240007', 'BK12301183', 'SLV', 325),
('S0064SHT0240008', 'BK10201361', 'SLV', 325),
('S0064SHT0240009', 'BK10701538', 'SLV', 325);

-- --------------------------------------------------------

--
-- Table structure for table `web_user`
--

CREATE TABLE `web_user` (
  `Web_User_ID` varchar(5) NOT NULL,
  `First_Name` varchar(15) DEFAULT NULL,
  `Last_Name` varchar(20) DEFAULT NULL,
  `Email_ID` varchar(30) DEFAULT NULL,
  `Age` int(11) DEFAULT NULL,
  `Phone_Number` varchar(10) NOT NULL,
  `password` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `web_user`
--

INSERT INTO `web_user` (`Web_User_ID`, `First_Name`, `Last_Name`, `Email_ID`, `Age`, `Phone_Number`, `password`) VALUES
('100', 'Amit', 'Sinha', 'amitsinhT04@gmail.com', 35, '9846273634', NULL),
('101', 'Raghav', 'Seth', 'seth.raghav987@gmail.com', 26, '7845279834', NULL),
('102', 'Anjali', 'Gupta', 'anjali23g@gmail.com', 30, '8849273345', NULL),
('103', 'Joy', 'Mathew', 'jmathew.123@gmail.com', 27, '9000567890', NULL),
('104', 'Sudha', 'Sunil', 'sudha_sunil07@gmail.com', 47, '8874323461', NULL),
('105', 'Ajay', 'Kumar', 'kumarajayv56@gmail.com', 19, '9078985643', NULL),
('106', 'Vikram', 'Joshi', 'jvikram.89@gmail.com', 23, '7750912345', NULL),
('107', 'Komal', 'Agarwal', 'komal.agarwal87@gmail.com', 15, '9345687654', NULL),
('108', 'Maitri', 'Shah', 'maitrishahj1@gmail.com', 32, '9922345016', NULL),
('109', 'Bhavya', 'Shastri', 'bhavyashastri@gmail.com', 25, '8567409098', NULL),
('110', 'Preeti', 'Jain', 'preeti.jain@gmail.com', 18, '7765433211', NULL),
('111', 'Shreya', 'Rathod', 'rathod_shreya@gmail.com', 38, '9800215673', NULL),
('112', 'Aditya', 'Rajesh', 'adityarajesh2902@gmail.com', 21, '9108996762', NULL),
('113', 'Keerti', 'Srivatsan', 'keertisri@gmail.com', 25, '7707378654', NULL),
('114', 'Rahul', 'Raghav', 'rahulrag@gmail.com', 23, '9591990037', NULL),
('115', 'Shrushti', 'Singh', 'shrushtikaul@gmail.com', 19, '9900554017', NULL),
('116', 'Mona', 'Mohammed', 'monaraisa@gmail.com', 23, '9591670037', NULL),
('117', 'Anushka', 'Sharma', 'sharmaanushka@gmail.com', 40, '9902432497', NULL),
('118', 'Yohanan', 'Veerappan', 'yohanv@gmail.com', 44, '8231239804', NULL),
('119', 'Kamala', 'Raghavendran', 'kamalag@gmail.com', 32, '9594390037', NULL),
('120', 'Janice', 'Fernandes', 'janicefernandes@gmail.com', 38, '9325880785', NULL),
('121', 'Sachin', 'Suresh', 'sachin1995@gmail.com', 23, '9325880785', NULL),
('122', 'Utham', 'Aiyappa', 'utham10@gmail.com', 21, '8581654798', NULL),
('123', 'Pranav', 'Gowda', 'pranavgowda06@gmail.com', 37, '8846085689', NULL),
('124', 'Krita', 'Prabhu', 'prabhukrita@gmail.com', 20, '9098107054', NULL),
('125', 'Aadrika', 'Bhandarkar', 'aadrikabhandarkar@gmail.com', 28, '9895287453', NULL),
('126', 'Sulohit', 'Avvaru', 'avvarusulohit1996@gmail.com', 22, '7180867407', NULL),
('127', 'Shriya', 'Bhimanadula', 'shriyab@gmail.com', 35, '9055932134', NULL),
('128', 'Ashmita', 'Rao', 'ashmitarao@gmail.com', 27, '7191088921', NULL),
('129', 'Nusaiba', 'Mehrunisa', 'nusaibafatima@gmail.com', 24, '8731990037', NULL),
('130', 'Tirthal', 'Patel', 'wdgwg@gmail.com', 19, '6355362202', '123'),
('131', 't', 'patel', 'fhworfo@gmail.com', 19, '6355362202', '1234'),
('132', 't', 'patel', 'ugefi@gmail.com', 19, '6355362202', '12345'),
('134', 'r', 'patel', 'xxx@gmail.com', 17, '6355362202', '12345'),
('135', 'Tirthal', 'Patel', 'wfdie2f@gmial.com', 19, '6355362202', '123'),
('136', 'Tirth', 'Patel', 'iegouwegfwgufowrfogrfug@gmail.', 20, '6355362202', '123'),
('137', 'Vedant', 'Joshi', 'jveda', 18, '987', '123KL'),
('138', 'Nishant', 'Timaniya', 'lodulalit.@main.com', 99, '987', 'chhaka_number_1'),
('139', '12', '12', '12', 18, '12', '12');

--
-- Triggers `web_user`
--
DELIMITER $$
CREATE TRIGGER `check_users_age` BEFORE INSERT ON `web_user` FOR EACH ROW BEGIN
    IF NEW.Age < 13 THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'User is underage and cannot register';
    END IF;
END
$$
DELIMITER ;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `booking`
--
ALTER TABLE `booking`
  ADD PRIMARY KEY (`Booking_ID`),
  ADD KEY `User_ID` (`User_ID`),
  ADD KEY `Show_ID` (`Show_ID`);

--
-- Indexes for table `movie`
--
ALTER TABLE `movie`
  ADD PRIMARY KEY (`Movie_ID`);

--
-- Indexes for table `screen`
--
ALTER TABLE `screen`
  ADD PRIMARY KEY (`Screen_ID`),
  ADD KEY `Theatre_ID` (`Theatre_ID`);

--
-- Indexes for table `show_table`
--
ALTER TABLE `show_table`
  ADD PRIMARY KEY (`Show_ID`),
  ADD KEY `Screen_ID` (`Screen_ID`),
  ADD KEY `Movie_ID` (`Movie_ID`);

--
-- Indexes for table `theatre`
--
ALTER TABLE `theatre`
  ADD PRIMARY KEY (`Theatre_ID`);

--
-- Indexes for table `ticket`
--
ALTER TABLE `ticket`
  ADD PRIMARY KEY (`Ticket_ID`),
  ADD KEY `Booking_ID` (`Booking_ID`);

--
-- Indexes for table `web_user`
--
ALTER TABLE `web_user`
  ADD PRIMARY KEY (`Web_User_ID`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `booking`
--
ALTER TABLE `booking`
  ADD CONSTRAINT `booking_ibfk_1` FOREIGN KEY (`User_ID`) REFERENCES `web_user` (`Web_User_ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `booking_ibfk_2` FOREIGN KEY (`Show_ID`) REFERENCES `show_table` (`Show_ID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `screen`
--
ALTER TABLE `screen`
  ADD CONSTRAINT `screen_ibfk_1` FOREIGN KEY (`Theatre_ID`) REFERENCES `theatre` (`Theatre_ID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `show_table`
--
ALTER TABLE `show_table`
  ADD CONSTRAINT `show_table_ibfk_1` FOREIGN KEY (`Screen_ID`) REFERENCES `screen` (`Screen_ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `show_table_ibfk_2` FOREIGN KEY (`Movie_ID`) REFERENCES `movie` (`Movie_ID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `ticket`
--
ALTER TABLE `ticket`
  ADD CONSTRAINT `ticket_ibfk_1` FOREIGN KEY (`Booking_ID`) REFERENCES `booking` (`Booking_ID`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
