# bot.py
import os
import asyncio
import random
from playsound import playsound

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

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
             

bot.run(TOKEN)