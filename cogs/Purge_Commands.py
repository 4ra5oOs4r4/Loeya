import time
import discord
from discord.ext import commands

# -------------------- Cogs --------------------

class purge(commands.Cog):
    def __init__(self, client):
        self.client = client

# -------------------- Launch --------------------

    @commands.Cog.listener()
    async def on_ready(self):
        print('Loaded Purge_Commands')

# -------------------- Clear Command --------------------

    @commands.command(aliases=['purge'])
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, amount : int):
        await ctx.send(f'**Cleaning** __**{amount}**__ **messages in the channel, Raise your feet!**')
        time.sleep(2)
        await ctx.channel.purge(limit=amount + 2)

# -------------------- ClearAll Command --------------------

    @commands.command(aliases=['purgeall'])
    @commands.has_permissions(administrator=True)
    async def clearall(self, ctx):
        await ctx.channel.purge()


# -------------------- Cogs Setup --------------------

def setup(client):
    client.add_cog(purge(client))
