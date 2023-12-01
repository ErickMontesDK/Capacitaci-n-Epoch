-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         11.1.2-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             12.3.0.6589
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para ejercicio_base_de_datos
CREATE DATABASE IF NOT EXISTS `ejercicio_base_de_datos` /*!40100 DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci */;
USE `ejercicio_base_de_datos`;

-- Volcando estructura para tabla ejercicio_base_de_datos.catdepartamentoproducto
CREATE TABLE IF NOT EXISTS `catdepartamentoproducto` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Volcando datos para la tabla ejercicio_base_de_datos.catdepartamentoproducto: ~10 rows (aproximadamente)
INSERT INTO `catdepartamentoproducto` (`id`, `descripcion`) VALUES
	(1, 'Electrónica'),
	(2, 'Ropa'),
	(3, 'Calzado'),
	(4, 'Alimentos y Bebidas'),
	(5, 'Hogar y Decoración'),
	(6, 'Belleza y Cuidado Personal'),
	(7, 'Juguetes'),
	(8, 'Libros y Papelería'),
	(9, 'Deportes y Aire Libre'),
	(10, 'Electrodomésticos');

-- Volcando estructura para tabla ejercicio_base_de_datos.catmarca
CREATE TABLE IF NOT EXISTS `catmarca` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Volcando datos para la tabla ejercicio_base_de_datos.catmarca: ~20 rows (aproximadamente)
INSERT INTO `catmarca` (`id`, `descripcion`) VALUES
	(1, 'Nescafé'),
	(2, 'Sony'),
	(3, 'Samsung'),
	(4, 'Apple'),
	(5, 'Nike'),
	(6, 'Adidas'),
	(7, 'Puma'),
	(8, 'Levi\'s'),
	(9, 'Coca-Cola'),
	(10, 'Pepsi'),
	(11, 'L\'Oréal'),
	(12, 'Maybelline'),
	(13, 'Sephora'),
	(14, 'Hershey\'s'),
	(15, 'Ferrero Rocher'),
	(16, 'Calvin Klein'),
	(17, 'Ralph Lauren'),
	(18, 'Toshiba'),
	(19, 'Canon'),
	(20, 'Dell');

-- Volcando estructura para tabla ejercicio_base_de_datos.cattipocliente
CREATE TABLE IF NOT EXISTS `cattipocliente` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Volcando datos para la tabla ejercicio_base_de_datos.cattipocliente: ~5 rows (aproximadamente)
INSERT INTO `cattipocliente` (`id`, `descripcion`) VALUES
	(1, 'Ocasional'),
	(2, 'Mayorista'),
	(3, 'Online'),
	(4, 'Jubilado'),
	(5, 'VIP');

