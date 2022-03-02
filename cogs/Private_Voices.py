import discord
from discord.ext import commands

# -------------------- Cogs --------------------

file = open("Private_Voices.txt", 'r')
counter = int(file.readline().strip())
file.close()

class autoprv(commands.Cog):
    def __init__(self, client):
        self.client = client

# -------------------- Launch --------------------

    @commands.Cog.listener()
    async def on_ready(self):
        print('Loaded Private_Voices')

# -------------------- Temp Voice --------------------

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        global counter 
        guild = member.guild
        category = self.client.get_channel(939083438684799006)
        permoverwrite = {guild.default_role: discord.PermissionOverwrite(view_channel=True, connect=True), member:discord.PermissionOverwrite(view_channel=True, connect=True, move_members=True, manage_channels=True, mute_members=True, deafen_members=True, manage_permissions=True, use_voice_activation=True)}
        if after.channel:
            if after.channel.id == (939078117727825957):
                counter += 1
                file = open('Private_Voices.txt', 'w')
                print(counter, file=file)
                file.close()
                new_channel = await guild.create_voice_channel(name=f"➖〉Room #{counter}" , category=category, overwrites=permoverwrite)
                await member.move_to(new_channel)
        if before.channel:
            if len(before.channel.members) == 0 and before.channel.category.id == 939083438684799006 and before.channel.id != 939078117727825957:
                await before.channel.delete()
                
# -------------------- Cogs Setup --------------------

def setup(client):
    client.add_cog(autoprv(client))
