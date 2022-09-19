import discord
import pymongo
from pymongo import MongoClient
from os import getenv
from random import *
from discord.ext import commands
import datetime
from discord.ext.commands import cooldown, BucketType
import asyncio

bot = commands.Bot(command_prefix = "!", description = "Bot by Vic")
global collection
global mango_url
global cluster
global db
mango_url = "mongodb+srv://Vicsi:RafaVic1!@cluster0.2ohdo.mongodb.net/?retryWrites=true&w=majority"
cluster = MongoClient(mango_url)
db = cluster["OkabeData"]
collection = db["new"]
   
@bot.event
async def on_ready():
    print("Ready !")

#CONNECT
@bot.command()
async def start(ctx):
   global user_id
   global author_id
   author_id = ctx.author.id
   user_id = {"_id": author_id}
   if ctx.author == bot.user:
      return
   if ctx.author.bot:
      return
   user_info = {"_id": author_id, "tpc": 0, "tr": 0, "ttr": 0, "te": 0, "tl": 0, "b1": 0, "b2":0, "b3":0, "money": 0, "boo":1, "timeb":0}
   collection.insert_one(user_info)
   await ctx.channel.send("👍 Your account have been created !")
@start.error
async def command_start_error(ctx, error):
   await ctx.channel.send("⚠️ Your account have already been created !")
    
#how 
@bot.command()
async def how(ctx):
    embed=discord.Embed(title=" ━━━━━━━━━━━━━━━━━━━━━", color=0x636363)
    embed.set_author(name="COMMANDS ⌨️")
    embed.add_field(name="!start", value="Pour commencer l'aventure...", inline=False)
    embed.add_field(name="!drop", value="Pour drop une réponse d'Okabe!", inline=False)
    embed.add_field(name="!daily", value="Pour récupérer votre récompense quotidienne", inline=False)
    embed.add_field(name="!Collection", value="Pour voir votre collection de mesages", inline=False)
    embed.add_field(name="!card", value="Pour voir votre profil de joueur", inline=False)
    embed.add_field(name="!score", value="Pour voir votre score", inline=False)
    embed.add_field(name="!badges", value="Pour connaître ce que réprésentent vos badges", inline=False)
    embed.add_field(name="!shop", value="Pour accéder au shop", inline=False)
    embed.add_field(name="!buy_[numéro]", value="Pour acheter un article du shop", inline=False)
    embed.add_field(name="!pack", value="Pour récupérer un Gift d'Okabe", inline=False)
    embed.add_field(name="!invocation", value="Pour récupérer une Invocation d'Okabe", inline=False)
    embed.add_field(name="!top", value="⚠️ En maintenance...", inline=False)
    await ctx.send(embed=embed)
        
#REWARD
@bot.command()
async def reward(ctx):
    embed=discord.Embed(title=" ━━━━━━━━━━━━━━━━━━━━━", color=0x636363)
    embed.set_author(name="REWARD 🏆")
    embed.add_field(name="🟡 Légendaire", value="Pour 1 légendaire: ⚙️ + 3🎟️ + 10,000,000💰", inline=False)
    embed.add_field(name="🟣 Epique", value="Pour 5 épiques: 1🎟️ + 5,000,000💰", inline=False)
    embed.add_field(name="🟢 Très Rare", value="Pour 40 très rares: 1🎟️ + 2,500,000💰", inline=False)
    embed.add_field(name="🟠 Rare", value="Pour 200 rares: 1🎟️ + 1,000,000💰", inline=False)
    embed.add_field(name="🔵 Peu commun", value="Pour 800 peu commun: 1,000,000💰", inline=False)
    await ctx.send(embed=embed)

#NAME
#vic
tl1=0
te1=0
ttr1=22
tr1=78
tpc1=395
s1=tpc1*1+tr1*15+ttr1*200+te1*1500+tl1*25000
#theo
tl2=0
te2=1
ttr2=8
tr2=95
tpc2=398
s2=tpc2*1+tr2*15+ttr2*200+te2*1500+tl2*25000
#doud
tl3=0
te3=0
ttr3=0
tr3=4
tpc3=12
s3=tpc3*1+tr3*15+ttr3*200+te3*1500+tl3*25000
#loujok
tl4=1
te4=1
ttr4=11
tr4=66
tpc4=291
s4=tpc4*1+tr4*15+ttr4*200+te4*1500+tl4*25000


#COLLECTION
@bot.command()
async def Collection(ctx, member:discord.Member=None):
    if member == None:
        author_id = ctx.author.id
        user_id = {"_id": author_id}
        name = await bot.fetch_user(author_id)
    else:
        author_id = member.id
        user_id = {"_id": author_id}
        name=member
    exp = collection.find(user_id)
    for tl in exp:
        cur_tl = tl["tl"]
    exp = collection.find(user_id)
    for te in exp:
        cur_te = te["te"]
    exp = collection.find(user_id)
    for ttr in exp:
        cur_ttr = ttr["ttr"]
    exp = collection.find(user_id)
    for tr in exp:
        cur_tr = tr["tr"]
    exp = collection.find(user_id)
    for tpc in exp:
        cur_tpc = tpc["tpc"]
    embed=discord.Embed(title=" ━━━━━━━━━━━━━━━━━━━━━", color=0x636363)
    embed.set_author(name="COLLECTION " f"{name}" " 📚")
    embed.add_field(name="🟡 Légendaire", value="Total:" f"{cur_tl}" " Différents:0/2", inline=False)
    embed.add_field(name="🟣 Epique", value="Total:" f"{cur_te}" " Différents:0/3", inline=False)
    embed.add_field(name="🟢 Très Rare", value="Total:" f"{cur_ttr}" " Différents:0/5", inline=False)
    embed.add_field(name="🟠 Rare", value="Total:" f"{cur_tr}" " Différents:0/7", inline=False)
    embed.add_field(name="🔵 Peu commun", value="Total:" f"{cur_tpc}" " Différents:0/12", inline=False)
    await ctx.send(embed=embed)

#MONEY
@bot.command()
async def money(ctx):
    global user_id
    global author_id
    author_id = ctx.author.id
    user_id = {"_id": author_id}
    exp = collection.find(user_id)
    for money in exp:
        cur_money = money["money"]
    embed=discord.Embed(title=" ━━━━━", color=0x636363)
    embed.set_author(name="MONEY 💸")
    embed.add_field(name="You have:", value=f"{cur_money}" " 💰", inline=False)
    await ctx.send(embed=embed)

#TOP
classement=[s1,s2,s3,s4]
classement.sort()
n1=classement[3]
n2=classement[2]
n3=classement[1]
n4=classement[0]
if n1==s1:
    name1="Vic"
elif n1==s2:
    name1="Theo"
elif n1==s3:
    name1="Doud"
elif n1==s4:
    name1="Loujok"
if n2==s1:
    name2="Vic"
elif n2==s2:
    name2="Theo"
elif n2==s3:
    name2="Doud"
elif n2==s4:
    name2="Loujok"
if n3==s1:
    name3="Vic"
elif n3==s2:
    name3="Theo"
elif n3==s3:
    name3="Doud"
elif n3==s4:
    name3="Loujok"
if n4==s1:
    name4="Vic"
elif n4==s2:
    name4="Theo"
elif n4==s3:
    name4="Doud"
elif n4==s4:
    name4="Loujok"

@bot.command()
async def top(ctx):
    embed=discord.Embed(title=" ━━━━━━━━━", color=0x636363)
    embed.set_author(name="TOP 🏆")
    embed.add_field(name="#1 " f"{name1}", value=f"{n1}" " pts", inline=False)
    embed.add_field(name="#2 " f"{name2}", value=f"{n2}" " pts", inline=False)
    embed.add_field(name="#3 " f"{name3}", value=f"{n3}" " pts", inline=False)
    embed.add_field(name="#4 " f"{name4}", value=f"{n4}" " pts", inline=False)
    await ctx.send(embed=embed)   

#CARD
@bot.command()
async def card(ctx, member:discord.Member=None):
    if member == None:
        author_id = ctx.author.id
        user_id = {"_id": author_id}
        name = await bot.fetch_user(author_id)
    else:
        author_id = member.id
        user_id = {"_id": author_id}
        name=member
    badge = None
    exp = collection.find(user_id)
    for b1 in exp:
        cur_b1 = b1["b1"]
    if cur_b1 == 1:
        if badge == None:
            badge = str()
        badge=badge+"⚙ ️"
    exp = collection.find(user_id)
    for b2 in exp:
        cur_b2 = b2["b2"]
    if cur_b2 == 1:
        if badge == None:
            badge = str()
        badge=badge+"⭐ "
    elif cur_b2 == 2:
        if badge == None:
            badge = str()
        badge=badge+"🌟 "
    elif cur_b2 == 3:
        if badge == None:
            badge = str()
        badge=badge+"✨ "
    exp = collection.find(user_id)
    for b3 in exp:
        cur_b3 = b3["b3"]
    if cur_b3 == 1:
        if badge == None:
            badge = str()
        badge=badge+"🌈 "
    exp = collection.find(user_id) 
    for tl in exp:
        cur_tl = tl["tl"]
    exp = collection.find(user_id)
    for te in exp:
        cur_te = te["te"]
    exp = collection.find(user_id)
    for ttr in exp:
        cur_ttr = ttr["ttr"]
    exp = collection.find(user_id)
    for tr in exp:
        cur_tr = tr["tr"]
    exp = collection.find(user_id)
    for tpc in exp:
        cur_tpc = tpc["tpc"]
    exp = collection.find(user_id)
    for money in exp:
        cur_money = money["money"]
    s=cur_tpc*1+cur_tr*15+cur_ttr*200+cur_te*1500+cur_tl*25000
    embed=discord.Embed(title=" ━━━━━━━━━", color=0x636363)
    embed.set_author(name="CARD " f"{name}" " 💾")
    embed.add_field(name="Score", value=f"{s}" " pts", inline=False)
    embed.add_field(name="Rank", value="⚠️ En maintenance...", inline=False)
    embed.add_field(name="Money", value=f"{cur_money}" " 💰", inline=False)
    embed.add_field(name="Badges", value=f"{badge}", inline=False)
    await ctx.send(embed=embed)

#SCORE
@bot.command()
async def score(ctx):
    global user_id
    global author_id
    global tl
    global te
    global ttr
    global tr
    global tpc
    global exp
    author_id = ctx.author.id
    user_id = {"_id": author_id}
    exp = collection.find(user_id)
    for tl in exp:
        cur_tl = tl["tl"]
    exp = collection.find(user_id)
    for te in exp:
        cur_te = te["te"]
    exp = collection.find(user_id)
    for ttr in exp:
        cur_ttr = ttr["ttr"]
    exp = collection.find(user_id)
    for tr in exp:
        cur_tr = tr["tr"]
    exp = collection.find(user_id)
    for tpc in exp:
        cur_tpc = tpc["tpc"]
    s=cur_tpc*1+cur_tr*15+cur_ttr*200+cur_te*1500+cur_tl*25000
    embed=discord.Embed(title=" ━━━━━", color=0x636363)
    embed.set_author(name="SCORE 🏆")
    embed.add_field(name="You have:", value=f"{s}" " pts", inline=False)
    await ctx.send(embed=embed)