-- Volcando estructura para tabla ejercicio_base_de_datos.clientes
CREATE TABLE IF NOT EXISTS `clientes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(30) DEFAULT NULL,
  `tipo_cliente` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `tipo_cliente` (`tipo_cliente`),
  CONSTRAINT `clientes_ibfk_1` FOREIGN KEY (`tipo_cliente`) REFERENCES `cattipocliente` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Volcando datos para la tabla ejercicio_base_de_datos.clientes: ~10 rows (aproximadamente)
INSERT INTO `clientes` (`id`, `nombre`, `tipo_cliente`) VALUES
	(1, 'María García', 3),
	(2, 'Carlos López', 2),
	(3, 'Ana Martínez', 5),
	(4, 'Javier Rodríguez', 4),
	(5, 'Laura Díaz', 1),
	(6, 'Pedro Sánchez', 2),
	(7, 'Sofía González', 1),
	(8, 'Diego Pérez', 3),
	(9, 'Valentina Gómez', 5),
	(10, 'Andrés Hernández', 4);

-- Volcando estructura para tabla ejercicio_base_de_datos.clientes_direcciones
CREATE TABLE IF NOT EXISTS `clientes_direcciones` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cliente_id` int(11) DEFAULT NULL,
  `direccion_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `cliente_id` (`cliente_id`),
  KEY `direccion_id` (`direccion_id`),
  CONSTRAINT `clientes_direcciones_ibfk_1` FOREIGN KEY (`cliente_id`) REFERENCES `clientes` (`id`),
  CONSTRAINT `clientes_direcciones_ibfk_2` FOREIGN KEY (`direccion_id`) REFERENCES `direcciones` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Volcando datos para la tabla ejercicio_base_de_datos.clientes_direcciones: ~20 rows (aproximadamente)
INSERT INTO `clientes_direcciones` (`id`, `cliente_id`, `direccion_id`) VALUES
	(1, 1, 27),
	(2, 2, 28),
	(3, 3, 29),
	(4, 4, 30),
	(5, 5, 31),
	(6, 6, 32),
	(7, 7, 33),
	(8, 8, 34),
	(9, 9, 35),
	(10, 10, 36),
	(11, 1, 37),
	(12, 2, 38),
	(13, 3, 39),
	(14, 4, 40),
	(15, 5, 41),
	(16, 6, 42),
	(17, 1, 43),
	(18, 1, 44),
	(19, 2, 45),
	(20, 3, 46);

-- Volcando estructura para vista ejercicio_base_de_datos.cliente_datos
-- Creando tabla temporal para superar errores de dependencia de VIEW
CREATE TABLE `cliente_datos` (
	`id Detalle Venta` INT(11) NOT NULL,
	`Cliente` VARCHAR(30) NULL COLLATE 'latin1_swedish_ci',
	`Tipo de cliente` VARCHAR(50) NULL COLLATE 'latin1_swedish_ci',
	`Fecha de venta` DATE NULL,
	`Productos` VARCHAR(50) NULL COLLATE 'latin1_swedish_ci',
	`Existencias` INT(11) NULL,
	`Vendidos` INT(11) NULL,
	`Costo` INT(11) NULL,
	`Precio de Venta` INT(11) NULL,
	`Importe` INT(11) NULL,
	`Id Venta` INT(11) NOT NULL,
	`Total` INT(11) NULL,
	`Empleado` VARCHAR(40) NULL COLLATE 'latin1_swedish_ci',
	`Sucursal` VARCHAR(60) NULL COLLATE 'latin1_swedish_ci',
	`Dirección` VARCHAR(318) NULL COLLATE 'latin1_swedish_ci',
	`Ciudad` VARCHAR(84) NULL COLLATE 'latin1_swedish_ci',
	`C.P.` INT(5) NULL
) ENGINE=MyISAM;

-- Volcando estructura para tabla ejercicio_base_de_datos.detalleventa
CREATE TABLE IF NOT EXISTS `detalleventa` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `producto` int(11) DEFAULT NULL,
  `cantidad` int(11) DEFAULT NULL,
  `precio_venta` int(11) DEFAULT NULL,
  `importe` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `producto` (`producto`),
  CONSTRAINT `detalleventa_ibfk_1` FOREIGN KEY (`producto`) REFERENCES `productos` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Volcando datos para la tabla ejercicio_base_de_datos.detalleventa: ~30 rows (aproximadamente)
INSERT INTO `detalleventa` (`id`, `producto`, `cantidad`, `precio_venta`, `importe`) VALUES
	(1, 1, 1, 50000, 50000),
	(2, 2, 1, 30000, 30000),
	(3, 3, 1, 55000, 55000),
	(4, 4, 1, 35000, 35000),
	(5, 5, 1, 6000, 6000),
	(6, 6, 1, 3500, 3500),
	(7, 7, 1, 25000, 25000),
	(8, 8, 1, 2000, 2000),
	(9, 9, 1, 5000, 5000),
	(10, 10, 1, 8000, 8000),
	(11, 11, 1, 52000, 52000),
	(12, 12, 1, 40000, 40000),
	(13, 13, 1, 5000, 5000),
	(14, 14, 1, 22000, 22000),
	(15, 15, 1, 4000, 4000),
	(16, 16, 1, 22000, 22000),
	(17, 17, 1, 1200, 1200),
	(18, 18, 1, 2000, 2000),
	(19, 19, 1, 6000, 6000),
	(20, 20, 1, 3000, 3000),
	(21, 21, 1, 1500, 1500),
	(22, 22, 1, 500, 500),
	(23, 23, 1, 900, 900),
	(24, 24, 1, 1200, 1200),
	(25, 25, 1, 1000, 1000),
	(26, 26, 1, 8000, 8000),
	(27, 27, 1, 5500, 5500),
	(28, 28, 1, 1200, 1200),
	(29, 29, 1, 900, 900),
	(30, 30, 1, 400, 400);

-- Volcando estructura para tabla ejercicio_base_de_datos.direcciones
CREATE TABLE IF NOT EXISTS `direcciones` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `calle_numero` varchar(255) DEFAULT NULL,
  `Colonia` varchar(60) DEFAULT NULL,
  `Municipio` varchar(60) DEFAULT NULL,
  `Estado` varchar(20) DEFAULT NULL,
  `CP` int(5) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=47 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Volcando datos para la tabla ejercicio_base_de_datos.direcciones: ~46 rows (aproximadamente)
INSERT INTO `direcciones` (`id`, `calle_numero`, `Colonia`, `Municipio`, `Estado`, `CP`) VALUES
	(1, 'Av. Juárez 123', 'Centro', 'Morelia', 'Michoacán', 58000),
	(2, 'Calle 16 de Septiembre 456', 'Chapultepec', 'Morelia', 'Michoacán', 58260),
	(3, 'Blvd. García de León 789', 'Las Américas', 'Morelia', 'Michoacán', 58270),
	(4, 'Paseo de la Reforma 10', 'Cuauhtémoc', 'Ciudad de México', 'Ciudad de México', 6030),
	(5, 'Av. Insurgentes Sur 20', 'Roma Norte', 'Ciudad de México', 'Ciudad de México', 6700),
	(6, 'Calle Madero 30', 'Centro Histórico', 'Ciudad de México', 'Ciudad de México', 6000),
	(7, 'Av. Hidalgo 40', 'Guadalupe Inn', 'Aguascalientes', 'Aguascalientes', 20130),
	(8, 'Blvd. Luis Donaldo Colosio 50', 'Jardines de la Concepción', 'Aguascalientes', 'Aguascalientes', 20120),
	(9, 'Calle Zaragoza 60', 'Centro', 'Aguascalientes', 'Aguascalientes', 20000),
	(10, 'Av. Universidad 70', 'Narvarte Poniente', 'Benito Juárez', 'Ciudad de México', 3020),
	(11, 'Av. Madero 222', 'Centro', 'Morelia', 'Michoacán', 58010),
	(12, 'Calle Mariano Escobedo 789', 'Chapultepec', 'Morelia', 'Michoacán', 58265),
	(13, 'Blvd. Juan Pablo II 333', 'Las Américas', 'Morelia', 'Michoacán', 58272),
	(14, 'Paseo de la República 55', 'Cuauhtémoc', 'Morelia', 'Michoacán', 58015),
	(15, 'Av. Reforma 25', 'Roma Sur', 'Ciudad de México', 'Ciudad de México', 6040),
	(16, 'Av. Insurgentes Norte 100', 'Condesa', 'Ciudad de México', 'Ciudad de México', 6710),
	(17, 'Calle Hamburgo 150', 'Juárez', 'Ciudad de México', 'Ciudad de México', 6020),
	(18, 'Av. Revolución 75', 'Del Valle', 'Ciudad de México', 'Ciudad de México', 6010),
	(19, 'Blvd. Rodolfo Landeros 300', 'Fátima', 'Aguascalientes', 'Aguascalientes', 20135),
	(20, 'Av. Convención de 1914 555', 'Las Flores', 'Aguascalientes', 'Aguascalientes', 20140),
	(21, 'Calle Benjamín de la Mora 40', 'Del Trabajo', 'Aguascalientes', 'Aguascalientes', 20010),
	(22, 'Blvd. José María Chávez 250', 'Jardines de las Fuentes', 'Aguascalientes', 'Aguascalientes', 20015),
	(23, 'Av. División del Norte 123', 'Nápoles', 'Benito Juárez', 'Ciudad de México', 3040),
	(24, 'Calle Luz Saviñón 456', 'Del Valle', 'Benito Juárez', 'Ciudad de México', 3050),
	(25, 'Blvd. Adolfo López Mateos 789', 'San José Insurgentes', 'Benito Juárez', 'Ciudad de México', 3060),
	(26, 'Av. Coyoacán 10', 'Portales', 'Benito Juárez', 'Ciudad de México', 3070),
	(27, 'Av. Abasolo 432', 'Centro', 'Morelia', 'Michoacán', 58005),
	(28, 'Calle Galeana 876', 'Chapultepec', 'Morelia', 'Michoacán', 58266),
	(29, 'Blvd. Gildardo Magaña 333', 'Las Américas', 'Morelia', 'Michoacán', 58273),
	(30, 'Paseo de la República 20', 'Cuauhtémoc', 'Morelia', 'Michoacán', 58018),
	(31, 'Av. Siervo de la Nación 1000', 'Campestre', 'Morelia', 'Michoacán', 58025),
	(32, 'Av. Xola 450', 'Narvarte Oriente', 'Ciudad de México', 'Ciudad de México', 6715),
	(33, 'Av. Cuitláhuac 789', 'Clavería', 'Ciudad de México', 'Ciudad de México', 6720),
	(34, 'Calle Amores 250', 'Del Valle Centro', 'Ciudad de México', 'Ciudad de México', 6730),
	(35, 'Blvd. Adolfo Ruíz Cortines 100', 'Colonia del Valle', 'Ciudad de México', 'Ciudad de México', 6740),
	(36, 'Av. Patriotismo 150', 'Escandón I Sección', 'Ciudad de México', 'Ciudad de México', 6750),
	(37, 'Blvd. José María Morelos 350', 'Fátima', 'Aguascalientes', 'Aguascalientes', 20138),
	(38, 'Av. Siglo XXI 555', 'Bosques del Prado', 'Aguascalientes', 'Aguascalientes', 20142),
	(39, 'Calle Vicente Guerrero 40', 'Del Trabajo', 'Aguascalientes', 'Aguascalientes', 20018),
	(40, 'Blvd. Juan Pablo II 250', 'Los Bosques', 'Aguascalientes', 'Aguascalientes', 20023),
	(41, 'Av. Convención de 1914 760', 'Insurgentes', 'Aguascalientes', 'Aguascalientes', 20030),
	(42, 'Av. Universidad 234', 'Santa Cruz Atoyac', 'Benito Juárez', 'Ciudad de México', 3045),
	(43, 'Calle Xochicalco 543', 'Nápoles', 'Benito Juárez', 'Ciudad de México', 3055),
	(44, 'Blvd. Félix Cuevas 876', 'Del Valle Sur', 'Benito Juárez', 'Ciudad de México', 3065),
	(45, 'Av. Eje 8 Sur 432', 'Portales Sur', 'Benito Juárez', 'Ciudad de México', 3075),
	(46, 'Calle Amores 550', 'Letrán Valle', 'Benito Juárez', 'Ciudad de México', 3085);

-- Volcando estructura para tabla ejercicio_base_de_datos.empleados
CREATE TABLE IF NOT EXISTS `empleados` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_completo` varchar(40) DEFAULT NULL,
  `fecha_nacimiento` date DEFAULT NULL,
  `genero` enum('masculino','femenino') DEFAULT NULL,
  `domicilio` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `domicilio` (`domicilio`),
  CONSTRAINT `empleados_ibfk_1` FOREIGN KEY (`domicilio`) REFERENCES `direcciones` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Volcando datos para la tabla ejercicio_base_de_datos.empleados: ~16 rows (aproximadamente)
