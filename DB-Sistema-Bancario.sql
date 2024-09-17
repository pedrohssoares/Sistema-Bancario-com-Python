DROP DATABASE IF EXISTS DbSistemaBancario;
CREATE DATABASE DbSistemaBancario;
USE DbSistemaBancario;

	CREATE TABLE TbLogin(
		Id INT PRIMARY KEY AUTO_INCREMENT,
        Cpf VARCHAR(11) NOT NULL,
        Senha VARCHAR(200) NOT NULL,
        Nome VARCHAR(200) NOT NULL,
        DataNasc DATE NOT NULL
    );
    
    CREATE TABLE TbContas(
		NumConta INT PRIMARY KEY AUTO_INCREMENT,
        NumAgencia INT NOT NULL,
        IdCli INT NOT NULL,
        Saldo DECIMAL NOT NULL,
        FOREIGN KEY (IdCli) REFERENCES TbLogin.Id
    );
    
   DELIMITER //
   CREATE PROCEDURE ConsultarSaldo(IN vCpf VARCHAR(11))
   BEGIN
   DECLARE vId INT;
   SELECT Id INTO vId FROM TbLogin WHERE Cpf = vCpf;
   SELECT Saldo FROM TbContas WHERE IdCli = vId;
   END //
   DELIMITER ;

   