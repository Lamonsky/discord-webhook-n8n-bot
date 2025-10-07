import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import aiohttp

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True  # Enable the message content intent
bot = commands.Bot(command_prefix='!', intents=intents)
TOKEN = os.getenv('DISCORD_BOT_TOKEN')

@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.author.global_name is None:
        return

    if message.channel.id != 1425143044461695208:
        return

    webhook_url = os.getenv('WEBHOOK_URL')
    
    if webhook_url:
        async with aiohttp.ClientSession() as session:
            payload = {"message": message.content, "session_id": str(message.author.id), "username": str(message.author.global_name)}
            await session.post(webhook_url, json=payload)
        #print(f"Forwarded message: {message.content}")
    
    await bot.process_commands(message)


bot.run(TOKEN)