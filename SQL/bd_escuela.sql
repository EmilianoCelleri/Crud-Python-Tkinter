CREATE DATABASE IF NOT EXISTS db_escuela;

USE db_escuela;

CREATE TABLE escuelas (
  id int(11) NOT NULL AUTO_INCREMENT,
  nombre varchar(45) DEFAULT NULL,
  localidad varchar(45) DEFAULT NULL,
  provincia varchar(45) DEFAULT NULL,
  capacidad int(11) DEFAULT NULL,
  PRIMARY KEY (id));

CREATE TABLE alumnos (
  id int(11) NOT NULL AUTO_INCREMENT,
  id_escuela int(11) DEFAULT NULL,
  legajo int(11) DEFAULT NULL,
  nombre varchar(45) DEFAULT NULL,
  nota decimal(10,0) DEFAULT NULL,
  grado int(11) DEFAULT NULL,
  email varchar(45) NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (id_escuela) REFERENCES escuelas(id));

INSERT INTO escuelas VALUES (1,'Normal 1','Quilmes','Buenos Aires',250),(2,'Gral. San Martín','San Salvador','Jujuy',100),(3,'Belgrano','Belgrano','Córdoba',150),(4,'EET Nro 2','Avellaneda','Buenos Aires',500),(5,'Esc. N° 2 Tomás Santa coloma','Capital Federal','Buenos Aires',250);

INSERT INTO alumnos VALUES (1,2,1000,'Ramón Mesa',8,1,'rmesa@mail.com'),(2,2,1002,'Tomás Smith',8,1,''),(4,1,101,'Juan Perez',10,3,''),(5,1,105,'Pedro González',9,3,''),(6,5,190,'Roberto Luis Sánchez',8,3,'robertoluissanchez@gmail.com'),(7,2,106,'Martín Bossio',NULL,3,''),(8,4,100,'Paula Remmi',3,1,'mail@mail.com'),(9,4,1234,'Pedro Gómez',6,2,'');