import discord
import os
from discord.ext import commands
#from dotenv import load_dotenv

#load_dotenv()
client = commands.Bot(command_prefix='!')
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
async def on_member_join(member,ctx):
    	print('Member Joined')
    	role = discord.utils.get(member.server.roles,name='Members')
	await client.add_roles(member,role)

client.run(token)	
