import disnake
from disnake.ext import commands

intents = disnake.Intents.default()
intents.message_content = True 
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'йоу бот запущен - {bot.user}')



# Запускаем бота с токеном
bot.run('YOUR_BOT_TOKEN_HERE')
