# coding=utf-8
"""Yeetbot is a discord bot using the discord.py that automatically responds to discord messages with yeet by  sending
some text or an image """
from random import randint
import re
import discord

# sets the client
client = discord.Client()

# listing of all the "yeets that the bot uses"
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
            "||https://cdn.discordapp.com/attachments/509753928058011683/509754586429653003/image0.png||",
            "https://cdn.discordapp.com/attachments/509753928058011683/509929714966724629/image0.png",
            "https://cdn.discordapp.com/attachments/509753928058011683/509929788291547153/image0.png",
            "https://cdn.discordapp.com/attachments/509753928058011683/510589660301492225/image0.png",
            "https://cdn.discordapp.com/attachments/509753928058011683/518128872777187359/unknown.png",
            "https://cdn.discordapp.com/attachments/509753928058011683/518128955639988225/1542689653507.png",
            "https://cdn.discordapp.com/attachments/509753928058011683/518129056483508235/bgztv2ihrp021.png",
            "https://cdn.discordapp.com/attachments/509753928058011683/518129350743162910/image0.png\nMade by a user "
            "in out support server!",
            "Time givin is us a sweet view of this yeet",
            "Happy Yeetsgiving",
            "Merry Yeetmas",
            "y e e t  m e  i n t o  t h e  *s u n*",
            "Yeetboi",
            "Yeetus Deletus",
            "Bayblade bayblade let it yeet",
            "pokemon, gotta yeet them all",
            "How in the yeet yoink did this happen",
            "||Things to say during sex: Yeet||",
            "Yeeter Things",
            "13 Yeetsons Why",
            "did you yeet today or did today yeet you?",
            "Season’s Yeetings",
            'The correct conjugation is “yote.”',
            "https://cdn.discordapp.com/attachments/509753928058011683/528339167856295956/0m67sdgjko621.png",
            "https://cdn.discordapp.com/attachments/509753928058011683/528339258856177664/9pqirbkp92621.png",
            "https://cdn.discordapp.com/attachments/509753928058011683/528339326803771402/ojp9ifwf28521.png",
            "https://res.cloudinary.com/teepublic/image/private/s--l5asAvo_--/t_Preview/b_rgb:c62b29,c_limit,f_jpg,"
            "h_630,q_90,w_630/v1541358374/production/designs/3442375_0.jpg",
            "No one says “this bitch empty” and y e e t s like Gaston",
            "yeet it my fellow youths",
            "Hit or yeet. I guess they never yeet, huh.",
            "AAAA YYYYYYEEEEEEEEEEEEEEEEEEEEEEEEEEEEET",
            "Yeet Monk",
            "Let’s Yeet this wheat",
            "Let's yeet into deep space",
            "Go commit bridge yeet",
            "(Yeet noises)",
            "I’m going to Yeet you into a fire",
            "||Yeet Yeet beat my meat||",
            "https://i.pinimg.com/originals/a2/1d/8d/a21d8d56f08772f8dde167fda9743b30.jpg",
            "https://i.pinimg.com/736x/ca/4c/17/ca4c17e6ed62edd2217ed65c3842ebb4.jpg",
            "https://cdn.discordapp.com/attachments/509753928058011683/541087726347354133/image0.png",
            "https://cdn.discordapp.com/attachments/509753928058011683/541088151943249947/Untitled.png",
            "https://i.redd.it/kzi17f2qtkn11.jpg",
            "https://66.media.tumblr.com/1ff11fac55a998b0825870ed1083c173/tumblr_pkj4kjInoF1y2hj88o3_250.jpg",
            "https://cdn.discordapp.com/attachments/509753928058011683/541088350724161537/image0.png",
            "||https://cdn.discordapp.com/attachments/509753928058011683/541088413579870228/unknown.png||",
            "https://cdn.discordapp.com/attachments/509753928058011683/541088587807064111/image0.png"
            'The correct conjugation is “yote.”',
            "https://cdn.discordapp.com/attachments/509753928058011683/555126639206596628/image0.png",
            "https://cdn.discordapp.com/attachments/509753928058011683/555129877779709952/image0.png",
            "https://cdn.discordapp.com/attachments/509753928058011683/555129905252401152/image0.png",
            "https://cdn.discordapp.com/attachments/509753928058011683/555129931214880788/image0.png",
            "yeet yeet lick my feet",
            "Yeet the child",
            "UwU Yeet UwU",
            "Ready to yeet into my bed and sleep for five years",
            "*Yeets with class and elegance*",
            "I will personally yeet God into the sun",
            "Yeet? Haven’t heard that word in a long time."
            "Y'all ever just wanna Yeet?",
            "Yeet wars the empire strikes yeet",
            "Do you kno teh yeet?",
            "Have a happy yeetyear",
            "Nohaxjustyeet",
            "Press yeet to pay respects for $10",
            "Tactical yeet, incoming!",
            "All i do is yeet yeet",
            "The avengers age of yeet",
            "The united states of yeet",
            "FUS ROH YEET",
            "Yeetington D.C.",
            "Airspeed20Yesterday at 8:57 AM",
            "Here comes the yeet",
            "We will wee will yeet you",
            "MR YEETSIES",
            "And so, the criminal was charged 14 years in jail for disrespecting the yeet",
            "Airspeed20Yesterday at 10:24 AM",
            "Yeetnado",
            "Yes, id like to order a burger with a side of yeet",
            "TURN UP THE YEET",
            "Beat your yeet",
            "NEWS FLASH: YEETocracy uprisings have been taking place in St. Peatersburg",
            "Yeet me if you want to",
            "Skrrut skrrut skruut YEET",
            "Airspeed20Yesterday at 3:12 PM",
            "Luke, you must YEET darth vader",
            "YEET, forest, YEET",
            "May the yeet be with you",
            "The russian yeeteratin",
            "mr yeetseeks",
            "What a Yeet!",
            "Take the Yeet!",
            "Yeeters gonna yeet",
            "Touch me 'til I YEET",
            "his bitch empty.  *YEET*",
            "Watch your language or the cleats will yeet",
            "KAMEHAMEYEET",
            "We yeeting off",
            "GOD BLESS AMERICA, LAND OF THE YEET",
            "Yeet, yeet, im a sheep i said yeet yeet im a sheep",
            "Y\nE\nE\nT",
            "Yeet is love, Yeet is life.",
            "yeet yeet, Appa",
            "YEET THE CHILD FOR THEIR HEALTH",
            "Yeet or be Yeeten",
            "Tonight, we YEET",
            "Its time to light up the sky with YEET",
            "Certified angus Yeet, fresh and homemade!",
            "yeet, in a manner of speaking",
            "I BELIEVE I CAN YEET",
            "yeetest",
            "YeEeEeEeEeEeEeEeEeEeEeEeT",
            "Stop Yeeting. I’m trying to sleep.",
            "https://i.redd.it/nw9e1sd6k8m21.jpg",
            "https://cdn.discordapp.com/attachments/509753928058011683/562400816158343178/image0.jpg",
            "https://cdn.discordapp.com/attachments/509753928058011683/562400922240548886"
            "/Thepathweallchoose_d36bd9_7017306.png",
            "https://cdn.discordapp.com/attachments/509753928058011683/562400985763414026/image0.png"
            ]