INSERT INTO `empleados` (`id`, `nombre_completo`, `fecha_nacimiento`, `genero`, `domicilio`) VALUES
	(1, 'Juan Pérez', '1990-05-12', 'masculino', 11),
	(2, 'María Rodríguez', '1988-09-24', 'femenino', 12),
	(3, 'Carlos García', '1995-03-08', 'masculino', 13),
	(4, 'Laura Martínez', '1992-07-17', 'femenino', 14),
	(5, 'Luis Hernández', '1987-12-30', 'masculino', 15),
	(6, 'Ana Sánchez', '1993-11-05', 'femenino', 16),
	(7, 'Pedro Díaz', '1994-08-21', 'masculino', 17),
	(8, 'Sofía Torres', '1989-06-16', 'femenino', 18),
	(9, 'Diego López', '1991-04-02', 'masculino', 19),
	(10, 'Elena Flores', '1986-10-29', 'femenino', 20),
	(11, 'Javier Ramírez', '1996-02-14', 'masculino', 21),
	(12, 'Paula Gómez', '1997-07-08', 'femenino', 22),
	(13, 'Roberto Ruiz', '1985-09-18', 'masculino', 23),
	(14, 'Natalia Hernández', '1998-12-05', 'femenino', 24),
	(15, 'Daniel Martín', '1999-04-19', 'masculino', 25),
	(16, 'Verónica Castillo', '1992-11-30', 'femenino', 26);

