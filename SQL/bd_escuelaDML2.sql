USE db_escuela22609;

# USO DE IS NULL / IS NOT NULL
# 17) Mostrar todos los datos de los alumnos que tengan notas.
# SELECT * FROM alumnos WHERE nota IS NOT NULL;

# 18) Mostrar todos los datos de los alumnos que no tengan notas.
# SELECT * FROM alumnos WHERE nota IS NULL;

# ALTER TABLE
# 19) Realizar lo siguiente:
#  a) Agregar a través de Alter Table una en la tabla escuelas columna llamada “Partido”, a la derecha de Localidad con una cadena vacía como valor por defecto (armar la sentencia a través de Alter Table).
/* ALTER TABLE escuelas ADD COLUMN partido VARCHAR(30) NULL DEFAULT '' AFTER localidad;*/

#  b) Ejecutar una consulta donde se vean todos los campos para confirmar que se ha agregado el campo “partido”.
# SELECT * FROM escuelas;

#  c) Eliminar esa columna utilizando Alter Table.
# ALTER TABLE escuelas DROP COLUMN partido;

# LIMIT Y ORDER BY
# 22) Obtener un ranking de las primeras 3 escuelas de mayor capacidad. */
/*SELECT nombre, capacidad 
FROM escuelas 
ORDER BY capacidad DESC 
LIMIT 3;*/

# FUNCIONES DE AGREGACIÓN Y AGRUPAMIENTO / USO DE IN
# 23) Contar la cantidad de alumnos de la tabla homónima. Llamar a la columna “Cantidad de alumnos”.
/* SELECT COUNT(*) AS 'Cantidad de alumnos'
FROM alumnos;*/

# 24) Repetir la consulta anterior contando solamente los alumnos cuya nota sea menor a 7.*/
/* SELECT COUNT(*) AS 'Cantidad de alumnos'
FROM alumnos WHERE nota < 7;*/


# 25) Obtener la capacidad total de las escuelas de la provincia de Buenos Aires*/
/*SELECT SUM(capacidad) AS 'Capacidad Total'
FROM escuelas
WHERE provincia LIKE 'Buenos Aires'; */
# provincia = 'Buenos Aires' tb VA
# SELECT * FROM escuelas; # chequeo

# 26) Repetir el ejercicio anterior pero solamente con las escuelas de Córdoba y Jujuy*/
/*SELECT SUM(capacidad) AS 'Capacidad Total'
FROM escuelas
WHERE provincia IN ('Córdoba','Jujuy');*/
# IN permite especificar valores múltiples en una cláusula WHERE
# una forma corta para múltiples OR

# 27) Obtener el promedio de notas de los alumnos aprobados con más de 7 
/*SELECT AVG(nota) AS 'Promedio'
FROM alumnos WHERE nota > 7;*/

# 28) Obtener la capacidad máxima y la capacidad mínima de alumnos*/
/*SELECT MAX(capacidad) AS 'Máxima capacidad', MIN(capacidad) AS 'Mínima capacidad' FROM escuelas;*/

# 29) Obtener el total de capacidad de las escuelas por provincia */
/* SELECT provincia AS 'Provincia', SUM(capacidad) AS 'Cantidad de vacantes' FROM escuelas GROUP BY provincia;*/

# 30) Obtener la cantidad de alumnos por grado */
/* SELECT grado AS 'Grado', COUNT(grado) AS 'Cantidad de inscriptos'
FROM alumnos GROUP BY grado;*/

# DIFERENCIAS ENTRE HAVING Y WHERE
# 31) Mostrar las escuelas y la nota máxima para cada una siempre y cuando sean mayores o iguales a 7.
/* SELECT e.nombre AS 'Escuela', MAX(a.nota) AS 'Mejor nota'
FROM escuelas e INNER JOIN alumnos a
ON e.id = a.id_escuela
WHERE nota >=7
GROUP BY e.nombre;*/

/* SELECT e.nombre AS 'Escuela', MAX(a.nota) AS 'Mejor nota'
FROM escuelas e INNER JOIN alumnos a
ON e.id = a.id_escuela
GROUP BY e.nombre HAVING MAX(a.nota) >=7;*/
# HAVING es el WHERE para el GROUP BY


# SUBCONSULTAS
# 32) Mostrar la información de las escuelas cuyos alumnos tengan una nota igual a 10, utilizando una subconsulta.
#SELECT * FROM escuelas
#WHERE id IN
#(SELECT id_escuela FROM alumnos WHERE nota=10);