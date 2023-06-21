import discord
from discord.ext import commands
import asyncio
import time

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
WorkWhile = False
time_of_work = 0

my_channel = None


@bot.event
async def on_ready():
    global my_channel
    my_channel = bot.get_channel(1121099578947670176)
    print("BOT WORK!!!")


@bot.command()
async def ee(ctx):
    await my_channel.send('Текст сообщения')


@bot.command()
async def q(ctx):
    await ctx.send('Запускаю цикл')
    global WorkWhile, time_of_work
    WorkWhile = True
    while WorkWhile:
        await my_channel.send('Цикл работает- ' + str(time_of_work) + ' секунд')
        time_of_work += 1
        await asyncio.sleep(1)


@bot.command()
async def w(ctx):
    await ctx.send("Цикл закончил работу")
    print(w)
    global WorkWhile
    WorkWhile = False


bot.run('MTVfs')
