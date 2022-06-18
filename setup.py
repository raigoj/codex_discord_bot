import discord

async def infoHandler(*arg):
    if len(arg) > 0:
        match arg[0]:
            case 'start':
                embed=discord.Embed(
                    title="How to use !start",
                    color=discord.Color.purple()
                )
                embed.add_field(name="!start", value="Starts easy challanges by default", inline=False)
                embed.add_field(name="!start easy", value="Starts easy challanges", inline=False)
                embed.add_field(name="!start hard", value="Starts hard challanges", inline=False)
                return embed
            case 'stop':
                embed=discord.Embed(
                    title="How to use !stop",
                    color=discord.Color.purple()
                )
                embed.add_field(name="!stop easy", value="Stops easy challanges", inline=False)
                embed.add_field(name="!stop hard", value="Stops hard challanges", inline=False)
                return embed

    else:
        embed=discord.Embed(
            title="Available commands",
            color=discord.Color.purple()
        )
        embed.add_field(name="Print Info", value="!info", inline=False)
        embed.add_field(name="Start Challange", value="!start <difficulty>", inline=False)
        embed.add_field(name="Stop Challange", value="!stop <difficulty>", inline=False)
        embed.add_field(name="Print Info About A Command", value="!info <command>", inline=False)
        return embed

def embedMsg(str):
    embed=discord.Embed(
        title=str,
        color=discord.Color.purple()
    )
    return embed