-- Volcando estructura para tabla ejercicio_base_de_datos.productos
CREATE TABLE IF NOT EXISTS `productos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  `costo` int(11) DEFAULT NULL,
  `precio_venta` int(11) DEFAULT NULL,
  `existencia` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Volcando datos para la tabla ejercicio_base_de_datos.productos: ~31 rows (aproximadamente)
INSERT INTO `productos` (`id`, `nombre`, `costo`, `precio_venta`, `existencia`) VALUES
	(1, 'Laptop Acer', 40000, 50000, 25),
	(2, 'Smartphone Samsung', 25000, 30000, 50),
	(3, 'PlayStation 5', 45000, 55000, 15),
	(4, 'Televisor Sony 55"', 30000, 35000, 20),
	(5, 'Zapatillas Nike', 4000, 6000, 100),
	(6, 'Jeans Levi\'s', 2500, 3500, 75),
	(7, 'Cámara Canon EOS', 20000, 25000, 30),
	(8, 'Reloj Casio', 1500, 2000, 60),
	(9, 'Perfume Chanel', 3500, 5000, 40),
	(10, 'Bolso Michael Kors', 6000, 8000, 25),
	(11, 'Consola Xbox Series X', 42000, 52000, 10),
	(12, 'Televisor Samsung 65"', 35000, 40000, 18),
	(13, 'Audífonos Sony', 4000, 5000, 45),
	(14, 'Tablet Apple iPad', 18000, 22000, 28),
	(15, 'Zapatos Adidas', 3000, 4000, 80),
	(16, 'Cámara Nikon', 18000, 22000, 35),
	(17, 'Gorra Nike', 800, 1200, 120),
	(18, 'Lentes de sol Ray-Ban', 1500, 2000, 55),
	(19, 'Audífonos Bose', 5000, 6000, 30),
	(20, 'Impresora HP', 2500, 3000, 40),
	(21, 'Ropa de cama', 1000, 1500, 100),
	(22, 'Libro "Cien años de soledad"', 300, 500, 200),
	(23, 'Pelota de fútbol Nike', 600, 900, 150),
	(24, 'Juego de mesa "Catan"', 800, 1200, 80),
	(25, 'Teclado y ratón inalámbricos', 700, 1000, 70),
	(26, 'Guitarra eléctrica Fender', 6000, 8000, 15),
	(27, 'Aspiradora Dyson', 4500, 5500, 25),
	(28, 'Maletín para laptop', 800, 1200, 90),
	(29, 'Sartén antiadherente', 600, 900, 120),
	(30, 'DVD de películas clásicas', 200, 400, 180),
	(31, 'Máquina de café Nespresso', 3500, 4500, 35);

-- Volcando estructura para tabla ejercicio_base_de_datos.productos_departamento
CREATE TABLE IF NOT EXISTS `productos_departamento` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `producto_id` int(11) DEFAULT NULL,
  `departamento_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `producto_id` (`producto_id`),
  KEY `departamento_id` (`departamento_id`),
  CONSTRAINT `productos_departamento_ibfk_1` FOREIGN KEY (`producto_id`) REFERENCES `productos` (`id`),
  CONSTRAINT `productos_departamento_ibfk_2` FOREIGN KEY (`departamento_id`) REFERENCES `catdepartamentoproducto` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Volcando datos para la tabla ejercicio_base_de_datos.productos_departamento: ~48 rows (aproximadamente)
