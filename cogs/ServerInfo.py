import time
import random
import datetime
import discord
from discord.ext import commands, tasks
from datetime import datetime

# -------------------- Cogs --------------------

class server(commands.Cog):
    def __init__(self, client):
        self.client = client

# -------------------- Launch --------------------

    @commands.Cog.listener()
    async def on_ready(self):
        print('Loaded Server Info')

# -------------------- Server Command --------------------

    @commands.command(alias=["info"])
    async def server(self, ctx):
        id = ctx.message.guild.id
        guildcreated = ctx.guild.created_at.strftime('[%Y/%b/%d - %X %p]')
        embed=discord.Embed(color=discord.Colour.random())
        embed.set_author(name=ctx.guild.name, url="https://discord.gg/stn69", icon_url=ctx.guild.icon_url)
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.add_field(name="🆔 Server ID:", value=id, inline=False) 
        embed.add_field(name=f"👥 Members:", value=f"{ctx.message.guild.member_count}", inline=False)
        embed.add_field(name="☄️ Boosts:", value=ctx.guild.premium_subscription_count, inline=False)
        embed.add_field(name="📅 Creation Date:", value=f"{guildcreated}", inline=False)
        embed.add_field(name="👑 Server Owner:", value=f"{ctx.guild.owner}", inline=False)
        embed.set_footer(text="Bot is made by: SamTheNoob#8698")
        if ctx.guild.premium_subscription_count == 0:
            ctx.guild.premium_subscription_count = 0
        await ctx.send(embed=embed)

# -------------------- Cogs Setup --------------------

def setup(client):
    client.add_cog(server(client))

# -------------------- Comment --------------------   
