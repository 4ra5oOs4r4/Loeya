
import datetime
import time
import discord
from discord.ext import commands

# -------------------- Cogs --------------------

class wlcandbye(commands.Cog):
    def __init__(self, client):
        self.client = client

# -------------------- Launch --------------------

    @commands.Cog.listener()
    async def on_ready(self):
        print('Loaded Welcomer')

# -------------------- Welcome DM --------------------   

    @commands.Cog.listener()
    async def on_member_join(self, member : discord.Member):
        channel = self.client.get_channel(939078117400649792)
        datetime = time.strftime('[%Y/%b/%d - %X %p]')
        embed = discord.Embed(color=discord.Colour.green())
        await channel.send(f'🎉 *{member}*  **Has joined the server!** 🎉')
        await member.edit(nick=f"[NEW]・{member.display_name}")

        embed.set_author(name="FallingSkull EZ💀NFT", url="https://discord.gg/xyyzsgaFR8")
        embed.add_field(name=f"👋 Greetings:", value=f"Welcome **{member}**", inline=False)
        embed.add_field(name="✅ Verify: ", value="First of all, Verify in [#✅〉verification](https://canary.discord.com/channels/939078117362896906/939078117400649789/939088851656380416)")
        embed.add_field(name="🎉 Giveaways:", value=f"Participate in [#🎉・giveaways](https://discord.com/channels/939078117362896906/939098590528299008/944989990230831197)", inline=False)
        embed.add_field(name="🎁 Invite Rewards:", value=f"Check out [#🎁・invite-rewards](https://canary.discord.com/channels/939078117362896906/939098605237710869/944848943676805130)", inline=False)
        embed.add_field(name="🆔 Member ID:", value=f"{member.id}", inline=False) 
        embed.set_footer(text=f"You joined in {datetime}")
        try:
            await member.send(embed=embed)
            print(f"Sent To {member}")
        except:
            print(f"Couldnt Send To {member}")

# -------------------- Goodbye Message --------------------

    @commands.Cog.listener()
    async def on_member_remove(self, member : discord.Member):
        channel = self.client.get_channel(939098347845845012)
        date = datetime.datetime.now().strftime('[%Y-%b-%d]')
        await channel.send(f'*{member}*  **Has left the server!** *{date}*')

# -------------------- Cogs Setup --------------------

def setup(client):
    client.add_cog(wlcandbye(client))

# -------------------- Comment --------------------   