#BADGES
@bot.command()
async def badges(ctx):
    author_id = ctx.author.id
    user_id = {"_id": author_id}
    name = await bot.fetch_user(author_id)
    badge = None
    exp = collection.find(user_id)
    for b1 in exp:
        cur_b1 = b1["b1"]
    if cur_b1 == 1:
        if badge == None:
            badge = str()
        badge=badge+"⚙ ️"
    exp = collection.find(user_id)
    for b2 in exp:
        cur_b2 = b2["b2"]
    if cur_b2 >= 1:
        if badge == None:
            badge = str()
        badge=badge+"⭐ "
    if cur_b2 >= 2:
        if badge == None:
            badge = str()
        badge=badge+"🌟 "
    if cur_b2 >= 3:
        if badge == None:
            badge = str() 
        badge=badge+"✨"
    exp = collection.find(user_id)
    for b3 in exp:
        cur_b3 = b3["b3"]
    if cur_b3 >= 1:
        if badge == None:
            badge = str() 
        badge=badge+"🌈"
    embed=discord.Embed(title=" ━━━━━", color=0x636363)
    embed.set_author(name="BADGES 🎗️")
    embed.add_field(name="You have:", value=f"{badge}", inline=False)
    message=await ctx.send(embed=embed)
    exp = collection.find(user_id)
    for b1 in exp:
        cur_b1 = b1["b1"]
    if cur_b1 == 1:
        await message.add_reaction("⚙")
    exp = collection.find(user_id)
    for b2 in exp:
        cur_b2 = b2["b2"]
    if cur_b2 >= 1:
        await message.add_reaction("⭐")
    if cur_b2 >= 2:
        await message.add_reaction("🌟")
    if cur_b2 >= 3:
        await message.add_reaction("✨")
    exp = collection.find(user_id)
    for b3 in exp:
        cur_b3 = b3["b3"]
    if cur_b3 >= 1:
        await message.add_reaction("🌈")
    def checkEmoji(reaction, user):
        return ctx.message.author == user and message.id==reaction.message.id and(str(reaction.emoji) == "⚙" or str(reaction.emoji) == "⭐" or str(reaction.emoji) == "🌟" or str(reaction.emoji) == "✨" or str(reaction.emoji) == "🌈")  
    reaction, user = await bot.wait_for("reaction_add", check=checkEmoji)
    if reaction.emoji == "⚙":
        embed=discord.Embed(color=0xd1d1d1)
        embed.add_field(name="⚙ Lab Member", value="Vous avez débloqué un légendaire", inline=False)
        await ctx.send(embed=embed)
        reaction, user = await bot.wait_for("reaction_add", check=checkEmoji)
    if reaction.emoji == "⭐":
        embed=discord.Embed(color=0xd1d1d1)
        embed.add_field(name="⭐ 1,000 pts", value="Vous avez obtenu 1,000pts", inline=False)
        await ctx.send(embed=embed)
        reaction, user = await bot.wait_for("reaction_add", check=checkEmoji)
    if reaction.emoji == "🌟":
        embed=discord.Embed(color=0xd1d1d1)
        embed.add_field(name="🌟  10,000 pts", value="Vous avez obtenu 10,000pts", inline=False)
        await ctx.send(embed=embed)
        reaction, user = await bot.wait_for("reaction_add", check=checkEmoji)
    if reaction.emoji == "✨":
        embed=discord.Embed(color=0xd1d1d1)
        embed.add_field(name="✨ 100,000 pts", value="Vous avez obtenu 100,000pts", inline=False)
        await ctx.send(embed=embed)
        reaction, user = await bot.wait_for("reaction_add", check=checkEmoji)
    if reaction.emoji == "🌈":
        embed=discord.Embed(color=0xd1d1d1)
        embed.add_field(name="🌈 All rarities unlocked", value="Vous avez obtenu au moins une réponse de chaque rareté", inline=False)
        await ctx.send(embed=embed)
        reaction, user = await bot.wait_for("reaction_add", check=checkEmoji)
      
#PROBA
liste = (range(1000000))
liste0 = (range(1000))
debut = ["Hey!", "Hi!", "Hello there"]
commun = ["Hmmmmm", "Still here?", "Pfff...", "2929831831...", "The people are like garbage", "I have to go on @channel", "No way...", "I hate that Alpacaman...", "I'm tired", "Are you serious?", "drop? haha", "Not today", "Don't disturb me", "...", "What are you waiting for?", "Stop doing that"]
communK = ["Yes, it's me", "My name is Hououin Kyouma", "Fuahaha", "It's time for a new operation", "Hehehehe", "Deceive the world"]
peucommun = ["Mission complete!", "Okey-Dokey !", "it's time to send a D-Mail...", "I'm the man who will destroy your ambitions.", "Butterfly Effect", "Gel-Banana...", "Oh-ha~! ♫", "The drink of the chosen ones, Dr Pepper !", "Daru, my Super Hacker!", "The Organization is chasing me after all.", "Future Gadget #1: The Bit Particle Gun!", "Future Gadget #2: The Bamboo Helicam!"]
rare = ["Future Gadget #6: the Cyalume Saber!", "Human is dead, mismatch", "The Time Leap Machine!", "the IBN 5100!", "Metal Upa!", "The Divergence Meter!", "Christina, my assistant !"]
tresrare = ["Fuahahahaha", "Huh? Mayushii's watch has stopped...", "The Reading Steiner!", "Future Gadget #8: the Phone Microwave!", "Tuturu! ♫"]
épique = ["I am the great mad scientist, HOUOUIN KYOUMA!", "Space has a beginning, but it has no end - infinite", "Stars too have a beginning, but are by their own power destroyed - finite"]
légendaire = ["El Psy Kongroo...", "This is the choice of Steins;Gate..."]
rec = (range(10000))


