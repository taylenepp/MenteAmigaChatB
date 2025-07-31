import sqlite3

# Caminho do banco de dados
DB_PATH = 'mensagens.db'

# Conecta e cria a tabela
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Criação da tabela
cursor.execute('''
CREATE TABLE IF NOT EXISTS mensagens (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo TEXT NOT NULL,
    conteudo TEXT NOT NULL
)
''')

# Inserção de mensagens por tipo
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

# Inserção no banco
cursor.executemany('INSERT INTO mensagens (tipo, conteudo) VALUES (?, ?)', mensagens)

# Salva e fecha conexão
conn.commit()
conn.close()

print("Banco de dados criado e populado com sucesso!")
