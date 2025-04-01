# intuitive

Sistema de Extração e Análise de Dados da ANS
Este sistema é composto por scripts Python e SQL para extrair, transformar e analisar dados do site da Agência Nacional de Saúde Suplementar (ANS). Ele é dividido em quatro partes principais:

1. Extração de Dados da Web (Scrappy.py)
Este script utiliza as seguintes bibliotecas Python:

requests: Para fazer requisições HTTP e baixar arquivos PDF do site da ANS.
BeautifulSoup (bs4): Para analisar o HTML do site e extrair os links dos arquivos PDF.
zipfile: Para compactar os arquivos PDF baixados em um arquivo ZIP.
os: Para manipulação de arquivos e diretórios.
logging: Para o registro de eventos e erros durante a execução do script.
Funções Principais:

criar_pasta(dir): Cria um diretório se ele não existir.
baixar_pdf(url, nome_arquivo): Baixa um arquivo PDF de uma URL e salva em um arquivo local.
scrappy_site(): Acessa o site da ANS, extrai os links dos PDFs do Anexo I e Anexo II e os baixa.
compactar_arquivos(diretorio, nome_zip): Compacta todos os arquivos em um diretório em um arquivo ZIP.
2. Transformação de Dados (Transformacao.py)
Este script utiliza as seguintes bibliotecas Python:

tabula: Para extrair tabelas de arquivos PDF.
pandas: Para manipulação e análise de dados em formato de tabela (DataFrame).
zipfile: Para compactar o arquivo CSV em um arquivo ZIP.
os: Para manipulação de arquivos e diretórios.
logging: Para o registro de eventos e erros durante a execução do script.
importlib: para verificar se o jpype está instalado.
Funções Principais:

extrair_tabela_anexo_i(arquivo_pdf): Extrai tabelas do PDF do Anexo I e retorna os dados como uma lista de listas.
substituir_abreviacoes(dados_arquivo): Substitui as abreviações "OD" e "AMB" pelas descrições completas nos dados extraídos.
salvar_csv(dados_arquivo, nome_arquivo): Salva os dados em um arquivo CSV.
compactar_csv(nome_arquivo_csv, nome_arquivo_zip): Compacta o arquivo CSV em um arquivo ZIP.
main(): Coordena a execução de todas as funções.
3. Análise de Dados com SQL (Criar_Tabelas.sql)
Este script SQL cria tabelas no MySQL ou PostgreSQL e importa dados de arquivos CSV para essas tabelas. Ele também realiza consultas analíticas para responder a perguntas sobre as despesas das operadoras.

Estrutura do Script:

Cria as tabelas Operadoras e DemonstracoesContabeis.
Importa dados dos arquivos CSV para as tabelas usando LOAD DATA INFILE (MySQL) ou COPY (PostgreSQL).
Realiza consultas SQL para encontrar as 10 operadoras com maiores despesas nos últimos três meses e no último ano.
4. API Web com Vue.js e Flask (server.py e intuitive.html)
Esta parte do sistema consiste em um servidor Python (Flask) e uma interface web Vue.js para realizar buscas textuais nos dados das operadoras.

server.py (Servidor Flask):

Utiliza as bibliotecas Flask, pandas e re.
Carrega os dados das operadoras do arquivo Operadoras.csv.
Define uma rota /buscar que recebe um parâmetro de consulta e retorna os resultados da busca em formato JSON.
intuitive.html (Interface Vue.js):

Utiliza as bibliotecas Vue.js e Axios.
Permite que o usuário insira um termo de busca e exibe os resultados em uma lista.
Instruções de Uso
Execute o script Scrappy.py para baixar os arquivos PDF e compactá-los.
Execute o script Transformacao.py para extrair os dados do PDF do Anexo I, salvá-los em CSV e compactar o CSV.
Execute o script Criar_Tabelas.sql no MySQL ou PostgreSQL para criar as tabelas e importar os dados.
Execute o script server.py para iniciar o servidor Flask.
Abra o arquivo intuitive.html em um navegador web para interagir com a interface de busca.
Use o Postman para testar a API /buscar com diferentes termos de busca.
Este README fornece uma visão geral do sistema e suas funcionalidades. Para mais detalhes, consulte os comentários nos arquivos de código.
