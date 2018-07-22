import discord
from discord.ext import commands
import config

description = '''Bot for CSJ discord discord, all questions should be directed to "Kirs"'''
bot = commands.Bot(command_prefix='!', description=description)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    bot.activeServer = bot.get_server(config.serverId)


@bot.command()
async def list():
    """Lists the roles you can have"""
    roles = ""
    for role in bot.activeServer.roles:
        if (role.name in config.roles):
            roles = "{}*{}\n".format(roles, role.name)
    await bot.say('You may set your type by typing ``!type roleName``:\n{}'.format(roles))

@bot.event
async def on_member_join(member):
    channel = member.server.get_channel('441994801102061581')
    fmt = 'Welcome to the Server {0.mention}, please read the rules and enjoy your stay. You may set your type by typing `!type <typeName>`.'
    await bot.send_message(channel, fmt.format(member))

@bot.command(pass_context=True)
async def type(ctx, group):
    """Assign yourself a specified type."""
    acceptedRole = None
    user = ctx.message.author
    attemptedGroup = group.upper()
    for role in bot.activeServer.roles:
        if role.name == format(attemptedGroup) and attemptedGroup in config.roles:
            try:
                await bot.add_roles(user, role)
                acceptedRole = role.name
            except Exception as e:
                print(e)
                continue
    if not acceptedRole:
        await bot.say('Could not find any role with that name')
    else:
        removeRoles = []
        for role in user.roles:
            if role.name != attemptedGroup and role.name in config.roles:
                removeRoles.append(role)
        if (len(removeRoles) > 0):
            try:
                print('removing role');
                print(removeRoles);
                await bot.remove_roles(user, *removeRoles)
            except Exception as e:
                print(e)
                return
        await bot.say('You joined {}'.format(acceptedRole))

bot.run(config.token)
