from project_handling import Project
import discord.ext
from discord.ext import commands
from discord.ext.commands import MemberConverter
import asyncio
from enum import Enum

# Initializing the variables required for the bot

projects = []
bot = commands.Bot(command_prefix='!')

@bot.command(name="start")
async def start_bot(ctx):
    """ Start function that uses the !start command to begin the bot within the server. """
    await ctx.send("Hey, I am here. What's up?")

@bot.command(name="new")
async def new_project(ctx):
    """ New Project function intializes a new project within the server. """
    await ctx.send("Alright, let's start a new project. \nGo ahead and give the new project a name!")
    new_project_name = await input(ctx)
    if new_project_name:
        await ctx.send("New Project Created: " + new_project_name.content)
        #await asyncio.sleep(3)
        await ctx.send("The project needs a manager, doesn't it? Appoint one!")
        project_manager = await input(ctx)
        if project_manager:
            await ctx.send(project_manager.content + " has been appointed as the project manager for " + new_project_name.content)   
            #await asyncio.sleep(3)
            await ctx.send("The project needs some members. Just tag the members you would like to add!")
            members = await input(ctx)
            if members:
                await ctx.send(members.content + " has been appointed as the members for the project: " + new_project_name.content)   
                #await asyncio.sleep(3)
                await ctx.send("Finally, let's attach a priority tag to the project! Choose from high, medium, or low.")
                priority_tag = await input(ctx)
                if priority_tag:
                    await ctx.send(new_project_name.content + "project has been appointed " + (str(priority_tag.content)).upper() + " priority tag.")   
                    #await asyncio.sleep(3)
                    await ctx.send("The project has been created!")
            

    new_project = Project(name = new_project_name.content, project_manager= project_manager.content, members = members.content, priority_tag=str(priority_tag).upper())
    projects.append(new_project)
@bot.command(name = "project_list")
async def get_project_list(ctx):
    """ Function to get the project list for a particular server"""

    embed=discord.Embed(title="Project List", description = "Here's the list of projects going on:")
    for i in range(len(projects)):
        temp_project = projects[i]
        embed.add_field(name = str(temp_project.get_name), value= str(temp_project.get_project_manager), inline= True)
    await ctx.send(embed=embed)

# @bot.command(name = "add_manager")
# async def add_project_manager(ctx):
#     """Function that adds a manager to an already existing project"""
#     await ctx.send("Please choose a project from the following list to add a manager to:")
#     get_project_list(ctx)
#     try:
#         project = await bot.wait_for("message", timeout=60, 
#                         check= lambda message : message.author == ctx.author 
#                         and message.channel == ctx.channel #lambda function 
#                                 #to make sure that the message received is by the author within the same channel
#         )

async def input(ctx):
    try:
        input_message = await bot.wait_for(
                "message", 
                timeout= 60, #the timeout period for the input
                check = lambda message : message.author == ctx.author 
                                and message.channel == ctx.channel #lambda function to make sure that the message received is by the author within the same channel
                )
        return input_message 
    except TimeoutError:
        await ctx.send("Looks like you took too much time to respond. Try again!")

with open("BOT_TOKEN.txt", "r") as token_file:
    TOKEN = token_file.read()
    print("Token file read")
    bot.run(TOKEN)