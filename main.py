import discord
from discord.ext import commands
import random
import rolling_dice # function (mine!)

client = commands.Bot(command_prefix = "$") # uses $ as prefix

@client.event
async def on_ready():
    print("READY!!!")

@client.command()
async def ping(ctx):
    await ctx.send("Pong!")

@client.command()
async def roll(ctx): # gives random number between
    resultRoll = str(rolling_dice.roll_once())
    await ctx.send(resultRoll)

@client.command()
async def doubleroll(ctx): # gives random number between
    resultDoubleRoll = str(rolling_dice.roll_twice())
    await ctx.send(resultDoubleRoll)
    if rolling_dice.sum() >= 9:
        await ctx.send("Impressive!")

@client.command()
async def commentTwice(ctx, arg1, arg2): # WIP
    unite = arg1 + " " + arg2
    await ctx.send(unite)

@client.command() # add phrase to element.txt
async def add(ctx, *arg1):
    addSpace = [word + ' ' for word in arg1]
    stringPhrase = ''.join(addSpace)
    openAppendTXT = open("element.txt", "a")
    openAppendTXT.write(stringPhrase + "\n")
    await ctx.send('" '+stringPhrase+'" has been added!') # "phrase" has been added!

@client.command()
async def phrase(ctx):
    randomPhrases = open("element.txt", "r")
    listFile = randomPhrases.readlines()

    rPhrase = random.choice(listFile) # chooses random element from element.txt
    await ctx.send(rPhrase)

@client.command()
async def showPhrases(ctx):
    phraseList = open("element.txt", "r")
    readPhraseList = phraseList.readlines()
    await ctx.send(readPhraseList)

@client.command()
async def logout(ctx):
    print("DISCONNECT! \n")
    await ctx.send("Disconnect!!!")
    await client.close()

token = None
client.run(token)