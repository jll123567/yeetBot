# YEET
import discord
import asyncio
from random import randint

client = discord.Client()

yeetList = ["ʏɛɛȶ",
            "yee\nwait...\nyeet*",
            "yeetn't",
            "its ya boi, **YEET**",
            "https://images.prod.meredith.com/product/f6a4f6da9db798cd5a762b861149b4a6/1514196065413/l/womens-funny-eat-sleep-yeet-repeat-popular-dance-tshirt-urban-slang-large-royal-blue"
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
        await client.send_message(message.channel, 'hello')

    if message.content.startswith('y!help'):
        await client.send_message(message.channel, "```y!yeet | yeet\n"
                                                   "m!help | this```")

    if message.content.startswith('y!yeet'):
        await client.send_message(message.channel, yeetList[randint(0, yeetList.__len__())])

client.run('token')
# https://discordapp.com/oauth2/authorize?client_id=494971719686291456&scope=bot&permissions=2048
# icon image credit: https://www.deviantart.com/mintivy/art/YEET-SMii7Y-Fanart-712996482
