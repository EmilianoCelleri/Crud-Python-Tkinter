USE audioteca;

#INSERT INTO artistas VALUES (1, 'Beyonce');
#INSERT INTO artistas VALUES (23,'George Michael'),(52,'Tina Turner'),(33, 'Madonna'),(48,'Billy Idol');



#UPDATE artistas SET nombre='The sign' WHERE nombre='Madonna';
#UPDATE artistas SET nombre='GM II' WHERE id_artista='1';
DELETE FROM artistas WHERE nombre='Tina Turner';

SELECT * FROM artistas;