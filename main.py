import ccxt
import re
from telethon import TelegramClient, events, sync
#gwapo si john lloyd hehe
#This is for Binance API
api_key = '2d815c7a0bcc926e1fdaa7452fc7ef5296c5fc262c56eeb20bbacf2a77bc5e1e'
api_secret = '934833360933db40f6c30fab2ed5b54204fc92da81ad7ad6883672c60a13f771'

#This is for Telegram APP API 
api_id = '24319261'
api_hash = '617b129d2d42790112702f2cc783211c'
phone_number = '+639539870591'

clientTelegram = TelegramClient('anon', api_id, api_hash)
clientBinance = ccxt.binance({'apiKey': api_key, 'secret': api_secret, 'options': {'defaultType': 'future'}})

clientBinance.set_sandbox_mode(True)
clientBinance.load_markets()


def filter_message(message):
    pattern = r"(?P<symbol>\w+)\s+(?P<action>buy|sell)\s+now\s+@\s+(?P<entry>\d+-\d+)\s+sl:(?P<sl>\d+)\s+tp1:(?P<tp1>\d+)tp2:(?P<tp2>\d+)"
    match = re.search(pattern, message)

    if match:
        # Extract information
        symbol = match.group("symbol")
        action = match.group("action")
        entry = match.group("entry")
        sl = match.group("sl")
        tp1 = match.group("tp1")
        tp2 = match.group("tp2")
        
        # print(f"Symbol: {symbol}")
        # print(f"Action: {action}")
        # print(f"Entry: {entry}")
        # print(f"Stop Loss (SL): {sl}")
        # print(f"Take Profit 1 (TP1): {tp1}")
        # print(f"Take Profit 2 (TP2): {tp2}")
        if(action == "buy"):
            ticker = clientBinance.fetch_ticker(symbol)
            print(f"Current {symbol} Price: {ticker['last']}")
            
    else:
        print("No match found!")

@clientTelegram.on(events.NewMessage)
async def my_event_handler(event):
    print(f'New Message: {event.raw_text}')
    filter_message(event.raw_text)

@clientTelegram.on(events.MessageEdited())
async def handler(event):
    print(f'Edited Message: {event.raw_text}')
    filter_message(event.raw_text)


clientTelegram.start(phone=phone_number)
clientTelegram.run_until_disconnected()








#order = client.create_order('BTC/USDT', 'market', 'buy', 0.001)