#DROP
hey=0
ope=0
opi=0
nb_inv=0
@bot.command()
async def drop(ctx):
    global new_money
    global user_id
    global author_id
    author_id = ctx.author.id
    user_id = {"_id": author_id}
    new_money=0
    exp = collection.find(user_id)
    for boo in exp:
        cur_boo = boo["boo"]
    exp = collection.find(user_id)
    for money in exp:
        cur_money = money["money"]
        new_money = cur_money + (1*cur_boo)
    collection.update_one({"_id": author_id}, {"$set":{"money":new_money}}, upsert=True)
    global hey
    global ope
    global opi
    opi = opi+0
    ope = ope+0
    hey = hey+1
    nb = choice(rec)
    a = choice(debut)
    b = choice(liste)
    c = choice(commun)
    d = choice(peucommun)
    e = choice(rare)
    f = choice(tresrare)
    g = choice(épique)
    h = choice(légendaire)
    k = choice(communK)
    if b==144078:
        print(b, ": légendaire")
        embed=discord.Embed(title=h, color=0xfff829)
        exp = collection.find(user_id)
        for tl in exp:
            cur_tl = tl["tl"]
            new_tl = cur_tl + 1
        collection.update_one({"_id": author_id}, {"$set":{"tl":new_tl}}, upsert=True)
        await ctx.send(embed=embed)
        if new_tl == 1:
            embed=discord.Embed(title=" ━━━━━━━━━━━━━━━━━", color=0x636363)
            embed.set_author(name="🎉 You become a member of the labo !")
            embed.add_field(name="New badge", value="⚙️ Member of the Labo", inline=False)
            embed.add_field(name="New commands", value="make ``!h0w`` with a zero instead of an o", inline=False)
        await ctx.send(embed=embed)
        if nb==500:
            print("-> giftx5!")
            embed=discord.Embed(title="🎁 Gift x5 ! (fais vite la commande `!pack`)", color=0xffffff)
            await ctx.send(embed=embed)
            ope=ope+5
    elif 10<=b<=50:
        print(b, ": épique")
        embed=discord.Embed(title=g, color=0xc955d8)
        exp = collection.find(user_id)
        for te in exp:
            cur_te = te["te"]
            new_te = cur_te + 1
        collection.update_one({"_id": author_id}, {"$set":{"te":new_te}}, upsert=True)
        await ctx.send(embed=embed)
        if nb==500:
            print("-> gift!")
            embed=discord.Embed(title="🎁 Gift x3 ! (fais vite la commande `!pack`)", color=0xffffff)
            await ctx.send(embed=embed)
            ope=ope+3
    elif 1300<=b<=1750:
        print(b, ": très rare")
        embed=discord.Embed(title=f, color=0x35d070)
        exp = collection.find(user_id)
        for ttr in exp:
            cur_ttr = ttr["ttr"]
            new_ttr = cur_ttr + 1
        collection.update_one({"_id": author_id}, {"$set":{"ttr":new_ttr}}, upsert=True)
        await ctx.send(embed=embed)
        if nb==500:
            print("-> gift!")
            embed=discord.Embed(title="🎁 Gift ! (fais vite la commande `!pack`)", color=0xffffff)
            await ctx.send(embed=embed)
            ope=ope+1
    elif 45033<=b<=47033:
        print(b, ": rare")
        embed=discord.Embed(title=e, color=0xf4911f)
        exp = collection.find(user_id)
        for tr in exp:
            cur_tr = tr["tr"]
            new_tr = cur_tr + 1
        collection.update_one({"_id": author_id}, {"$set":{"tr":new_tr}}, upsert=True)
        await ctx.send(embed=embed)
        if nb==500:
            print("-> gift!")
            embed=discord.Embed(title="🎁 Gift ! (fais vite la commande `!pack`)", color=0xffffff)
            await ctx.send(embed=embed)
            ope=ope+1
    elif 345500<=b<=355550:
        print(b, ": peu commun")
        embed=discord.Embed(title=d, color=0x5aa7ce)
        exp = collection.find(user_id)
        for tpc in exp:
            cur_tpc = tpc["tpc"]
            new_tpc = cur_tpc + 1
        collection.update_one({"_id": author_id}, {"$set":{"tpc":new_tpc}}, upsert=True)
        await ctx.send(embed=embed)
        if nb==500:
            print("-> gift!")
            embed=discord.Embed(title="🎁 Gift ! (fais vite la commande `!pack`)", color=0xffffff)
            await ctx.send(embed=embed)
            ope=ope+1
    elif 100<b<200 or b==1000000:
        print("-> mega gift!")
        embed=discord.Embed(title="🎁 MEGA Gift ! (fais vite la commande `!pack`)", color=0xffffff)
        await ctx.send(embed=embed)
        opi=opi+1
    else:
        if hey==1:
            await ctx.send("**Bot has been uptaded!**" )
            await ctx.send(a)
        else:
            exp = collection.find(user_id)
            for boo in exp:
                cur_boo = boo["boo"]
            if cur_boo == 3:
                await ctx.send(k)
            else:
                await ctx.send(c)
            if 500<=nb<=600:
                print("-> gift!", nb)
                embed=discord.Embed(title="🎁 Gift ! (fais vite la commande `!pack`)", color=0xffffff)
                await ctx.send(embed=embed)
                ope=ope+1
            if 700<=nb<=800:
                print("-> sac d'or!", nb)
                embed=discord.Embed(title="Sac d'or ! +10 💰", color=0xffffff)
                await ctx.send(embed=embed)
                nb_mo_1 = 10
                exp = collection.find(user_id)
                for money in exp:
                  cur_money = money["money"]
                  new_money = cur_money + nb_mo_1
                collection.update_one({"_id": author_id}, {"$set":{"money":new_money}}, upsert=True)
            if 900<=nb<=920:
                print("-> virtual card!", nb)
                embed=discord.Embed(title="Virtual Card 💳 ! +50 💰", color=0xffffff)
                await ctx.send(embed=embed)
                nb_mo_1 = 50
                exp = collection.find(user_id)
                for money in exp:
                  cur_money = money["money"]
                  new_money = cur_money + nb_mo_1
                collection.update_one({"_id": author_id}, {"$set":{"money":new_money}}, upsert=True)
            if nb==990:
                print("-> diamant!", nb)
                embed=discord.Embed(title="Diamant 💎 ! +500 💰", color=0xffffff)
                await ctx.send(embed=embed)
                nb_mo_1 = 500
                exp = collection.find(user_id)
                for money in exp:
                  cur_money = money["money"]
                  new_money = cur_money + nb_mo_1
                collection.update_one({"_id": author_id}, {"$set":{"money":new_money}}, upsert=True)
            if 0<=nb<=10 or nb==1000:
                print("-> gift!x3")
                embed=discord.Embed(title="🎁 Gift x3 (fais vite la commande `!pack`)", color=0xffffff)
                await ctx.send(embed=embed)
                ope=ope+3
    exp = collection.find(user_id)
    for tl in exp:
        cur_tl = tl["tl"]
    exp = collection.find(user_id)
    for te in exp:
        cur_te = te["te"]
    exp = collection.find(user_id)
    for ttr in exp:
        cur_ttr = ttr["ttr"]
    exp = collection.find(user_id)
    for tr in exp:
        cur_tr = tr["tr"]
    exp = collection.find(user_id)
    for tpc in exp:
        cur_tpc = tpc["tpc"]
    exp = collection.find(user_id)
    for b2 in exp:
        cur_b2 = b2["b2"]
    exp = collection.find(user_id)
    for b3 in exp:
        cur_b3 = b3["b3"]
    if cur_b3 == 0:
        if cur_tpc>=1 and cur_tr>=1 and cur_ttr>=1 and cur_te>=1 and cur_tl>=1:
            embed=discord.Embed(color=0xd1d1d1)
            embed.add_field(name="New badge", value="🌈 All rarities unlocked", inline=False)
            await ctx.send(embed=embed)
            exp = collection.find(user_id)
            for b3 in exp:
                new_b3 = cur_b3 + 1
            collection.update_one({"_id": author_id}, {"$set":{"b3":new_b3}}, upsert=True)
    if cur_b2 == 0:
        s=cur_tpc*1+cur_tr*15+cur_ttr*200+cur_te*1500+cur_tl*25000
        if 10000>s>=1000:
            embed=discord.Embed(color=0xd1d1d1)
            embed.add_field(name="New badge", value="⭐ 1,000pts", inline=False)
            await ctx.send(embed=embed)
            exp = collection.find(user_id)
            for b2 in exp:
                new_b2 = cur_b2 + 1
            collection.update_one({"_id": author_id}, {"$set":{"b2":new_b2}}, upsert=True)
        elif 100000>s>=10000:
            embed=discord.Embed(color=0xd1d1d1)
            embed.add_field(name="New badge", value="🌟 10,000pts", inline=False)
            await ctx.send(embed=embed)
            exp = collection.find(user_id)
            for b2 in exp:
                new_b2 = cur_b2 + 2
            collection.update_one({"_id": author_id}, {"$set":{"b2":new_b2}}, upsert=True)
        elif s>=100000:
            embed=discord.Embed(color=0xd1d1d1)
            embed.add_field(name="New badge", value="✨ 100,000pts", inline=False)
            await ctx.send(embed=embed)
            exp = collection.find(user_id)
            for b2 in exp:
                new_b2 = cur_b2 + 3
            collection.update_one({"_id": author_id}, {"$set":{"b2":new_b2}}, upsert=True)
    if cur_b2 == 1:
        s=cur_tpc*1+cur_tr*15+cur_ttr*200+cur_te*1500+cur_tl*25000
        if 100000>s>=10000:
            embed=discord.Embed(color=0xd1d1d1)
            embed.add_field(name="New badge", value="🌟 10,000pts", inline=False)
            await ctx.send(embed=embed)
            exp = collection.find(user_id)
            for b2 in exp:
                new_b2 = cur_b2 + 1
            collection.update_one({"_id": author_id}, {"$set":{"b2":new_b2}}, upsert=True)
        elif s>=100000:
            embed=discord.Embed(color=0xd1d1d1)
            embed.add_field(name="New badge", value="✨ 100,000pts", inline=False)
            await ctx.send(embed=embed)
            exp = collection.find(user_id)
            for b2 in exp:
                new_b2 = cur_b2 + 2
            collection.update_one({"_id": author_id}, {"$set":{"b2":new_b2}}, upsert=True)
    if cur_b2 == 2:
        s=cur_tpc*1+cur_tr*15+cur_ttr*200+cur_te*1500+cur_tl*25000
        if s>=100000:
            embed=discord.Embed(color=0xd1d1d1)
            embed.add_field(name="New badge", value="✨ 100,000pts", inline=False)
            await ctx.send(embed=embed)
            exp = collection.find(user_id)
            for b2 in exp:
                new_b2 = cur_b2 + 1
            collection.update_one({"_id": author_id}, {"$set":{"b2":new_b2}}, upsert=True)

#SHOP
@bot.command()
async def shop(ctx):
    embed=discord.Embed(title=" ━━━━━━━━━━━━━━━━━━━━━", color=0x636363)
    embed.set_author(name="SHOP 🛒️")
    embed.add_field(name="1) 1x gift 🎁", value="75 💰", inline=False)
    embed.add_field(name="2) 3x gifts 🎁", value="150 💰", inline=False)
    embed.add_field(name="3) Invocation ☄", value="750 💰", inline=False)
    embed.add_field(name="4) MEGA gift 🎁", value="3000 💰", inline=False)
    embed.add_field(name="5) Invocation divine ☄", value="5000 💰", inline=False)
    embed.add_field(name="6) Kyouma mode 🥼", value="750 💰", inline=False)
    await ctx.send(embed=embed)
@bot.command()
async def buy_1(ctx):
    global user_id
    global author_id
    global new_money
    global ope
    author_id = ctx.author.id
    user_id = {"_id": author_id}
    new_money=0
    exp = collection.find(user_id)
    for money in exp:
        cur_money = money["money"]
    if cur_money>=75:
        embed=discord.Embed(title="You buy 🎁 Gift x1 !", color=0xffffff)
        new_money = cur_money - 75
        collection.update_one({"_id": author_id}, {"$set":{"money":new_money}}, upsert=True)
        ope=ope+1
    else:
        embed=discord.Embed(title="❌ You don't have enough money !", color=0x636363)
    await ctx.send(embed=embed)
@bot.command()
async def buy_2(ctx):
    global ope
    global user_id
    global author_id
    global new_money
    author_id = ctx.author.id
    user_id = {"_id": author_id}
    new_money=0
    exp = collection.find(user_id)
    for money in exp:
        cur_money = money["money"]
    if cur_money>=150:
        embed=discord.Embed(title="You buy 🎁 Gift x3 !", color=0xffffff)
        new_money = cur_money - 150
        collection.update_one({"_id": author_id}, {"$set":{"money":new_money}}, upsert=True)
        ope=ope+3
    else:
        embed=discord.Embed(title="❌ You don't have enough money !", color=0x636363)
    await ctx.send(embed=embed)
@bot.command()
async def buy_3(ctx):
    global user_id
    global author_id
    global new_money
    global ope
    author_id = ctx.author.id
    user_id = {"_id": author_id}
    new_money=0
    exp = collection.find(user_id)
    for money in exp:
        cur_money = money["money"]
    if cur_money>=750:
        new_money = cur_money - 750
        collection.update_one({"_id": author_id}, {"$set":{"money":new_money}}, upsert=True)
        global c_i1
        global c_i2
        global c_i3
        global nb_inv
        global ipc
        global ir
        global itr
        global ie
        nb_inv = nb_inv+1
        ipc = "🔵"
        ir = "🟠"
        itr = "🟢" 
        ie = "🟣"
        il = "✨"
        inv = (range(10000))
        ch_i1 = choice(inv)
        if 0<=ch_i1<=3000 or 7000<=ch_i1<=9000:
            c_i1 = ipc
        elif 3000<ch_i1<=5000 or 5500<=ch_i1<7000 or 9000<ch_i1<=9800:
            c_i1 = ir
        elif 5000<ch_i1<=5450 or 9850<=ch_i1<=10000:
            c_i1 = itr
        else:
            c_i1 = ie   
        ch_i2 = choice(inv)
        if 0<=ch_i2<=3000 or 7000<=ch_i2<=9000:
            c_i2 = ipc
        elif 3000<ch_i2<=5000 or 5500<=ch_i2<7000 or 9000<ch_i2<=9800:
            c_i2 = ir
        elif 5000<ch_i2<=5450 or 9850<=ch_i2<=10000:
            c_i2 = itr
        else:
            c_i2 = ie           
        ch_i3 = choice(inv)
        if 0<=ch_i3<=3000 or 7000<=ch_i3<=9000:
            c_i3 = ipc
        elif 3000<ch_i3<=5000 or 5500<=ch_i3<7000 or 9000<ch_i3<=9800:
            c_i3 = ir
        elif 5000<ch_i3<=5450 or 9850<=ch_i3<=10000:
            c_i3 = itr
        else:
            c_i3 = ie
        embed=discord.Embed(title=f"{c_i1}" f"{c_i2}" f"{c_i3}" "-> !invocation", color=0xffffff)
    else:
        embed=discord.Embed(title="❌ You don't have enough money !", color=0x636363)
    await ctx.send(embed=embed)
@bot.command()
async def buy_4(ctx):
    global opi
    global user_id
    global author_id
    global new_money
    author_id = ctx.author.id
    user_id = {"_id": author_id}
    new_money=0
    exp = collection.find(user_id)
    for money in exp:
        cur_money = money["money"]
    if cur_money>=3000:
        embed=discord.Embed(title="You buy 🎁 MEGA Gift !", color=0xffffff)
        new_money = cur_money - 3000
        collection.update_one({"_id": author_id}, {"$set":{"money":new_money}}, upsert=True)
        opi=opi+1
    else:
        embed=discord.Embed(title="❌ You don't have enough money !", color=0x636363)
    await ctx.send(embed=embed)
