import discord
from discord.ext import commands
import requests
import os
import time

def current_milli_time():
    return round(time.time() * 1000)

update_time = 300000

#permessi per poter effettuare qualsiasi azione
client = commands.Bot(command_prefix=">", intents = discord.Intents.all())

@client.event
async def on_ready():

    time = current_milli_time()
    
    sum = 0

    channel = client.get_channel(int(os.environ['CHANNEL_ID']))
    guild = client.get_guild(int(os.environ['GUILD_ID']))

    while(True):
        if(current_milli_time() - time) >= update_time:
            #esclude i bot dalla conta dei membri
            members = await guild.fetch_members().flatten()
            for m in members:
                if not m.bot:
                    sum += 1
                    
            await channel.send('Il numero di utenti è ' + str(sum))
            time = current_milli_time()
            sum = 0
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return

#chiamta procedura d'avvio del bot
client.run(os.environ['DISCORD_BOT_KEY'])
