import os
import requests
from bs4 import BeautifulSoup
import zipfile

path_down = os.path.abspath("./arquivos")

def criar_pasta(dir: str):
    if not os.path.exists(dir):
        os.makedirs(dir)
        print(f"Pasta '{dir}' criada com sucesso!")
    return dir

def baixar_pdf(url, nome_arquivo):
    print(f"Baixando PDF de {url}...")
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(nome_arquivo, "wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        print(f"Download concluído: {nome_arquivo}")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao baixar PDF: {e}")

def scrappy_site():
    url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        links_pdf = soup.find_all("a", href=lambda href: href and ( "Anexo_I_Rol" in href or "Anexo_II_DUT" in href))
        for link in links_pdf:
            pdf_url = link["href"]
            nome_arquivo = os.path.join(path_down, pdf_url.split("/")[-1])
            baixar_pdf(pdf_url, nome_arquivo)
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar o site: {e}")

def compactar_arquivos(diretorio, nome_zip):
    try:
        with zipfile.ZipFile(nome_zip, 'w', zipfile.ZIP_DEFLATED) as arquivo_zip:
            for nome_arquivo in os.listdir(diretorio):
                caminho_arquivo = os.path.join(diretorio, nome_arquivo)
                if os.path.isfile(caminho_arquivo):
                    arquivo_zip.write(caminho_arquivo, nome_arquivo)
        print(f"Arquivos compactados em {nome_zip}")
    except Exception as e:
        print(f"Erro ao compactar arquivos: {e}")

if __name__ == "__main__":
    criar_pasta(path_down)
    scrappy_site()
    compactar_arquivos(path_down, "anexos.zip")
