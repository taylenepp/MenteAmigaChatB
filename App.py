from flask import Flask, request 
import os 
from dotenv import load_dotenv 
import sqlite3 

load_dotenv() 

import sqlite3
import os

# Criar banco uma vez se ainda não existir
if not os.path.exists("mensagens.db"):
    conn = sqlite3.connect('mensagens.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS mensagens (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tipo TEXT NOT NULL,
        conteudo TEXT NOT NULL
    )
    ''')
    mensagens = [
        ('apoio', 'Sinto muito por você estar assim. Você não está sozinho. ❤️'),
        ('apoio', 'Estou aqui com você. Respire fundo, vai passar.'),
        ('respiracao', 'Vamos respirar juntos? Inspire... Segure... Expire lentamente.'),
        ('respiracao', 'Feche os olhos por 10 segundos e respire fundo. Tudo bem.'),
        ('humor', 'Sabe qual o cúmulo da paciência? Esperar um cego achar uma agulha no palheiro 😂'),
        ('humor', 'Por que o livro foi ao médico? Porque ele tinha muitas páginas em branco! 🤓'),
        ('emergencia', 'Se você estiver em perigo imediato, ligue para 188 (CVV) ou procure ajuda médica.'),
        ('emergencia', 'Por favor, busque ajuda imediatamente. Ligue para 188 ou fale com alguém de confiança.'),
        ('abertura', 'Olá! Como você está se sentindo hoje?'),
        ('abertura', 'Oi! Estou aqui para conversar com você. Como posso ajudar?')
    ]
    cursor.executemany('INSERT INTO mensagens (tipo, conteudo) VALUES (?, ?)', mensagens)
    conn.commit()
    conn.close()
    print("Banco de dados criado e populado com sucesso!")


app = Flask(__name__) 

# Conectar com o banco de dados 
DB_PATH = 'mensagens.db' 

def obter_resposta(tipo): 
    conn = sqlite3.connect(DB_PATH) 
    cursor = conn.cursor() 
    cursor.execute("SELECT conteudo FROM mensagens WHERE tipo = ? ORDER BY RANDOM() LIMIT 1", (tipo,)) 
    resultado = cursor.fetchone() 
    conn.close() 
    return resultado[0] if resultado else "Tudo bem! Estou aqui com você." 

@app.route("/webhook", methods=["POST"]) 
def whatsapp_webhook(): 
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

if __name__ == "__main__": 
    app.run(host="0.0.0.0", port=5000)