@bot.command()
async def buy_5(ctx):
    global user_id
    global author_id
    global new_money
    global ope
    author_id = ctx.author.id
    user_id = {"_id": author_id}
    new_money=0
    exp = collection.find(user_id)
    for money in exp:
        cur_money = money["money"]
    if cur_money>=5000:
        new_money = cur_money - 5000
        collection.update_one({"_id": author_id}, {"$set":{"money":new_money}}, upsert=True)
        global c_i1
        global c_i2
        global c_i3
        global c_i4
        global c_i5
        global nb_inv
        global ipc
        global ir
        global itr
        global ie
        global il
        nb_inv = nb_inv+1
        ipc = "🔵"
        ir = "🟠"
        itr = "🟢" 
        ie = "🟣"
        il = "✨"
        inv = (range(10000))
        ch_i1 = choice(inv)
        if 0<=ch_i1<=2000 or 8500<ch_i1<9000:
            c_i1 = ipc
        elif 2000<ch_i1<=5500:
            c_i1 = ir
        elif 5500<ch_i1<8000 or 9000<=ch_i1<10000:
            c_i1 = itr
        elif 8030<ch_i1<=8500:
            c_i1 = ie
        elif 8000<=ch_i1<=8030:
            c_i1 = il   
        ch_i2 = choice(inv)
        if 0<=ch_i2<=2000 or 8500<ch_i2<9000:
            c_i2 = ipc
        elif 2000<ch_i2<=5500:
            c_i2 = ir
        elif 5500<ch_i2<8000 or 9000<=ch_i2<10000:
            c_i2 = itr
        elif 8030<ch_i2<=8500:
            c_i2 = ie
        elif 8000<=ch_i2<=8030:
            c_i2 = il   
        ch_i3 = choice(inv)
        if 0<=ch_i3<=2000 or 8500<ch_i3<9000:
            c_i3 = ipc
        elif 2000<ch_i3<=5500:
            c_i3 = ir
        elif 5500<ch_i3<8000 or 9000<=ch_i3<10000:
            c_i3 = itr
        elif 8030<ch_i3<=8500:
            c_i3 = ie
        elif 8000<=ch_i3<=8030:
            c_i3 = il 
        ch_i4 = choice(inv)
        if 0<=ch_i4<=2000 or 8500<ch_i4<9000:
            c_i4 = ipc
        elif 2000<ch_i4<=5500:
            c_i4 = ir
        elif 5500<ch_i4<8000 or 9000<=ch_i4<10000:
            c_i4 = itr
        elif 8030<ch_i4<=8500:
            c_i4 = ie
        elif 8000<=ch_i4<=8030:
            c_i4 = il 
        ch_i5 = choice(inv)
        if 0<=ch_i5<=2000 or 8500<ch_i5<9000:
            c_i5 = ipc
        elif 2000<ch_i5<=5500:
            c_i5 = ir
        elif 5500<ch_i5<8000 or 9000<=ch_i5<10000:
            c_i5 = itr
        elif 8030<ch_i5<=8500:
            c_i5 = ie
        elif 8000<=ch_i5<=8030:
            c_i5 = il 
        embed=discord.Embed(title=f"{c_i1}" f"{c_i2}" f"{c_i3}" f"{c_i4}" f"{c_i5}" "-> !invocation_divine", color=0xffffff)
    else:
        embed=discord.Embed(title="❌ You don't have enough money !", color=0x636363)
    await ctx.send(embed=embed)
@bot.command()
async def buy_6(ctx):
    global user_id
    global author_id
    global cur_timeb
    author_id = ctx.author.id
    user_id = {"_id": author_id}
    exp = collection.find(user_id)
    for money in exp:
        cur_money = money["money"]
    if cur_money>=750:
        exp = collection.find(user_id)
        for timeb in exp:
            cur_timeb = timeb["timeb"]
            new_timeb = 1200
            print(new_timeb)
        collection.update_one({"_id": author_id}, {"$set":{"timeb":new_timeb}}, upsert=True)
        new_money = cur_money-750
        collection.update_one({"_id": author_id}, {"$set":{"money":new_money}}, upsert=True)
        embed=discord.Embed(color=0x5c998a)
        embed.add_field(name="🥼 Begin of the Kyouma Mode !", value="Vous gagnez 3 💰 par ``!drop`` pendant 20min",  inline=False)
        await ctx.send(embed=embed)
        message = await ctx.send(new_timeb)
        exp = collection.find(user_id)
        for boo in exp:
            cur_boo = boo["boo"]
            new_boo = 3
        collection.update_one({"_id": author_id}, {"$set":{"boo":new_boo}}, upsert=True)
        exp = collection.find(user_id)
        for timeb in exp:
            cur_timeb = timeb["timeb"]
        while cur_timeb > 1:
            await asyncio.sleep(100)
            exp = collection.find(user_id)
            for timeb in exp:
                cur_timeb = timeb["timeb"]
                new_timeb = cur_timeb-100
                print(new_timeb)
            collection.update_one({"_id": author_id}, {"$set":{"timeb":new_timeb}}, upsert=True)
            exp = collection.find(user_id)
        embed=discord.Embed(color=0x995c5c)
        embed.add_field(name="❌ End of the Kyouma Mode !", value="Vous gagnez à nouveau 1 💰 par ``!drop``", inline=False)
        await ctx.send(embed=embed)
        exp = collection.find(user_id)
        for boo in exp:
            cur_boo = boo["boo"]
            new_boo = 1
        collection.update_one({"_id": author_id}, {"$set":{"boo":new_boo}}, upsert=True)
        exp = collection.find(user_id)
        for timeb in exp:
            cur_timeb = timeb["timeb"]
            new_timeb = 0
        collection.update_one({"_id": author_id}, {"$set":{"timeb":new_timeb}}, upsert=True)
    else:
        embed=discord.Embed(title="❌ You don't have enough money !", color=0x636363)
        await ctx.send(embed=embed)

#KYOUMA MODE
@bot.command()
async def k_time(ctx):
   author_id = ctx.author.id
   user_id = {"_id": author_id}
   exp = collection.find(user_id)
   for timeb in exp:
      cur_timeb = timeb["timeb"]
   embed = discord.Embed(title=f"KYOUMA MODE - TIME",description=f"You have " + str(datetime.timedelta(seconds=int(cur_timeb))) + f" left", color=0x575757)
   await ctx.send(embed=embed)
      
      
#INVOCATION
@bot.command()
async def invocation(ctx):
    global c_i1
    global c_i2
    global c_i3
    global nb_inv
    global new_tpc
    global new_tr
    global new_ttr
    global new_te
    global new_tl
    global ipc
    global ir
    global itr
    global ie
    global user_id
    global author_id
    global tl
    global te
    global ttr
    global tr
    global tpc
    global exp
    author_id = ctx.author.id
    user_id = {"_id": author_id}
    if nb_inv>=1:
        nb_inv=nb_inv-1
        if c_i1 == ipc:
            d = choice(peucommun)
            embed=discord.Embed(title=d, color=0x5aa7ce)
            exp = collection.find(user_id)
            for tpc in exp:
                cur_tpc = tpc["tpc"]
                new_tpc = cur_tpc + 1
            collection.update_one({"_id": author_id}, {"$set":{"tpc":new_tpc}}, upsert=True)
            await ctx.send(embed=embed)
        elif c_i1 == ir:
            e = choice(rare)
            embed=discord.Embed(title=e, color=0xf4911f)
            exp = collection.find(user_id)
            for tr in exp:
                cur_tr = tr["tr"]
                new_tr = cur_tr + 1
            collection.update_one({"_id": author_id}, {"$set":{"tr":new_tr}}, upsert=True)
            await ctx.send(embed=embed)
        elif c_i1 == itr:
            f = choice(tresrare)
            embed=discord.Embed(title=f, color=0x35d070)
            exp = collection.find(user_id)
            for ttr in exp:
                cur_ttr = ttr["ttr"]
                new_ttr = cur_ttr + 1
            collection.update_one({"_id": author_id}, {"$set":{"ttr":new_ttr}}, upsert=True)
            await ctx.send(embed=embed)
        elif c_i1 == ie:
            g = choice(épique)
            embed=discord.Embed(title=g, color=0xc955d8)
            exp = collection.find(user_id)
            for te in exp:
                cur_te = te["te"]
                new_te = cur_te + 1
            collection.update_one({"_id": author_id}, {"$set":{"te":new_te}}, upsert=True)
            await ctx.send(embed=embed) 
        if c_i2 == ipc:
            d = choice(peucommun)
            embed=discord.Embed(title=d, color=0x5aa7ce)
            exp = collection.find(user_id)
            for tpc in exp:
                cur_tpc = tpc["tpc"]
                new_tpc = cur_tpc + 1
            collection.update_one({"_id": author_id}, {"$set":{"tpc":new_tpc}}, upsert=True)
            await ctx.send(embed=embed)
        elif c_i2 == ir:
            e = choice(rare)
            embed=discord.Embed(title=e, color=0xf4911f)
            exp = collection.find(user_id)
            for tr in exp:
                cur_tr = tr["tr"]
                new_tr = cur_tr + 1
            collection.update_one({"_id": author_id}, {"$set":{"tr":new_tr}}, upsert=True)
            await ctx.send(embed=embed)
        elif c_i2 == itr:
            f = choice(tresrare)
            embed=discord.Embed(title=f, color=0x35d070)
            exp = collection.find(user_id)
            for ttr in exp:
                cur_ttr = ttr["ttr"]
                new_ttr = cur_ttr + 1
            collection.update_one({"_id": author_id}, {"$set":{"ttr":new_ttr}}, upsert=True)
            await ctx.send(embed=embed)
        elif c_i2 == ie:
            g = choice(épique)
            embed=discord.Embed(title=g, color=0xc955d8)
            exp = collection.find(user_id)
            for te in exp:
                cur_te = te["te"]
                new_te = cur_te + 1
            collection.update_one({"_id": author_id}, {"$set":{"te":new_te}}, upsert=True)
            await ctx.send(embed=embed)
        if c_i3 == ipc:
            d = choice(peucommun)
            embed=discord.Embed(title=d, color=0x5aa7ce)
            exp = collection.find(user_id)
            for tpc in exp:
                cur_tpc = tpc["tpc"]
                new_tpc = cur_tpc + 1
            collection.update_one({"_id": author_id}, {"$set":{"tpc":new_tpc}}, upsert=True)
            await ctx.send(embed=embed)
        elif c_i3 == ir:
            e = choice(rare)
            embed=discord.Embed(title=e, color=0xf4911f)
            exp = collection.find(user_id)
            for tr in exp:
                cur_tr = tr["tr"]
                new_tr = cur_tr + 1
            collection.update_one({"_id": author_id}, {"$set":{"tr":new_tr}}, upsert=True)
            await ctx.send(embed=embed)
        elif c_i3 == itr:
            f = choice(tresrare)
            embed=discord.Embed(title=f, color=0x35d070)
            exp = collection.find(user_id)
            for ttr in exp:
                cur_ttr = ttr["ttr"]
                new_ttr = cur_ttr + 1
            collection.update_one({"_id": author_id}, {"$set":{"ttr":new_ttr}}, upsert=True)
            await ctx.send(embed=embed)
        elif c_i3 == ie:
            g = choice(épique)
            embed=discord.Embed(title=g, color=0xc955d8)
            exp = collection.find(user_id)
            for te in exp:
                cur_te = te["te"]
                new_te = cur_te + 1
            collection.update_one({"_id": author_id}, {"$set":{"te":new_te}}, upsert=True)
            await ctx.send(embed=embed)
    else:
        embed=discord.Embed(title="❌ You haven't any invocation ❌", color=0x636363)
        await ctx.send(embed=embed)
    exp = collection.find(user_id)
    for tl in exp:
        cur_tl = tl["tl"]
    exp = collection.find(user_id)
    for te in exp:
        cur_te = te["te"]
    exp = collection.find(user_id)
    for ttr in exp:
        cur_ttr = ttr["ttr"]
    exp = collection.find(user_id)
    for tr in exp:
        cur_tr = tr["tr"]
    exp = collection.find(user_id)
    for tpc in exp:
        cur_tpc = tpc["tpc"]
    exp = collection.find(user_id)
    for b2 in exp:
        cur_b2 = b2["b2"]
    if cur_b2 == 0:
        s=cur_tpc*1+cur_tr*15+cur_ttr*200+cur_te*1500+cur_tl*25000
        if 10000>s>=1000:
            embed=discord.Embed(color=0xd1d1d1)
            embed.add_field(name="New badge", value="⭐ 1,000pts", inline=False)
            await ctx.send(embed=embed)
            exp = collection.find(user_id)
            for b2 in exp:
                new_b2 = cur_b2 + 1
            collection.update_one({"_id": author_id}, {"$set":{"b2":new_b2}}, upsert=True)
        elif 100000>s>=10000:
            embed=discord.Embed(color=0xd1d1d1)
            embed.add_field(name="New badge", value="🌟 10,000pts", inline=False)
            await ctx.send(embed=embed)
            exp = collection.find(user_id)
            for b2 in exp:
                new_b2 = cur_b2 + 2
            collection.update_one({"_id": author_id}, {"$set":{"b2":new_b2}}, upsert=True)
        elif s>=100000:
            embed=discord.Embed(color=0xd1d1d1)
            embed.add_field(name="New badge", value="✨ 100,000pts", inline=False)
            await ctx.send(embed=embed)
            exp = collection.find(user_id)
            for b2 in exp:
                new_b2 = cur_b2 + 3
            collection.update_one({"_id": author_id}, {"$set":{"b2":new_b2}}, upsert=True)
    if cur_b2 == 1:
        s=cur_tpc*1+cur_tr*15+cur_ttr*200+cur_te*1500+cur_tl*25000
        if 100000>s>=10000:
            embed=discord.Embed(color=0xd1d1d1)
            embed.add_field(name="New badge", value="🌟 10,000pts", inline=False)
            await ctx.send(embed=embed)
            exp = collection.find(user_id)
            for b2 in exp:
                new_b2 = cur_b2 + 1
            collection.update_one({"_id": author_id}, {"$set":{"b2":new_b2}}, upsert=True)
        elif s>=100000:
            embed=discord.Embed(color=0xd1d1d1)
            embed.add_field(name="New badge", value="✨ 100,000pts", inline=False)
            await ctx.send(embed=embed)
            exp = collection.find(user_id)
            for b2 in exp:
                new_b2 = cur_b2 + 2
            collection.update_one({"_id": author_id}, {"$set":{"b2":new_b2}}, upsert=True)
    if cur_b2 == 2:
        s=cur_tpc*1+cur_tr*15+cur_ttr*200+cur_te*1500+cur_tl*25000
        if s>=100000:
            embed=discord.Embed(color=0xd1d1d1)
            embed.add_field(name="New badge", value="✨ 100,000pts", inline=False)
            await ctx.send(embed=embed)
            exp = collection.find(user_id)
            for b2 in exp:
                new_b2 = cur_b2 + 1
            collection.update_one({"_id": author_id}, {"$set":{"b2":new_b2}}, upsert=True)

