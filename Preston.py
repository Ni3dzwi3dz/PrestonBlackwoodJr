# -*- coding: utf-8 -*-

# Preston Blackwood Jr
#
# Freeform Universal RPG dice bot
#       for Discord
#
# Created by Ni3dzwi3dz


import discord
import asyncio
from random import randint
import bot_credentials as bc 
from discord.ext import commands

#This is our bot
class PrestonBlackwoodJr(commands.Bot):

    
    #This gets called, when bot connects
    async def on_ready(self):
        print('Nazywam się Preston Blackwood Jr. Z tych Blackwoodów')

    async def on_error(self,context, message, error):
        await context.send(content=f'Aby rzucić kostką wpisz !roll, dodaj "+" za każdą dodatkową i "-" za każdą karną kość')

bot= PrestonBlackwoodJr(command_prefix='!')


@bot.command(name='roll', description='Basic dice roll function')
async def roll(ctx,arg=''):
#Basic roll function
#optional argument is for negative and positive dice
    FU =  { 1 : 'Nie i...', 2 : 'Nie, po prostu nie', 3 : 'Nie, ale...', 
            4 : 'Tak, ale', 5 : 'Tak, udało się', 6 : 'Whoooa! Tak i...',
            0 : 'Kostka mi wpadła pod szafkę, rzuć jeszcze raz' }

    modifier = arg.count('+') - arg.count('-')
    results = []
    result = 0

    for _ in range(1+abs(modifier)):
        results.append(randint(1,6))
    try:
        if modifier < 0:
            result = FU[min(results)]
        else:
            result = FU[max(results)]
    except:
        result= FU[0]

    desc = f'{results} \n Ostateczny wynik to: {result}'

    resp = discord.Embed(description=desc)

    resp.set_author(
        name=f'{ctx.author.name} rukulał:',
        icon_url=f'{ctx.author.avatar_url}')
    
    await ctx.send(embed=resp)

if __name__ == "__main__":
    bot.run(TOKEN, bot=True, reconnect=True)
    



