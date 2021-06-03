from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.command(name="start", )
async def idea(ctx):
    await ctx.send("Alright, let's start a new project!")

with open("BOT_TOKEN.txt", "r") as token_file:
    TOKEN = token_file.read()
    print("Token file read")
    bot.run(TOKEN)