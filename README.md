# MenteAmigaChatB
# Chatbot de Apoio à Saúde Mental via WhatsApp

Este projeto é um chatbot que envia mensagens humanizadas para auxiliar usuários emocionalmente, via WhatsApp.

## Funcionalidades
- Mensagens de acolhimento e apoio
- Dicas de respiração e alívio emocional
- Piadinhas e sugestões para melhorar o humor
- Alerta de emergência com contato do CVV

## Tecnologias
- Python + Flask
- SQLite
- Twilio (para envio de mensagens via WhatsApp)

## Como rodar localmente
1. Instale as dependências: pip install -r requirements.txt
2. Crie o banco de dados: sqlite3 mensagens.db < db_setup.sql
3. Configure seu .env com os dados da sua conta Twilio.
4. Execute: python app.py
5. Use Ngrok para expor: ngrok http 5000
6. Cole o link no Twilio Sandbox com o final /webhook.

## Observação
Este chatbot é um recurso de apoio e não substitui profissionais da saúde mental.
