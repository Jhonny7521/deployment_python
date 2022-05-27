-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema belt_python
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema belt_python
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `belt_python` DEFAULT CHARACTER SET utf8 COLLATE utf8_bin ;
USE `belt_python` ;

-- -----------------------------------------------------
-- Table `belt_python`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `belt_python`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(150) NULL,
  `last_name` VARCHAR(150) NULL,
  `email` VARCHAR(150) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `belt_python`.`shows`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `belt_python`.`shows` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(150) NULL,
  `network` VARCHAR(150) NULL,
  `release_date` DATETIME NULL,
  `description` TEXT NULL,
  `like` INT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `users_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_shows_users_idx` (`users_id` ASC) VISIBLE,
  CONSTRAINT `fk_shows_users`
    FOREIGN KEY (`users_id`)
    REFERENCES `belt_python`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `belt_python`.`users_has_shows`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `belt_python`.`users_has_shows` (
  `users_id` INT NOT NULL,
  `shows_id` INT NOT NULL,
  PRIMARY KEY (`users_id`, `shows_id`),
  INDEX `fk_users_has_shows_shows1_idx` (`shows_id` ASC) VISIBLE,
  INDEX `fk_users_has_shows_users1_idx` (`users_id` ASC) VISIBLE,
  CONSTRAINT `fk_users_has_shows_users1`
    FOREIGN KEY (`users_id`)
    REFERENCES `belt_python`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_shows_shows1`
    FOREIGN KEY (`shows_id`)
    REFERENCES `belt_python`.`shows` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
