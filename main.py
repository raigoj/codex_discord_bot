import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
# client = discord.Bot()
token = os.getenv('TOKEN')
client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.command()
async def say(ctx, arg):
    embed=discord.Embed(
        title="You said:",
        color=discord.Color.blurple()
    )
    embed.add_field(name=arg, value=" ", inline=True)
    await ctx.send(embed=embed)


client.run(token)