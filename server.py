from flask import Flask, request, jsonify
import pandas as pd
import re
import os

app = Flask(__name__)

# Carrega os dados do CSV
caminho_csv = os.path.join(os.getcwd(), 'Operadoras.csv')
try:
    df = pd.read_csv(caminho_csv)
except FileNotFoundError:
    print(f"Erro: Arquivo 'Operadoras.csv' não encontrado em: {caminho_csv}")
    df = pd.DataFrame()  # Cria um DataFrame vazio para evitar erros posteriores

@app.route('/buscar', methods=['GET'])
def buscar():
    consulta = request.args.get('consulta', '')
    if not consulta:
        return jsonify(df.to_dict(orient='records'))

    # Realiza a busca textual em todas as colunas
    def contar_correspondencias(row):
        texto = ' '.join(row.astype(str).values)
        return len(re.findall(consulta, texto, re.IGNORECASE))

    resultados = df[df.apply(lambda row: contar_correspondencias(row) > 0, axis=1)].copy()
    resultados['relevancia'] = resultados.apply(lambda row: contar_correspondencias(row), axis=1)
    resultados = resultados.sort_values(by='relevancia', ascending=False)
    return jsonify(resultados.drop(columns=['relevancia']).to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
