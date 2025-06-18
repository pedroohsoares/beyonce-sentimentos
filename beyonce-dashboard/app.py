from flask import Flask, jsonify, render_template
import pandas as pd

# Inicializa o aplicativo Flask
app = Flask(__name__)

# Carrega os dados do seu CSV. 
# Ajuste o caminho se necessário.
df = pd.read_csv('data/analise_musical_beyonce.csv')

# --- Nossas Rotas (os "links" do site) ---

# Rota 1: A página principal (index.html)
@app.route('/')
def home():
    # O Flask vai procurar por 'index.html' na pasta 'templates'
    return render_template('index.html')

# Rota 2: A API que entrega os dados em formato JSON
@app.route('/api/dados-albuns')
def get_dados_albuns():
    # Converte o DataFrame para um formato de dicionário (JSON)
    dados_json = df.to_dict(orient='records')
    # Retorna os dados usando jsonify para o navegador entender
    return jsonify(dados_json)

# --- Fim das Rotas ---


# Roda o servidor quando o script é executado
if __name__ == '__main__':
    # debug=True faz o servidor reiniciar sozinho quando você salva uma alteração
    app.run(debug=True)