@bot.command()
async def invocation_divine(ctx):
    global c_i1
    global c_i2
    global c_i3
    global nb_inv
    global new_tpc
    global new_tr
    global new_ttr
    global new_te
    global new_tl
    global ipc
    global ir
    global itr
    global ie
    global user_id
    global author_id
    global tl
    global te
    global ttr
    global tr
    global tpc
    global exp
    author_id = ctx.author.id
    user_id = {"_id": author_id}
    if nb_inv>=1:
        nb_inv=nb_inv-1
        if c_i1 == ipc:
            d = choice(peucommun)
            embed=discord.Embed(title=d, color=0x5aa7ce)
            exp = collection.find(user_id)
            for tpc in exp:
                cur_tpc = tpc["tpc"]
                new_tpc = cur_tpc + 1
            collection.update_one({"_id": author_id}, {"$set":{"tpc":new_tpc}}, upsert=True)
            await ctx.send(embed=embed)
        elif c_i1 == ir:
            e = choice(rare)
            embed=discord.Embed(title=e, color=0xf4911f)
            exp = collection.find(user_id)
            for tr in exp:
                cur_tr = tr["tr"]
                new_tr = cur_tr + 1
            collection.update_one({"_id": author_id}, {"$set":{"tr":new_tr}}, upsert=True)
            await ctx.send(embed=embed)
        elif c_i1 == itr:
            f = choice(tresrare)
            embed=discord.Embed(title=f, color=0x35d070)
            exp = collection.find(user_id)
            for ttr in exp:
                cur_ttr = ttr["ttr"]
                new_ttr = cur_ttr + 1
            collection.update_one({"_id": author_id}, {"$set":{"ttr":new_ttr}}, upsert=True)
            await ctx.send(embed=embed)
        elif c_i1 == ie:
            g = choice(épique)
            embed=discord.Embed(title=g, color=0xc955d8)
            exp = collection.find(user_id)
            for te in exp:
                cur_te = te["te"]
                new_te = cur_te + 1
            collection.update_one({"_id": author_id}, {"$set":{"te":new_te}}, upsert=True)
            await ctx.send(embed=embed) 
        elif c_i1 == il:
            h = choice(légendaire)
            embed=discord.Embed(title=h, color=0xfff829)
            exp = collection.find(user_id)
            for tl in exp:
                cur_tl = tl["tl"]
                new_tl = cur_tl + 1
            collection.update_one({"_id": author_id}, {"$set":{"tl":new_tl}}, upsert=True)
            await ctx.send(embed=embed)
            if new_tl == 1:
               embed=discord.Embed(title=" ━━━━━━━━━━━━━━━━━", color=0x636363)
               embed.set_author(name="🎉 You become a member of the labo !")
               embed.add_field(name="New badge", value="⚙️ Member of the Labo", inline=False)
               embed.add_field(name="New commands", value="make ``!h0w`` with a zero instead of an o", inline=False)
               await ctx.send(embed=embed)
        if c_i2 == ipc:
            d = choice(peucommun)
            embed=discord.Embed(title=d, color=0x5aa7ce)
            exp = collection.find(user_id)
            for tpc in exp:
                cur_tpc = tpc["tpc"]
                new_tpc = cur_tpc + 1
            collection.update_one({"_id": author_id}, {"$set":{"tpc":new_tpc}}, upsert=True)
            await ctx.send(embed=embed)
        elif c_i2 == ir:
            e = choice(rare)
            embed=discord.Embed(title=e, color=0xf4911f)
            exp = collection.find(user_id)
            for tr in exp:
                cur_tr = tr["tr"]
                new_tr = cur_tr + 1
            collection.update_one({"_id": author_id}, {"$set":{"tr":new_tr}}, upsert=True)
            await ctx.send(embed=embed)
        elif c_i2 == itr:
            f = choice(tresrare)
            embed=discord.Embed(title=f, color=0x35d070)
            exp = collection.find(user_id)
            for ttr in exp:
                cur_ttr = ttr["ttr"]
                new_ttr = cur_ttr + 1
            collection.update_one({"_id": author_id}, {"$set":{"ttr":new_ttr}}, upsert=True)
            await ctx.send(embed=embed)
        elif c_i2 == ie:
            g = choice(épique)
            embed=discord.Embed(title=g, color=0xc955d8)
            exp = collection.find(user_id)
            for te in exp:
                cur_te = te["te"]
                new_te = cur_te + 1
            collection.update_one({"_id": author_id}, {"$set":{"te":new_te}}, upsert=True)
            await ctx.send(embed=embed)
        elif c_i2 == il:
            h = choice(légendaire)
            embed=discord.Embed(title=h, color=0xfff829)
            exp = collection.find(user_id)
            for tl in exp:
                cur_tl = tl["tl"]
                new_tl = cur_tl + 1
            collection.update_one({"_id": author_id}, {"$set":{"tl":new_tl}}, upsert=True)
            await ctx.send(embed=embed) 
            if new_tl == 1:
               embed=discord.Embed(title=" ━━━━━━━━━━━━━━━━━", color=0x636363)
               embed.set_author(name="🎉 You become a member of the labo !")
               embed.add_field(name="New badge", value="⚙️ Member of the Labo", inline=False)
               embed.add_field(name="New commands", value="make ``!h0w`` with a zero instead of an o", inline=False)
               await ctx.send(embed=embed)
        if c_i3 == ipc:
            d = choice(peucommun)
            embed=discord.Embed(title=d, color=0x5aa7ce)
            exp = collection.find(user_id)
            for tpc in exp:
                cur_tpc = tpc["tpc"]
                new_tpc = cur_tpc + 1
            collection.update_one({"_id": author_id}, {"$set":{"tpc":new_tpc}}, upsert=True)
            await ctx.send(embed=embed)
        elif c_i3 == ir:
            e = choice(rare)
            embed=discord.Embed(title=e, color=0xf4911f)
            exp = collection.find(user_id)
            for tr in exp:
                cur_tr = tr["tr"]
                new_tr = cur_tr + 1
            collection.update_one({"_id": author_id}, {"$set":{"tr":new_tr}}, upsert=True)
            await ctx.send(embed=embed)
        elif c_i3 == itr:
            f = choice(tresrare)
            embed=discord.Embed(title=f, color=0x35d070)
            exp = collection.find(user_id)
            for ttr in exp:
                cur_ttr = ttr["ttr"]
                new_ttr = cur_ttr + 1
            collection.update_one({"_id": author_id}, {"$set":{"ttr":new_ttr}}, upsert=True)
            await ctx.send(embed=embed)
        elif c_i3 == ie:
            g = choice(épique)
            embed=discord.Embed(title=g, color=0xc955d8)
            exp = collection.find(user_id)
            for te in exp:
                cur_te = te["te"]
                new_te = cur_te + 1
            collection.update_one({"_id": author_id}, {"$set":{"te":new_te}}, upsert=True)
            await ctx.send(embed=embed)
        elif c_i3 == il:
            h = choice(légendaire)
            embed=discord.Embed(title=h, color=0xfff829)
            exp = collection.find(user_id)
            for tl in exp:
                cur_tl = tl["tl"]
                new_tl = cur_tl + 1
            collection.update_one({"_id": author_id}, {"$set":{"tl":new_tl}}, upsert=True)
            await ctx.send(embed=embed) 
            if new_tl == 1:
               embed=discord.Embed(title=" ━━━━━━━━━━━━━━━━━", color=0x636363)
               embed.set_author(name="🎉 You become a member of the labo !")
               embed.add_field(name="New badge", value="⚙️ Member of the Labo", inline=False)
               embed.add_field(name="New commands", value="make ``!h0w`` with a zero instead of an o", inline=False)
               await ctx.send(embed=embed)
        if c_i4 == ipc:
            d = choice(peucommun)
            embed=discord.Embed(title=d, color=0x5aa7ce)
            exp = collection.find(user_id)
            for tpc in exp:
                cur_tpc = tpc["tpc"]
                new_tpc = cur_tpc + 1
            collection.update_one({"_id": author_id}, {"$set":{"tpc":new_tpc}}, upsert=True)
            await ctx.send(embed=embed)
        elif c_i4 == ir:
            e = choice(rare)
            embed=discord.Embed(title=e, color=0xf4911f)
            exp = collection.find(user_id)
            for tr in exp:
                cur_tr = tr["tr"]
                new_tr = cur_tr + 1
            collection.update_one({"_id": author_id}, {"$set":{"tr":new_tr}}, upsert=True)
            await ctx.send(embed=embed)
        elif c_i4 == itr:
            f = choice(tresrare)
            embed=discord.Embed(title=f, color=0x35d070)
            exp = collection.find(user_id)
            for ttr in exp:
                cur_ttr = ttr["ttr"]
                new_ttr = cur_ttr + 1
            collection.update_one({"_id": author_id}, {"$set":{"ttr":new_ttr}}, upsert=True)
            await ctx.send(embed=embed)
        elif c_i4 == ie:
            g = choice(épique)
            embed=discord.Embed(title=g, color=0xc955d8)
            exp = collection.find(user_id)
            for te in exp:
                cur_te = te["te"]
                new_te = cur_te + 1
            collection.update_one({"_id": author_id}, {"$set":{"te":new_te}}, upsert=True)
            await ctx.send(embed=embed) 
        elif c_i4 == il:
            h = choice(légendaire)
            embed=discord.Embed(title=h, color=0xfff829)
            exp = collection.find(user_id)
            for tl in exp:
                cur_tl = tl["tl"]
                new_tl = cur_tl + 1
            collection.update_one({"_id": author_id}, {"$set":{"tl":new_tl}}, upsert=True)
            await ctx.send(embed=embed) 
            if new_tl == 1:
               embed=discord.Embed(title=" ━━━━━━━━━━━━━━━━━", color=0x636363)
               embed.set_author(name="🎉 You become a member of the labo !")
               embed.add_field(name="New badge", value="⚙️ Member of the Labo", inline=False)
               embed.add_field(name="New commands", value="make ``!h0w`` with a zero instead of an o", inline=False)
               await ctx.send(embed=embed)
        if c_i5 == ipc:
            d = choice(peucommun)
            embed=discord.Embed(title=d, color=0x5aa7ce)
            exp = collection.find(user_id)
            for tpc in exp:
                cur_tpc = tpc["tpc"]
                new_tpc = cur_tpc + 1
            collection.update_one({"_id": author_id}, {"$set":{"tpc":new_tpc}}, upsert=True)
            await ctx.send(embed=embed)
        elif c_i5 == ir:
            e = choice(rare)
            embed=discord.Embed(title=e, color=0xf4911f)
            exp = collection.find(user_id)
            for tr in exp:
                cur_tr = tr["tr"]
                new_tr = cur_tr + 1
            collection.update_one({"_id": author_id}, {"$set":{"tr":new_tr}}, upsert=True)
            await ctx.send(embed=embed)
        elif c_i5 == itr:
            f = choice(tresrare)
            embed=discord.Embed(title=f, color=0x35d070)
            exp = collection.find(user_id)
            for ttr in exp:
                cur_ttr = ttr["ttr"]
                new_ttr = cur_ttr + 1
            collection.update_one({"_id": author_id}, {"$set":{"ttr":new_ttr}}, upsert=True)
            await ctx.send(embed=embed)
        elif c_i5 == ie:
            g = choice(épique)
            embed=discord.Embed(title=g, color=0xc955d8)
            exp = collection.find(user_id)
            for te in exp:
                cur_te = te["te"]
                new_te = cur_te + 1
            collection.update_one({"_id": author_id}, {"$set":{"te":new_te}}, upsert=True)
            await ctx.send(embed=embed) 
        elif c_i5 == il:
            h = choice(légendaire)
            embed=discord.Embed(title=h, color=0xfff829)
            exp = collection.find(user_id)
            for tl in exp:
                cur_tl = tl["tl"]
                new_tl = cur_tl + 1
            collection.update_one({"_id": author_id}, {"$set":{"tl":new_tl}}, upsert=True)
            await ctx.send(embed=embed)
            if new_tl == 1:
               embed=discord.Embed(title=" ━━━━━━━━━━━━━━━━━", color=0x636363)
               embed.set_author(name="🎉 You become a member of the labo !")
               embed.add_field(name="New badge", value="⚙️ Member of the Labo", inline=False)
               embed.add_field(name="New commands", value="make ``!h0w`` with a zero instead of an o", inline=False)
               await ctx.send(embed=embed)
               exp = collection.find(user_id)
               for badge in exp:
                  cur_badge = badge["badge"]
                  new_badge = cur_badge + 1
               collection.update_one({"_id": author_id}, {"$set":{"badge":new_badge}}, upsert=True)
    else:
        embed=discord.Embed(title="❌ You haven't any invocation ❌", color=0x636363)
        await ctx.send(embed=embed)
    exp = collection.find(user_id)
    for tl in exp:
        cur_tl = tl["tl"]
    exp = collection.find(user_id)
    for te in exp:
        cur_te = te["te"]
    exp = collection.find(user_id)
    for ttr in exp:
        cur_ttr = ttr["ttr"]
    exp = collection.find(user_id)
    for tr in exp:
        cur_tr = tr["tr"]
    exp = collection.find(user_id)
    for tpc in exp:
        cur_tpc = tpc["tpc"]
    exp = collection.find(user_id)
    for b2 in exp:
        cur_b2 = b2["b2"]
    if cur_b2 == 0:
        s=cur_tpc*1+cur_tr*15+cur_ttr*200+cur_te*1500+cur_tl*25000
        if 10000>s>=1000:
            embed=discord.Embed(color=0xd1d1d1)
            embed.add_field(name="New badge", value="⭐ 1,000pts", inline=False)
            await ctx.send(embed=embed)
            exp = collection.find(user_id)
            for b2 in exp:
                new_b2 = cur_b2 + 1
            collection.update_one({"_id": author_id}, {"$set":{"b2":new_b2}}, upsert=True)
        elif 100000>s>=10000:
            embed=discord.Embed(color=0xd1d1d1)
            embed.add_field(name="New badge", value="🌟 10,000pts", inline=False)
            await ctx.send(embed=embed)
            exp = collection.find(user_id)
            for b2 in exp:
                new_b2 = cur_b2 + 2
            collection.update_one({"_id": author_id}, {"$set":{"b2":new_b2}}, upsert=True)
        elif s>=100000:
            embed=discord.Embed(color=0xd1d1d1)
            embed.add_field(name="New badge", value="✨ 100,000pts", inline=False)
            await ctx.send(embed=embed)
            exp = collection.find(user_id)
            for b2 in exp:
                new_b2 = cur_b2 + 3
            collection.update_one({"_id": author_id}, {"$set":{"b2":new_b2}}, upsert=True)
    if cur_b2 == 1:
        s=cur_tpc*1+cur_tr*15+cur_ttr*200+cur_te*1500+cur_tl*25000
        if 100000>s>=10000:
            embed=discord.Embed(color=0xd1d1d1)
            embed.add_field(name="New badge", value="🌟 10,000pts", inline=False)
            await ctx.send(embed=embed)
            exp = collection.find(user_id)
            for b2 in exp:
                new_b2 = cur_b2 + 1
            collection.update_one({"_id": author_id}, {"$set":{"b2":new_b2}}, upsert=True)
        elif s>=100000:
            embed=discord.Embed(color=0xd1d1d1)
            embed.add_field(name="New badge", value="✨ 100,000pts", inline=False)
            await ctx.send(embed=embed)
            exp = collection.find(user_id)
            for b2 in exp:
                new_b2 = cur_b2 + 2
            collection.update_one({"_id": author_id}, {"$set":{"b2":new_b2}}, upsert=True)
    if cur_b2 == 2:
        s=cur_tpc*1+cur_tr*15+cur_ttr*200+cur_te*1500+cur_tl*25000
        if s>=100000:
            embed=discord.Embed(color=0xd1d1d1)
            embed.add_field(name="New badge", value="✨ 100,000pts", inline=False)
            await ctx.send(embed=embed)
            exp = collection.find(user_id)
            for b2 in exp:
                new_b2 = cur_b2 + 1
            collection.update_one({"_id": author_id}, {"$set":{"b2":new_b2}}, upsert=True)

