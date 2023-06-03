import time
import os
import threading
import discord
from discord.ext import commands
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import asyncio

# Discord bot token
TOKEN = str(os.environ.get('DISCORD_TOKEN'))

# Flag to control the execution
exit_flag = False

# Discord bot command prefix
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

# Global database to store codes
global_codes = set()
# Dictionary to store subscribed channels
subscribed_channels = {}

# Lock to synchronize access to the global database and subscribed channels
database_lock = threading.Lock()

# Path to ChromeDriver executable
CHROME_DRIVER_PATH = 'D:\Downloads\chromedriver_win32\chromedriver'

def crawl_website(url):
    service = Service(CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=service)

    while not exit_flag:
        driver.get(url)

        # Wait for 2 seconds
        time.sleep(2)

        # Find all <a> tags with class="label-code"
        a_tags = driver.find_elements(By.CSS_SELECTOR, 'a.label-code')

        # Create a set to store existing codes
        existing_codes = set()

        # Read existing codes from the global database
        with database_lock:
            existing_codes.update(global_codes)

        # Save new codes to the global database
        new_codes = []
        for a in a_tags:
            code = a.text
            if code not in existing_codes:
                new_codes.append(code)
                existing_codes.add(code)

        # Update the global database with new codes
        with database_lock:
            global_codes.update(new_codes)
           
        # Notify subscribed channels of new codes]
        if len(new_codes) > 0:
            for channel in subscribed_channels.values():
                asyncio.run_coroutine_threadsafe(channel.send(f'New code found: {", ".join(new_codes)}'), bot.loop)

        time.sleep(60)  # Delay for 1 minute

        driver.refresh()

async def send_new_codes():
    while not exit_flag:
        await asyncio.sleep(60)  # Delay for 1 minute

        # Send new codes to all subscribed channels
        with database_lock:
            new_codes = global_codes.copy()

        for code in new_codes:
      

            if len(code) > 0:
                # Code is not empty, send it to subscribed channels
                for channel in subscribed_channels.values():
                    asyncio.run_coroutine_threadsafe(channel.send(f'New code found: {code}'), bot.loop)
                    
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def last_code(ctx):
    if global_codes:
        last_code = max(global_codes)
        await ctx.send(f'Last code: {last_code}')
    else:
        await ctx.send('No codes found in the database.')

@bot.command()
async def last_10_codes(ctx):
    if global_codes:
        last_10_codes = '\n'.join(sorted(global_codes)[-10:])
        await ctx.send(f'Last 10 codes:\n{last_10_codes}')
    else:
        await ctx.send('No codes found in the database.')

@bot.command()
async def start_swqbot(ctx):
    with database_lock:
        if ctx.channel.id in subscribed_channels:
            await ctx.send('Crawler is already running.')
        else:
            subscribed_channels[ctx.channel.id] = ctx.channel
            await ctx.send('Crawler started. Codes will be published in this channel.')

@bot.command()
async def stop_swqbot(ctx):
    with database_lock:
        if ctx.channel.id in subscribed_channels:
            del subscribed_channels[ctx.channel.id]
            await ctx.send('Crawler stopped.')
        else:
            await ctx.send('Crawler is not running.')

# Start the crawler thread
crawler_thread = threading.Thread(target=crawl_website, args=('https://swq.jp',))
crawler_thread.start()

# Start the code publishing task
loop = asyncio.get_event_loop()
loop.create_task(send_new_codes())

# Start the Discord bot
bot.run(TOKEN)
