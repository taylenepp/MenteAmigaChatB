from flask import Flask, request
import os
from dotenv import load_dotenv
import sqlite3

load_dotenv()

app = Flask(_name_)

# Conectar com o banco de dados
DB_PATH = 'mensagens.db'

def obter_resposta(tipo):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT conteudo FROM mensagens WHERE tipo = ? ORDER BY RANDOM() LIMIT 1", (tipo,))
    resultado = cursor.fetchone()
    conn.close()
    return resultado[0] if resultado else "Tudo bem! Estou aqui com você."

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.form
    msg = data.get('Body', '').lower()

    if 'triste' in msg or 'mal' in msg:
        resposta = obter_resposta('apoio')
    elif 'respirar' in msg:
        resposta = obter_resposta('respiracao')
    elif 'humor' in msg:
        resposta = obter_resposta('humor')
    elif 'ajuda' in msg or 'socorro' in msg:
        resposta = obter_resposta('emergencia')
    else:
        resposta = obter_resposta('abertura')

    return resposta, 200

if _name_ == '_main_':
    app.run(debug=True) 