#DAILY
@bot.command()
@cooldown(1, 86400, BucketType.user)
async def daily(ctx): 
    global nb_da
    global new_tpc
    global new_tr
    global new_ttr
    global new_te
    global user_id
    global author_id
    global te
    global ttr
    global tr
    global tpc
    global exp
    global ope
    author_id = ctx.author.id
    user_id = {"_id": author_id}
    ti_da_1 = range(90)
    ti_da_2 = range(250)
    ti_da_3 = range(500)
    ti_da_4 = range(1500)
    nb_mo_1 = choice(ti_da_1) + 10
    nb_mo_2 = choice(ti_da_2) + 250
    nb_mo_3 = choice(ti_da_3) + 500
    nb_mo_4 = choice(ti_da_4) + 1500
    nb_da = choice(rec) 
    await ctx.channel.send("📅 DAILY REWARD")
    if 0<=nb_da<=3000:
        exp = collection.find(user_id)
        for money in exp:
            cur_money = money["money"]
            new_money = cur_money + nb_mo_1
        collection.update_one({"_id": author_id}, {"$set":{"money":new_money}}, upsert=True)
        embed=discord.Embed(title="+" f"{nb_mo_1}" " 💰", color=0xffffff)
        await ctx.send(embed=embed)
    elif 3000<nb_da<=6000:
        d = choice(peucommun)
        embed=discord.Embed(title=d, color=0x5aa7ce)
        exp = collection.find(user_id)
        for tpc in exp:
            cur_tpc = tpc["tpc"]
            new_tpc = cur_tpc + 1
        collection.update_one({"_id": author_id}, {"$set":{"tpc":new_tpc}}, upsert=True)
        await ctx.send(embed=embed)
    elif 6000<nb_da<=7500:
        e = choice(rare)
        embed=discord.Embed(title=e, color=0xf4911f)
        exp = collection.find(user_id)
        for tr in exp:
            cur_tr = tr["tr"]
            new_tr = cur_tr + 1
        collection.update_one({"_id": author_id}, {"$set":{"tr":new_tr}}, upsert=True)
        await ctx.send(embed=embed)
    elif 7500<nb_da<=8000:
        exp = collection.find(user_id)
        for money in exp:
            cur_money = money["money"]
            new_money = cur_money + nb_mo_2
        collection.update_one({"_id": author_id}, {"$set":{"money":new_money}}, upsert=True)
        embed=discord.Embed(title="+" f"{nb_mo_2}" " 💰", color=0xffffff)
        await ctx.send(embed=embed)
    elif 8000<nb_da<=9500:
        embed=discord.Embed(title="🎁 Gift x3 (fais vite la commande `!pack`)", color=0xffffff)
        await ctx.send(embed=embed)
        ope=ope+3
    elif 9500<nb_da<=9800:
        f = choice(tresrare)
        embed=discord.Embed(title=f, color=0x35d070)
        exp = collection.find(user_id)
        for ttr in exp:
            cur_ttr = ttr["ttr"]
            new_ttr = cur_ttr + 1
        collection.update_one({"_id": author_id}, {"$set":{"ttr":new_ttr}}, upsert=True)
        await ctx.send(embed=embed)
    elif 9800<nb_da<=9900:
        exp = collection.find(user_id)
        for money in exp:
            cur_money = money["money"]
            new_money = cur_money + nb_mo_3
        collection.update_one({"_id": author_id}, {"$set":{"money":new_money}}, upsert=True)
        embed=discord.Embed(title="+" f"{nb_mo_3}" " 💰", color=0xffffff)
        await ctx.send(embed=embed)
    elif 9900<nb_da<=9950:
        global c_i1
        global c_i2
        global c_i3
        global nb_inv
        global ipc
        global ir
        global itr
        global ie
        nb_inv = nb_inv+1
        ipc = "🔵"
        ir = "🟠"
        itr = "🟢" 
        ie = "🟣"
        il = "✨"
        inv = (range(10000))
        ch_i1 = choice(inv)
        if 0<=ch_i1<=3000 or 7000<=ch_i1<=9000:
            c_i1 = ipc
        elif 3000<ch_i1<=5000 or 5500<=ch_i1<7000 or 9000<ch_i1<=9800:
            c_i1 = ir
        elif 5000<ch_i1<=5450 or 9850<=ch_i1<=10000:
            c_i1 = itr
        else:
            c_i1 = ie   
        ch_i2 = choice(inv)
        if 0<=ch_i2<=3000 or 7000<=ch_i2<=9000:
            c_i2 = ipc
        elif 3000<ch_i2<=5000 or 5500<=ch_i2<7000 or 9000<ch_i2<=9800:
            c_i2 = ir
        elif 5000<ch_i2<=5450 or 9850<=ch_i2<=10000:
            c_i2 = itr
        else:
            c_i2 = ie           
        ch_i3 = choice(inv)
        if 0<=ch_i3<=3000 or 7000<=ch_i3<=9000:
            c_i3 = ipc
        elif 3000<ch_i3<=5000 or 5500<=ch_i3<7000 or 9000<ch_i3<=9800:
            c_i3 = ir
        elif 5000<ch_i3<=5450 or 9850<=ch_i3<=10000:
            c_i3 = itr
        embed=discord.Embed(title=f"{c_i1}" f"{c_i2}" f"{c_i3}" "-> !invocation", color=0xffffff)
    elif 9950<nb_da<=9980:
        exp = collection.find(user_id)
        for money in exp:
            cur_money = money["money"]
        new_money = cur_money + nb_mo_4
        collection.update_one({"_id": author_id}, {"$set":{"money":new_money}}, upsert=True)
        embed=discord.Embed(title="+" f"{nb_mo_4}" " 💰", color=0xffffff)
        await ctx.send(embed=embed)
    elif 9980<nb_da<=10000:
        g = choice(épique)
        embed=discord.Embed(title=g, color=0xc955d8)
        exp = collection.find(user_id)
        for te in exp:
            cur_te = te["te"]
        new_te = cur_te + 1
        collection.update_one({"_id": author_id}, {"$set":{"te":new_te}}, upsert=True)
        await ctx.send(embed=embed)
    exp = collection.find(user_id)
    for tl in exp:
        cur_tl = tl["tl"]
    exp = collection.find(user_id)
    for te in exp:
        cur_te = te["te"]
    exp = collection.find(user_id)
    for ttr in exp:
        cur_ttr = ttr["ttr"]
    exp = collection.find(user_id)
    for tr in exp:
        cur_tr = tr["tr"]
    exp = collection.find(user_id)
    for tpc in exp:
        cur_tpc = tpc["tpc"]
    exp = collection.find(user_id)
    for b2 in exp:
        cur_b2 = b2["b2"]
    if cur_b2 == 0:
        s=cur_tpc*1+cur_tr*15+cur_ttr*200+cur_te*1500+cur_tl*25000
        if 10000>s>=1000:
            embed=discord.Embed(color=0xd1d1d1)
            embed.add_field(name="New badge", value="⭐ 1,000pts", inline=False)
            await ctx.send(embed=embed)
            exp = collection.find(user_id)
            for b2 in exp:
                new_b2 = cur_b2 + 1
            collection.update_one({"_id": author_id}, {"$set":{"b2":new_b2}}, upsert=True)
        elif 100000>s>=10000:
            embed=discord.Embed(color=0xd1d1d1)
            embed.add_field(name="New badge", value="🌟 10,000pts", inline=False)
            await ctx.send(embed=embed)
            exp = collection.find(user_id)
            for b2 in exp:
                new_b2 = cur_b2 + 2
            collection.update_one({"_id": author_id}, {"$set":{"b2":new_b2}}, upsert=True)
        elif s>=100000:
            embed=discord.Embed(color=0xd1d1d1)
            embed.add_field(name="New badge", value="✨ 100,000pts", inline=False)
            await ctx.send(embed=embed)
            exp = collection.find(user_id)
            for b2 in exp:
                new_b2 = cur_b2 + 3
            collection.update_one({"_id": author_id}, {"$set":{"b2":new_b2}}, upsert=True)
    if cur_b2 == 1:
        s=cur_tpc*1+cur_tr*15+cur_ttr*200+cur_te*1500+cur_tl*25000
        if 100000>s>=10000:
            embed=discord.Embed(color=0xd1d1d1)
            embed.add_field(name="New badge", value="🌟 10,000pts", inline=False)
            await ctx.send(embed=embed)
            exp = collection.find(user_id)
            for b2 in exp:
                new_b2 = cur_b2 + 1
            collection.update_one({"_id": author_id}, {"$set":{"b2":new_b2}}, upsert=True)
        elif s>=100000:
            embed=discord.Embed(color=0xd1d1d1)
            embed.add_field(name="New badge", value="✨ 100,000pts", inline=False)
            await ctx.send(embed=embed)
            exp = collection.find(user_id)
            for b2 in exp:
                new_b2 = cur_b2 + 2
            collection.update_one({"_id": author_id}, {"$set":{"b2":new_b2}}, upsert=True)
    if cur_b2 == 2:
        s=cur_tpc*1+cur_tr*15+cur_ttr*200+cur_te*1500+cur_tl*25000
        if s>=100000:
            embed=discord.Embed(color=0xd1d1d1)
            embed.add_field(name="New badge", value="✨ 100,000pts", inline=False)
            await ctx.send(embed=embed)
            exp = collection.find(user_id)
            for b2 in exp:
                new_b2 = cur_b2 + 1
            collection.update_one({"_id": author_id}, {"$set":{"b2":new_b2}}, upsert=True)