INSERT INTO `productos_departamento` (`id`, `producto_id`, `departamento_id`) VALUES
	(1, 1, 1),
	(2, 1, 5),
	(3, 2, 1),
	(4, 2, 10),
	(5, 2, 8),
	(6, 3, 1),
	(7, 3, 7),
	(8, 3, 8),
	(9, 4, 1),
	(10, 5, 3),
	(11, 5, 7),
	(12, 6, 2),
	(13, 7, 1),
	(14, 8, 5),
	(15, 8, 6),
	(16, 9, 6),
	(17, 9, 8),
	(18, 10, 2),
	(19, 11, 1),
	(20, 11, 7),
	(21, 12, 1),
	(22, 13, 1),
	(23, 14, 1),
	(24, 15, 2),
	(25, 15, 3),
	(26, 16, 1),
	(27, 16, 7),
	(28, 17, 3),
	(29, 17, 7),
	(30, 17, 8),
	(31, 18, 2),
	(32, 19, 3),
	(33, 20, 1),
	(34, 21, 5),
	(35, 21, 10),
	(36, 22, 8),
	(37, 23, 9),
	(38, 23, 7),
	(39, 24, 7),
	(40, 25, 8),
	(41, 26, 1),
	(42, 27, 5),
	(43, 28, 1),
	(44, 29, 5),
	(45, 29, 10),
	(46, 30, 8),
	(47, 31, 4),
	(48, 31, 8);

