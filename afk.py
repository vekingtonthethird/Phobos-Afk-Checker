import discord, os, random, json
from discord.ext import commands
import colorama
from colorama import init, Fore, Back, Style


client = commands.Bot(command_prefix='$', case_insensitive=True, self_bot=True)
client.remove_command("help")

os.system('title PHOBOS AFK CHECKER')
token = input(f'[{Fore.MAGENTA}>{Fore.WHITE}] Token: ')
os.system('title PHOBOS AFK CHECKER')
os.system('cls')
AfkPrefix = input(f'[{Fore.MAGENTA}>{Fore.WHITE}] Your Prefix to start the checker: ')
os.system('title PHOBOS AFK CHECKER')
os.system('cls')
StartAfk = int(input(f'[{Fore.MAGENTA}>{Fore.WHITE}] Number you want the start the checker: '))
os.system('title PHOBOS AFK CHECKER')
os.system('cls')
EndAfk = int(input(f'[{Fore.MAGENTA}>{Fore.WHITE}] Number you want the finish the checker: '))
os.system('title PHOBOS AFK CHECKER')
os.system('cls')

os.system('title PHOBOS AFK CHECKER')
@client.event
async def on_ready():
  print(f""" \u001B[35m
 ██▓███   ██░ ██  ▒█████   ▄▄▄▄    ▒█████    ██████ 
▓██░  ██▒▓██░ ██▒▒██▒  ██▒▓█████▄ ▒██▒  ██▒▒██    ▒ 
▓██░ ██▓▒▒██▀▀██░▒██░  ██▒▒██▒ ▄██▒██░  ██▒░ ▓██▄   
▒██▄█▓▒ ▒░▓█ ░██ ▒██   ██░▒██░█▀  ▒██   ██░  ▒   ██▒
▒██▒ ░  ░░▓█▒░██▓░ ████▓▒░░▓█  ▀█▓░ ████▓▒░▒██████▒▒
▒▓▒░ ░  ░ ▒ ░░▒░▒░ ▒░▒░▒░ ░▒▓███▀▒░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░
░▒ ░      ▒ ░▒░ ░  ░ ▒ ▒░ ▒░▒   ░   ░ ▒ ▒░ ░ ░▒  ░ ░
░░        ░  ░░ ░░ ░ ░ ▒   ░    ░ ░ ░ ░ ▒  ░  ░  ░  
          ░  ░  ░    ░ ░   ░          ░ ░        ░  
                                ░                  

══════════════════════════╦══════════════════════════
                          ║
            ╔═════════════╩═════════════╗
            ║                           ║
  ╔═════════╩═══════════╗   ╔═══════════╩═════════╗
  ║     made by vek     ║   ║  vek runs you lol   ║
  ╚═════════════════════╝   ╚═════════════════════╝

Btw to activate the checker, do "{AfkPrefix} @user"

""")

 
@client.event
async def on_message(message):
    channel = message.channel
    if message.content.startswith(AfkPrefix):
      for i in range(StartAfk, EndAfk):
        await message.channel.send(i)

client.run(token, bot=False)