<!--A normalização de dados é um processo realizado nas tabelas para evitar anomalias. Com base no conteúdo visto no Hipertexto 3, transforme a tabela em anexo na Primeira Forma Normal (1FN).
 
Realize essa atividade no WORD ou no Bloco de Notas, suba esse arquivo para algum repositório e compartilhe o link no campo ao lado 
para que outros desenvolvedores possam analisá-lo.-->

CREATE TABLE Pessoas ( <br>
Identificador INT, <br>
Nome VARCHAR(255), <br>
Telefone VARCHAR(255), <br>
Endereco VARCHAR(255), <br>
Email VARCHAR(255), <br>
); <br>

INSERT INTO Pessoas(Identificador, Nome, Telefone, Endereco, Email) <br>
VALUES <br>
	(01, ‘Reinaldo’, ‘68 0945-8723’, ‘Rua, 10, 34, São Paulo, 12345-00, Brasil’, ‘reinaldo00@gmail.com’), <br>
	(01, ‘Reinaldo’, ‘68 8734-2343’, ‘Rua, 10, 34, São Paulo, 12345-00, Brasil’, ‘reinaldo00@gmail.com’), <br>
	(01, ‘Reinaldo’, ‘68 2143-5469’, ‘Rua, 10, 34, São Paulo, 12345-00, Brasil’, ‘reinaldo@outlook.com’), <br>
(02, ‘Nestor’, ‘92 5400-0043’, ‘Avenida Bela, 45, Paulo Afonso, BA, 00034-000, Brasil’,	 ‘nestor123@gmail.com’), <br>
(03, ‘Raquel’, ‘87 4300-0000’, ‘Rua Cardoso, 100, Salvador, BA, 2222-00, Brasil’, ‘raquel@outlook.com’), <br>
	(04, ‘Tati’, ‘41 5400-1232’, ‘Bairro Canoa, 002, Rio de Janeiro, RJ, 34251-324, Brasil’, ‘tati000@gmail.com’), <br>
(04, ‘Tati’, ‘41 4345-555’, ‘Bairro Canoa, 002, Rio de Janeiro, RJ, 34251-324, Brasil’, ‘tati@outlook.com’), <br>
(05, ‘Lia’, ‘98 1234-5678’, ‘Rua 50,41, Macei[o, AL, 32450-0435, Brasil’, ‘lia@outlook.com’), <br>
(06, ‘Paty’, ‘81 2123-2425’, ‘Rua 01, 500, Pinheiros, SP, 90000-00, Brasil’, ‘paty@outlook.com’)


