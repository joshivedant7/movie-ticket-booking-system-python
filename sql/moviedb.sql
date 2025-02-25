-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 09, 2025 at 02:24 PM
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
('BK10000015', 4, 1400, '1303333985175724', 'Amit Sinha', '100', 'SHT0120001', NULL, NULL);
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
('T014', 'T01', 2, 8, '1101100001110110', 5, 6, '001000110001000011001011010111'),
('T021', 'T02', 2, 8, '1111111001001010', 5, 6, '101011110101010100111001011010'),
('T022', 'T02', 2, 8, '1111111001001010', 5, 6, '101011110101010100111001011010'),
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
('SHT0120001', '09:00:00', '0004-04-18', 20, 60, 400, 350, 'T012', '002'),
('SHT0120002', '04:20:00', '0004-04-18', 20, 60, 400, 350, 'T012', '013'),
('SHT0120009', '07:30:00', '0006-04-18', 20, 60, 400, 350, 'T012', '010'),
('SHT0130001', '09:00:00', '0004-04-18', 20, 60, 400, 350, 'T013', '003'),
('SHT0130002', '04:20:00', '0004-04-18', 20, 60, 400, 350, 'T013', '014'),
('SHT0130009', '07:30:00', '0006-04-18', 20, 60, 400, 350, 'T013', '011'),
('SHT0140001', '09:00:00', '0004-04-18', 20, 60, 400, 350, 'T014', '004'),
('SHT0140002', '04:20:00', '0004-04-18', 20, 60, 400, 350, 'T014', '015'),
('SHT0210001', '09:00:00', '0004-04-18', 22, 64, 395, 325, 'T021', '005'),
('SHT0210002', '04:20:00', '0004-04-18', 22, 64, 395, 325, 'T021', '016'),
('SHT0220001', '09:00:00', '0004-04-18', 22, 64, 395, 325, 'T022', '006'),
('SHT0220002', '04:20:00', '0004-04-18', 22, 64, 395, 325, 'T022', '001'),
('SHT0230001', '09:00:00', '0004-04-18', 22, 64, 395, 325, 'T023', '007'),
('SHT0230002', '04:20:00', '0004-04-18', 22, 64, 395, 325, 'T023', '002'),
('SHT0240001', '09:00:00', '0004-04-18', 22, 64, 395, 325, 'T024', '008'),
('SHT0240002', '04:20:00', '0004-04-18', 22, 64, 395, 325, 'T024', '003'),
('SHT0310001', '09:00:00', '0004-04-18', 20, 50, 425, 350, 'T031', '009'),
('SHT0310002', '04:20:00', '0004-04-18', 20, 50, 425, 350, 'T031', '004'),
('SHT0320001', '09:00:00', '0004-04-18', 20, 50, 425, 350, 'T032', '010'),
('SHT0320002', '04:20:00', '0004-04-18', 20, 50, 425, 350, 'T032', '005'),
('SHT0330001', '09:00:00', '0004-04-18', 20, 50, 425, 350, 'T033', '011'),
('SHT0330002', '04:20:00', '0004-04-18', 20, 50, 425, 350, 'T033', '006');

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
('G0001SHT0110009', 'BK10000010', 'GLD', 400),
('G0001SHT0120002', 'BK10000015', 'GLD', 400);
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
('100', 'Amit', 'Sinha', 'amitsinhT04@gmail.com', 35, '9846273634', NULL);
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
