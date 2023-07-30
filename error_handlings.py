from discord.ext import commands
#if someone didnt mention someone
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'**Evarinanna Mention chey ra** {ctx.author.mention}')
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send('**That is currently unavailable. Try another action!**')