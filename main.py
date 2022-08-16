from discord.ext import commands

bot = commands.Bot(command_prefix='!')
TOKEN = 'MTAwOTIxMTUxNTE1NDQ2ODkwNA.GMeAkN.LVCcqdOOTHT_S_aYXgQ5CcjrMSYbzdEbLlZJAw'
cogs_to_add = [
    'cogs.events_watch_cog',
    'cogs.start_deal_cog',
    'cogs.get_fees_cog',
    'cogs.help_cog'
]

if __name__ == "__main__":
    for cog in cogs_to_add:
        print(f'Loading : {cog}')
        bot.load_extension(cog)

bot.run(TOKEN)