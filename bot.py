from project_handling import Project
import discord.ext
from discord.ext import commands
from discord.ext.commands import MemberConverter
import asyncio

# Initializing the variables required for the bot

priority_tag_list = ['HIGH', 'LOW', 'MEDIUM']
projects = []
bot = commands.Bot(command_prefix='!')

@bot.command(name="hello")
async def start_bot(ctx):
    """ Start function that uses the !start command to begin the bot within the server. """
    await ctx.send("Hey, I am here. What's up?")

@bot.command(name="new_project")
async def new_project_func(ctx):
    """ New Project function intializes a new project within the server. """
    await ctx.send("Alright, let's start a new project. \nGo ahead and give the new project a name!")
    new_project_name = await input(ctx)
    if new_project_name:
        await ctx.send("New Project Created: " + new_project_name.content)
        await asyncio.sleep(0.5)
        await ctx.send("The project needs a manager, doesn't it? Appoint one!")
        project_manager = await input(ctx)
        if project_manager:
            await ctx.send(project_manager.content + " has been appointed as the project manager for " + new_project_name.content)   
            await asyncio.sleep(0.5)
            await ctx.send("The project needs some members. Just tag the members you would like to add!")
            members = await input(ctx)
            if members:
                await ctx.send(members.content + " has been appointed as the members for the project: " + new_project_name.content)   
                await asyncio.sleep(0.5)
                await ctx.send("Finally, let's attach a priority tag to the project! Choose from high, medium, or low.")
                priority_tag = await input(ctx)
                if priority_tag:
                    if (priority_tag.content).upper() in priority_tag_list:
                        await ctx.send(new_project_name.content + "project has been appointed " + (str(priority_tag.content)).upper() + " priority tag.")
                        await asyncio.sleep(0.5)
                        await ctx.send("The project has been created!")
                    else:
                        await ctx.send("Now, I'm just a bot but that doesn't look like a priority tag to me. Let's try again?")
                        await new_project_func(ctx)    

    new_project_function = Project(name = new_project_name, project_manager= project_manager, members = members, priority_tag=str(priority_tag).upper())
    projects.append(new_project_function)
    await ctx.guild.create_text_channel(new_project_name.content)
@bot.command(name = "project_list")
async def get_project_list(ctx):
    """ Function to get the project list for a particular server"""

    embed=discord.Embed(title="Project List", description = "Here's the list of projects going on:")
    embed.insert_field_at(index = 2, name = "Project Name: ", value = "Project Manager: ", inline = True)
    for i in range(len(projects)):
        temp_project = projects[i]
        name = temp_project.get_name().content
        value = temp_project.get_project_manager().content
        
        embed.add_field(name = name, value = value, inline= True, )
    await ctx.send(embed=embed)

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