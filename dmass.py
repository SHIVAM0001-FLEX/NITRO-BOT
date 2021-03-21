import discord
from discord.ext import commands
import platform
import random
import time


bot = commands.Bot(command_prefix='+', case_insensitive=True)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}(ID: +{bot.user.id}) |'
          f'Connected to {str(len(bot.guilds))} servers |'
          f'Connected to {str(len(set(bot.get_all_members())))} users')
    print('--------')
    print('CREATED AND HOSTED BY INVADER OP | Fixed Version')


@bot.event
async def on_command_error(ctx, error):
    # Ignore these errors:
    ignored = (
        commands.CommandNotFound, commands.UserInputError, commands.BotMissingPermissions, commands.MissingPermissions, discord.errors.Forbidden, commands.CommandInvokeError, commands.MissingRequiredArgument)
    if isinstance(error, ignored):
        return


@bot.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def userinfo(ctx, user: discord.Member):
    try:
        embed = discord.Embed(title="{}'s info".format(user.name),
                              description="Here's what I could find.",
                              color=discord.Colour.dark_red())

        embed.add_field(name="Name", value=user.name, inline=True)
        embed.add_field(name="ID", value=user.id, inline=True)
        embed.add_field(name="Status", value=user.status, inline=True)
        embed.add_field(name="Highest role", value=user.top_role)
        embed.add_field(name="Joined", value=user.joined_at)
        embed.set_thumbnail(url=user.avatar_url)

        await ctx.send(embed=embed)
    except:
        await ctx.send("Missing Requrired Args")


@commands.has_permissions(administrator=True)
@bot.command(pass_context=True)
async def send(ctx, *, content: str):
    for member in ctx.guild.members:
        c = await member.create_dm()
        try:
            await c.send(content)
            await ctx.send("Message Sent to Targets")
        except:
            await ctx.send("DM can't send to : {} :x: ".format(member))


bot.run("YOUR BOT'S TOKEN HERE")