-- Volcando estructura para tabla ejercicio_base_de_datos.sucursales
CREATE TABLE IF NOT EXISTS `sucursales` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(60) DEFAULT NULL,
  `direccion` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `direccion` (`direccion`),
  CONSTRAINT `sucursales_ibfk_1` FOREIGN KEY (`direccion`) REFERENCES `direcciones` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Volcando datos para la tabla ejercicio_base_de_datos.sucursales: ~10 rows (aproximadamente)
INSERT INTO `sucursales` (`id`, `nombre`, `direccion`) VALUES
	(1, 'Sanborns Morelia Centro', 1),
	(2, 'Sanborns Chapultepec', 2),
	(3, 'Sanborns Las Américas', 3),
	(4, 'Sanborns Cuauhtémoc', 4),
	(5, 'Sanborns Roma Norte', 5),
	(6, 'Sanborns Centro Histórico', 6),
	(7, 'Sanborns Guadalupe Inn', 7),
	(8, 'Sanborns Jardines de la Concepción', 8),
	(9, 'Sanborns Aguascalientes Centro', 9),
	(10, 'Sanborns Narvarte Poniente', 10);

-- Volcando estructura para tabla ejercicio_base_de_datos.ventas
CREATE TABLE IF NOT EXISTS `ventas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` date DEFAULT NULL,
  `cliente` int(11) DEFAULT NULL,
  `total` int(11) DEFAULT NULL,
  `sucursal` int(11) DEFAULT NULL,
  `empleado` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `cliente` (`cliente`),
  KEY `sucursal` (`sucursal`),
  KEY `empleado` (`empleado`),
  CONSTRAINT `ventas_ibfk_1` FOREIGN KEY (`cliente`) REFERENCES `clientes` (`id`),
  CONSTRAINT `ventas_ibfk_2` FOREIGN KEY (`sucursal`) REFERENCES `sucursales` (`id`),
  CONSTRAINT `ventas_ibfk_3` FOREIGN KEY (`empleado`) REFERENCES `empleados` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Volcando datos para la tabla ejercicio_base_de_datos.ventas: ~10 rows (aproximadamente)
