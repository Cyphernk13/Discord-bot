#Creator: Cypher, Date Created: 20/12/22
#Libraries needed to install to run the bot--> discord,animec,requests
import discord
from discord.ext import commands
import animec
import random
import requests
import asyncio
# import wikipedia
# import youtube_dl
# import nacl
from youtube_search import YoutubeSearch
intents=discord.Intents.all()
bot = commands.Bot(command_prefix='akio ',help_command=None,intents=intents)




##-------->Setting up Bot<------------##
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="akio help"))
    print(f'Logged in as {bot.user.name}')


'''
─█▀▀█ ░█▀▀█ ▀█▀    ░█─▄▀ ░█▀▀▀ ░█──░█ ░█▀▀▀█ 
░█▄▄█ ░█▄▄█ ░█─    ░█▀▄─ ░█▀▀▀ ░█▄▄▄█ ─▀▀▀▄▄ 
░█─░█ ░█─── ▄█▄    ░█─░█ ░█▄▄▄ ──░█── ░█▄▄▄█'''



##------------>TENOR GIF URL API FUNCTION<-----------##
def get_top_8_gifs(query):
    apikey = "AIzaSyA9UYbVirf-1c8_hqqi0xUb5oRB80-o-NI"  # click to set to your apikey
    lmt = 30
    ckey = "my_test_app"
    try:
        response = requests.get(
    "https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %       (query, apikey, ckey,  lmt))
        response.raise_for_status()
        data = response.json()
        gifs = data.get("results", [])
        top_8_gifs = [gif["media_formats"]["gif"]["url"] for gif in gifs]
        return top_8_gifs
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        return []
    


"""

░█▀▀█ ░█▀▀▀█ ▀▀█▀▀   ░█▀▀█ ░█▀▀▀█ ░█▀▄▀█ ░█▀▄▀█ ─█▀▀█ ░█▄─░█ ░█▀▀▄ ░█▀▀▀█ 
░█▀▀▄ ░█──░█ ─░█──   ░█─── ░█──░█ ░█░█░█ ░█░█░█ ░█▄▄█ ░█░█░█ ░█─░█ ─▀▀▀▄▄ 
░█▄▄█ ░█▄▄▄█ ─░█──   ░█▄▄█ ░█▄▄▄█ ░█──░█ ░█──░█ ░█─░█ ░█──▀█ ░█▄▄▀ ░█▄▄▄█     """



##--------->COMMANDS<---------------##
@bot.command()
##----->HELLO COMMAND👋🏻<-------##
async def hello(ctx):
    await ctx.send(f'Hello, {ctx.author.name}!')

@bot.command()
async def say(ctx, *, message):
    # Delete the user's message
    await ctx.message.delete()

    # Send the message as the bot
    await ctx.send(message)

@bot.command()
async def echo(ctx, *, message):
    await ctx.send(message)

@bot.command()
async def anime(ctx,*,query):
    try:
        anime=animec.Anime(query)
    except:
        await ctx.send(discord.Embed(description="Hmm can't find such anime try checking the spelling maybe? 🤔",color=discord.Color.red()))
        return
    embed=discord.Embed(title=anime.title_english,url=anime.url,description=f"{anime.description[:200]}...",color=discord.Color.random())
    embed.add_field(name="Episodes",value=str(anime.episodes))
    embed.add_field(name="Ranking",value=str(anime.ranked))
    embed.add_field(name="Rating",value=str(anime.rating))
    embed.add_field(name="Status",value=str(anime.status))
    embed.add_field(name="Type",value=str(anime.type))
    embed.add_field(name="NSFW Status",value=str(anime.is_nsfw()))
    embed.set_thumbnail(url=anime.poster)
    await ctx.send(embed=embed)

#------------> PFP COMMAND 🖼️ <--------------#

@bot.command()
async def pfp(ctx,member: discord.Member = None):
    if member:
        avatar_url = member.avatar.url
    else:
        avatar_url = ctx.author.avatar.url
    await ctx.channel.send(avatar_url)


#-------------->HUG COMMAND 🤗<--------------#
@bot.command()
async def hug(ctx,member: discord.Member = None):
    # Example usage
    query = ["Anime hug","hug anime","anime hugging","sweet anime hug"]
    l = get_top_8_gifs(random.choice(query))
    auto=discord.Embed(color=discord.Color.random())
    if member:
        if member.name==ctx.author.name:
            auto.title = f"Aww {ctx.author.name} I'll give you a hug..."
        else:
            auto.title = f"{ctx.author.name} hugged {member.name}!"
    else:
        auto.title = f"Aww {ctx.author.name} I'll give you a hug..."
    auto.set_image(url=random.choice(l))
    await ctx.send(embed=auto)


#-------------->PAT COMMAND 🤗<--------------#
@bot.command()
async def pat(ctx,member: discord.Member = None):
    # Example usage
    query = ["Anime pat","pat anime","anime patting","sweet anime pat"]
    l = get_top_8_gifs(random.choice(query))
    auto=discord.Embed(color=discord.Color.random())
    if member:
        if member.name==ctx.author.name:
            auto.title = f"Aww {ctx.author.name} come here :)..."
        else:
            auto.title = f"{ctx.author.name} pats {member.name} "
    else:
        auto.title = f"Aww {ctx.author.name} come here :)..."
    auto.set_image(url=random.choice(l))
    await ctx.send(embed=auto)

#-------------->SLAP COMMAND 🤚🏻<--------------#
@bot.command()
async def slap(ctx,member: discord.Member = None):
    # Example usage
    query = ["Anime slap","slap anime","anime slapping","brutal anime slap"]
    l = get_top_8_gifs(random.choice(query))
    auto=discord.Embed(color=discord.Color.random())
    if member:
        if member.name==ctx.author.name:
            auto.title = f"Baka!! {ctx.author.name}, here you deserve it >:(..."
        else:
            auto.title = f"{ctx.author.name} slapped {member.name}!"
    else:
        auto.title = f"Baka!! {ctx.author.name}, here you deserve it >:(..."
    auto.set_image(url=random.choice(l))
    await ctx.send(embed=auto)

#-------------->KISS COMMAND 💋<--------------#
@bot.command()
async def kiss(ctx,member: discord.Member = None):
    # Example usage
    query = ["Anime kiss","kiss anime","anime kissing","romantic anime kiss"]
    l = get_top_8_gifs(random.choice(query))
    auto=discord.Embed(color=discord.Color.random())
    if member:
        if member.name==ctx.author.name:
            auto.title = f"Umm {ctx.author.name}, I don't mind it if it is with you >///<..."
        else:
            auto.title = f"{ctx.author.name} kissed {member.name} !"
    else:
        auto.title = f"Umm {ctx.author.name}, I don't mind it if it is with you >///<..."
    auto.set_image(url=random.choice(l))
    await ctx.send(embed=auto)

#-------------->KILL COMMAND 🔪<--------------#
@bot.command()
async def kill(ctx,member: discord.Member = None):
    # Example usage
    query = ["Anime kill","kill anime","anime killing","brutal anime kill"]
    l = get_top_8_gifs(random.choice(query))
    auto=discord.Embed(color=discord.Color.random())
    if member:
        if member.name==ctx.author.name:
            auto.title = f"DIE {ctx.author.name}!!!!"
        else:
            auto.title = f"{ctx.author.name} killed {member.name} !"
    else:
        auto.title = f"DIE {ctx.author.name}!!!!"
    auto.set_image(url=random.choice(l))
    await ctx.send(embed=auto)


#-------------->BLUSH COMMAND 😳<--------------#
@bot.command()
async def blush(ctx,member: discord.Member = None):
    # Example usage
    query = ["Anime blush","blushing anime","anime blushing","cute anime blush"]
    l = get_top_8_gifs(random.choice(query))
    auto=discord.Embed(color=discord.Color.random())
    if member:
        if member.name==ctx.author.name:
            auto.title = f"{ctx.author.name} is blushing >///<"
        else:
            auto.title = f"{ctx.author.name} blushes on {member.name} UwU!"
    else:
        auto.title = f"{ctx.author.name} is blushing >///<"
        pass
    auto.set_image(url=random.choice(l))
    await ctx.send(embed=auto)

@bot.command()
async def kuru(ctx):
    await ctx.send("kuru~ kuru~ kuru~ kuru~ kuru~ kuru~ kuru~ kuru~ kuru kururin kuru kururin")
    await ctx.send("https://tenor.com/hCh8h4nNTBe.gif")

#-------------->SHRUG COMMAND ＼（〇_ｏ）／<--------------#
@bot.command()
async def shrug(ctx,member: discord.Member = None):
    # Example usage
    query = ["Anime shrug","shruging anime","anime shruging","cute anime shrug"]
    l = get_top_8_gifs(random.choice(query))
    auto=discord.Embed(color=discord.Color.random())
    if member:
        if member.name==ctx.author.name:
            auto.title = f"{ctx.author.name} shrugged ¯\_(ツ)_/¯"
        else:
            auto.title = f"{ctx.author.name} shrugged ¯\_(ツ)_/¯"
    else:
        auto.title = f"{ctx.author.name} shrugged ¯\_(ツ)_/¯"
        pass
    auto.set_image(url=random.choice(l))
    await ctx.send(embed=auto)


#-------------->POUT COMMAND 😒<--------------#
@bot.command()
async def pout(ctx,member: discord.Member = None):
    # Example usage
    query = ["Anime pout","pouting anime","anime pouting","cute anime pout"]
    l = get_top_8_gifs(random.choice(query))
    auto=discord.Embed(color=discord.Color.random())
    if member:
        if member.name==ctx.author.name:
            auto.title = f"{ctx.author.name} is angry !!"
        else:
            auto.title = f"{ctx.author.name} is angry !!"
    else:
        auto.title = f"{ctx.author.name} is angry !!"
        pass
    auto.set_image(url=random.choice(l))
    await ctx.send(embed=auto)


#-------------->SPIN COMMAND 💫<--------------#
@bot.command()
async def spin(ctx,member: discord.Member = None):
    # Example usage
    query = ["Anime spin","spinning anime","anime spinning","cute anime spin"]
    l = get_top_8_gifs(random.choice(query))
    auto=discord.Embed(color=discord.Color.random())
    if member:
        if member.name==ctx.author.name:
            auto.title = f"Woah {ctx.author.name} is spinning! "
        else:
            auto.title = f"{member.name} is spinning hard!!"
    else:
        auto.title = f"Woah {ctx.author.name} is spinning! "
        pass
    auto.set_image(url=random.choice(l))
    await ctx.send(embed=auto)


#-------------->DANCE COMMAND 💃🏻<--------------#
@bot.command()
async def dance(ctx,member: discord.Member = None):
    # Example usage
    query = ["Anime dance","dancing anime","anime dancing","cute anime dance"]
    l = get_top_8_gifs(random.choice(query))
    auto=discord.Embed(color=discord.Color.random())
    if member:
        if member.name==ctx.author.name:
            auto.title = f"Nice moves {ctx.author.name}"
        else:
            auto.title = f"{member.name} is dancing :D"
    else:
        auto.title = f"{ctx.author.name} loves dancing"
        pass
    auto.set_image(url=random.choice(l))
    await ctx.send(embed=auto)

#-------------->WAVE COMMAND 👋🏻<--------------#
@bot.command()
async def wave(ctx,member: discord.Member = None):
    # Example usage
    query = ["Anime wave","waving anime","anime waving","cute anime wave"]
    l = get_top_8_gifs(random.choice(query))
    auto=discord.Embed(color=discord.Color.random())
    if member:
        if member.name==ctx.author.name:
            auto.title = f"{ctx.author.name} is waving "
        else:
            auto.title = f"{ctx.author.name} waves at {member.name} "
    else:
        auto.title = f"{ctx.author.name} is waving"
        pass
    auto.set_image(url=random.choice(l))
    await ctx.send(embed=auto)


#-------------->LAUGH COMMAND 😆<--------------#
@bot.command()
async def laugh(ctx,member: discord.Member = None):
    # Example usage
    query = ["Anime laugh","laughing anime","anime laughing","cute anime laugh"]
    l = get_top_8_gifs(random.choice(query))
    auto=discord.Embed(color=discord.Color.random())
    if member:
        if member.name==ctx.author.name:
            auto.title = f"{ctx.author.name} is laughing "
        else:
            auto.title = f"{ctx.author.name} laughs at {member.name} "
    else:
        auto.title = f"{ctx.author.name} is laughing"
        pass
    auto.set_image(url=random.choice(l))
    await ctx.send(embed=auto)

#-------------->WINK COMMAND 😉<--------------#
@bot.command()
async def wink(ctx,member: discord.Member = None):
    # Example usage
    query = ["Anime wink","winking anime","anime winking","cute anime wink"]
    l = get_top_8_gifs(random.choice(query))
    auto=discord.Embed(color=discord.Color.random())
    if member:
        if member.name==ctx.author.name:
            auto.title = f"{ctx.author.name} is winking "
        else:
            auto.title = f"{ctx.author.name} winks at {member.name} "
    else:
        auto.title = f"{ctx.author.name} is winking"
        pass
    auto.set_image(url=random.choice(l))
    await ctx.send(embed=auto)

#-------------->CHEER COMMAND 🥳<--------------#
@bot.command()
async def cheer(ctx,member: discord.Member = None):
    # Example usage
    query = ["Anime cheer","cheering anime","anime cheering","cute anime cheer"]
    l = get_top_8_gifs(random.choice(query))
    auto=discord.Embed(color=discord.Color.random())
    if member:
        if member.name==ctx.author.name:
            auto.title = f"{ctx.author.name} is cheering "
        else:
            auto.title = f"{ctx.author.name} cheers {member.name} "
    else:
        auto.title = f"{ctx.author.name} is cheering"
        pass
    auto.set_image(url=random.choice(l))
    await ctx.send(embed=auto)


#-------------->THINK COMMAND 🤔<--------------#
@bot.command()
async def think(ctx,member: discord.Member = None):
    # Example usage
    query = ["Anime think","thinking anime","anime thinking","cute anime think"]
    l = get_top_8_gifs(random.choice(query))
    auto=discord.Embed(color=discord.Color.random())
    if member:
        if member.name==ctx.author.name:
            auto.title = f"{ctx.author.name} is thinking hard!! "
        else:
            auto.title = f"{ctx.author.name} thinks about {member.name} "
    else:
        auto.title = f"{ctx.author.name} is thinking hard!!"
        pass
    auto.set_image(url=random.choice(l))
    await ctx.send(embed=auto)

#-------------->HIGHFIVE COMMAND 🙏🏻<--------------#
@bot.command()
async def highfive(ctx,member: discord.Member = None):
    # Example usage
    query = ["Anime highfive","highfiving anime","anime highfiving","cute anime highfive"]
    l = get_top_8_gifs(random.choice(query))
    auto=discord.Embed(color=discord.Color.random())
    if member:
        if member.name==ctx.author.name:
            auto.title = f"We are the best fr {ctx.author.name} "
        else:
            auto.title = f"{ctx.author.name} highfives {member.name} "
    else:
        auto.title = f"We are the best fr {ctx.author.name}"
        pass
    auto.set_image(url=random.choice(l))
    await ctx.send(embed=auto)

#-------------->SALUTE COMMAND 🫡<--------------#
@bot.command()
async def salute(ctx,member: discord.Member = None):
    # Example usage
    query = ["Anime salute","saluting anime","anime saluting","cute anime salute"]
    l = get_top_8_gifs(random.choice(query))
    auto=discord.Embed(color=discord.Color.random())
    if member:
        if member.name==ctx.author.name:
            auto.title = f"{ctx.author.name} salutes 🫡"
        else:
            auto.title = f"{ctx.author.name} salutes {member.name} "
    else:
        auto.title = f"{ctx.author.name} salutes 🫡"
        pass
    auto.set_image(url=random.choice(l))
    await ctx.send(embed=auto)

#-------------->APPLAUD COMMAND 👏🏻<--------------#
@bot.command()
async def applaud(ctx,member: discord.Member = None):
    # Example usage
    query = ["Anime applaud","applauding anime","anime applauding","cute anime applaud"]
    l = get_top_8_gifs(random.choice(query))
    auto=discord.Embed(color=discord.Color.random())
    if member:
        if member.name==ctx.author.name:
            auto.title = f"{ctx.author.name} applauds!"
        else:
            auto.title = f"{ctx.author.name} applauds {member.name} "
    else:
        auto.title = f"{ctx.author.name} applauds!"
        pass
    auto.set_image(url=random.choice(l))
    await ctx.send(embed=auto)


#-------------->CLAP COMMAND 👏🏻<--------------#
@bot.command()
async def clap(ctx,member: discord.Member = None):
    # Example usage
    query = ["Anime clap","clapping anime","anime clapping","cute anime clap"]
    l = get_top_8_gifs(random.choice(query))
    auto=discord.Embed(color=discord.Color.random())
    if member:
        if member.name==ctx.author.name:
            auto.title = f"{ctx.author.name} is clapping 👏🏻"
        else:
            auto.title = f"{ctx.author.name} claps for {member.name} "
    else:
        auto.title = f"{ctx.author.name} is clapping!"
        pass
    auto.set_image(url=random.choice(l))
    await ctx.send(embed=auto)


#-------------->BULLY COMMAND <--------------#
@bot.command()
async def bully(ctx,member: discord.Member = None):
    # Example usage
    query = ["Anime bully","bullying anime","anime bullying","cute anime bully"]
    l = get_top_8_gifs(random.choice(query))
    auto=discord.Embed(color=discord.Color.random())
    if member:
        if member.name==ctx.author.name:
            auto.title = f" Hahaha how's that {ctx.author.name}"
        else:
            auto.title = f"{ctx.author.name} is bullying {member.name} >:)"
    else:
        auto.title = f"{ctx.author.name} gets bullied"
        pass
    auto.set_image(url=random.choice(l))
    await ctx.send(embed=auto)

'''
░█▀▄▀█ ─█▀▀█ ▀▀█▀▀ ░█─░█ ░█▀▀▀█ 
░█░█░█ ░█▄▄█ ─░█── ░█▀▀█ ─▀▀▀▄▄ 
░█──░█ ░█─░█ ─░█── ░█─░█ ░█▄▄▄█'''
import math
@bot.command()
async def root(ctx,number):
    number=float(number)
    if number<0:
        await ctx.send("Please provide a non negative number :(")
        return
    number=number**0.5
    await ctx.send(str(number))

@bot.command()
async def square(ctx,number):
    number=float(number)
    number=number*number
    await ctx.send(str(number))

@bot.command()
async def power(ctx, query):
    try:
        l = query.split(',')
        if len(l) == 2:
            await ctx.send("%.2f" % math.pow(float(l[0]), float(l[1])))
        else:
            await ctx.send("Please provide input in this format: akio power num1,num2")
    except:
        await ctx.send("Invalid input. Please provide numbers in the correct format.")

@bot.command()
async def log(ctx, query):
    try:
        l = query.split(',')
        if len(l) == 2:
            await ctx.send("%.2f" % math.log(float(l[0]), float(l[1])))
        else:
            await ctx.send("Please provide input in this format: akio log num,base with base > 1")
    except:
        await ctx.send("Invalid input. Please provide numbers in the correct format.")

@bot.command()
async def add(ctx, query):
    try:
        l = query.split(',')
        if len(l) == 2:
            await ctx.send(str(float(l[0])+float(l[1])))
        else:
            await ctx.send("Please provide input in this format: akio log num1,num2")
    except:
        await ctx.send("Invalid input. Please provide numbers in the correct format.")

@bot.command()
async def sub(ctx, query):
    try:
        l = query.split(',')
        if len(l) == 2:
            await ctx.send(str(float(l[0])-float(l[1])))
        else:
            await ctx.send("Please provide input in this format: akio log num1,num2")
    except:
        await ctx.send("Invalid input. Please provide numbers in the correct format.")

@bot.command()
async def mul(ctx, query):
    try:
        l = query.split(',')
        if len(l) == 2:
            await ctx.send(str(float(l[0])*float(l[1])))
        else:
            await ctx.send("Please provide input in this format: akio log num1,num2")
    except:
        await ctx.send("Invalid input. Please provide numbers in the correct format.")

@bot.command()
async def div(ctx, query):
    try:
        l = query.split(',')
        if len(l) == 2:
            await ctx.send(str(float(l[0])/float(l[1])))
        else:
            await ctx.send("Please provide input in this format: akio log num1,num2")
    except:
        await ctx.send("Invalid input. Please provide numbers in the correct format.")

'''
░█▀▄▀█ ░█─░█ ░█▀▀▀█ ▀█▀ ░█▀▀█ 
░█░█░█ ░█─░█ ─▀▀▀▄▄ ░█─ ░█─── 
░█──░█ ─▀▄▄▀ ░█▄▄▄█ ▄█▄ ░█▄▄█'''

########STILL WORKING ON IT####################


"""
░█▀▀█ █▀▀█ ▀▀█▀▀    █──█ █▀▀ █── █▀▀█ 
░█▀▀▄ █──█ ──█──    █▀▀█ █▀▀ █── █──█ 
░█▄▄█ ▀▀▀▀ ──▀──    ▀──▀ ▀▀▀ ▀▀▀ █▀▀▀"""

@bot.command()
async def help(ctx):
    auto = discord.Embed(title="Help Commands", description="Prefix is ```akio```\n1. For now, I can give you info about your favorite anime by using ```akio anime <anime_name>```\n2. Hehe, wanna hug/kiss/kill/slap etc. someone? Just mention them! Use ```akio <action> <mention>```\n ``` current actions available: hug kiss slap kill blush shrug pat bully clap applaud salute highfive think cheer wink laugh wave dances spin and pout```\n3. I can repeat your sentences as well as sing with you :D Use ```akio echo <sentence to repeat>```\n4. GAMES!!! ```akio guess, akio hangman```\n5. Maths! do some fun maths operations currently available ```add sub mul div root square log power```\n6. Fetch pfp of a user by ```akio pfp <mention>```\n6. kuru~ kuru~ kuru~ kuru~ kuru~ kuru~ kuru~ kuru~ kuru kururin kuru kururin ```akio kuru```" , color=discord.Color.random())
    avatar_url = bot.user.avatar.url
    auto.set_thumbnail(url=avatar_url)
    await ctx.send(embed=auto)



""" 
░█▀▀█ ─█▀▀█ ░█▀▄▀█ ░█▀▀▀ ░█▀▀▀█ 
░█─▄▄ ░█▄▄█ ░█░█░█ ░█▀▀▀ ─▀▀▀▄▄ 
░█▄▄█ ░█─░█ ░█──░█ ░█▄▄▄ ░█▄▄▄█       """

# Create an empty dictionary to store leaderboard data
leaderboard = {}

@bot.command()
async def guess(ctx):
    number = random.randint(1, 100)
    attempts = 0
    
    await ctx.send("I'm thinking of a number between 1 and 100. Can you guess it?")
    
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel and message.content.isdigit()
    
    while True:
        try:
            guess = await bot.wait_for("message", check=check, timeout=30)
            guess = int(guess.content)
        except asyncio.TimeoutError:
            await ctx.send("Time's up! You took too long to guess.")
            return
        
        attempts += 1
        
        if guess < number:
            await ctx.send("Too low! Try guessing a higher number.")
        elif guess > number:
            await ctx.send("Too high! Try guessing a lower number.")
        else:
            await ctx.send(f"Congratulations! You guessed the number {number} correctly in {attempts} attempts!")
            
            # Update the leaderboard
            user_id = str(ctx.author.id)
            if user_id not in leaderboard or attempts < leaderboard[user_id]:
                leaderboard[user_id] = attempts
            
            return

@bot.command()
async def guess_lead(ctx):
    if leaderboard:
        sorted_leaderboard = sorted(leaderboard.items(), key=lambda x: x[1])
        leaderboard_embed = discord.Embed(title="Leaderboard", color=discord.Color.blue())
        for index, (user_id, attempts) in enumerate(sorted_leaderboard, start=1):
            member = ctx.guild.get_member(int(user_id))
            if member:
                leaderboard_embed.add_field(name=f"#{index} {member.display_name}", value=f"Attempts: {attempts}", inline=False)
        await ctx.send(embed=leaderboard_embed)
    else:
        await ctx.send("No leaderboard data available.")


@bot.command()
async def hangman(ctx):
    url = "https://random-word-api.herokuapp.com/word"
    parameters = {
        "number": 1,
    }
    response = requests.get(url, params=parameters)
    if response.status_code != 200:
        await ctx.send("Failed to fetch a random word. Please try again later.")
        return
    
    words = response.json()
    word = random.choice(words)
    word_letters = set(word)
    guessed_letters = set()
    attempts = 6
    
    await ctx.send("Let's play Hangman! I've chosen a word. Start guessing letters.")
    
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel and len(message.content) == 1
    
    while attempts > 0:
        display = "".join([f"{letter}" if letter in guessed_letters else "-" for letter in word])
        await ctx.send(f"Word: {display}")
        await ctx.send(f"Attempts left: {attempts}\nGuess a letter:")
        
        guess = await bot.wait_for("message", check=check)
        guess = guess.content.lower()
        
        if guess in guessed_letters:
            await ctx.send("You already guessed that letter. Try again!")
            continue
        
        guessed_letters.add(guess)
        
        if display == word or len(list(guessed_letters))==len(word_letters):
            await ctx.send(f"Congratulations! You guessed the word '{word}' correctly!")
            return
        elif guess not in word_letters:
            attempts -= 1
            await ctx.send(f"Wrong guess! The letter '{guess}' is not in the word. Attempts left: {attempts}")
    
    await ctx.send(f"Game over! You ran out of attempts. The word was '{word}'.")













'''

████████╗░█████╗░██╗░░██╗███████╗███╗░░██╗
╚══██╔══╝██╔══██╗██║░██╔╝██╔════╝████╗░██║
░░░██║░░░██║░░██║█████═╝░█████╗░░██╔██╗██║
░░░██║░░░██║░░██║██╔═██╗░██╔══╝░░██║╚████║
░░░██║░░░╚█████╔╝██║░╚██╗███████╗██║░╚███║
░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝'''

##------------>TOKEN<-----------##
bot.run('MTA0ODczNjYxNTYzMzI3MjkzMw.GHU0_p.MW3nJtMyKtNuJCucvVwqf8NhwQg5H_YqY0QHy8')

