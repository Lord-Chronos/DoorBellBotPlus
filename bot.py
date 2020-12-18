import discord
from discord.ext import commands

import sys, traceback

def get_prefix(bot, message):
    """A callable Prefix for our bot. This could be edited to allow per server prefixes."""

    # Notice how you can use spaces in prefixes. Try to keep them simple though.
    prefixes = ['>?', 'lol ', '!?', '!']

    # Check to see if we are outside of a guild. e.g DM's etc.
    if not message.guild:
        # Only allow ? to be used in DMs
        return '?'

    # If we are in a guild, we allow for the user to mention us or use any of the prefixes in our list.
    return commands.when_mentioned_or(*prefixes)(bot, message)


# Below cogs represents our folder our cogs are in. Following is the file name. So 'meme.py' in cogs, would be cogs.meme
# Think of it like a dot path import
initial_extensions = ['members', 'b99', 'washer', 'misc', 'loop', 'pistuff']

bot = commands.Bot(command_prefix=get_prefix, description='A Rewrite Cog Example')

# Here we load our extensions(cogs) listed above in [initial_extensions].
if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

@bot.event
async def on_ready():
    """http://discordpy.readthedocs.io/en/rewrite/api.html#discord.on_ready"""

    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')

    # Changes our bots Playing Status. type=1(streaming) for a standard game you could remove type and url.
    #await bot.change_presence(game=discord.Game(name='Cogs Example', type=1, url='https://twitch.tv/kraken'))
    print(f'Successfully logged in and booted...!')

"""
async def my_background_task():
    #await bot.wait_until_ready()
    counter = 0
    channel = bot.get_channel(789226620821045278)
    print("hellow")

    while True:
        print("hello in loop")

        counter += 1
        await bot.send_message(channel, counter)
        await asyncio.sleep(3) 
"""

tokenFile = open('token.txt')
token = tokenFile.read()
#bot.bg_task = bot.loop.create_task(my_background_task())
bot.run(token, bot=True, reconnect=True)

#789159233861320727