import discord
from discord.ext import commands
import random,os

intents = discord.Intents.default()
intents.message_content=True

bot=commands.Bot(command_prefix='$',intents=intents)

@bot.event
async def on_ready():
    print('bot telah siap')

@bot.command()
async def sampahlagi(ctx):
    img_name=random.choice(os.lisdir('kerajinan'))
    with open(f'kerajinan/{img_name}','rb') as gambar:
        picture=discord.File(gambar)
    await ctx.send(picture)
bot.run('MTExMDU1NzgxNjY3NjE3NTg3Mg.GhgZFr.ocR_OinAVayNIH8sNNV_WY2p9r11Zjq-ApcDAk')