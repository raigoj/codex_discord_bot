import os
from dotenv import load_dotenv
from discord.ext import commands, tasks
from setup import *
from easyChallenge import *

# global variables
easyChannelId = None
hardChannelId = None

# client setup
load_dotenv()
token = os.getenv('TOKEN')
client = commands.Bot(command_prefix = "!")

# Connecting to the server
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

# Timer function to send new easy challange every day
@tasks.loop(seconds=15)
async def startEasy():
    global easyChannelId
    message_channel = client.get_channel(easyChannelId)
    await easyChallenge(message_channel)

# Timer function to send new hard challange every day
@tasks.loop(seconds=15)
async def startHard():
    global hardChannelId
    message_channel = client.get_channel(hardChannelId)
    await message_channel.send("hard")

# Info command -> Print text with all avaliable commands
@client.command()
async def info(ctx, *arg):
    helpContent = await infoHandler(*arg)
    await ctx.send(embed=helpContent)

# Start the challange
@client.command()
async def start(ctx, *arg):
    global hardChannelId
    global easyChannelId
    if (len(arg) < 1):
        easyChannelId = ctx.channel.id
        await startEasy.start()
    else:
        if arg[0].lower() == "hard":
            hardChannelId = ctx.channel.id
            await startHard.start()
        elif arg[0].lower() == "easy":
            easyChannelId = ctx.channel.id
            await startEasy.start()
        else:
            error = embedMsg("Invalid argument. Use \"!info start\" for help")
            await ctx.send(embed=error)

# Stop challange
@client.command()
async def stop(ctx, *arg):
    if arg[0].lower() == "easy":
        startEasy.cancel()
        msg = embedMsg("Easy challanges have been stopped")
        await ctx.send(embed=msg)
    elif arg[0].lower() == "hard":
        startHard.cancel()
        msg = embedMsg("Hard challanges have been stopped")
        await ctx.send(embed=msg)
    else:
        msg = embedMsg("Invalid argument. Use \"!info stop\" for help")
        await ctx.send(embed=msg)


# RUN FOREST RUN
client.run(token)