import discord
import sys
import requests
import string
import random
import colorama
import os
import collections
import datetime
from datetime import date, time
import math
import asyncio
from discord.ext import commands
from discord.ext import tasks
import random
from json import load
from colorama import init, Fore
init()

with open("config.json") as f:
    config = load(f)
    prefix = config["prefix"]
    token = config["token"]
    GuildName = config["GuildName"]
    ChannelName = config["channelname"]
    Status = config["Status"]

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix=prefix, intents=intents, self_bot=True, fetch_offline_members=False)
aspire_version = "1.0"
client.remove_command("help")

@client.event
async def on_ready():
    os.system(f"clear")
    print(Fore.CYAN + ".▄▄ · ▄▄▄▄▄      ▄▄▄  • ▌ ▄ ·. ")
    print(Fore.CYAN + "▐█ ▀. •██  ▪     ▀▄ █··██ ▐███▪")
    print(Fore.BLUE + "▄▀▀▀█▄ ▐█.▪ ▄█▀▄ ▐▀▀▄ ▐█ ▌▐▌▐█·")
    print(Fore.BLUE + "▐█▄▪▐█ ▐█▌·▐█▌.▐▌▐█•█▌██ ██▌▐█▌")
    print(Fore.BLUE + " ▀▀▀▀  ▀▀▀  ▀█▄▀▪.▀  ▀▀▀  █▪▀▀▀")
    print()
    print()
    print(Fore.CYAN + "╔══════════════════════════════╗")
    print(f"  Welcome: {client.user.name}               ")
    print(f"  Prefix: {prefix}                    ")
    print(f"  ID: {client.user.id}       ")
    print(f"  Discord Version: {discord.__version__}       ")
    print(f"  {Fore.BLUE}Storm Version: 0.2.4")
    print("╚══════════════════════════════╝")
    print(Fore.GREEN + "╔══════════════════════════════╗")
    print("║           Console            ║")
    print("╚══════════════════════════════╝")

@client.command()
async def botping(ctx):
    print(f"|  [COMMAND >>>> Bot Ping]  [USER >>>> {client.user.name}]  |")
    await ctx.message.delete()
    await ctx.send(f"Storm Selfbot Ping Is {round(client.latency*1000)}ms.")

@client.command()
async def help(ctx):
    print(f"|  [COMMAND >>>> Help]  [USER >>>> {client.user.name}]  |")
    await ctx.message.delete()
    embed = discord.Embed(title="Storm Commands")
    embed.add_field(name="Fun Commands", value="Dog, Cat, Cute, Cum, Hug, Kiss, 8ball, Slots, Massreact", inline=False)
    embed.add_field(name="Spam Commands", value="Spam, Espam, Numspam, Hentaispam, Stopspam", inline=False)
    embed.add_field(name="Activity Commands", value="Listening, Watching, Streaming, Playing, Stopactivity", inline=False)
    embed.add_field(name="Nuke Commands", value="Nuke, Massrole, Channelcreate, Banall", inline=False)
    embed.add_field(name="Troll Commands", value="Fnitro, Fclassic", inline=False)
    embed.add_field(name="NSFW Commands", value="Boobs, Hentai", inline=False)
    embed.add_field(name="Info", value="Botping, Uptime, Contact, Donate, Info, Aspire", inline=False)
    embed.add_field(name="Tools", value="Ip, Ping, Av, Whois", inline=False)
    embed.set_footer(text=f"Your prefix is {prefix}", icon_url = "https://cdn.discordapp.com/attachments/902428786627330079/902473971570704414/11-117755_remove-muzzle-flash-cod-s-gaming-logo-png.png")
    embed.set_image(url="https://cdn.discordapp.com/attachments/897696343215198210/902020797256826941/20211024_222810.gif")
    await ctx.send(embed=embed)

@client.command()
async def vixx(ctx):
    print(f"|  [Secret >>>> vixx]  [USER >>>> {client.user.name}]  |")
    await ctx.message.delete()
    vixx = discord.Embed(title="Vixx is poggers")
    await ctx.send(embed=vixx)

