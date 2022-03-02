from discord.ext import commands

# -------------------- Cogs --------------------

class lockandhide(commands.Cog):
    def __init__(self, client):
        self.client = client

# -------------------- Launch --------------------

    @commands.Cog.listener()
    async def on_ready(self):
        print('Loaded Lock_Unlock Command')

# -------------------- Lock Command --------------------

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def lock(self, ctx):
        overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
        if overwrite.send_messages == False:
            await ctx.send("Channel is already locked")
        else:
            await ctx.channel.set_permissions(ctx.guild.default_role,send_messages=False)
            await ctx.send(f"{ctx.channel.mention} is now locked.")
            await ctx.channel.edit(topic="This channel is currently Locked!")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def hide(self, ctx):
        guild = self.client.get_guild(939078117362896906)
        role = guild.get_role(939081396352319500)
        await ctx.channel.set_permissions(role, view_channel=False)
        await ctx.channel.edit(topic="This channel is currently Hidden!")


# -------------------- Unlock Command --------------------

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def unlock(self, ctx):
        overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
        if overwrite.send_messages == True:
            await ctx.send("Channel is already unlocked")
        else:
            await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
            await ctx.send(f"{ctx.channel.mention} is now unlocked.")
            await ctx.channel.edit(topic="This channel is not locked!")
    
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unhide(self, ctx):
        guild = self.client.get_guild(939078117362896906)
        role = guild.get_role(939081396352319500)
        await ctx.channel.set_permissions(role, view_channel=True)
        await ctx.channel.edit(topic="This channel is currently Hidden!")

# -------------------- Cogs Setup --------------------

def setup(client):
    client.add_cog(lockandhide(client))
