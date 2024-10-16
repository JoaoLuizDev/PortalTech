-- Crie uma base de dados chamada "Faculdade"
CREATE DATABASE Faculdade;

-- Use a base de dados
\c Faculdade;

-- Crie a tabela "Alunos" com uma coluna de ID auto incremento
CREATE TABLE Alunos (
    ID SERIAL PRIMARY KEY,
    Nome VARCHAR(255),
    Email VARCHAR(255),
    Matricula VARCHAR(15)
);

-- Crie a tabela "Cursos" com uma coluna de AlunoID que é uma chave estrangeira referenciando Alunos
CREATE TABLE Cursos (
    ID SERIAL PRIMARY KEY,
    AlunoID INT,
    NomeCurso VARCHAR(255),
    Creditos INT,
    DataInscricao DATE,
    FOREIGN KEY (AlunoID) REFERENCES Alunos(ID)
);

-- Insira dados na tabela "Alunos"
INSERT INTO Alunos (Nome, Email, Matricula)
VALUES
    ('João Luiz', 'joaoluiz@email.com', '20232023'),
    ('Maria Dias', 'mariadias@email.com', '20222022');

-- Insira dados na tabela "Cursos"
INSERT INTO Cursos (AlunoID, NomeCurso, Creditos, DataInscricao)
VALUES
    (1, 'Ciências da Computação', 120, '2023-10-15'),
    (2, 'Engenharia Elétrica', 110, '2023-10-16');
    
-- Utilize os comandos Joins para realizar consultas nas tabelas. 

-- Consulta de alunos e cursos usando INNER JOIN
SELECT Alunos.Nome, Cursos.NomeCurso
FROM Alunos
INNER JOIN Cursos ON Alunos.ID = Cursos.AlunoID;

-- Consulta de alunos e cursos usando LEFT JOIN
SELECT Alunos.Nome, Cursos.NomeCurso
FROM Alunos
LEFT JOIN Cursos ON Alunos.ID = Cursos.AlunoID;

-- Consulta de alunos e cursos usando RIGHT JOIN
SELECT Alunos.Nome, Cursos.NomeCurso
FROM Alunos
RIGHT JOIN Cursos ON Alunos.ID = Cursos.AlunoID;

-- Consulta de alunos e cursos usando FULL OUTER JOIN
SELECT Alunos.Nome, Cursos.NomeCurso
FROM Alunos
FULL OUTER JOIN Cursos ON Alunos.ID = Cursos.AlunoID;

-- Consulta de todos os pares possíveis de aluno e curso usando CROSS JOIN
SELECT Alunos.Nome, Cursos.NomeCurso
FROM Alunos
CROSS JOIN Cursos;
