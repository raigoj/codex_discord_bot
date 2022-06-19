import os
from dotenv import load_dotenv
from discord.ext import commands, tasks
from setup import *
from easyChallenge import *
# from hardChallenge import *

# global variables
easyChannelId = None
# hardChannelId = None

# client setup
load_dotenv()
token = os.getenv('TOKEN')
client = commands.Bot(command_prefix = "!")

# Connecting to the server
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

# Timer function to send new easy challange every day
@tasks.loop(hours=24)
async def startEasy():
    global easyChannelId
    message_channel = client.get_channel(easyChannelId)
    await easyChallenge(message_channel)

# Timer function to send new hard challange every day
# @tasks.loop(seconds=15)
# async def startHard():
#     global hardChannelId
#     message_channel = client.get_channel(hardChannelId)
#     await message_channel.send("hard")

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
        # if arg[0].lower() == "hard":
        #     hardChannelId = ctx.channel.id
        #     await startHard.start()
        if arg[0].lower() == "easy":
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
        msg = embedMsg("Easy challenges have been stopped")
        await ctx.send(embed=msg)
    # elif arg[0].lower() == "hard":
    #     startHard.cancel()
    #     msg = embedMsg("Hard challanges have been stopped")
    #     await ctx.send(embed=msg)
    else:
        msg = embedMsg("Invalid argument. Use \"!info stop\" for help")
        await ctx.send(embed=msg)


# Starts hard challenge
@client.command()
async def challenge(ctx):
    embed=discord.Embed(title="Challenge: Patterns search", description="You know the following facts regarding patterns.\n  >>Natural pulsing patterns of various life-forms can be written down as a sequence of ( and ).\n  >>A pattern is valid only if every starting ( has a closing ) which follows it. E.g. () and ()() are both valid patterns, whereas )(, ()) and ()( are all invalid.\n  >>A pattern can nest ( and ), so that (), ((())) and (()(())) would all be valid patterns.\n  >>For pulse swords and shields, the pattern stays valid for the entirety of its length, e.g. ()(())(())().\n  >>For life-forms, the pattern becomes invalid after a certain length, e.g. ()(())(())()))))((((.\n  >>The Pulsing Coefficient for any pulsing pattern is the length of valid pattern characters in such a sequence, starting from the beginning. E.g. the pulsing coefficient for the valid sequence () is 2, ()() is 4, and ((())) is 6, whilst the pulsing coefficient for the invalid sequence ())() is only 2, ())))))) is also 2, and for ((())))((((((( it is 6.\n\n  Count the number of right sequences.", color=0x9D00FF)
    await ctx.send(embed=embed)

    data=discord.Embed(title="DATA: Patterns search", description="()((()()))()()()((()(()())()))((((())))())()((())()(()())((((())))((())))()()(()()))(())((((()(())()(())(((())()(((())(())))(()())(()))(((()()))))(((((()))()()()((((())()())(()(()))(((())()(()))))(()(()((()()()(((())(()()())(()))())))((()(())(()))))(()((())(((()((()()))())))()()())()))(()()))(()())())))()(((()())(())()))))()))(())(())()()(())((()()())(()()((())))(((((())))((((((())()))))((()())((((()))(())(())())()))))(((()()((())()(()())((((((()()(()()()())())())(((()(()((())()((()()())()))))))))((())))))))((()((()()()(((((()(())))((()(((())(())((((((())))()))((())((())))()))()))))((()(((()(()())((())())((())(())))))())))((((())(((((()))))((())(())())((()())()(((()(())()((()))()(())()(()))))())(((((((()()())))))()()(()()())()()))(((())()))))())()))(((()))()(())))(())(((()()()(()(())(((()()))))))())((())(()))()(((((()(()())()))((((()()()(()((()))()((()())(()())(()))(()(()))(()()))(())(()())()())(()())()(()()())()(())()))((())((()()())))(())(()((((((())()()))))()()()(((((())()()()))((())()(()))))()))((((())())(())()())))()))()()(((()))())(((())()()))(()))))()()()(())()(((((()())())))))((())())(()()))()()))()()()()((())()(()))(()((((()))()((()()())())()()()()()(())))())(()())(())()()()(()((((()((()))))())))())))((())(((())(((()))()()((())((()()()))()(())((((()(((((())()())(()(()()))(()(()()((()()((())))((())((((((()((())))()()())))))(()))(()))((()())(())()()(())(())))))))(())()(()(((((())((()((((()))()(()()())())()()())((((()(()(()((((())()))(()(()))()((()(()(())))(())()()))())())()))))))))()((((((()))())(()(((())())(())(())(((())()((()))((())))())())(())()((()(((())(())))))((())(", color=0x9D00FF)
    await ctx.send(embed=data)

    await ctx.send(f"You have started the challenge called: Patterns search. Good luck!")

    await on_answerCheck(ctx)

"""Cheaks the answers until gets thr right one"""
async def on_answerCheck(ctx):
    while True:
        msg = await client.wait_for("message")

        if msg.content == "1226":
            await msg.add_reaction("✅")
            break
        else:
            await msg.add_reaction("❌")

# RUN FOREST RUN
client.run(token)