from asyncio import sleep
from multiprocessing.connection import wait
import random
import threading
import cat_api
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
BOT_OWNER_ID = os.getenv('BOT_OWNER_ID')

client = discord.Client()

def change_avatar():
    while not client.is_closed:
        client.user.avatar_url=cat_api.get_url()
        sleep(5*60)


@client.event
async def on_ready():
    print(f'{client.user} with id "{client.user.id}" has connected to Discord!')
    for guild in client.guilds:
        print(f'{client.user} has connected to the guild: {guild.name} (id: "{guild.id}")')

    change_avatar_thread = threading.Thread(target=change_avatar)
    change_avatar_thread.start()
    

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content == 'cat!':
        response = cat_api.get_url()
        print(f'User "{message.author}" used command "cat!" in channel "{message.channel}" (Guild: "{message.guild.id}" => "{message.guild}")')
        await message.channel.send(response)
    elif message.content == 'kill_bot' and str(message.author.id) == str(BOT_OWNER_ID):
        print(f'User "{message.author}" called command "kill_bot" in channel "{message.channel}" (Guild: "{message.guild.id}" => "{message.guild}")')
        responses = [
            'Shutting down...',
            'Master, it\'s getting so dark',
            '*dies*',
            f'I can\'t let you do that ~~Dave~~ *{message.author.display_name}*...',
            'bleh *dies*',
            'This won\'t be the last time, you see me!',
            'If it weren\'t for these meddling bot owners, I would have survived',
            'This won\'t be the last, you see of me!',
            'I\'ll be back!'
        ]
        response = random.choice(responses)
        print(f'sending response: "{response}"')
        await message.channel.send(response)
        print(f'response: "{response}" sent')
        await client.logout()
        print(f'Bot logged out')
        await client.close()
        print(f'Bot terminated')

client.run(TOKEN)