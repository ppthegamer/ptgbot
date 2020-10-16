import discord

client = discord.Client()
bot_log = 756116165218009118
@client.event
async def on_ready():
		print('We have logged in as {0.user}'.format(client))
@client.event
async def on_message(message):
		if message.author == client.user:
			return
@client.event
async def on_member_join(member):
		for channel in member.guild.channels:
			if str(channel)=="test":
				await channel.send(f"""**Welcome to the server** {member.mention}""") 

@client.event
async def on_member_remove(member):
		for channel in member.guild.channels:
			if str(channel)=="test":
				await channel.send(f"""{member.mention} **Left the Server**""")

@client.event
async def on_message_delete(message):
		#messDeleter = message.author
		embed = discord.Embed(title=f"""**{message.author}**""",color=0xf40000)
		embed.add_field(name="Message deleted", value=""+message.content + " **was Deleted** "+f"""**by {message.author}**""", inline=False)
		chann = message.guild.get_channel(bot_log)
		await chann.send(embed=embed)
client.run('Njg3MTUwOTQ4NTUyMTQ2OTQ0.XmhlMA.3JZKobucntVJligumsO3u_0A8aQ')
