from discord.ext.commands.core import command
import datetime
import os
import discord
from itertools import cycle
from discord.ext import commands, tasks
from TOKEN import token_id
import random
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
client = commands.Bot(command_prefix='?', case_insensitive=True, intents = discord.Intents.all())
status = cycle(['ArasoOsara', 'Kids Die Inside'])
activity = cycle([discord.ActivityType.listening, discord.ActivityType.watching])

def is_it_me(ctx):
    return ctx.author.id == 938826491653918831

@client.event
async def on_ready():
    guild = client.get_guild(939078117362896906)
    change_status.start()
    print(f"{client.user.name} is now online.")
    guild = client.get_guild(939078117362896906)
    for invalid_guilds in list(filter(lambda x: x.name.title().startswith('➖〉Room #'), guild.voice_channels)):
        if len(invalid_guilds.members) == 0:
            await invalid_guilds.delete()
        else:
            pass
@client.event
async def on_message(message):
    RESPONSES = ["Don't mention me!", "Stop mentioning me!", "I won't repeat it, DON'T MENTION ME!!!", "Can you not mention my name?", "I already have a passport, STOP MENTIONING MY NAME!!!", "STFU before I fuck you up, AND DON'T EVER CALL MY NAME AGAIN!"]
    CHARACTERS =["Stop spamming characters kid...", "Don't spam characters.", "Can you not?"]
    ASKED = ["I asked.", "Your Mom?", "Dogs don't ask, They listen.", "Excuse me? I DID!", f"?ban {message.author.mention} ???", "Don't need permission...", "If you didn't ask, Then why are you listening?", "Who said you were apart of the conversation?!", "You just asked who asked...", "Your lost dad", "100% Not your dad.", "It's not a Q&A."]
    for word in message.content.split(" "):
        temp_l=""
        i=0
        max_i = 5
        for l in word:
            if i >= max_i:
                return await message.reply(f'{random.choice(CHARACTERS)}')
            if l == temp_l:
                i += 1
            temp_l = l
    print(fuzz.ratio("who asked", message.content))
    if message.author.bot:
        return
    if fuzz.ratio("who asked", message.content) in range(50, 101) or fuzz.ratio("WHO ASKED", message.content) in range(50, 101):
        await message.reply(f'{random.choice(ASKED)}')
        
    await client.process_commands(message)
    if "WhoAsked" in message.content or "Who Asked" in message.content:
        await message.reply(f'{random.choice(ASKED)}')
    if client.user in message.mentions or "Loeya" in message.content:
        await message.reply(f'{random.choice(RESPONSES)}')
        
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! I response in {round(client.latency * 1000, 2)} milliseconds!')
    
@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Activity(type=(next(activity)), name=(next(status))))

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(token_id)
