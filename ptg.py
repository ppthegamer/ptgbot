import discord
import os
import discord.member
from discord.ext import commands
#from dotenv import load_dotenv

#load_dotenv()
intents =discord.Intents().default()
intents.members = True
client = commands.Bot(command_prefix='!',intents =intents)
token ='Njg3MTUwOTQ4NTUyMTQ2OTQ0.XmhlMA.3JZKobucntVJligumsO3u_0A8aQ'
bot_log = 756116165218009118

@client.event
async def on_ready():
		print('HGello logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
		if message.author == client.user:
			return
@client.event
async def on_member_join(member:discord.Member):

    role = discord.utils.get(member.guild.roles,id=796709135344992257)
    await member.add_roles(role)

client.run(token)	
