import tabula
import pandas as pd
import zipfile
import os
import logging
import importlib

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def extrair_tabela_anexo_i(arquivo_pdf):
    """Extrai tabelas de um arquivo PDF."""
    try:
        logging.info(f"Extraindo tabelas do PDF: {arquivo_pdf}")
        if not os.path.exists(arquivo_pdf):
            logging.error(f"Arquivo PDF não encontrado: {arquivo_pdf}")
            return None

        if importlib.util.find_spec('jpype') is None:
          logging.warning

        tabelas = tabula.read_pdf(arquivo_pdf, pages="all")
        if tabelas:
            df = pd.concat(tabelas)
            logging.info("Tabelas extraídas com sucesso.")
            return df
        else:
            logging.warning("Nenhuma tabela encontrada no PDF.")
            return None
    except Exception as e:
        logging.error(f"Erro ao extrair tabela do PDF: {e}")
        return None

def substituir_abreviacoes(df):
    """Substitui abreviações 'OD' e 'AMB' por suas descrições completas."""
    if df is not None:
        try:
            logging.info("Substituindo abreviações.")
            df.replace(
                {"OD": "Obrigatoriedade de cobertura definida para o segmento odontológico",
                 "AMB": "Obrigatoriedade de cobertura definida para o segmento ambulatorial"},
                inplace=True,
            )
            logging.info("Abreviações substituídas com sucesso.")
            return df
        except Exception as e:
            logging.error(f"Erro ao substituir abreviações: {e}")
            return df
    else:
        logging.warning("Não é possível substituir abreviações.")
        return None

def salvar_csv(df, nome_arquivo):
    if df is not None:
        try:
            logging.info(f"Salvando DataFrame em CSV: {nome_arquivo}")
            df.to_csv(nome_arquivo, index=False, encoding="utf-8")
            logging.info("DataFrame salvo em CSV com sucesso.")
        except Exception as e:
            logging.error(f"Erro ao salvar CSV: {e}")
    else:
        logging.warning("DataFrame é None. Não é possível salvar em CSV.")

def compactar_csv(nome_arquivo_csv, nome_arquivo_zip):
    """Compacta um arquivo CSV em um arquivo ZIP."""
    try:
        logging.info(f"Compactando CSV em ZIP: {nome_arquivo_zip}")
        with zipfile.ZipFile(nome_arquivo_zip, 'w', zipfile.ZIP_DEFLATED) as arquivo_zip:
            arquivo_zip.write(nome_arquivo_csv)
        logging.info(f"Arquivo CSV compactado em {nome_arquivo_zip}")
    except FileNotFoundError:
        logging.error(f"Arquivo CSV não encontrado: {nome_arquivo_csv}")
    except Exception as e:
        logging.error(f"Erro ao compactar CSV: {e}")

def main():
    """Função principal para coordenar todas as operações."""
    try:
        arquivo_pdf = os.path.join(os.path.abspath("./arquivos"), "Anexo_I_Rol_2021RN_465.2021_RN473.pdf")
        nome_arquivo_csv = "tabela_anexo_i.csv"
        nome_arquivo_zip = "juniormorais.zip"

        df = extrair_tabela_anexo_i(arquivo_pdf)
        if df is not None:
            df_substituido = substituir_abreviacoes(df)
            salvar_csv(df_substituido, nome_arquivo_csv)
            compactar_csv(nome_arquivo_csv, nome_arquivo_zip)
        else:
            logging.error("Falha ao extrair DataFrame do PDF. Operações subsequentes ignoradas.")
    except Exception as e:
        logging.critical(f"Erro crítico no fluxo principal: {e}")

if __name__ == "__main__":
    main()
