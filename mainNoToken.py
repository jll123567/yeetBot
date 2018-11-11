# YEET
from random import randint
import re
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
            "yeetsoda ~ \"mmm tasty\"",
            "yeetocheetos",
            "yuckyYEET",
            "asparayeet",
            "yeetos and sauce",
            "yeetelayheehoo",
            "yeetache",
            "yeetusyokus",
            "croncheet",
            "somebodytouchamyyeetet",
            "someyeetyonceyeeted",
            "youwouldnotbelieveyouryeet",
            "yeetsamongus",
            "yeetchus",
            "yeeter",
            "yeetjuice",
            "//yeets in spanish",
            "skyeet",
            "the yeetoneers used to ride these babies for miles",
            "yeetles",
            "yeetyyeetmus",
            "mr yetama",
            "then yeetish",
            "yooooooote",
            "im yeeting",
            "//yeets in japanese",
            "yoklesetocsah",
            "glory to yeetsotshka(edited)",
            "yeetamir putin",
            "where's the Yeet sauce!",
            "eetle my yeetle",
            "https://i.redditmedia.com/JPIWA8xCyCzBEW3vtgSOzQTzlUaOb1nfs6mYCKqu4jw.jpg?fit=crop&crop=faces%2Centropy"
            "&arh=2&w=960&s=3f9cab5e3921ad88fa0ef77b81aa9cc6",
            "Yeet or be yeeted",
            "https://preview.redd.it/4cg7wkvajir11.png?width=640&crop=smart&s=dfffd5e5f55a7980c7d66e73bba794b21cc930bf",
            "I have looked god in the eye and said “yeet”",
            "Press X to Yeet",
            "Yeetus the fetus",
            "Whats a yeet",
            "\*expand YEET\*",
            "you are what you yeet",
            "https://cdn.discordapp.com/attachments/509753928058011683/509754488769216512/unknown.png",
            "https://pics.me.me/parayeet-27518099.png",
            "read a book? more like yEET a book amirite fellas?",
            "https://cdn.discordapp.com/attachments/509753928058011683/509754529588183040/image0.png",
            "Type yeet to yeet",
            "Yeethaw",
            "https://cdn.discordapp.com/attachments/509753928058011683/509754559221071892/image0.png",
            "https://cdn.discordapp.com/attachments/509753928058011683/509754586429653003/image0.png",
            "https://cdn.discordapp.com/attachments/509753928058011683/509929714966724629/image0.png",
            "https://cdn.discordapp.com/attachments/509753928058011683/509929788291547153/image0.png",
            "https://cdn.discordapp.com/attachments/509753928058011683/510589660301492225/image0.png",
            ]


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_guild_join(guild):
    general = discord.utils.find(lambda x: x.name == 'general', guild.text_channels)
    if general and general.permissions_for(guild.me).send_messages:
        await general.send("YEET!\n please join our support server: https://discord.gg/PJwQxHR\ny!help for the "
                           "commands list")


@client.event
async def on_message(message):
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

    elif re.search(r"(.)*yeet(.)*", message.content, re.IGNORECASE):
        if message.author == client.user:
            pass
        else:
            await message.channel.send(yeetList[randint(0, yeetList.__len__() - 1)])

    elif re.search(r"(.)*nigger(.)*", message.content, re.IGNORECASE):
        await message.channel.send("Don't please!")


client.run('token')
# https://discordapp.com/oauth2/authorize?client_id=494971719686291456&scope=bot&permissions=2048
# support server: https://discord.gg/PJwQxHR
# icon image credit: https://www.deviantart.com/mintivy/art/YEET-SMii7Y-Fanart-712996482
