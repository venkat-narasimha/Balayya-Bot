import random
from urls import *
import discord
from discord.ext import commands

client = commands.Bot(command_prefix='balayya ', help_command=None,intents=discord.Intents.all())

#balayya profile
@client.command()
async def profile(ctx):
    embed_prf= discord.Embed(description= '**Name**: Nandamuri Balakrishna \n' '**Age**: 60+ years \n' '**Occupation**: All Rounder \n' '**Brand**: Mansion House' , color=random.randint(0, 0xffffff))
    embed_prf.set_author(name='Balayya Profile' , icon_url=dp2)
    embed_prf.set_thumbnail(url= mansion_house)
    await ctx.send(embed=embed_prf)

#help command
@client.command(pass_context=True,aliases=['commands'])
async def help(ctx):
    message = discord.Embed(title="Jai Balayya",description="__A telugu film god, Here are some commands you can use__" , color=random.randint(0, 0xffffff) )
    message.add_field(name="balayya profile", value="Sends information about balayya")
    message.add_field(name="balayya emote", value="alias: balayya action\nSends a random balayya emote")
    message.add_field(name="balayya fun", value="alias: balayya fd\nSends a random funny image of balayya")
    message.add_field(name="balayya movie", value="alias: balayya md\nSends a random movie dialogues")
    message.add_field(name="balayya slogan", value="alias: balayya s, balayya jai\nSends balayya slogans")
    message.add_field(name="balayya namaste", value="alias: balayya namaskaram, balayya vanakam\nBalayya will say namskaram to you")
    message.add_field(name="balayya greet @user", value="Balayya will greet the mentioned user")
    message.add_field(name="balayya invite", value="Balayya will send a invite link to your DM")
    message.add_field(name="Some random actions", value="You can use as follows some actions with prefix\nactions: fight,bye,hi,eat,...")
    message.set_thumbnail(url= dp2)
    await ctx.send(embed=message)

#for random balayya gifs from actions
@client.command(aliases=['action'])
async def emote(ctx):
    random_action = random.choice(random.choice(actions_list))
    await ctx.send(random_action)

#for random fun dailouge pics
@client.command(aliases=['fd'])
async def fun(ctx):
    embed_fun = discord.Embed(description = '__**Jai Balayya**__', color = random.randint(0, 0xffffff))
    random_link = random.choice(dailouge_pics)
    embed_fun.set_image(url= random_link)
    await ctx.send(embed = embed_fun)

#for random movie dailouge pics
@client.command(aliases=['md'])
async def movie(ctx):
    embed_movied = discord.Embed(color = random.randint(0, 0xffffff))
    random_movie_dialogue = random.choice(movie_dialouge)
    embed_movied.set_image(url= random_movie_dialogue)
    await ctx.send(f'{ctx.author.mention}' , embed = embed_movied)

#for random balayya slogans
@client.command(aliases=['s','jai'])
async def slogan(ctx):
    random_slogan = random.choice(slogans)
    embed_slogan = discord.Embed(description = random_slogan, color = random.randint(0, 0xffffff))
    await ctx.send(embed=embed_slogan)

#for random namastes
@client.command(aliases=['namaskaram', 'vanakam'])
async def namaste(ctx):
    embed_namaskaram = discord.Embed(description = f'**Namaskaram :pray:**', color = random.randint(0, 0xffffff))
    random_greet = random.choice(greeting_gifs)
    embed_namaskaram.set_image(url= random_greet)
    await ctx.send(f'{ctx.author.mention}' , embed = embed_namaskaram)

#will greet someone when we mention someone
@client.command()
async def greet(ctx, arg):
    value = random.randint(0, 0xffffff)
    embed_greet = discord.Embed(color = value)
    random_greet = random.choice(greeting_gifs)
    embed_greet.set_image(url= random_greet)
    await ctx.send( '**Namaskaram :pray: ** ' +str(arg) , embed = embed_greet)

#for bot invite link
@client.command()
async def invite(ctx):
    embed_invite = discord.Embed(title='__Balayya Babu Invite link__', description = invite_link, color=random.randint(0, 0xffffff))
    await ctx.send('📥 __Check your DM__')
    await ctx.author.send(embed =embed_invite)
