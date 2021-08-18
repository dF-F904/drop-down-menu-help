import discord
from discord import embeds
from discord.ext import commands
from discord.ext.commands import bot
from discord.gateway import DiscordClientWebSocketResponse

HELP_OPTIONS = [
        discord.SelectOption(label="Moderation", description="Auto moderation help", emoji="🛡️"),
        #discord.SelectOption(label="ChatBot", description="ChatBot help", emoji="🤖"),
        discord.SelectOption(label="Fun", description="Fun help", emoji="🎯"),
        #discord.SelectOption(label="Giveaway", description="Giveaway help", emoji="🎉"),
        #discord.SelectOption(label="Karma", description="Karma help", emoji="🎭"),
        #discord.SelectOption(label="Leveling", description="Leveling help", emoji=var.E_LEVELING),
        #discord.SelectOption(label="Moderation", description="Moderation help", emoji="🔨"),
        #discord.SelectOption(label="Reaction Roles", description="Reaction roles help", emoji="✨"),
        #discord.SelectOption(label="Verification", description="Member verification help", emoji="✅"),
        #discord.SelectOption(label="Welcome", description="Welcome greeting help", emoji="👋"),
        #discord.SelectOption(label="Extras", description="Extra commands help (not a plugin)", emoji="▶️"),
        #discord.SelectOption(label="Settings", description="Bot settings help (not a plugin)", emoji=var.E_SETTINGS)
    ]



async def moderation_embed(ctx: commands.Context):
    embed=discord.Embed(title="**Moderation Help** 🛡️", color=discord.Color.blurple())
    embed.set_author(name=ctx.author, icon_url=ctx.author.avatar.url)
    embed.add_field(name="Command: $warn", value="**Description:** Warn a member in the guild\n**Usage:** $warn [member] [reason]", inline=False)
    embed.add_field(name="Command: $mute", value="**Description:** Mute a member from the guild \n**Usage:** $mute [member] [optional reason]", inline=False)
    embed.add_field(name="Command: $ban", value="**Description:** Ban a member from the guild \n**Usage:** $ban [member] [optional reason]", inline=False)
    embed.add_field(name="Command: $unban", value="**Description:** Unban a user from the guild \n**Usage:** $unban [user ID] [optional reason]", inline=False)
    embed.add_field(name="Command: $modlogs", value="**Description:** View all warnings on a user in the guild\n**Usage:** $modlogs [member]", inline=False)

    return embed





class View(discord.ui.View):
    def __init__(self, ctx):
        self.ctx = ctx
        super().__init__(timeout=None)

    async def on_timeout(self):
        print("Timed out")
        
    async def interaction_check(self, interaction: discord.Interaction):
        if not interaction.user == self.ctx.author:
            await interaction.response.send_message("You can't select items in someone else's command!", ephemeral=True)
        return interaction.user == self.ctx.author
    
    @discord.ui.select(placeholder="Select a category!", options=HELP_OPTIONS)
    async def callback(self, select: discord.ui.select, interaction: discord.Interaction):
        help_type = interaction.data["values"][0]

        if help_type == "Moderation":
            await interaction.message.edit(embed=await moderation_embed(self.ctx))


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        help_embed = discord.Embed(title="Help | Commands", description=f"Use the dropdown menu below to get more help on a specfic command category", color=discord.Color.random()) 
        help_embed.add_field(name="**__Moderation__**", value=f"`warn` | `mute` | `ban` | `unban` | `modlogs`", inline=False)
        #help_embed.add_field(name="**__Self Roles__**", value=f"`android` | `asia` | `emulator` | `europe` | `ios` | `NA` | `SA`", inline=False)
        #help_embed.add_field(name="**__Fun__**", value=f"`av` |  `beg` | `buy` | `cat` | `coins` | `dadjoke` | `daily` | `dice` | `dog` | `eightball` `give` | `poll` | `rank` | `reminder` | `richest` | `rob` | `shop` | `slots` | `top` | `work`", inline=False) 
        #help_embed.add_field(name="**__Other__**", value=f"`activity` | `CRcolor` | `CRmove` | `CRname` | `join` | `pause` `play` | `resume` | `serverinfo`\n \n \n **__Support Website__** | [Click here](https://juicy-celestial-backpack.glitch.me/)", inline=False)
        help_embed.set_author(name=ctx.author, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=help_embed, view=View(ctx))




def setup(bot):
    bot.add_cog(Help(bot))
