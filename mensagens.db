import sqlite3

# Nome do arquivo do banco
DB_PATH = 'mensagens.db'

# Conexão com o banco
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Criar a tabela
cursor.execute('''
CREATE TABLE IF NOT EXISTS mensagens (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo TEXT NOT NULL,
    conteudo TEXT NOT NULL
)
''')

# Dados de exemplo (você pode adicionar mais)
mensagens = [
    ('apoio', 'Sinto muito que esteja passando por isso. Estou aqui com você. 💙'),
    ('apoio', 'Você não está sozinha(o), tá bom? Pode conversar comigo.'),
    ('respiracao', 'Vamos respirar juntos: inspire por 4 segundos, segure por 4, expire por 4. Repita.'),
    ('respiracao', 'Feche os olhos por um momento e respire fundo. Você está seguro(a).'),
    ('humor', 'Qual o cúmulo do absurdo? Jogar xadrez com o espelho e perder! 😄'),
    ('humor', 'Sabe por que o lápis foi demitido? Porque ele estava sem ponta! ✏️😂'),
    ('emergencia', 'Se estiver em perigo ou precisar de ajuda urgente, por favor procure alguém de confiança ou disque 188 (CVV).'),
    ('abertura', 'Olá! Como posso te ajudar hoje? Estou aqui para você. 💬'),
]

# Inserir as mensagens
cursor.executemany("INSERT INTO mensagens (tipo, conteudo) VALUES (?, ?)", mensagens)

# Salvar e fechar
conn.commit()
conn.close()
