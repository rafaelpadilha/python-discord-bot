from discord.ext import commands
from version import __version__
from random import choice
from pickle import load, dump
import os

#https://www.freecodecamp.org/news/how-to-set-up-continuous-deployment-in-your-home-project-the-easy-way-41b84a467eed/
#https://medium.com/better-programming/github-actions-for-docker-eaf22bbcc879

config = {}

#TODO Get token from OS
TOKEN = "Nzg2MDU5NDk3Mzk5MjU1MTAw.X9A49A.BiC0llrXzzmFIePdc0BFHUIeltk"

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print("Ready!")
        

@bot.command(pass_context=True)
async def info(context):
    await context.message.channel.send(f"Versão atual: {__version__}")

bot.run(TOKEN)