INSERT INTO `ventas` (`id`, `fecha`, `cliente`, `total`, `sucursal`, `empleado`) VALUES
	(1, '2023-10-01', 1, 135000, 1, 1),
	(2, '2023-10-02', 2, 44500, 2, 2),
	(3, '2023-10-03', 3, 32000, 3, 3),
	(4, '2023-10-04', 4, 100000, 4, 4),
	(5, '2023-10-05', 5, 31000, 5, 5),
	(6, '2023-10-06', 6, 25200, 6, 6),
	(7, '2023-10-07', 7, 10500, 7, 7),
	(8, '2023-10-08', 8, 2600, 8, 8),
	(9, '2023-10-09', 9, 14500, 9, 9),
	(10, '2023-10-10', 10, 2500, 10, 10);

-- Volcando estructura para tabla ejercicio_base_de_datos.venta_detalleventa
CREATE TABLE IF NOT EXISTS `venta_detalleventa` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `venta_id` int(11) DEFAULT NULL,
  `detalle_venta_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `venta_id` (`venta_id`),
  KEY `detalle_venta_id` (`detalle_venta_id`),
  CONSTRAINT `venta_detalleventa_ibfk_1` FOREIGN KEY (`venta_id`) REFERENCES `ventas` (`id`),
  CONSTRAINT `venta_detalleventa_ibfk_2` FOREIGN KEY (`detalle_venta_id`) REFERENCES `detalleventa` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Volcando datos para la tabla ejercicio_base_de_datos.venta_detalleventa: ~30 rows (aproximadamente)
INSERT INTO `venta_detalleventa` (`id`, `venta_id`, `detalle_venta_id`) VALUES
	(1, 1, 1),
	(2, 1, 2),
	(3, 1, 3),
	(4, 2, 4),
	(5, 2, 5),
	(6, 2, 6),
	(7, 3, 7),
	(8, 3, 8),
	(9, 3, 9),
	(10, 4, 10),
	(11, 4, 11),
	(12, 4, 12),
	(13, 5, 13),
	(14, 5, 14),
	(15, 5, 15),
	(16, 6, 16),
	(17, 6, 17),
	(18, 6, 18),
	(19, 7, 19),
	(20, 7, 20),
	(21, 7, 21),
	(22, 8, 22),
	(23, 8, 23),
	(24, 8, 24),
	(25, 9, 25),
	(26, 9, 26),
	(27, 9, 27),
	(28, 10, 28),
	(29, 10, 29),
	(30, 10, 30);

-- Volcando estructura para vista ejercicio_base_de_datos.cliente_datos
-- Eliminando tabla temporal y crear estructura final de VIEW
DROP TABLE IF EXISTS `cliente_datos`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `cliente_datos` AS SELECT	a.id AS 'id Detalle Venta',
			c.nombre AS 'Cliente',
			t.descripcion AS 'Tipo de cliente', 
			v.fecha AS 'Fecha de venta',
			p.nombre AS 'Productos',
			p.existencia AS 'Existencias',
			a.cantidad AS 'Vendidos',
			p.costo AS 'Costo',
			a.precio_venta AS 'Precio de Venta',
			a.importe AS 'Importe',
			v.id AS 'Id Venta',
			v.total AS 'Total',
			e.nombre_completo AS 'Empleado',
			s.nombre AS 'Sucursal',
			CONCAT(d.calle_numero,', ',d.Colonia,'.') AS 'Dirección',
			CONCAT(d.Municipio,', ',d.Estado,'. ') AS 'Ciudad',
			d.CP AS 'C.P.'	
FROM detalleventa a
INNER JOIN productos p ON a.producto = p.id
INNER JOIN venta_detalleventa b ON a.id = b.detalle_venta_id
INNER JOIN ventas v ON b.venta_id = v.id
INNER JOIN clientes c ON v.cliente = c.id
INNER JOIN sucursales s ON v.sucursal = s.id
INNER JOIN empleados e ON v.empleado = e.id
INNER JOIN direcciones d ON s.direccion = d.id
INNER JOIN cattipocliente t ON c.tipo_cliente = t.id ;

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
