from discord.ext.commands import Bot
from PIL import Image
#from pytesseract import image_to_string
import random
import requests
from io import StringIO
from io import BytesIO
import aiohttp

BOT_PREFIX=("??","!!","?")
TOKEN = '' #use ur token

client = Bot(command_prefix=BOT_PREFIX)

@client.command(name='hi',
                aliases =["hello","sup","wassup","yo"],
                pass_context=True)
async def hello(context):
    possible_responses =[
        "OwO what's this?",
        "konichiwa Senpai",
        "Arigato Gozaimas",
        ]
    await client.say(random.choice(possible_responses))
    

        
#@client.command(name='help_ruben',
#                description="Post an image of riven to see tips and tricks!",
#                pass_context=True)

    
#async def help_ruben(ctx):
#    a_list = (ctx.message.attachments)
#    b=a_list[0]
#    url = b["url"]
#    filename = b["filename"]
#    async with aiohttp.ClientSession() as client_session:
#        async with client_session.get(url) as response:
#                image_bytes = await response.read()
#
#    img = Image.open(BytesIO(image_bytes))
#    ##img.show()
#    text=image_to_string(img)
#    if ("land" in text or "headshots" in text):
#        await client.say("Go to POE with a sniper.  This one's easy and kind of self explanatory")
#
#    if ("fish" in text or "gem" in text or "metal" in text):
#        await client.say("Go to POE and find a proper place with a ore a fishing spot and an enemy nearby. Gara throt near the entrance is a good place and be quick")
#                         
#                         
#    print (text)
#    
     

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')    

client.run(TOKEN)
