#Rogue Bot programmed and signed by Virgil (Tsukiumi, Littlep1) on 9/13/2018

import discord
import asyncio
import random
import requests
import youtube_dl
from discord import Game
from discord.ext import commands
from discord.ext.commands import Bot

TOKEN = "NDg5OTc3MDc2NzExOTQ4Mjk4.DnzY7w.qzw2dRmW3qpsEsPX6hscYIiWe6c"

client = Bot(command_prefix=".")

client.remove_command('help')

players = {}

@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author
    
    embed = discord.Embed(
        title = 'Help Menu',
        description = 'Displays a list of usable commands for the bot.',
        colour = discord.Colour.orange()
    )
    
    embed.set_author(name='List of usable commands')
    embed.add_field(name='.8ball', value='Answers yes or no questions.', inline=False)
    embed.add_field(name='.hello', value='Greet Rogue Bot!', inline=False)
    embed.add_field(name='.clear', value='Clear chats up to the number indicated.', inline=False)
    embed.add_field(name='.stop', value='Stops the bot.', inline=False)
    await client.send_message(author, embed=embed) 

# Clear messages    
@client.command(pass_context=True)
async def clear(ctx, amount=100):
    author = ctx.message.author
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount)):
        messages.append(message)
    if message.author.id == '237121186570567690' or '194428450038087680' or '284172718406893578' or '163018805361115136' or '252181713957027843' or '131474171443019776':
        await client.delete_messages(messages)
        await client.send_message(author, ctx.message.author.mention + ', message delete request processed successfully.')
    else:
        return

# 8ball
@client.command(name = '8ball',
                description = "Answers yes or no questions.",
                brief = "Let the magic 8ball decide your answer!",
                aliases=['eight_ball','eightball','8','8-ball'],
                pass_context=True)
async def eight_ball(context):
    possible_responses = [
        'Most definitely',
        'Not likely',
        'Not a chance',
        'Sure',
        'No',
        'Yes',
        'It is possible',
        ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)

# Auto sets user role
@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name = 'Rogue-ling [Trial]')
    await client.add_roles(member, role)


# Greets users that say hello to bot    
@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('.hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    await client.process_commands(message)
        
    
#Plays Music
@client.command(pass_context=True)
async def play(ctx, url):
    server=ctx.message.server
    voice_client=client.voice_client_in(server)
    channel=ctx.message.author.voice.voice_channel
    player=await voice_client.create_ytdl_player(url)
    players[server.id] = player
    await client.join_voice_channel(channel)
    player.start()


# Stops the bot
@client.event
async def on_message(message):
    if message.content == '.stop':
        # Super user id list
        if message.author.id == '237121186570567690' or '194428450038087680' or '284172718406893578' or '163018805361115136' or '252181713957027843' or '131474171443019776':
            await client.logout()
        else:
            return
    await client.process_commands(message)


# Prints startup status.        
@client.event
async def on_ready():
    await client.change_presence(game=Game(name="Type .help for help."))
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
