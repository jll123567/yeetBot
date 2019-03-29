# coding=utf-8
"""Yeetbot is a discord bot using the discord.py that automaticly responds to discord messages with yeet by  sending
some text or an image """
from random import randint
import re
import discord

# sets the client
client = discord.Client()

# listing of all the "yeets that the bot uses"
yeetList = ["zzz"]


@client.event
async def on_ready():
    """on login print information about the bot."""
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_guild_join(guild):
    """on joining a discord server(guild) find the #general channel and send a welcome message."""
    general = discord.utils.find(lambda x: x.name == 'general', guild.text_channels)
    if general and general.permissions_for(guild.me).send_messages:
        await general.send("YEET!\n please join our support server: https://discord.gg/PJwQxHR\ny!help for the "
                           "commands list")


@client.event
async def on_message(message):
    """depending on the message, send a response to the channel the message was received from.
    y!test: Say hello.
    y!certainImg <int>: Pick a certain yeet from the list specified with the preceding <int>.
    y!help: Show help information.
    y!yeet: Pick a yeet from the list at random and send it.
    yeet anywhere in the message: Preform the same action as y!yeet.
    A racial slur anywhere in the message: Send a message requesting users to not use that language.
    """

    if message.content.startswith('y!test'):
        await message.channel.send('hello')

    elif message.content.startswith("y!certainImg"):
        certainYeet = "unknown error"
        try:
            yeetDex = int(message.content[-1 * (message.content.__len__() - 13):])
            certainYeet = yeetList[yeetDex]
        except ValueError:
            certainYeet = "`y!certainImg <int>`"
        except IndexError:
            certainYeet = ("`yeet list max: " + str(yeetList.__len__() - 1) + '`')
        except:
            print("unknown error")
        finally:
            await message.channel.send(certainYeet)
            # print(certainYeet+"\n", message.content[-1 * (message.content.__len__() - 13):])

    elif message.content.startswith('y!help'):
        await message.channel.send("```y!yeet | yeet\n"
                                   "m!help | this```\nsupport server: https://discord.gg/PJwQxHR")

    elif message.content.startswith('y!yeet'):
        await message.channel.send(yeetList[randint(0, yeetList.__len__() - 1)])

    elif re.search(r"(.)*ye(e)+t(.)*", message.content, re.IGNORECASE):
        if message.author == client.user:
            pass
        else:
            await message.channel.send(yeetList[randint(0, yeetList.__len__() - 1)])

    elif re.search(r"(.)*nigger(.)*", message.content, re.IGNORECASE):
        await message.channel.send("Don't please!")

# start the bot using the token(placeholder used here)
client.run('token')
# https://discordapp.com/oauth2/authorize?client_id=494971719686291456&scope=bot&permissions=2048
# support server: https://discord.gg/PJwQxHR
# icon image credit: https://www.deviantart.com/mintivy/art/YEET-SMii7Y-Fanart-712996482
# little documentation at: https://yeetbot.readthedocs.io/en/latest/
