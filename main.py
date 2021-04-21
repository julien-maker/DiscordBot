import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "/", description = "Bot De Rivox")

@bot.event
async def on_ready():
	print("Lancé")

bot.run("ODM0NDM0MjcyMTQ0MjYxMTQx.YIA1eQ.oNFrcqzC1A-5G7pIqZKuYzC5sBU")
