#Balayya Babu Test Bot

from balayya_commands import *
from actions import *
from error_handlings import on_command_error
import os
from dotenv import load_dotenv
load_dotenv()

# get the bot token from the .env file
BotToken = os.getenv('BOT_TOKEN')
if BotToken is None:
    raise ValueError("BOT_TOKEN environment variable not set. Please set it in your environment or .env file.")

client = commands.Bot(command_prefix='balayya ', help_command=None,intents=discord.Intents.all())

@client.event
async def on_ready():
    print('Dhabidi Dhibide')
    await client.change_presence(activity=discord.Activity(type = discord.ActivityType.listening, name = 'balayya help'))

#commands from the command.py file
client.add_command(profile)
client.add_command(help)
client.add_command(emote)
client.add_command(fun)
client.add_command(movie)
client.add_command(slogan)
client.add_command(namaste)
client.add_command(greet)
client.add_command(invite)
#action commands
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

#errors
client.event(on_command_error)

client.run(BotToken)