@client.command()
async def ip(ctx, ip: str=None):
    print(f"|  [COMMAND >>>> IP]  [USER >>>> {client.user.name}]  |")
    await ctx.message.delete()
    if ip is None: await ctx.send("Please include an IP address");return
    else:
        try:
            with requests.session() as ses:
                resp = ses.get(f'https://ipinfo.io/{ip}/json')
                if "Wrong ip" in resp.text:
                    await ctx.send("Invalid IP address")
                    return
                else:
                    try:
                        j = resp.json()
                        embed= discord.Embed(title="IP Info")
                        embed.add_field(name=f'IP', value=f'{ip}', inline=True)
                        embed.add_field(name=f'City', value=f'{j["city"]}', inline=True)
                        embed.add_field(name=f'Region', value=f'{j["region"]}', inline=True)
                        embed.add_field(name=f'Country', value=f'{j["country"]}', inline=True)
                        embed.add_field(name=f'Coordinates', value=f'{j["loc"]}', inline=True)
                        embed.add_field(name=f'Postal', value=f'{j["postal"]}', inline=True)
                        embed.add_field(name=f'Timezone', value=f'{j["timezone"]}', inline=True)
                        embed.add_field(name=f'Organization', value=f'{j["org"]}', inline=True)
                        embed.set_footer(text=" made by 0x72")
                        await ctx.send(embed=embed)
                    except discord.HTTPException:
                        await ctx.send(f'**{ip} Info**\n\nCity: {j["city"]}\nRegion: {j["region"]}\nCountry: {j["country"]}\nCoordinates: {j["loc"]}\nPostal: {j["postal"]}\nTimezone: {j["timezone"]}\nOrganization: {j["org"]}')
        except Exception as e:
            await ctx.send(f"Error: {e}")

@client.command()
async def boobs(ctx):
    print(f"|  [COMMAND >>>> Boobs]  [USER >>>> {client.user.name}]  |")
    await ctx.message.delete()
    api = requests.get("https://nekos.life/api/v2/img/boobs")
    json = api.json()
    msg = discord.Embed(description=" Down Bad ")
    msg.set_image(url=json['url'])
    await ctx.send(embed=msg)

@client.command()
async def hentai(ctx):
    print(f"|  [COMMAND >>>> Hentai]  [USER >>>> {client.user.name}]  |")
    await ctx.message.delete()
    api = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif")
    json = api.json()
    msg = discord.Embed(description=" Hentai is good for the soul ")
    msg.set_image(url=json['url'])
    await ctx.send(embed=msg)

@client.command()
async def spam(ctx, amount:int=None,*,message:str=None):
    print(f"|  [COMMAND >>>> Spam {message} {amount}]  [USER >>>> {client.user.name}]  |")
    await ctx.message.delete()
    for each in range (0, amount):
        await ctx.send(f"{message}")

@client.command()
async def espam(ctx, amount:int=None):
    print(f"|  [COMMAND >>>> Espam {amount}]  [USER >>>> {client.user.name}]  |")
    await ctx.message.delete()
    for each in range (0, amount):
        await ctx.send("@everyone")

@client.command()
async def numspam(ctx, amount:int=None):
    print(f"|  [COMMAND >>>> Number Spam {amount}]  [USER >>>> {client.user.name}]  |")
    await ctx.message.delete()
    for each in range (0, amount):
        await ctx.send("1010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010")


@client.command()
async def contact(ctx):
    print(f"|  [COMMAND >>>> Contact]  [USER >>>> {client.user.name}]  |")
    await ctx.message.delete()
    emb = discord.Embed(title="Contact")
    emb.add_field(name="Dev Contact", value="Instagram: @shady.ily", inline=False)
    emb.set_footer(text=f"Your prefix is {prefix}", icon_url = "https://cdn.discordapp.com/attachments/902428786627330079/902473971570704414/11-117755_remove-muzzle-flash-cod-s-gaming-logo-png.png")
    await ctx.send(embed=emb)

