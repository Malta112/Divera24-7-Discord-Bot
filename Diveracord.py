#!/usr/bin/env python3


Token = '[YOUR TOKEN]'
prefix = '$'
autoupdate = True
discordchannel = [Channelid für Screenshots] #Image

########################################################################################
import glob, os
import os.path
from PIL import Image, ImageDraw, ImageFont
from tkinter import filedialog
from tkinter import Tk
import discord
import logging
from discord.ext import commands
from discord.ui import Button, View
intents = discord.Intents.default()
intents.message_content = True
import subprocess
from subprocess import check_output
import time
import datetime
import sys
import pyautogui
import asyncio

client = commands.Bot(intents=intents, command_prefix=prefix)

def monitoroff():	
	subprocess.Popen(['bash','-c','. divera_commands.sh; monitor off'])	
def monitoron():
	subprocess.Popen(['bash','-c','. divera_commands.sh; monitor on'])
	pyautogui.moveTo(100, 150)

@client.command()
async def hilfe(cfx):
	embedVar = discord.Embed(title="Hilfemenu", description="Zeigt alle derzeitigen Commands an", color=0x00ff00, url = "https://github.com/Malta112")
	embedVar.add_field(name=prefix + "hilfe", value="Zeigt dir diese Hilfe an", inline=False)
	embedVar.add_field(name=prefix + "monitor (+ an/aus)", value="Startet/Stoppt die Anzeige Von Divera", inline=False)
	embedVar.add_field(name=prefix + "neustart", value="Startet den Divera Monitor neu", inline=False)
	embedVar.add_field(name=prefix + "update", value="Startet ein manluelles update", inline=False)
	embedVar.add_field(name=prefix + "Bildschirmfoto", value="Macht ein Bildschirmfoto und zeigt den Aktuellen Stand, Gut um nachzuschauen ob die Anzeige stimmt", inline=False)
	await cfx.send(embed=embedVar)
		
@client.command()
async def monitor(ctx, arg):
	if arg in ['on', 'an']:
		if "divera" in [y.name.lower() for y in ctx.message.author.roles]:
			monitoron()
			await ctx.send(arg)
		else:
			await ctx.send('Sie haben nicht die Berechtigung')
		
	else:
		if "divera" in [y.name.lower() for y in ctx.message.author.roles]:
			monitoroff()
			await ctx.send(arg)
		else:
			await ctx.send('Sie haben nicht die Berechtigung')

@client.command()
async def update(ctx):
	if "divera" in [y.name.lower() for y in ctx.message.author.roles]:
		await ctx.send('Update')
		subprocess.Popen(['sudo', 'apt', 'update']).wait()
		subprocess.Popen(['sudo', 'apt', '--yes', '--force-yes', 'upgrade']).wait()
		subprocess.Popen(['sudo', 'reboot'])
	else:
			await ctx.send('Sie haben nicht die Berechtigung')

@client.command()
async def neustart(ctx):
	if "divera" in [y.name.lower() for y in ctx.message.author.roles]:
		await ctx.send('Startet neu')
		subprocess.Popen(['sudo', 'reboot']).wait()
	else:
			await ctx.send('Sie haben nicht die Berechtigung')
def water(ort):
	opened_image = Image.open(ort)
	image_width, image_height = opened_image.size
	draw = ImageDraw.Draw(opened_image)
	font_size = int(image_width / 6)
	font = ImageFont.truetype("FreeMono.ttf", 40)	
	x, y = int(0), int(image_height - 40)
	draw.text((x, y), 'Malta112', font=font, fill='#FFF', stroke_width=5, stroke_fill='#222')
	opened_image.save('foto.jpg')	


@client.command()
async def Bildschirmfoto(ctx):
	if "divera" in [y.name.lower() for y in ctx.message.author.roles]:
		
		subprocess.Popen(['scrot', './image.png']).wait()
		water("./image.png")
		#time.sleep(10)
		channel = client.get_channel(discordchannel)
		with open('./foto.jpg', 'rb') as f:
			picture = discord.File(f)
			await channel.send(file=picture)
		subprocess.Popen(['rm', './image.png']).wait()
		subprocess.Popen(['rm', './foto.jpg']).wait()
	else:
			await ctx.send('Sie haben nicht die Berechtigung')
	
@client.event
async def on_ready():
	monitoron()
	
	if(os.path.isfile("/home/pi/divera247_app_v2_icon.png")):
		print("file exists")
		with open('divera247_app_v2_icon.png', 'rb') as image:
			await client.user.edit(avatar=image.read())
	else:
		subprocess.Popen(['wget', 'https://cdn.discordapp.com/attachments/849294019959717888/1046467220236144741/divera247_app_v2_icon.png']).wait()		
		with open('divera247_app_v2_icon.png', 'rb') as image:
			await client.user.edit(avatar=image.read())
	
client.run(Token)
if(autoupdate == True):
	while True:
		now=datetime.datetime.now()
		hour=now.hour
		minutes=now.minute
		if(hour == 23 and minutes == 9):
			webhook('Neustart durch Update')
			time.sleep(45)
			subprocess.Popen(['sudo', 'apt', 'update']).wait()
			subprocess.Popen(['sudo', 'apt', '--yes', '--force-yes', 'upgrade']).wait()
			time.sleep(5)
			subprocess.Popen(['sudo', 'reboot'])
		time.sleep(30)
