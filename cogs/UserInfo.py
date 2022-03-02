import datetime
import random
import discord
from discord.ext import commands
from datetime import datetime

# -------------------- Cogs --------------------

class userinfo(commands.Cog):
    def __init__(self, client):
        self.client = client

# -------------------- Launch --------------------

    @commands.Cog.listener()
    async def on_ready(self):
        print('Loaded User Info')


# -------------------- User Command --------------------

    @commands.command(alias=["userinfo"])
    async def user(self, ctx, member : discord.Member=None):

        if member ==  None:
            member = ctx.message.author
            
        userid = member.id
        date = member.created_at.strftime('[%Y/%b/%d - %X %p]')
        joindate = member.joined_at.strftime('[%Y/%b/%d - %X %p]')
        pfp = member.avatar_url  

        embed=discord.Embed(color=discord.Colour.random())
        embed.set_author(name=f"{member}'s Info")
        embed.set_thumbnail(url=pfp)
        embed.add_field(name="🆔 User's ID:", value=userid, inline=False) 
        embed.add_field(name="📅 User's Creation Date:", value=date, inline=False)
        embed.add_field(name="👑 User's Server Join Date:", value=joindate, inline=False)
        embed.set_footer(text="Bot is created by: SamTheNoob#8698")
        await ctx.send(embed=embed)

# -------------------- Cogs Setup --------------------

def setup(client):
    client.add_cog(userinfo(client))

# -------------------- Comment --------------------   
