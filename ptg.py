import discord
import os
from discord.ext import commands
#from dotenv import load_dotenv

#load_dotenv()
client = commands.Bot(command_prefix='!')
clientA = discord.Client()
bot_log = 756116165218009118

@client.event
async def on_ready():
		print('We have logged in as {0.user}'.format(client))

@client.command(name='as')
async def ping(ctx):
		print("sdfsdf")
		await ctx.channel.send('ssfds')
@client.event
async def on_message(message):
		if message.author == client.user:
			return
@client.event
async def on_member_join(member,ctx):
		for channel in member.guild.channels:
			if str(channel)=="test":
				await ctx.channel.send(f"""**Welcome to the server** {member.mention}""") 
				

@client.event
async def on_member_remove(member,ctx):
		for channel in member.guild.channels:
			if str(channel)=="test":
				await ctx.channel.send(f"""{member.mention} **Left the Server**""")

@client.event
async def on_message_delete(message,ctx):
	
		#messDeleter = message.author
		embed = discord.Embed(title=f"""**{message.author}**""",color=0xf40000)
		#h = clientA.get_channel
		embed.add_field(name="Message deleted", value=""+message.content + " **was Deleted** "+f"""**by {message.author}**""", inline=False)
		#chann = message.guild.get_channel(bot_log)
		await ctx.channel.send(embed=embed)



client.run(os.environ['TOKEN'])	