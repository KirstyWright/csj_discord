import discord
from discord.ext import commands
import random
import config

description = '''Bot for Kugu discord, all questions should be directed to "Kirsty (Princess Vamps)"'''
bot = commands.Bot(command_prefix='!', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def list():
    """Lists the channels you can join"""
    await bot.say('You may join any of the listed groups by typing ``!join channelName``\nnsfw food tunes politcs')

@bot.command()
async def join(group : str):
    """Join a discord group (channel)"""
    await bot.say('You tried to join: '+group)

bot.run(config.token)
