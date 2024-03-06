import discord
from discord.ext import commands
from time import sleep

intents = discord.Intents.default()

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    channel = bot.get_channel(1214997049397874768)
    while True:
        await channel.send('<@&1208863657203601408>')
        sleep(0.5)


bot.run('token')