import time
import discord
from discord.ext import commands

# -------------------- Cogs --------------------

class verify(commands.Cog):
    def __init__(self, client):
        self.client = client

# -------------------- Launch --------------------

    @commands.Cog.listener()
    async def on_ready(self):
        print('Loaded Verifier')

# -------------------- Account Checker --------------------   

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.client.get_channel(939087473760436264)
        if time.time() - member.created_at.timestamp() < 1209600:
            await channel.send(f"{member}'s account is **younger** than 14 days! >> ({round(time.time() - member.created_at.timestamp()) // 86400} Days!)")  
        else:
            await channel.send(f"{member}'s account is *older* than 14 days! >> ({round(time.time() - member.created_at.timestamp()) // 86400} Days!)")                

# -------------------- Cogs Setup --------------------

def setup(client):
    client.add_cog(verify(client))

# -------------------- Comment --------------------   