@client.command()
async def info(ctx):
    print(f"|  [COMMAND >>>> Info]  [USER >>>> {client.user.name}]  |")
    await ctx.message.delete()
    em = discord.Embed(title="Storm Info")
    em.add_field(name="Storm Version:", value="0.1.0", inline=True)
    em.add_field(name="Discord Version:", value=f"{discord.__version__}", inline=True)
    em.add_field(name="Logged in as:", value=f"{client.user.name} ({client.user.id})", inline=True)
    em.set_footer(text=f"Your prefix is {prefix}", icon_url = "https://cdn.discordapp.com/attachments/902428786627330079/902473971570704414/11-117755_remove-muzzle-flash-cod-s-gaming-logo-png.png")
    await ctx.send(embed=em)

@tasks.loop(seconds=.5)
async def ImageSpam(ctx):
    api = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif")
    json = api.json()
    embed = discord.Embed()
    embed.set_image(url=json["url"])
    await ctx.send(embed=embed)


@client.command()
async def hentaispam(ctx):
    print(f"|  [COMMAND >>>> Hentai Spam]  [USER >>>> {client.user.name}]  |")
    await ctx.message.delete()
    ImageSpam.start(ctx)

@client.command()
async def stopspam(ctx):
    print(f"|  [COMMAND >>>> Stopspam]  [USER >>>> {client.user.name}]  |")
    await ctx.message.delete()
    ImageSpam.stop()

@client.command()
async def backfriend(ctx):
    print(f"|  [COMMAND >>>> Backfriend]  [USER >>>> {client.user.name}]  |")
    print(f"[BACKUP] {client.user.friends}")
    await ctx.message.delete()
    embed = discord.Embed(title="Backup")
    embed.add_field(name="Friends Backup", value="Friends Successfully Backed Up", inline=False)
    embed.set_footer(text=f"Your prefix is {prefix}", icon_url = "https://cdn.discordapp.com/attachments/902428786627330079/902473971570704414/11-117755_remove-muzzle-flash-cod-s-gaming-logo-png.png")
    await ctx.send(embed=embed)

# Fake Nitro #
@client.command()
async def fnitro(ctx, *, user: discord.Member = None):
    print(f"|  [COMMAND >>>> Fake Nitro]  [USER >>>> {client.user.name}]  |")
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    embed = discord.Embed(title=f"Nitro", url="https://discordgift.site/bnXnA5ZSAix7eRyZ",
                          description=f"Expires in 48 hours", color=0xcb82d0)
    embed.set_thumbnail(url='https://discordgift.site/nitro.png')
    embed.set_author(name=f"A WILD GIFT APPEARS!")
    await ctx.send(embed=embed)

# Fake Nitro Classic #
@client.command()
async def fclassic(ctx, *, user: discord.Member = None):
    print(f"|  [COMMAND >>>> Fake Classic Nitro]  [USER >>>> {client.user.name}]  |")
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    embed = discord.Embed(title=f"Nitro Classic", url="https://discordgift.site/bnXnA5ZSAix7eRyZ",
                          description=f"Expires in 48 hours", color=0x92a7e6)
    embed.set_thumbnail(url='https://discordgift.site/classic.png')
    embed.set_author(name=f"A WILD GIFT APPEARS!")
    await ctx.send(embed=embed)

@client.command()
async def donate(ctx):
    print(f"|  [COMMAND >>>> Donate]  [USER >>>> {client.user.name}]  |")
    await ctx.message.delete()
    embed = discord.Embed(title="Show Support")
    embed.add_field(name="Cashapp:", value="$RootSkimask", inline=True)
    embed.set_footer(text=f"Your prefix is {prefix}")
    await ctx.send(embed=embed)

