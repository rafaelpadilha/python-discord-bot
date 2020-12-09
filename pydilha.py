from discord.ext import commands
from version import __version__
from random import choice
from pickle import load, dump
from urllib import request
import os

#TEMP
import json

CFG_PATH = 'cfg/'
SND_PATH = CFG_PATH + "sounds/"
TOKEN = os.environ.get("BOT_TOKEN")

bot = commands.Bot(command_prefix='$', help_command=None)
cfg = {}


def save_cfg(config):
    with open(CFG_PATH + 'settings.pickle', 'wb') as f:
        dump(config, f)


def load_cfg():
    config = {}
    if os.path.exists(CFG_PATH):
        if os.path.isfile(CFG_PATH + 'settings.pickle'):
            with open(CFG_PATH + 'settings.pickle', 'rb') as f:
                config = load(f)
            print("Config file loaded.")
        else:
            config = {}
            save_cfg(config)
    else:
        os.makedirs(CFG_PATH)
        os.makedirs(CFG_PATH + "/sounds/")
        os.makedirs("tmp/")
        config = {}
        save_cfg(config)
    return config

@bot.event
async def on_ready():
    global cfg
    print("Ready!")
    cfg = load_cfg()
    for guild in bot.guilds:
        if guild not in cfg:
            cfg[guild.id]={}
            cfg[guild.id]["annoucements"]=True
            cfg[guild.id]["sfx"]={}
            save_cfg(cfg)
    print(json.dumps(cfg, indent=4))

    

@bot.command(pass_context=True)
async def info(context):
    await context.message.channel.send(f"Versão atual: {__version__}\nCriador: Rafael Padilha")

@bot.command(pass_context=True)
async def help(context):
    help_text = """
    Oi eu sou o Goku ! 
    ```
info: Informações gerais sobre o bot.
    ```"""
    await context.message.channel.send(help_text)

@bot.command(pass_context=True)
async def sfx(context, option, arg1=None ,arg2=None):
    global cfg
    print(f"Option:{option}")

    if option == "add":
        if arg1 and arg2:
            request.urlretrieve(arg2, SND_PATH + arg1 + '.mp3')
        else:
            await context.message.channel.send(f"Fala direito cmg >.< \n ```sfx add nome link_mp3```")
    elif option == "list":
        msg = f"Efeitos sonoros para {context.guild.name}: \n```"
        if len(cfg[context.guild.id]["sfx"]) > 0:
            for sound in cfg[context.guild.id]["sfx"].keys():
                msg = msg + sound + '\n'
        else:
            msg += "Nenhum cadastrado :("
        msg += "```"
        await context.message.channel.send(msg)
    else:
        if option in cfg[context.guild.id]["sfx"]:
            if arg1:
                pass
                # TODO play cfg[context.guild.id]['sfx'][option] 
            else:
                await context.message.channel.send(f"Onde garai ? \n```sfx nome canal```")
        else:
            await context.message.channel.send(f"Num zei ! \n```sfx  add nome link\nsfx list \nsfx nome canal ```")

bot.run(TOKEN)
