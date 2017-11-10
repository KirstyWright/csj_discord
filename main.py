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
    bot.activeServer = bot.get_server(config.serverID)

@bot.command()
async def list():
    """Lists the channels you can join"""
    roles = ""
    for role in bot.activeServer.roles:
        if (role.name.startswith("auto_")):
            roles = "{}*{}\n".format(roles,role.name[5:])
    await bot.say('You may join any of the listed groups by typing ``!join channelName``\n{}'.format(roles))

@bot.command(pass_context=True)
async def join(ctx,*groups):
    """Join a discord group (channel). If you want to join multiple groups, then separate the names via a space."""
    acceptedRoles = []
    user = ctx.message.author
    for attemptedGroup in groups:
        attemptedGroup = attemptedGroup.lower()
        for role in bot.activeServer.roles:
            if role.name == "auto_{}".format(attemptedGroup):
                try:
                    await bot.add_roles(user,role)
                    acceptedRoles.append(role.name[5:])
                except Exception as e:
                    print(e)
                    continue
    if not acceptedRoles:
        await bot.say('Could not find any channels with those names')
    else:
        await bot.say('You joined {}'.format(', '.join(acceptedRoles)))

@bot.command(pass_context=True)
async def leave(ctx,*groups):
    """Leave a discord group (channel). If you want to leave multiple groups, then separate the names via a space."""
    acceptedRoles = []
    user = ctx.message.author
    for attemptedGroup in groups:
        attemptedGroup = attemptedGroup.lower()
        for role in bot.activeServer.roles:
            if role.name == "auto_{}".format(attemptedGroup):
                try:
                    await bot.remove_roles(user,role)
                    acceptedRoles.append(role.name[5:])
                except Exception as e:
                    print(e)
                    continue

    if not acceptedRoles:
        await bot.say('Could not find any channels with those names')
    else:
        await bot.say('You left {}'.format(', '.join(acceptedRoles)))

@bot.command(pass_context=True)
async def groups(ctx):
    """Lists the discord groups (channels) you are in."""
    acceptedRoles = []
    user = ctx.message.author
    for role in user.roles:
        if (role.name.startswith("auto_")):
            acceptedRoles.append(role.name[5:])
    await bot.reply('You are in {}'.format(', '.join(acceptedRoles)))
bot.run(config.token)
