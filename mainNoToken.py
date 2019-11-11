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
            "https://cdn.discordapp.com/attachments/509753928058011683/541088587807064111/image0.png",
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
            "https://cdn.discordapp.com/attachments/509753928058011683/562400985763414026/image0.png",
            "YEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEET"
            "YEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEET"
            "YEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEET"
            "YEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEE"
            "TYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEET"
            "YEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEET"
            "YEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEET"
            "YEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEET"
            "YEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEET"
            "YEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEET"
            "YEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEET"
            "YEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEET"
            "YEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEET"
            "YEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEET"
            "YEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEETYEET"
            "YEET",
            "I have Yeeted John Cena into space like Chuck Norris",
            "You’vE EaTen",
            "We are brave because we know how to YEET like men",
            "Yeet?",
            "Yeet!",
            "Yeet...",
            "Yeet that piano down the stairs Johnny",
            "I sexually identify as a yeet",
            "DO YOU UNDERSTAND THE YEET COMIN OUTA MAH MOUTH?!?!",
            "They Hath choseth thyne yeet",
            "They be yeetin",
            "They see me yeeting, they hate it, patroling and gonna catch me yeetin dirty",
            "You’re not my daddy, I can YEET as much as I want!",
            "#yeet",
            "Yeet translates to Yeet in German",
            "360YEETSCOPE",
            "wait, how do you yeet again?",
            "Mama Mia\nhere I yeet again\nmy my\nHow can I Skeet ya",
            "Can you please yeet me?",
            "Yeet me a cookie",
            "Yeet me out the window",
            "Yeet Yeet drop the beet",
            "Yeetbeer",
            "Mama mia thats a spicy yeet",
            "give me life or give me yeet",
            "Yeet deez nuts",
            "One Yeet, Two Yeet, Red Yeet, Blue Yeet.",
            "Deja yeet",
            "Yeetoburrito popperito",
            "I don’t give a yeet",
            "Look mom! I can Yeet!",
            "He protec, he attac, but most importantly, he yeet.",
            "mmmmm, thats a tasty yeet",
            "A train is coming to yeet your car. Chuga. Chuga.",
            "One does not simply yeet",
            "The yeet has spoken.",
            "Yeet that pie into his face already!",
            "You yeet what you sow",
            "Yeet yote yeet yote",
            "Yeet Yeet touch my... wait... this seems firmilliar...",
            "Yeetspam",
            "yeet me harder",
            "I’d like to order a hamburger with a side of yeet, please",
            "God said, “LET THERE BE YEET.”",
            "Its a bird! Its a plane! Nevermind, its just a yeet.",
            "I'm babey call yeet skeet repeat",
            "Y:joy:e:joy:e:joy:t:joy:",
            "Urban Dictionary defenition of yeet: to discard an item at a high velocity.",
            "Yeeti",
            "Yeets of steel",
            "You’ve yeet’d yer last haw",
            "Yeet me in the middle",
            "How many yeets can you yeet in a yeet?",
            "https://cdn.discordapp.com/attachments/509753928058011683/573615116264669225/image0.png",
            "https://cdn.discordapp.com/attachments/509753928058011683/573615182815690828/image0.png",
            "https://cdn.discordapp.com/attachments/509753928058011683/573615249002070016/image0.png",
            "https://cdn.discordapp.com/attachments/509753928058011683/573615313980227625/image0.png",
            "https://cdn.discordapp.com/attachments/509753928058011683/573615421983555604/image0.png",
            "https://cdn.discordapp.com/attachments/509753928058011683/573615486689083422/image0.png",
            "https://cdn.discordapp.com/attachments/509753928058011683/573615745766785035/image0.gif",
            "https://cdn.discordapp.com/attachments/509753928058011683/573616567426875450/unknown.png",
            "https://cdn.discordapp.com/attachments/509753928058011683/573616686528200734/aea18b_6305077.png",
            "https://cdn.discordapp.com/attachments/509753928058011683/573616968783888413/unknown.png",
            "https://cdn.discordapp.com/attachments/509753928058011683/573617183876448266/unknown.png",
            "https://cdn.discordapp.com/attachments/509753928058011683/573617443235168279/unknown.png",
            "Yeetmate",
            "Yeetslav",
            "Yeetmilk",
            "A wild YEET appeared!",
            "Yeet. Say it back.",
            "Yeetball",
            "Yeet cemetery",
            "Yeet cremery",
            "This bitch full... no YEET required",
            "Yeet sheet",
            "YEET THAT COKE CAN OUT THE WINDOW",
            "//yeets in dutch",
            "//yeets in american",
            "yeetopauttamous",
            "https://ih0.redbubble.net/image.562324831.7631/flat,550x550,075,f.u3.jpg",
            "https://res.cloudinary.com/teepublic/image/private/s--gau70PrD--/t_Preview/b_rgb:ffffff,c_limit,f_jpg,h_630,q_90,w_630/v1530329505/production/designs/2840683_0.jpg",
            "https://i.redd.it/s7strpkk9xx01.jpg",
            "https://i1.sndcdn.com/artworks-000394305447-aympqv-t500x500.jpg",
            "https://www.dailydot.com/wp-content/uploads/2018/09/Screen-Shot-2018-09-12-at-2.14.39-PM-800x211.png",
            "https://cdn.discordapp.com/attachments/509753928058011683/586296717318815754/y.png",
            "https://cdn.discordapp.com/attachments/509753928058011683/586296931203153942/image0.png",
            "https://cdn.discordapp.com/attachments/509753928058011683/586297048404459521/image0.png",
            "this bitch still empty. yeet",
            "https://i.imgur.com/Yi0BpS6.gif",
            "Scientist creates plane engine that sounds like somebody screaming yeet",
            "Yeetus yeetus trashnite deletus",
            "Yeet it daddy",
            "www.yeetmymeat.com",
            "https://preview.redd.it/1ag3i9xtqa531.png?width=986&auto=webp&s=a5cefe745df77e0b115540f7463e904e63786bbb",
            "Yeetball",
            "1-800-are-you-yeeting",
            "How you yeeting?",
            "is it a boy or a girl? its a yeet",
            "This is so sad can I get a yeet in chat",
            "Yeet! Child",
            "yeet yeet take a seat",
            "https://cdn.discordapp.com/attachments/509753928058011683/595303929139560456/image0.png",
            "Do you wanna yeet a snowman?",
            "WE WILL BUILD A GREAT BIG WALL AND WILL MAKE THE MEXICANS YEET FOR IT",
            "https://66.media.tumblr.com/5b1b10ac27d3fca65438a80f9132d05c/tumblr_piokc3XyCc1y0p6zko3_1280.jpg",
            "Jokes on you: this country sucks! **ya YEET**",
            "https://66.media.tumblr.com/6faaf07ba82f37ad83ec3c100f53789e/tumblr_pmfxkc1n7Q1xpvizao1_540.jpg",
            "yeet.exe has stopped working",
            "yeetwagon",
            "Make your dreams come true. Yeet as loud as you can at chuck norris",
            "Very honorable, master yeet.",
            "Live out your wildest fantasies. Yeet yourself into a fridge",
            "WHACHA YEETIN",
            "teacher: \"complete the sentence: only cool kids _____.\"\n\*writes yeet the blank\*",
            "https://cdn.discordapp.com/attachments/509753928058011683/608313790722867220/image0.png",
            "https://cdn.discordapp.com/attachments/509753928058011683/608313833924198494/image0.png",
            "https://66.media.tumblr.com/57d7c61507bd433185e2b895e86e3a91/25319b2e0c4b4481-de/s540x810/c9b8743f9751b1705b575eb2de647af927758094.jpg",
            "YEET 'EM ON THE I88",
            "Yeetgurt",
            "Idk what to say so yeet",
            "yeet my meat with my feet while dropping the beat",
            "https://cdn.discordapp.com/attachments/509753928058011683/626769639736737852/image0.png",
            "https://cdn.discordapp.com/attachments/509753928058011683/626769783618142235/image0.png",
            "https://cdn.discordapp.com/attachments/509753928058011683/626770523933900807/image0.png",
            "https://cdn.discordapp.com/attachments/509753928058011683/626770633925197824/image0.png",
            "https://cdn.discordapp.com/attachments/509753928058011683/626770777131450369/image0.png",
            "Yeet the rich",
            "йет",
            "https://i.redd.it/6mkba2ya7wt31.jpg",
            "Yeet the tea",
            "Spooky Yeet",
            "Welcome message: hewwo I'm yeet bot pleasure to meet you",
            "Yeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeet",
            "Yeet yank yoink",
            "https://cdn.discordapp.com/attachments/509753928058011683/643259078377996290/image0.png",
            "https://cdn.discordapp.com/attachments/509753928058011683/643259231188942878/image0.png"
            ]


