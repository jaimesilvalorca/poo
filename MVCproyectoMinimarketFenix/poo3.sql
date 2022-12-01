-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 01-12-2022 a las 05:47:49
-- Versión del servidor: 10.4.25-MariaDB
-- Versión de PHP: 7.4.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `poo3`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cargo`
--

CREATE TABLE `cargo` (
  `IDCARGO` int(11) NOT NULL,
  `NUMEROCARGO` int(11) NOT NULL,
  `NOMBRECARGO` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `cargo`
--

INSERT INTO `cargo` (`IDCARGO`, `NUMEROCARGO`, `NOMBRECARGO`) VALUES
(1, 1, 'ADMINISTRADOR'),
(7, 3, 'LADRON'),
(10, 20, ''),
(11, 30, 'ADMINISTRATIVO'),
(12, 31, 'ADMINISTRATIVO'),
(13, 32, 'ADMINISTRADOR');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `comuna`
--

CREATE TABLE `comuna` (
  `IDCOMUNA` int(11) NOT NULL,
  `NUMEROCOMUNA` int(11) NOT NULL,
  `NOMBRECOMUNA` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `comuna`
--

INSERT INTO `comuna` (`IDCOMUNA`, `NUMEROCOMUNA`, `NOMBRECOMUNA`) VALUES
(1, 13110, 'LA FLORIDA'),
(15, 20, 'SANTIAGO'),
(16, 20, 'HOLA'),
(17, 30, 'HOLA'),
(19, 31, 'LA FLORIDA');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empleado`
--

CREATE TABLE `empleado` (
  `IDEMPLEADO` int(11) NOT NULL,
  `IDCARGO` int(11) NOT NULL,
  `IDCOMUNA` int(11) NOT NULL,
  `RUN` varchar(10) NOT NULL,
  `NOMBRE` varchar(15) DEFAULT NULL,
  `APELLIDO` varchar(15) DEFAULT NULL,
  `DIRECCION` varchar(30) DEFAULT NULL,
  `CLAVE` varchar(40) NOT NULL,
  `CORREO` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `empleado`
--

INSERT INTO `empleado` (`IDEMPLEADO`, `IDCARGO`, `IDCOMUNA`, `RUN`, `NOMBRE`, `APELLIDO`, `DIRECCION`, `CLAVE`, `CORREO`) VALUES
(2, 1, 1, '11111111-1', 'CARLOS', 'GUAJARDO', 'ALMIRANTE BARROSO 76', '6b27261d2376675ed03f852cd30474d3', 'CG@INACAP.CL');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `cargo`
--
ALTER TABLE `cargo`
  ADD PRIMARY KEY (`IDCARGO`);

--
-- Indices de la tabla `comuna`
--
ALTER TABLE `comuna`
  ADD PRIMARY KEY (`IDCOMUNA`);

--
-- Indices de la tabla `empleado`
--
ALTER TABLE `empleado`
  ADD PRIMARY KEY (`IDEMPLEADO`),
  ADD KEY `FK_RELATIONSHIP_1` (`IDCARGO`),
  ADD KEY `FK_RELATIONSHIP_2` (`IDCOMUNA`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `cargo`
--
ALTER TABLE `cargo`
  MODIFY `IDCARGO` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT de la tabla `comuna`
--
ALTER TABLE `comuna`
  MODIFY `IDCOMUNA` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT de la tabla `empleado`
--
ALTER TABLE `empleado`
  MODIFY `IDEMPLEADO` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `empleado`
--
ALTER TABLE `empleado`
  ADD CONSTRAINT `FK_RELATIONSHIP_1` FOREIGN KEY (`IDCARGO`) REFERENCES `cargo` (`IDCARGO`),
  ADD CONSTRAINT `FK_RELATIONSHIP_2` FOREIGN KEY (`IDCOMUNA`) REFERENCES `comuna` (`IDCOMUNA`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
