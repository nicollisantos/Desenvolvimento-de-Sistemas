CREATE DATABASE IF NOT EXISTS aula_terca;

USE aula_terca;
CREATE TABLE IF NOT EXISTS alunos(
	matricula INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    idade INT,
    curso VARCHAR(50)
);

-- TRUNCATE TABLE alunos;

INSERT INTO alunos (nome, idade, curso) VALUES ("Nicolli", 17, "Jovem Programador");
INSERT INTO alunos (nome, idade, curso) VALUES ("Lorrany", 16, "teatro");
INSERT INTO alunos (nome, idade, curso) VALUES ("Lucas", 19, "Desenvolvimento de Sistemas");
INSERT INTO alunos (nome, idade, curso) VALUES ("Eduardo", 18, "Comunicação Visual");
INSERT INTO alunos (nome, idade, curso) VALUES ("Manuela", 18, "Jovem Aprendiz");

SELECT * FROM alunos;
