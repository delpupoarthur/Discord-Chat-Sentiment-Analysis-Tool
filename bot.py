import os
import discord
import logging
import pandas as pd
from decouple import config
from datetime import datetime, timedelta
from gemini_analysis import analyze_sentiment

# Configuração do logging
logging.basicConfig(level=logging.INFO)

# Configuração do bot
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# Função para verificar se uma mensagem é um comando
def is_command(message):
    return len(message.content) > 0 and message.content.split()[0] == '_scan'

# Evento on_ready
@client.event
async def on_ready():
    print(f'Logado como: {client.user}')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='_help para mais informações'))

# Evento on_message
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    elif message.content.startswith('_'):
        cmd = message.content.split()[0].replace("_", "")
        parameters = message.content.split()[1:] if len(message.content.split()) > 1 else []

        if cmd == 'scan':
            try:
                if len(message.channel_mentions) > 0:
                    channel = message.channel_mentions[0]
                else:
                    channel = message.channel

                days_ago = int(parameters[1])

                end_date = datetime.now()
                start_date = end_date - timedelta(days=days_ago)

                logging.info(f"Coletando mensagens do canal {channel.name} entre {start_date} e {end_date}")

                data = pd.DataFrame(columns=['content', 'time', 'author'])
                async for msg in channel.history(after=start_date, before=end_date):
                    logging.info(f"Coletando mensagem: {msg.content}")
                    if msg.author != client.user and not is_command(msg):
                        new_data = pd.DataFrame({'content': [msg.content],
                                                 'time': [msg.created_at],
                                                 'author': [msg.author.name]})
                        data = pd.concat([data, new_data], ignore_index=True)

                file_location = f"{str(channel.guild.id)}_{str(channel.id)}.csv"
                data.to_csv(file_location, index=False, encoding='utf-8')

                answer = discord.Embed(title="Aqui está o seu arquivo .CSV",
                                      description=f"""\n\n`Server` : **{message.guild.name}**\n`Channel` : **{channel.name}**\n`Messages Read` : **{len(data)}**""",
                                      colour=0x1a7794)

                await message.author.send(embed=answer)
                await message.author.send(file=discord.File(file_location, filename='data.csv'))
                os.remove(file_location)

            except (discord.errors.Forbidden, ValueError, Exception) as e:
                logging.error(f"Erro no comando scan: {e}")
                await message.channel.send("Erro: Verifique os parâmetros e permissões do bot.")

        elif cmd == 'analyse':
            try:
                if len(message.channel_mentions) > 0:
                    channel = message.channel_mentions[0]
                else:
                    channel = message.channel

                days_ago = int(parameters[1])

                end_date = datetime.now()
                start_date = end_date - timedelta(days=days_ago)

                logging.info(f"Coletando mensagens do canal {channel.name} entre {start_date} e {end_date}")

                messages = []
                async for msg in channel.history(after=start_date, before=end_date):
                    if msg.author != client.user and not is_command(msg):
                        messages.append(msg.content)

                text = " ".join(messages)  # Concatenar as mensagens em um único texto

                # Análise de sentimento
                analysis_result = analyze_sentiment(text)

                # Enviar mensagem no chat informando a quantidade de mensagens coletadas e que o resultado será enviado por DM
                await message.channel.send(f"{message.author.mention}, foram coletadas {len(messages)} mensagens. O resultado da análise será enviado em breve por mensagem privada.")

                # Enviar resultado para o usuário por DM
                await message.author.send(f"Análise de Sentimento:\n{analysis_result}")

            except (discord.errors.Forbidden, ValueError, Exception) as e:
                logging.error(f"Erro no comando analyze: {e}")
                await message.channel.send("Erro: Verifique os parâmetros e permissões do bot.")


        elif cmd == 'help':
            answer = discord.Embed(title="Formatação do Comando",
                                   description="""
                                   `_scan <canal> days <numero_de_dias>`\n
                                   `_analyze <canal> days <numero_de_dias>`\n\n
                                    `<canal>`: **o canal que você deseja escanear**\n
                                    `<numero_de_dias>`: **o número de dias anteriores à data atual que você deseja escanear**\n\n
                                    *A ordem dos parâmetros não importa.*
                                    """,
                                   colour=0x1a7794)
            await message.channel.send(embed=answer)
# Iniciar o bot
client.run(config('DISCORD_TOKEN'))
