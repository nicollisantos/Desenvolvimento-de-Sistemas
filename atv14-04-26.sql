CREATE DATABASE IF NOT EXISTS livraria_db;

USE livraria_db;
CREATE TABLE IF NOT EXISTS livros(
	id INT AUTO_INCREMENT PRIMARY KEY,
	título VARCHAR(10000),
    autor VARCHAR(100),
    ano_publicacao INT,
    preco DECIMAL(65,2)
);

INSERT INTO livros (título, autor, ano_publicacao, preco) VALUES ("Coraline", "Neil Gaiman", 2002, 51.96);
INSERT INTO livros (título, autor, ano_publicacao, preco) VALUES ("O Homem de Giz", "C. J. Tudor", 2018, 56.00);
INSERT INTO livros (título, autor, ano_publicacao, preco) VALUES ("Um Estudo em Vermelho", "Árthur Conan Doyle", 1887, 18.90);
INSERT INTO livros (título, autor, ano_publicacao, preco) VALUES ("Harry Potter e A Pedra Filosofal", "J. K. Rowling", 1997, 38.94);

SELECT *FROM livros;

SELECT * FROM livros WHERE autor = "Neil Gaiman";
-- TRUNCATE TABLE livros;
-- DROP TABLE livros;