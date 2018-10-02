# YEET
from random import randint

import discord

client = discord.Client()

yeetList = ["ʏɛɛȶ",
            "yee\nwait...\nyeet*",
            "yeetn't",
            "its ya boi, **YEET**",
            "https://images.prod.meredith.com/product/f6a4f6da9db798cd5a762b861149b4a6/1514196065413/l/womens-funny"
            "-eat-sleep-yeet-repeat-popular-dance-tshirt-urban-slang-large-royal-blue",
            "https://pre00.deviantart.net/338a/th/pre/f/2017/306/0/9/new_canvastdvybujk_by_mintivy-dbshzlu.png",
            "yeet|teey",
            "ɎɆɆ₮",
            "🍸🎗🎗🌴",
            "*ｙ  ｅ  ｅ  ｔ*",
            "y♥e♥e♥t♥",
            "( °□°）╯︵︵︵︵︵︵︵O**YEET**",
            "`•.¸¸.•´´¯`••._.• yeet •._.••`¯´´•.¸¸.•`",
            "yote"
            ]


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    if message.content.startswith('y!test'):
        await message.channel.send('hello')

    if message.content.startswith("y!certainImg"):
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
            await  message.channel.send(certainYeet)
            # print(certainYeet+"\n", message.content[-1 * (message.content.__len__() - 13):])

    if message.content.startswith('y!help'):
        await message.channel.send("```y!yeet | yeet\n"
                                           "m!help | this```")

    if message.content.startswith('y!yeet'):
        await message.channel.send(yeetList[randint(0, yeetList.__len__() - 1)])


client.run('token')
# https://discordapp.com/oauth2/authorize?client_id=494971719686291456&scope=bot&permissions=2048
# icon image credit: https://www.deviantart.com/mintivy/art/YEET-SMii7Y-Fanart-712996482
