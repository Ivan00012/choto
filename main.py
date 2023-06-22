import keyboard
import discord
import asyncio
import mouse
import time
from discord.ext import commands
from art import tprint


async def auto_enchant(sleep_kb, sleep_ms):
    # Вывод в консоль информации
    print(magenta + f'{n}Цикл работает\n',
          blue + "Основные значения"'\033[34;49;1m' + ":\n", sep='')
    print(blue_bold + f'auto_enchant(sleep_kb = {sleep_kb}, sleep_ms = {sleep_ms})\n',
          blue_bold + f'Зачаровано кирок - {str(enchanted_pickaxes)}\n',
          blue_bold + f'Потрачено ∼∼ {str(enchanted_pickaxes * 9000)}$\n', sep='')
    # Авто зачаровывание

    # await asyncio.sleep(3.3)
    # # sleep_kb = 0.7
    # # sleep_ms = 0.2
    # mouse.move(-16, 10, absolute=False, duration=0.1)
    # await asyncio.sleep(sleep_ms)
    # mouse.click(button='right')
    # await asyncio.sleep(sleep_ms)
    # kb.press_and_release('1')
    # await asyncio.sleep(sleep_kb)
    # kb.press_and_release('e')
    # await asyncio.sleep(sleep_kb)
    # mouse.move(16, 0, absolute=False, duration=0.1)
    # await asyncio.sleep(sleep_ms)
    # mouse.click(button='right')
    # await asyncio.sleep(sleep_ms)
    # kb.press_and_release('2')
    # await asyncio.sleep(sleep_kb)
    # kb.press_and_release('e')
    # await asyncio.sleep(sleep_kb)
    # mouse.move(16, 0, absolute=False, duration=0.1)
    # await asyncio.sleep(sleep_ms)
    # mouse.click(button='right')
    # await asyncio.sleep(sleep_ms)
    # kb.press_and_release('3')
    # await asyncio.sleep(sleep_kb)
    # kb.press_and_release('e')
    # await asyncio.sleep(sleep_kb)
    # kb.press_and_release('1')
    # await asyncio.sleep(sleep_kb)
    # mouse.move(-12, 100, absolute=False, duration=0.1)
    # await asyncio.sleep(sleep_ms)
    # mouse.click(button='right')
    # await asyncio.sleep(sleep_ms)
    # kb.press_and_release('9')
    # await asyncio.sleep(sleep_kb)
    # mouse.move(0, -40, absolute=False, duration=0.1)
    # await asyncio.sleep(sleep_ms)
    # mouse.click(button='right')
    # await asyncio.sleep(sleep_ms)
    # mouse.move(-260, -100, absolute=False, duration=0.1)
    # await asyncio.sleep(sleep_ms)
    # kb.press_and_release('3')
    # await asyncio.sleep(sleep_kb)
    # mouse.move(100, 0, absolute=False, duration=0.1)
    # await asyncio.sleep(sleep_ms)
    # kb.press_and_release('2')
    # await asyncio.sleep(sleep_kb)
    # mouse.move(80, 10, absolute=False, duration=0.1)
    # await asyncio.sleep(sleep_ms)
    # mouse.click(button='left')
    # await asyncio.sleep(sleep_kb)
    # mouse.move(-180, -10, absolute=False, duration=0.1)
    # await asyncio.sleep(sleep_ms)
    # kb.press_and_release('3')
    # await asyncio.sleep(sleep_kb)
    # kb.press_and_release('esc')
    # await asyncio.sleep(sleep_kb)
    # mouse.move(100, 0, absolute=False, duration=0.1)
    # await asyncio.sleep(sleep_ms)
    # kb.press_and_release('3')
    # await asyncio.sleep(sleep_kb)
    # kb.press_and_release('q')
    # await asyncio.sleep(sleep_kb)
    # kb.press_and_release('/')
    # await asyncio.sleep(sleep_kb)
    # kb.write('home pve')
    # await asyncio.sleep(sleep_kb)
    # kb.press_and_release('enter')


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

work_while = False
work_channel = None
enchanted_pickaxes = 0
n = '\n' * 11

# Цвета текста
blue = '\033[34;49m'
blue_bold = '\033[34;49;1m'
magenta = '\033[35;49m'


@bot.event
async def on_ready():
    global work_channel
    work_channel = bot.get_channel(1121099578947670176)
    tprint("BOT  WORK !")


@bot.command()
async def start_enchant(ctx):
    if ctx.author.name == 'sam_ivan':
        await ctx.send('Запускаю цикл')
        print('Цикл запущен')
        global work_while, enchanted_pickaxes
        work_while = True

        while work_while:
            enchanted_pickaxes += 1
            await work_channel.send(f'> \n Цикл работает\nЗачаровано кирок-{str(enchanted_pickaxes)}\n')
            await auto_enchant(0.7, 0.2)
            await asyncio.sleep(1)

    else:
        await ctx.send('Снегур, у тебя не достаточно прав!')


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
        await ctx.send('Снегур, у тебя не достаточно прав!')


bot.run('myTOKENO')
