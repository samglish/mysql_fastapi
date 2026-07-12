-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jul 12, 2026 at 05:13 AM
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
-- Database: `ecole`
--

-- --------------------------------------------------------

--
-- Table structure for table `cours`
--

CREATE TABLE `cours` (
  `id` int(11) NOT NULL,
  `nom` varchar(100) NOT NULL,
  `code` varchar(20) DEFAULT NULL,
  `heures` int(11) DEFAULT 30
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `cours`
--

INSERT INTO `cours` (`id`, `nom`, `code`, `heures`) VALUES
(1, 'Mathématiques', 'MAT101', 60),
(2, 'Informatique', 'INF201', 45),
(3, 'Anglais', 'ANG101', 30);

-- --------------------------------------------------------

--
-- Table structure for table `etudiants`
--

CREATE TABLE `etudiants` (
  `id` int(11) NOT NULL,
  `nom` varchar(100) NOT NULL,
  `prenom` varchar(100) NOT NULL,
  `email` varchar(150) NOT NULL,
  `age` int(11) DEFAULT NULL,
  `telephone` varchar(20) DEFAULT NULL,
  `adresse` text DEFAULT NULL,
  `date_ins` date DEFAULT curdate()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `etudiants`
--

INSERT INTO `etudiants` (`id`, `nom`, `prenom`, `email`, `age`, `telephone`, `adresse`, `date_ins`) VALUES
(1, 'Diallo', 'Moussa', 'moussa@email.com', 22, NULL, NULL, '2026-06-27'),
(2, 'string', 'string', 'string', 0, 'string', NULL, '2026-06-27'),
(3, 'Touré', 'Ibrahim', 'ibrahim@email.com', 24, NULL, NULL, '2026-06-27'),
(4, 'Bah', 'Aminata', 'aminata@email.com', 21, NULL, NULL, '2026-06-27'),
(5, 'BEIDI', 'DINA', 'samuel@gmail.com', 20, '697241071', 'Garoua', '2026-07-07'),
(6, 'NNNNN', 'string', 'nada@gmail.com', 2, '6982', 'paris', '2026-07-07');

-- --------------------------------------------------------

--
-- Table structure for table `inscriptions`
--

CREATE TABLE `inscriptions` (
  `id` int(11) NOT NULL,
  `etudiant_id` int(11) NOT NULL,
  `cours_id` int(11) NOT NULL,
  `note` decimal(4,2) DEFAULT NULL,
  `date_ins` date DEFAULT curdate()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `inscriptions`
--

INSERT INTO `inscriptions` (`id`, `etudiant_id`, `cours_id`, `note`, `date_ins`) VALUES
(1, 1, 1, 15.50, '2026-06-27'),
(2, 1, 2, 12.00, '2026-06-27'),
(3, 2, 1, 14.00, '2026-06-27'),
(4, 3, 3, 16.50, '2026-06-27');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `cours`
--
ALTER TABLE `cours`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `code` (`code`);

--
-- Indexes for table `etudiants`
--
ALTER TABLE `etudiants`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `inscriptions`
--
ALTER TABLE `inscriptions`
  ADD PRIMARY KEY (`id`),
  ADD KEY `etudiant_id` (`etudiant_id`),
  ADD KEY `cours_id` (`cours_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `cours`
--
ALTER TABLE `cours`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `etudiants`
--
ALTER TABLE `etudiants`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `inscriptions`
--
ALTER TABLE `inscriptions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `inscriptions`
--
ALTER TABLE `inscriptions`
  ADD CONSTRAINT `inscriptions_ibfk_1` FOREIGN KEY (`etudiant_id`) REFERENCES `etudiants` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `inscriptions_ibfk_2` FOREIGN KEY (`cours_id`) REFERENCES `cours` (`id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
