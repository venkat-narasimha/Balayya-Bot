# Balayya Babu Test Bot

import os
import asyncio
from dotenv import load_dotenv
from aiohttp import web
import discord
from discord.ext import commands

# Custom imports
from balayya_commands import *
from actions import *
from error_handlings import on_command_error

# Load .env variables
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise ValueError("BOT_TOKEN is not set in .env")

# Create bot
client = commands.Bot(command_prefix='balayya ', help_command=None, intents=discord.Intents.all())

# On ready
@client.event
async def on_ready():
    print('Dhabidi Dhibide')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='balayya help'))

# Aiohttp keep-alive server
async def handle(request):
    return web.Response(text="Balayya Bot is alive!")

async def start_webserver():
    app = web.Application()
    app.router.add_get('/', handle)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', port=int(os.environ.get('PORT', 8080)))
    await site.start()

# Add commands
client.add_command(profile)
client.add_command(help)
client.add_command(emote)
client.add_command(fun)
client.add_command(movie)
client.add_command(slogan)
client.add_command(namaste)
client.add_command(greet)
client.add_command(invite)

client.add_command(bye)
client.add_command(come)
client.add_command(dance)
client.add_command(eat)
client.add_command(entry)
client.add_command(fight)
client.add_command(flirt)
client.add_command(night)
client.add_command(hi)
client.add_command(peace)
client.add_command(shock)

# Error handler
client.event(on_command_error)

# Main async entry
async def main():
    await start_webserver()
    await client.start(TOKEN)

# Run main
if __name__ == "__main__":
    asyncio.run(main())
