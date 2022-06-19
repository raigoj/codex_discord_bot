from typing import Counter
import discord
from discord.ui import Button, View
from discord.ext import commands
# import random

q1 = {
    "q": "Which heading tag in html is the biggest?",
    "C": "<h1>",
    "w1": "<h5>",
    "w2": "<h3>",
    "w3": "<h6>"
}
q2 = {
    "q": "Which html tag defines a single line break?",
    "w1": "<dl>",
    "w2": "<rb>",
    "C": "<br>",
    "w3": "<ld>"
}
q3 = {
    "q": "Which html tag defines style information for a document?",
    "w1": "<script>",
    "C": "<style>",
    "w2": "<st>",
    "w3": "<s>"
}
q4 = {
    "q": "Which html tag defines a title for the document?",
    "C": "<title>",
    "w1": "<t>",
    "w2": "<tl>",
    "w3": "<!DOCTYPE>"
}
question = [q1, q2, q3, q4]
ezQuestionCounter = 0

# class Buttons(discord.ui.View):
#     global question
#     global ezQuestionCounter
#     # awnser = random.shuffle([question["C"], question["w1"], question["w2"], question["w3"]])
#     def __init__(self, *, timeout=180):
#         super().__init__(timeout=timeout)
#     @discord.ui.button(label=question[ezQuestionCounter]["C"],style=discord.ButtonStyle.grey) #awnser[1]
#     async def blurple_button(self,button:discord.ui.Button,interaction:discord.Interaction):
#         button.disabled=True
#         await interaction.response.send_message("Congratulations! \n Your awnser was correct!")
#     @discord.ui.button(label=question[ezQuestionCounter]["w1"],style=discord.ButtonStyle.grey) 
#     async def gray_button(self,button:discord.ui.Button,interaction:discord.Interaction):
#         button.disabled=True
#         await interaction.response.send_message("Sorry, wrong awnser!")
#     @discord.ui.button(label=question[ezQuestionCounter]["w2"],style=discord.ButtonStyle.grey)
#     async def green_button(self,button:discord.ui.Button,interaction:discord.Interaction):
#         button.disabled=True
#         await interaction.response.send_message("Sorry, wrong awnser!")
#     @discord.ui.button(label=question[ezQuestionCounter]["w3"],style=discord.ButtonStyle.grey) 
#     async def red_button(self,button:discord.ui.Button,interaction:discord.Interaction):
#         await interaction.response.send_message("Sorry, wrong awnser!")

async def easyChallenge(ctx):
    global question
    global ezQuestionCounter
    # view=Buttons()
    # awnser = random.shuffle([question["C"], question["w1"], question["w2"], question["w3"]])
    button1 = Button(label=question[ezQuestionCounter]["C"],style=discord.ButtonStyle.grey)
    button2 = Button(label=question[ezQuestionCounter]["w1"],style=discord.ButtonStyle.grey)
    button3 = Button(label=question[ezQuestionCounter]["w2"],style=discord.ButtonStyle.grey)
    button4 = Button(label=question[ezQuestionCounter]["w3"],style=discord.ButtonStyle.grey)

    async def correctAnws(interaction):
        await interaction.response.send_message("Congratulations!\nCorrect anwser!")
    async def wrongAnws(interaction): 
        await interaction.response.send_message("Sorry!\nWrong anwser!")
    button1.callback = correctAnws
    button2.callback = wrongAnws
    button3.callback = wrongAnws
    button4.callback = wrongAnws

    view = View()
    view.add_item(button1)
    view.add_item(button2)
    view.add_item(button3) 
    view.add_item(button4)
    # async def button_callback(interaction):
    #     await interaction.response.send_message("Congratulations! /n Your awnser was correct!")
    
    # Buttons.button.callback = button_callback
    # async def interaction_check(self, interaction) -> bool:
    #     if interaction.user != self.ctx.author:
    #         await interaction.response.send_message("You can't use that!", ephemeral=True)
    #         return False
    #     else:
    #         return True
    embed=discord.Embed(
        title=question[ezQuestionCounter]["q"],
        color=discord.Color.purple()
        
    )
    embed.add_field(name="filler", value="filler", inline=True)
    await ctx.send(embed=embed,view=view)
    ezQuestionCounter += 1