@client.event
async def on_ready():
    """On login print information about the bot."""
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_guild_join(guild):
    """On joining a discord server(guild) find the #general channel and send a welcome message."""
    general = discord.utils.find(lambda x: x.name == 'general', guild.text_channels)
    if general and general.permissions_for(guild.me).send_messages:
        await general.send("YEET!\n please join our support server: https://discord.gg/PJwQxHR\ny!help for the "
                           "commands list")


# noinspection PyBroadException
@client.event
async def on_message(message):
    """Depending on the message, send a response to the channel the message was received from.
        y!test: Say hello.
        y!certainImg <int>: Pick a certain yeet from the list specified with the preceding <int>.
        y!help: Show help information.
        y!yeet: Pick a yeet from the list at random and send it.
        Yeet anywhere in the message: Preform the same action as y!yeet.
        A racial slur anywhere in the message: Send a message requesting users to not use that kind of language.
    """
    if message.author.bot:
        pass
    else:
        if message.content.startswith('y!test'):
            await message.channel.send('hello')

        elif message.content.startswith("y!pick"):
            certainYeet = "unknown error"

            try:
                yeetDex = int(message.content[-1 * (message.content.__len__() - 7):])
                certainYeet = yeetList[yeetDex]

            except ValueError:
                certainYeet = "`y!pick <int>`"

            except IndexError:
                certainYeet = ("`yeet list max: " + str(yeetList.__len__() - 1) + '`')

            except:
                print("unknown error")

            finally:
                await message.channel.send(certainYeet)
                # print(certainYeet+"\n", message.content[-1 * (message.content.__len__() - 13):])

        elif message.content.startswith('y!help'):
            await message.channel.send("```y!yeet | yeet\n"
                                       "y!help | this```\nsupport server: https://discord.gg/PJwQxHR")

        elif message.content.startswith('y!yeet'):
            await message.channel.send(yeetList[randint(0, yeetList.__len__() - 1)])

        elif re.search(r"(.)*y( )*e( )*(e( )*)+t(.)*", message.content, re.IGNORECASE):
                await message.channel.send(yeetList[randint(0, yeetList.__len__() - 1)])

        elif re.search(r"(.)*(n)+(i)+(g)+(.)*(r)+(.)*", message.content, re.IGNORECASE):
            await message.channel.send("Don't please!")


# start the bot using the token(placeholder used here)
client.run('token')
# https://discordapp.com/oauth2/authorize?client_id=494971719686291456&scope=bot&permissions=2048
# support server: https://discord.gg/PJwQxHR
# icon image credit: https://www.deviantart.com/mintivy/art/YEET-SMii7Y-Fanart-712996482
# little documentation at: https://yeetbot.readthedocs.io/en/latest/
