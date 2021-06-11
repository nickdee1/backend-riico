-- CREATE TABLE

use riico;

--
-- Table structure for table `furniture`
--

DROP TABLE IF EXISTS `Furniture`;
CREATE TABLE `Furniture` (
	`id` INT unsigned NOT NULL AUTO_INCREMENT COMMENT 'Furniture ID',
	`category` VARCHAR(64) NOT NULL COMMENT 'Category of a furniture',
	`name` VARCHAR(64) NOT NULL  COMMENT 'Brand name of a furniture',
	`color` VARCHAR(64) NOT NULL COMMENT 'Color of a furniture',
	`location` VARCHAR(64) NOT NULL COMMENT 'Location of a furniture',
	`material` VARCHAR(64) NOT NULL  COMMENT 'Material',
	`width` INT unsigned NOT NULL COMMENT 'Width of a model',
	`height` INT unsigned NOT NULL COMMENT 'Height of a model',
	PRIMARY KEY (`id`)
);


DROP TABLE IF EXISTS `Component`;
CREATE TABLE `Component` (
	`id` INT unsigned NOT NULL AUTO_INCREMENT COMMENT 'Component ID - foreign key',
	`name` VARCHAR(64) NOT NULL COMMENT 'Brand name of a furniture',
	`price` INT unsigned NOT NULL COMMENT 'Price of a component',
	PRIMARY KEY (`id`)
);


DROP TABLE IF EXISTS `FurnitureComponent`;
CREATE TABLE `FurnitureComponent` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `furniture_id` INT NOT NULL,
    `component_id` INT NOT NULL,
	PRIMARY KEY (`id`)
);


ALTER TABLE `FurnitureComponent` ADD CONSTRAINT `FurnitureComponent_fk0` FOREIGN KEY (`furniture_id`) REFERENCES `Furniture` (`id`);

ALTER TABLE `FurnitureComponent` ADD CONSTRAINT `FurnitureComponent_fk1` FOREIGN KEY (`component_id`) REFERENCES `Component` (`id`);


