import project_handling
import discord
import discord.ext
from discord.ext import commands

# Initializing the variables required for the bot

#current_project = Project()
projects = []
bot = commands.Bot(command_prefix='!')
client = discord.Client()
start = "Hey, I am here. What's up?"
new_project_info= "Alright, let's start a new project. \nGo ahead and give the new project a name!"


@bot.command(name="start")
async def start(ctx):
    """ Start function that uses the !start command to begin the bot within the server. """
    await ctx.send(start)

@bot.command(name="new")
async def new(ctx, *args):
    """ New Project function intializes a new project within the server. """
    await ctx.send(new_project_info)
    try:
        new_project_name = await bot.wait_for(
            "message", 
            timeout= 60, 
            check = lambda message : message.author == ctx.author 
                            and message.channel == ctx.channel
            )
        if new_project_name:
            await ctx.send("New Project Created: " + str(new_project_name.content))
    except TimeoutError:
        await ctx.send("You took too much time, try again!")  

with open("BOT_TOKEN.txt", "r") as token_file:
    TOKEN = token_file.read()
    print("Token file read")
    bot.run(TOKEN)

# @client.event
# async def on_message(message):
#     """ Function to handle the messages within the channel """
#     if message.author == client.user:
#         # if message.content == new_project:
#             # else:
#         return    
#    #if message.
#
# @bot.command(name = "current")
# async def current_project(ctx):
#     await ctx.send(projects[-1])
