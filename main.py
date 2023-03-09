import os
import discord
import random

from time import sleep

import discord.utils

from flask import Flask, ctx
from threading import Thread

app = Flask('')

TOKEN = os.environ['BotKey']

@app.route('/')
def main():
  return "Jombot is awake :)"


def run():
  app.run(host="0.0.0.0", port=8000)


def keep_alive():
  server = Thread(target=run)
  server.start()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$help'):
    await message.channel.send('''my current commands are as follows:
      - hi/hello
      - gamer time?
      - $pets
      - $motivate
      - $ds3 build
      and some secret ones you'll need to find yourself.
      they also need to be typed quote precicely as discord.py won't let me concatonate :\.
      that is it but i am doing my best.
      ''')

  if message.content.startswith('hi') or message.content.startswith(
      'Hi') or message.content.startswith(
        "hello") or message.content.startswith("Hello"):
    await message.channel.send('Hello ' + message.author.name)

  if message.content.startswith('$motivate'):

    quoteList = open('quotes.txt', 'r')

    quotes = quoteList.readlines()

    quoteSelector = random.randint(0, 16)

    selectedQuote = quotes[quoteSelector]

    await message.channel.send(f'{selectedQuote} :)')

    quoteList.close()

  if message.content.startswith('$pets'):
    await message.channel.send(':D thanks.')
    await message.channel.send(file=discord.File('pet_the_jombot.gif'))

  if message.content.startswith('balls'):
    await message.channel.send('>:(')

  if message.content.startswith('yippee') or message.content.startswith(
      'Yippee'):
    await message.channel.send('https://tenor.com/view/yipee-meme-gif-25350387'
                               )

  if message.content.startswith('can we get much higher'):
    await message.channel.send('so high')

  if message.content.startswith('gamer time?'):
    await message.channel.send('gamer time >:)')
    gifSelector = random.randint(0, 4)

    gifs = [
      'https://tenor.com/view/dante-devil-may-cry-guitar-guitar-hero-dmc-gif-19980655',
      'https://tenor.com/view/gaming-twitch-emote-bttv-gif-18722020',
      'https://tenor.com/view/halo-hello-chat-gif-master-chief-hello-chat-hello-chat-meme-gif-25650006',
      'https://tenor.com/view/minecraft-frog-minecraft-frog-frogs-minecraft-frogs-gif-24147692',
      'https://tenor.com/view/get-on-hypixel-hypixel-flex-spongebob-gif-19211609'
    ]

    await message.channel.send(gifs[gifSelector])

  if message.content.startswith('goodnight') or message.content.startswith(
      'nosdda'):
    await message.channel.send('nighty night :).')

  if message.content.startswith('fuck you jombot') or message.content.startswith('Fuck u JomBot'):
        await message.channel.send('rude >:(')

  if message.content.startswith('$ds3 build'):
    builds = [
      "dex", "mage", "dex/faith", "paladin", "quality (str/dex)", "strength",
      "pyromancer", "sellsword twinblade >:)"
    ]
    buildSelector = random.randint(0, 7)

    await message.channel.send(
      f"play dark souls 3 with a {builds[buildSelector]} build")
    
keep_alive()

client.run(TOKEN)
