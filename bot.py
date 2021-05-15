# bot.py
import os
import asyncio
import random
from playsound import playsound
from discord.ext import commands
from dotenv import load_dotenv
import youtube_dl
import discord
from discord.ext import commands,tasks
from datetime import datetime

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')



#prefix for all commands
bot = commands.Bot(command_prefix='!')

#testing for TEXT channels
@bot.command(name='flip', help='Flips a coin')
async def nine_nine(ctx):
    chance = ['**HEADS**','**TAILS**']
    response = random.choice(chance)
    await ctx.send(response)
    
@bot.command(name='roll_dice', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))
    
    
@bot.command(name='bee', help='Displays a certain script line-by-line')
async def beeMovie(ctx):
    file1 = open("beeScript.txt", "r")
    Lines = file1.readlines()
    for line in Lines:
        await asyncio.sleep(2)
        await ctx.send(line)
        
@bot.command(name='members', help='Displays a list of all members')
async def members(ctx):
     for member in ctx.guild.members:
          await ctx.send(member.name)
             
@bot.command(name='time', help='Gets time down to the millisecond')
async def clock(ctx):
    time = datetime.now()
    await ctx.send(time)

#testing for VOICE channels
@bot.command(name='join', help='Tells the bot to join the voice channel')
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
    
@bot.command(name='leave', help='To make the bot leave the voice channel')
async def leave(ctx):
    await ctx.voice_client.disconnect()      

#WORK ON THIS!!!
@bot.command(name='play', help='Plays music from youtube')
async def play_music(ctx, url):
    
    voice_client = ctx.voice_client
    player = await voice_client.create_ytdl_player(url)
    #players[server.id] = player
    player.start()
             

bot.run(TOKEN)