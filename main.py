import random
import cat_api
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
BOT_OWNER_ID = os.getenv('BOT_OWNER_ID')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    for guild in client.guilds:
        print(f'{client.user} has connected to the guild: {guild.name} (id: "{guild.id}")')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content == 'cat!':
        response = cat_api.get_url()
        print(f'User "{message.author}" used command "cat!" in channel "{message.channel}" (Guild: "{message.guild.id}" => "{message.guild}")')
        await message.channel.send(response)
    

client.run(TOKEN)