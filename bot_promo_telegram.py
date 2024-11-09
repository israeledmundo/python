'''
TENTANDO ENVIAR MENSAGEM PRA GRUPO'''
from telethon import TelegramClient, events

# Substitua com seus próprios valores
API_ID = 20566335
API_HASH = '0576e5e891d4aa47d7db8558cb1e34d7'
TELEGRAM_ID = -4574050097  # Seu próprio ID do Telegram
CHANNEL_USERNAME = ['@gatunopromos', '@promo_imperdivel','@pobregram','@garimposdodepinho','@ttcupons']  # Username do canal que você quer monitorar

# Lista de palavras-chave a serem monitoradas
PALAVRAS_CHAVE = ["S23", "Ultra", "aspirador"]

# Armazenando os IDs das mensagens já processadas
mensagens_processadas = set()

# Inicializa o cliente do Telethon
client = TelegramClient('sessao', API_ID, API_HASH)

# Evento que escuta mensagens no canal


@client.on(events.NewMessage(chats=CHANNEL_USERNAME))
async def handler(event):
    mensagem = event.message.message
    # Verifique se a mensagem já foi processada
    if event.message.id not in mensagens_processadas:
        if any(palavra in mensagem for palavra in PALAVRAS_CHAVE):
            # Envia a mensagem para o seu Telegram
            await client.send_message(TELEGRAM_ID, mensagem)
            # Marca a mensagem como processada para evitar duplicação
            mensagens_processadas.add(event.message.id)
print("Monitoramento de canal iniciado.....")
# Inicia o cliente
client.start()
client.run_until_disconnected()