@client.event
async def on_ready():
    """On login print information about the bot."""
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    print("yeets available: ", yeetList.__len__())


@client.event
async def on_guild_join(guild):
    """On joining a discord server(guild) send a welcome message."""
    print("guild join")
    for channel in guild.text_channels:
        if channel and channel.permissions_for(guild.me).send_messages:
            await channel.send("hewwo! I'm yeet bot pleasure to meet you!\n please join our support server: https://discord.gg/PJwQxHR\ny!help for the "
                               "commands list")
            break


# noinspection PyBroadException
@client.event
async def on_message(message):
    """
    Depending on the message, send a response to the channel the message was received from.
    y!test: Say hello.
    y!pick <int>: Pick a certain yeet from the list specified with the preceding <int>.
    y!help: Show help information.
    Yeet anywhere in the message: Pick a yeet from the list at random and send it.
    The n-word anywhere in the message: Send a message requesting users to not use that kind of language.
    """
    if message.author.bot:
        pass
    else:
        if message.content.startswith('y!test'):
            print("test")
            await message.channel.send('hello')

        elif message.content.startswith("y!get"):
            print("get")
            file = open("./yeets.txt", 'w', encoding="utf-8")
            async for yeet in message.channel.history(limit=300):
                file.write(yeet.content + '\n')
            file.close()

        elif message.content.startswith("y!pick"):
            certainYeet = "unknown error"
            yeetDex = 0
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
                print("pick", yeetDex)
                await message.channel.send(certainYeet)
                # print(certainYeet+"\n", message.content[-1 * (message.content.__len__() - 13):])

        elif message.content.startswith('y!help'):
            print("help")
            await message.channel.send("```y!yeet | yeet\n"
                                       "y!help | this\n"
                                       "y!pick <integer> | say a specific yeet```"
                                       "\nsupport server: https://discord.gg/PJwQxHR")

        elif re.search(r".*y *e *e+ *t.*", message.content, re.IGNORECASE):
            print("yeet")
            await message.channel.send(yeetList[randint(0, yeetList.__len__() - 1)])
            file = open("./yeetStat.txt", "r")
            countText = file.read()
            file.close()
            count = int(re.search(r"yeets:([0-9]+)", countText).group(1))
            count += 1
            file = open("./yeetStat.txt", "w")
            file.write("yeets:" + str(count))
            file.close()

        elif re.search(r".*nig+e*r.*", message.content, re.IGNORECASE):
            print("n-word")
            await message.channel.send("Don't please!")


# start the bot using the token(placeholder used here)
client.run("Token")
# https://discordapp.com/oauth2/authorize?client_id=494971719686291456&scope=bot&permissions=2048
# support server: https://discord.gg/PJwQxHR
# icon image credit: https://www.deviantart.com/mintivy/art/YEET-SMii7Y-Fanart-712996482
# little documentation at: https://yeetbot.readthedocs.io/en/latest/
