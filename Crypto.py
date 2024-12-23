import discord
from discord.ext import commands
import requests


DISCORD_TOKEN = 'DISCORD_TOKEN'
COIN_API_URL = 'COIN_API_URL'
COIN_API_KEY = 'COIN_API_KEY'


intents = discord.Intents.default()
intents.messages = True  
intents.message_content = True 


bot = commands.Bot(command_prefix='!', intents = intents)

# !coin komutu 
@bot.command()
async def coin(ctx, symbol: str):
    try:
        symbol = symbol.upper()
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': COIN_API_KEY,
        }
        parameters = {'symbol': symbol}
        response = requests.get(COIN_API_URL, headers = headers , params = parameters)
        data = response.json()

        
        coin_data = data['data'][symbol]
        coin_name = coin_data['name']
        coin_price = round(coin_data['quote']['USD']['price'], 5)

        
        await ctx.send(f"{coin_name}: {coin_price} USD")
    except KeyError:
        await ctx.send("Geçersiz sembol veya veri bulunamadı.")
    except Exception as e:
        await ctx.send(f"Hata: {e}")

bot.run(DISCORD_TOKEN)
