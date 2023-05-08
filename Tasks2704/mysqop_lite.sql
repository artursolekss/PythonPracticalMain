-- SQLite3 dump
-- version 3.33.0

PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;

--
-- Table structure for table `categories`
--

CREATE TABLE `categories` (
  `id` INTEGER NOT NULL,
  `name` TEXT NOT NULL,
  `external_id` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`id`)
);

--
-- Data for table `categories`
--

INSERT INTO `categories` (`id`, `name`, `external_id`) VALUES
(7, 'Fruits', '0001'),
(8, 'Vegetables', '0002'),
(9, 'Drinks', '0003');

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `id` INTEGER NOT NULL,
  `name` VARCHAR(60) NOT NULL,
  `surname` VARCHAR(60) NOT NULL,
  `phone` BIGINT NOT NULL,
  `email` TEXT NOT NULL,
  `ext_id` VARCHAR(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
);

--
-- Data for table `customer`
--

INSERT INTO `customer` (`id`, `name`, `surname`, `phone`, `email`, `ext_id`) VALUES
(1, 'Arturs', 'Olekss', 28574076, 'ao@gmail.com', 'CUS00001'),
(2, 'Jacks', 'Sparrow', 28496047, 'js@gmail.com', 'CUS00002');

--
-- Table structure for table `orders`
--

CREATE TABLE `orders` (
  `id` INTEGER NOT NULL,
  `date` DATE NOT NULL,
  `customer_id` INTEGER NOT NULL,
  `status` INTEGER NOT NULL,
  `ext_id` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`customer_id`) REFERENCES `customer`(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`status`) REFERENCES `status`(`id`) ON DELETE CASCADE
);

--
-- Data for table `orders`
--

INSERT INTO `orders` (`id`, `date`, `customer_id`, `status`, `ext_id`) VALUES
(15, '2022-02-01', 1, 3, 'ORD00001'),
(16, '2022-05-07', 2, 3, 'ORD00002');

--
-- Table structure for table `order_products`
--

CREATE TABLE `order_products` (
  `order_id` INTEGER NOT NULL,
  `product_id` INTEGER NOT NULL,
  `product_amount` INTEGER NOT NULL,
  FOREIGN KEY (`order_id`) REFERENCES `orders`(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`product_id`) REFERENCES `products`(`id`) ON DELETE CASCADE
);

--
-- Data for table `order_products`
--

INSERT INTO `order_products` (`order_id`, `product_id`, `product_amount`) VALUES
(15, 1, 5),
(15, 2, 3),
(16, 1, 3);

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `id` INTEGER NOT NULL,
  `title` VARCHAR(20) NOT NULL,
  `description` TEXT NOT NULL,
  `price` FLOAT NOT NULL,
  `warranty` VARCHAR(30) NOT NULL,
  `category` INTEGER NOT NULL,
  `supplier_id` INTEGER NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`category`) REFERENCES `categories`(`id`) ON DELETE CASCADE
);