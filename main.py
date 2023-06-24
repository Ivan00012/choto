import discord
import asyncio
from discord.ext import commands
from pypresence import Presence
from art import tprint
from config import *
from time import *


async def auto_enchant(sleep_kb, sleep_ms):
    # Вывод в консоль информации
    print(magenta + '\n' * 11 + 'Цикл работает\n',
          blue + "Основные значения"'\033[34;49;1m' + ":\n", sep='')
    print(blue_bold + f'auto_enchant(sleep_kb = {sleep_kb}, sleep_ms = {sleep_ms})\n',
          blue_bold + f'Зачаровано кирок - {str(enchanted_pickaxes)}\n',
          blue_bold + f'Потрачено ∼∼ {str(enchanted_pickaxes * 9000)}$\n', sep='')
    p(sleep_kb, sleep_ms)


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

work_while = False
work_channel = None
enchanted_pickaxes = 0

# Цвета текста
blue = '\033[34;49m'
blue_bold = '\033[34;49;1m'
magenta = '\033[35;49m'


@bot.event
async def on_ready():
    global work_channel
    work_channel = bot.get_channel(1121099578947670176)
    await bot.change_presence(activity=discord.Game(name="WORK"))
    tprint("BOT  WORK !")


@bot.command()
async def start_enchant(ctx):
    if ctx.author.name == 'sam_ivan':
        global work_while, enchanted_pickaxes
        if not work_while:
            await ctx.send('Запускаю цикл')
            print('Цикл запущен')
            work_while = True

            while work_while:
                enchanted_pickaxes += 1
                await work_channel.send(f'> \n Цикл работает\nЗачаровано кирок-{str(enchanted_pickaxes)}\n')
                await auto_enchant(0.7, 0.2)
                await asyncio.sleep(1)

        elif work_while:
            await ctx.send('Цикл был ранее запущен')

        else:
            await ctx.send("Как?")

    else:
        await ctx.send('Снегур, у тебя недостаточно прав!')


@bot.command()
async def stop_enchant(ctx):
    if ctx.author.name == 'sam_ivan':
        global work_while

        if not work_while:
            await ctx.send("Ошибка, цикл был ранее :skull_crossbones: **...**")

        elif work_while:
            work_while = False
            await ctx.send("Цикл :skull_crossbones: **...**")
            print('Цикл закончил работу')

        else:
            await ctx.send("КАК???")

    else:
        await ctx.send('Снегур, у тебя недостаточно прав!')

# RPC = Presence("1121024552655409213")
#
# btns = [
#     {
#         "label": "Botik",
#         "url": "https://bot.com"
#     }
# ]
#
# RPC.connect()
# RPC.update(
#     details="qweqwe",
#     state="123?",
#     start=time(),
#     buttons=btns,
#     large_image='qwer',
#     small_image='qwer',
#     large_text="Тут могла бы быть ваша реклама"
# )

bot.run(token)
