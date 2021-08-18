import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.members = True
intents.presences = True

bot = commands.Bot(command_prefix=commands.when_mentioned_or("$"), intents=intents, case_insensitive=True, help_command=None)


@bot.event
async def on_ready():
    print(f"{bot.user} is ready!")
    
  
### not really any other commands needed here, still a project in beta.



for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')


bot.run('token')
