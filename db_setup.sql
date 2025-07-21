CREATE TABLE mensagens (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo TEXT NOT NULL,
    conteudo TEXT NOT NULL
);

-- Abertura
INSERT INTO mensagens (tipo, conteudo) VALUES 
('abertura', 'Oi! Como posso te ajudar hoje?'),
('abertura', 'Olá, tudo bem? Está precisando conversar?');

-- Apoio
INSERT INTO mensagens (tipo, conteudo) VALUES 
('apoio', 'Sinto muito que esteja se sentindo assim. Estou aqui com você.'),
('apoio', 'Você não está sozinho. Quer conversar um pouco?');

-- Respiração
INSERT INTO mensagens (tipo, conteudo) VALUES 
('respiracao', 'Vamos tentar uma respiração profunda? Inspire por 4 segundos, segure por 7 e expire por 8.'),
('respiracao', 'Feche os olhos, respire fundo... estamos juntos.');

-- Humor
INSERT INTO mensagens (tipo, conteudo) VALUES 
('humor', '😄 Sabia que rir libera endorfina? Que tal ver algo leve e engraçado hoje?'),
('humor', '😊 Uma piadinha: Por que o tomate foi ao banco? Porque queria extrato!');

-- Emergência
INSERT INTO mensagens (tipo, conteudo) VALUES 
('emergencia', 'Se estiver em risco, ligue 188 (CVV) ou procure ajuda médica imediatamente. Você é importante.'),
('emergencia', 'Você é valioso. Em situações de emergência, procure um profissional ou ligue 188 (CVV).');
