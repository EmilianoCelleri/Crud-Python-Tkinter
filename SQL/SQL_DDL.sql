CREATE DATABASE IF NOT EXISTS audioteca;

USE audioteca;

CREATE TABLE IF NOT EXISTS artistas(
    id_artista INTEGER PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS temas(
    id_tema INTEGER PRIMARY KEY,
    nombre_tema VARCHAR(50) NOT NULL,
    id_artista INTEGER,
    FOREIGN KEY (id_artista) REFERENCES
    artistas(id_artista)
);


#SHOW TABLES FROM audioteca;
#DESCRIBE artistas;
#DESCRIBE temas;

CREATE TABLE IF NOT EXISTS random (columna1 INTEGER);

#AGREGAR COLUMNAS

#ALTER TABLE random ADD columna2 VARCHAR(30);
#ALTER TABLE random ADD columna3 VARCHAR(150);
#ALTER TABLE random DROP columna2;
#DESCRIBE random;
DROP TABLE IF EXISTS random;

ALTER TABLE temas ADD genero VARCHAR(30);