@client.command()
async def whois(ctx, *, user: discord.Member = None):
    print(f"|  [COMMAND >>>> Who Is]  [USER >>>> {client.user.name}]  |")
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    if isinstance(ctx.message.channel, discord.Guild):
        date_format = "%a, %d %b %Y %I:%M %p"
        em = discord.Embed(description=user.mention)
        em.set_author(name=str(user), icon_url=user.avatar_url)
        em.set_thumbnail(url=user.avatar_url)
        em.add_field(name="Registered", value=user.created_at.strftime(date_format))
        em.add_field(name="Joined", value=user.joined_at.strftime(date_format))
        members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
        em.add_field(name="Join position", value=str(members.index(user) + 1))
        if len(user.roles) > 1:
            role_string = ' '.join([r.mention for r in user.roles][1:])
            em.add_field(name="Roles [{}]".format(len(user.roles) - 1), value=role_string, inline=False)
        perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
        em.add_field(name="Permissions", value=perm_string, inline=False)
        em.set_footer(text='ID: ' + str(user.id))
        return await ctx.send(embed=em)
    else:
        date_format = "%a, %d %b %Y %I:%M %p"
        em = discord.Embed(description=user.mention)
        em.set_author(name=str(user), icon_url=user.avatar_url)
        em.set_thumbnail(url=user.avatar_url)
        em.add_field(name="Created", value=user.created_at.strftime(date_format))
        em.set_footer(text='ID: ' + str(user.id))
        return await ctx.send(embed=em)

@client.command(aliases=['slots', 'bet', "slotmachine"])
async def slot(ctx):
    print(f"|  [COMMAND >>>> Slots]  [USER >>>> {client.user.name}]  |")
    await ctx.message.delete()
    emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
    a = random.choice(emojis)
    b = random.choice(emojis)
    c = random.choice(emojis)
    slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"
    if a == b == c:
        await ctx.send(embed=discord.Embed.from_dict(
            {"title": "Slot machine", "description": f"{slotmachine} All matchings, you won!"}))
    elif (a == b) or (a == c) or (b == c):
        await ctx.send(embed=discord.Embed.from_dict(
            {"title": "Slot machine", "description": f"{slotmachine} 2 in a row, you won!"}))
    else:
        await ctx.send(embed=discord.Embed.from_dict(
            {"title": "Slot machine", "description": f"{slotmachine} No match, you lost"}))

@client.command(aliases=["rekt", "rape"])
async def nuke(ctx):
    print(f"|  [COMMAND >>>> Nuke]  [USER >>>> {client.user.name}]  |")
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.ban()
            print("[NUKE] Users Banned")
        except:
            pass
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
            print("[NUKE] Channels Deleted")
        except:
            pass
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
            print("[NUKE] Roles Deleted")
        except:
            pass
    try:
        await ctx.guild.edit(
            name=RandString(),
            description="STORM SELFBOT",
            reason="STORM SELFBOT",
            icon=None,
            banner=None
        )
    except:
        pass
    for _i in range(250):
        await ctx.guild.create_text_channel(name=f"NUKED BY {client.user.name}")
        print("[NUKE] Channels Created")

@client.command(aliases=["stopstreaming", "stopstatus", "stoplistening", "stopplaying", "stopwatching"])
async def stopactivity(ctx):
    print(f"|  [COMMAND >>>> Stop Activity]  [USER >>>> {client.user.name}]  |")
    await ctx.message.delete()
    await client.change_presence(activity=None, status=discord.Status.dnd)

@client.command(aliases=["watch"])
async def watching(ctx, *, message):
    await ctx.message.delete()
    await client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=message
        ))

@client.command(aliases=["listen"])
async def listening(ctx, *, message):
    await ctx.message.delete()
    await client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening,
            name=message,
        ))

@client.command(alises=["game"])
async def playing(ctx, *, message):
    await ctx.message.delete()
    game = discord.Game(
        name=message
    )
    await client.change_presence(activity=game)

@client.command(aliases=["streaming"])
async def stream(ctx, *, message):
    await ctx.message.delete()
    stream = discord.Streaming(
        name=message,
        url="https://twitch.com/LulzStorm",
    )
    await client.change_presence(activity=stream)



client.run(token, bot=False)