@daily.error
async def command_daily_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        remaining_time = str(datetime.timedelta(seconds=int(error.retry_after)))
        embed = discord.Embed(title=f"Pas de ``daily`` disponible!",description=f"Try again in " + str(remaining_time), color=0x575757)
        await ctx.send(embed=embed)
   
#GIFT
@bot.command()
async def pack(ctx):
    global ope
    global opi
    global user_id
    global author_id
    global new_money
    a = choice(debut)
    b = choice(liste)
    c = choice(commun)
    d = choice(peucommun)
    e = choice(rare)
    f = choice(tresrare)
    g = choice(épique)
    h = choice(légendaire)
    author_id = ctx.author.id
    user_id = {"_id": author_id}
    if ope>=1:
        await ctx.send("All I want to say is...")
        nb = choice(rec)
        ope=ope-1
        if 0<=nb<=400:
            print("-> giftx3!")
            embed=discord.Embed(title="🎁 Gift x3 (fais vite la commande `!pack`)", color=0xffffff)
            await ctx.send(embed=embed)
            ope=ope+3
        elif 750<nb<=1750:
            print("-> giftx2!")
            embed=discord.Embed(title="🎁 Gift x2 ! (fais vite la commande `!pack`)", color=0xffffff)
            await ctx.send(embed=embed)
            ope=ope+2
        elif 500<nb<=750 or 1750<nb<=2500:
            print("-> gift!", nb)
            embed=discord.Embed(title="Sac d'or ! +10 💰", color=0xffffff)
            await ctx.send(embed=embed)
            nb_mo_1 = 10
            exp = collection.find(user_id)
            for money in exp:
               cur_money = money["money"]
               new_money = cur_money + nb_mo_1
            collection.update_one({"_id": author_id}, {"$set":{"money":new_money}}, upsert=True)
        elif 2500<nb<8400:
            print("gift : peu commun")
            embed=discord.Embed(title=d, color=0x5aa7ce)
            exp = collection.find(user_id)
            for tpc in exp:
                cur_tpc = tpc["tpc"]
                new_tpc = cur_tpc + 1
            collection.update_one({"_id": author_id}, {"$set":{"tpc":new_tpc}}, upsert=True)
            await ctx.send(embed=embed)
        elif 400<nb<=500 or 8400<=nb<=9825:
            print("gift : rare")
            embed=discord.Embed(title=e, color=0xf4911f)
            exp = collection.find(user_id)
            for tr in exp:
                cur_tr = tr["tr"]
                new_tr = cur_tr + 1
            collection.update_one({"_id": author_id}, {"$set":{"tr":new_tr}}, upsert=True)
            await ctx.send(embed=embed)
        elif 9825<nb<=9993:
            print("gift : très rare")
            embed=discord.Embed(title=f, color=0x35d070)
            exp = collection.find(user_id)
            for ttr in exp:
                cur_ttr = ttr["ttr"]
                new_ttr = cur_ttr + 1
            collection.update_one({"_id": author_id}, {"$set":{"ttr":new_ttr}}, upsert=True)
            await ctx.send(embed=embed)
        elif 9993<nb<10000:
            print(b, ": épique")
            embed=discord.Embed(title=g, color=0xc955d8)
            exp = collection.find(user_id)
            for te in exp:
                cur_te = te["te"]
                new_te = cur_te + 1
            collection.update_one({"_id": author_id}, {"$set":{"te":new_te}}, upsert=True)
            await ctx.send(embed=embed)
            await ctx.send("tag @Vic pour avoir ce message dans ta collection ! (épique)")
        elif nb==10000:
            print("-> giftx10!")
            embed=discord.Embed(title="🎁 Gift x10 ! (fais vite la commande `!pack`)", color=0xffffff)
            await ctx.send(embed=embed)
            ope=ope+10
    elif opi>=1:
        await ctx.send("Lucky...")
        nb = choice(rec)
        opi=opi-1
        if nb<5500:
            print("mega gift : très rare")
            embed=discord.Embed(title=f, color=0x35d070)
            exp = collection.find(user_id)
            for ttr in exp:
                cur_ttr = ttr["ttr"]
                new_ttr = cur_ttr + 1
            collection.update_one({"_id": author_id}, {"$set":{"ttr":new_ttr}}, upsert=True)
            await ctx.send(embed=embed)      
        elif 6000<nb<8000:
            print("-> giftx15!")
            embed=discord.Embed(title="🎁 Gift x10 ! (fais vite la commande `!pack`)", color=0xffffff)
            await ctx.send(embed=embed)
            ope=ope+15
        elif 5500<=nb<5800 or 8000<=nb<=9800:
            print("mega gift : épique")
            embed=discord.Embed(title=g, color=0xc955d8)
            exp = collection.find(user_id)
            for te in exp:
                cur_te = te["te"]
                new_te = cur_te + 1
            collection.update_one({"_id": author_id}, {"$set":{"te":new_te}}, upsert=True)
            await ctx.send(embed=embed)
            await ctx.send("tag @Vic pour avoir ce message dans ta collection ! épique)")
        elif 9800<nb<9900:
            print("mega gift : légendaire")
            embed=discord.Embed(title=h, color=0xfff829)
            exp = collection.find(user_id)
            for tl in exp:
                cur_tl = tl["tl"]
                new_tl = cur_tl + 1
            collection.update_one({"_id": author_id}, {"$set":{"tl":new_tl}}, upsert=True)
            await ctx.send(embed=embed)
            await ctx.send("tag @Vic pour avoir ce message dans ta collection ! (légendaire)")
        elif 9900<=nb<=10000 or 5800<=nb<=6000:
            print("-> giftx30!")
            embed=discord.Embed(title="🎁 Gift x30 ! (fais vite la commande `!pack`)", color=0xffffff)
            await ctx.send(embed=embed)
            ope=ope+30
    else:
        embed=discord.Embed(title="❌ There isn't any gift ❌", color=0x636363)
        await ctx.send(embed=embed)
    exp = collection.find(user_id)
    for tl in exp:
        cur_tl = tl["tl"]
    exp = collection.find(user_id)
    for te in exp:
        cur_te = te["te"]
    exp = collection.find(user_id)
    for ttr in exp:
        cur_ttr = ttr["ttr"]
    exp = collection.find(user_id)
    for tr in exp:
        cur_tr = tr["tr"]
    exp = collection.find(user_id)
    for tpc in exp:
        cur_tpc = tpc["tpc"]
    exp = collection.find(user_id)
    for b2 in exp:
        cur_b2 = b2["b2"]
    if cur_b2 == 0:
        s=cur_tpc*1+cur_tr*15+cur_ttr*200+cur_te*1500+cur_tl*25000
        if 10000>s>=1000:
            embed=discord.Embed(color=0xd1d1d1)
            embed.add_field(name="New badge", value="⭐ 1,000pts", inline=False)
            await ctx.send(embed=embed)
            exp = collection.find(user_id)
            for b2 in exp:
                new_b2 = cur_b2 + 1
            collection.update_one({"_id": author_id}, {"$set":{"b2":new_b2}}, upsert=True)
        elif 100000>s>=10000:
            embed=discord.Embed(color=0xd1d1d1)
            embed.add_field(name="New badge", value="🌟 10,000pts", inline=False)
            await ctx.send(embed=embed)
            exp = collection.find(user_id)
            for b2 in exp:
                new_b2 = cur_b2 + 2
            collection.update_one({"_id": author_id}, {"$set":{"b2":new_b2}}, upsert=True)
        elif s>=100000:
            embed=discord.Embed(color=0xd1d1d1)
            embed.add_field(name="New badge", value="✨ 100,000pts", inline=False)
            await ctx.send(embed=embed)
            exp = collection.find(user_id)
            for b2 in exp:
                new_b2 = cur_b2 + 3
            collection.update_one({"_id": author_id}, {"$set":{"b2":new_b2}}, upsert=True)
    if cur_b2 == 1:
        s=cur_tpc*1+cur_tr*15+cur_ttr*200+cur_te*1500+cur_tl*25000
        if 100000>s>=10000:
            embed=discord.Embed(color=0xd1d1d1)
            embed.add_field(name="New badge", value="🌟 10,000pts", inline=False)
            await ctx.send(embed=embed)
            exp = collection.find(user_id)
            for b2 in exp:
                new_b2 = cur_b2 + 1
            collection.update_one({"_id": author_id}, {"$set":{"b2":new_b2}}, upsert=True)
        elif s>=100000:
            embed=discord.Embed(color=0xd1d1d1)
            embed.add_field(name="New badge", value="✨ 100,000pts", inline=False)
            await ctx.send(embed=embed)
            exp = collection.find(user_id)
            for b2 in exp:
                new_b2 = cur_b2 + 2
            collection.update_one({"_id": author_id}, {"$set":{"b2":new_b2}}, upsert=True)
    if cur_b2 == 2:
        s=cur_tpc*1+cur_tr*15+cur_ttr*200+cur_te*1500+cur_tl*25000
        if s>=100000:
            embed=discord.Embed(color=0xd1d1d1)
            embed.add_field(name="New badge", value="✨ 100,000pts", inline=False)
            await ctx.send(embed=embed)
            exp = collection.find(user_id)
            for b2 in exp:
                new_b2 = cur_b2 + 1
            collection.update_one({"_id": author_id}, {"$set":{"b2":new_b2}}, upsert=True)







