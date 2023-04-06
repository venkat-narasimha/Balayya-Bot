#actions_code

import random
import discord
from discord.ext import commands
from urls import bye_list,come_list,dance_list,eat_list,entry_list,fight_list,flirt_list,night_list,hi_list,peace_list,shock_list

client = commands.Bot(command_prefix='balayya ', help_command=None,intents=discord.Intents.all())

"""@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CommandNotFound):
        await ctx.send('Sorry, that is currently unavailable. Try another action!')"""

#bye
@client.command(aliases=['tata','chaio'])
async def bye(ctx):
    random_url = random.choice(bye_list)
    await ctx.send(random_url)

#come
@client.command(aliases=['raa','aavo'])
async def come(ctx):
    random_url = random.choice(come_list)
    await ctx.send(random_url)

#dance
@client.command(aliases=['natyam'])
async def dance(ctx):
    random_url = random.choice(dance_list)
    await ctx.send(random_url)

#eat
@client.command(aliases=['eating'])
async def eat(ctx):
    random_url = random.choice(eat_list)
    await ctx.send(random_url)

#entry
@client.command()
async def entry(ctx):
    random_url = random.choice(entry_list)
    await ctx.send(random_url)

#fight
@client.command(aliases=['warn','warning','kill'])
async def fight(ctx):
    random_url = random.choice(fight_list)
    await ctx.send(random_url)

#flirt
@client.command(aliases=['love','naughty'])
async def flirt(ctx):
    random_url = random.choice(flirt_list)
    await ctx.send(random_url)

#good_night
@client.command(aliases=['goodnight'])
async def night(ctx):
    random_url = random.choice(night_list)
    await ctx.send(random_url)

#hi
@client.command(aliases=['hello'])
async def hi(ctx):
    random_url = random.choice(hi_list)
    await ctx.send(random_url)

#peace
@client.command()
async def peace(ctx):
    random_url = random.choice(peace_list)
    await ctx.send(random_url)

#shock
@client.command(aliases=['fear'])
async def shock(ctx):
    random_url = random.choice(shock_list)
    await ctx.send(random_url)
