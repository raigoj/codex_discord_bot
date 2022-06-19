from main import client
import discord

"""Starts the challenge"""
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