#H0W 
@bot.command()
async def h0w(ctx):
    embed=discord.Embed(title=" ━━━━━━━━━━━━━━━━━━━━━", color=0x636363)
    embed.set_author(name="C0MMANDS ⌨️")
    embed.add_field(name="!dr0p", value="Nécessite d'être membre du labo", inline=False)
    embed.add_field(name="!C0llecti0n", value="Pour voir votre collection des membres du labo", inline=False)
    embed.add_field(name="!sh0p", value="Nécessite de débloquer tous les membres du labo", inline=False)
    await ctx.send(embed=embed)
    
#DR0P
@bot.command()
@cooldown(1, 3600, BucketType.user)
async def dr0p(ctx):
   global user_id
   global author_id
   author_id = ctx.author.id
   user_id = {"_id": author_id} 
   exp = collection.find(user_id)
   for tl in exp:
        cur_tl = tl["tl"]
   if cur_tl >= 1:
      z = choice(liste0)
      if 743<=z<=747:
         print(z, ": Hououin Kyoumaaaa ``aka Mad Scientist``")
         embed=discord.Embed(title="Hououin Kyoumaaaa ``aka Mad Scientist``", color=0xfff829)
         await ctx.send(embed=embed, file=discord.File('Kyouma_Hououin.png'))
      elif 358<=z<=378:
         print(z, ": Makise Kurisu ``aka Christina``")
         embed=discord.Embed(title="Makise Kurisu ``aka Christina``", color=0xfff829)
         await ctx.send(embed=embed, file=discord.File('Kurisu_Makise.jpg'))
      elif 888<=z<=908:
         print(z, ": Okabe Rintaro ``aka Okarin``")
         embed=discord.Embed(title="Okabe Rintaro ``aka Okarin``", color=0xfff829)
         await ctx.send(embed=embed, file=discord.File('Rintarou_Okabe.jpg'))
      elif 220<=z<=270:
         print(z, ": Hashida Daru ``aka Supah Hakah``")
         embed=discord.Embed(title="Hashida Daru ``aka Supah Hakah``", color=0xfff829)
         await ctx.send(embed=embed, file=discord.File('Daru_Hashida.jpg'))
      elif 510<=z<=550:
         print(z, ": Shiina Mayuri ``aka Mayushii``")
         embed=discord.Embed(title="Shiina Mayuri ``aka Mayushii``", color=0xfff829)
         await ctx.send(embed=embed, file=discord.File('Mayuri_Shiina.jpg'))
      elif 150<=z<=200:
         print(z, ": Amane Suzuha ``aka Part-Time Warrior``")
         embed=discord.Embed(title="Amane Suzuha ``aka Part-Time Warrior``", color=0xfff829)
         await ctx.send(embed=embed, file=discord.File('Suzuha_Amane.jpg'))
      elif 25<=z<=75:
         print(z, ": Urushibara Luka ``aka Lukako``")
         embed=discord.Embed(title="Urushibara Luka ``aka Lukako``", color=0xfff829)
         await ctx.send(embed=embed, file=discord.File('Urushibara_Luka.jpg'))
      elif 855<=z<=905:
         print(z, ": Akiha Rumiho ``aka Faris NyanNyan``")
         embed=discord.Embed(title="Akiha Rumiho ``aka Faris NyanNyan``", color=0xfff829)
         await ctx.send(embed=embed, file=discord.File('Faris_NyanNyan.jpg'))
      else:
         embed=discord.Embed(title="Nothing here... Come back later...", color=0x8b8989)
         await ctx.send(embed=embed)
   else:
      embed=discord.Embed(title="❌ You aren't a member of the labo ! ❌", color=0x636363)
      await ctx.send(embed=embed)
@dr0p.error
async def command_dr0p_error(ctx, error):
   if isinstance(error, commands.CommandOnCooldown):
      global user_id
      global author_id
      global cur_tl
      author_id = ctx.author.id
      user_id = {"_id": author_id} 
      exp = collection.find(user_id)
      for tl in exp:
        cur_tl = tl["tl"]
      if cur_tl >= 1:
         remaining_time = str(datetime.timedelta(seconds=int(error.retry_after)))
         embed = discord.Embed(title=f"Pas de ``dr0p`` disponible!",description=f"Try again in " + str(remaining_time), color=0x575757)
         await ctx.send(embed=embed)
      else:
         embed=discord.Embed(title="❌ You aren't a member of the labo ! ❌", color=0x636363)
         await ctx.send(embed=embed) 

#C0LLECTI0N
@bot.command()
async def C0llecti0n(ctx):
    global user_id
    global author_id
    author_id = ctx.author.id
    user_id = {"_id": author_id} 
    name = await bot.fetch_user(author_id)
    embed=discord.Embed(title=" ━━━━━━━━━━━━━━━━━━━━━", color=0x636363)
    embed.set_author(name="C0LLECTI0N " f"{name}" " 🔬")
    embed.add_field(name="Lab Member 001", value="???????", inline=False)
    embed.add_field(name="Lab Member 002", value="???????", inline=False)
    embed.add_field(name="Lab Member 003", value="???????", inline=False)
    embed.add_field(name="Lab Member 004", value="???????", inline=False)
    embed.add_field(name="Lab Member 005", value="???????", inline=False)
    embed.add_field(name="Lab Member 006", value="???????", inline=False)
    embed.add_field(name="Lab Member 007", value="???????", inline=False)
    embed.add_field(name="Lab Member 008", value="???????", inline=False)
    await ctx.send(embed=embed)

bot.run(getenv('TOKEN'))
