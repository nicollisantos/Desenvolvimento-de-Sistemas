CREATE DATABASE IF NOT EXISTS senac;

USE senac;

CREATE TABLE IF NOT EXISTS alunos(
	nome VARCHAR(100),
    idade INT
);

INSERT INTO alunos (nome, idade) VALUES ("Matheus", 23);
INSERT INTO alunos (nome, idade) VALUES ("Claudio", 45);

SELECT * FROM alunos;

UPDATE alunos SET nome = "Roger", idade = 30 WHERE nome = "Matheus";

DELETE FROM alunos WHERE nome = "Claudio";

TRUNCATE TABLE alunos;