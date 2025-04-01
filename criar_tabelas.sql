-- Tabela para Dados Cadastrais das Operadoras
CREATE TABLE Operadoras (
    RegistroANS VARCHAR(255) PRIMARY KEY,
    CNPJ VARCHAR(255),
    RazaoSocial VARCHAR(255),
    NomeFantasia VARCHAR(255),
    Modalidade VARCHAR(255),
    Logradouro VARCHAR(255),
    Numero VARCHAR(255),
    Complemento VARCHAR(255),
    Bairro VARCHAR(255),
    Cidade VARCHAR(255),
    UF VARCHAR(255),
    CEP VARCHAR(255),
    DDD VARCHAR(255),
    Telefone VARCHAR(255),
    Fax VARCHAR(255),
    EnderecoEletronico VARCHAR(255),
    DataRegistroANS DATE
);

-- Tabela para Demonstrações Contábeis
CREATE TABLE DemonstracoesContabeis (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    RegistroANS VARCHAR(255),
    Data DATE,
    CD_CONTA_CONTABIL VARCHAR(255),
    DS_CONTA_CONTABIL VARCHAR(255),
    VL_SALDO_FINAL DECIMAL(18, 2)
);

-- Importar dados do CSV para a tabela Operadoras
LOAD DATA INFILE '/caminho/arquivo/Operadoras.csv'
INTO TABLE Operadoras
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- Importar dados do CSV para a tabela DemonstracoesContabeis
LOAD DATA INFILE '/caminho/arquivo/DemonstracoesContabeis.csv'
INTO TABLE DemonstracoesContabeis
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- Queries analíticas
SELECT RegistroANS, SUM(VL_SALDO_FINAL) AS TotalDespesas
FROM DemonstracoesContabeis
WHERE DS_CONTA_CONTABIL = 'EVENTOS/SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR'
AND Data >= DATE_SUB(CURDATE(), INTERVAL 3 MONTH)
GROUP BY RegistroANS
ORDER BY TotalDespesas DESC
LIMIT 10;

-- 10 operadoras com maiores despesas no último ano
SELECT RegistroANS, SUM(VL_SALDO_FINAL) AS TotalDespesas
FROM DemonstracoesContabeis
WHERE DS_CONTA_CONTABIL = 'EVENTOS/SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR'
AND Data >= DATE_SUB(CURDATE(), INTERVAL 1 YEAR)
GROUP BY RegistroANS
ORDER BY TotalDespesas DESC
LIMIT 10;
