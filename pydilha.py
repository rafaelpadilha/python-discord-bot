from discord.ext import commands
from version import __version__
from random import choice
from pickle import load, dump
import os

config = {}

TOKEN = os.environ.get("BOT_TOKEN")

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print("Ready!")
        

@bot.command(pass_context=True)
async def info(context):
    await context.message.channel.send(f"Versão atual: {__version__}")

bot.run(TOKEN)

