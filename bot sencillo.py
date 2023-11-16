import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)
client = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')
    
@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)
@bot.command()
async def ayuda(ctx):
    comandos= f'$hello: El bot te da un saludo \n$joined + tu nombre de usario: Recibe la fecha y hora esacta a la que ingresaste por primera vez al servidor \n$repeat + el numero que quieres que se repita tu mensaje + el mensaje: Usa solo este comando en canales especialemente hechos para el spam \n$ayuda: ¡Usa este comando para revisar que otros comandos tiene el servidor!'
    await ctx.send(comandos)
bot.run("COLOCA TU TOKEN")
