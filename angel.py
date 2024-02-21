import pyotp


from SmartApi import SmartConnect #or from SmartApi.smartConnect import SmartConnect

from telethon import TelegramClient, events
import time

api_id = 29395559
api_hash = 'd3f70d97f92a979dc5578168c14fa117'
client = TelegramClient('s1', api_id, api_hash)

api_key = 'kAELgp1J'
clientId = 'N51889834'
pwd = 9862
token = "FKVSHLRW7RDNV6YUYAIK7F5D4I"
totp = pyotp.TOTP(token).now()
correlation_id = "abc123"

smartApi = SmartConnect(api_key)
data = smartApi.generateSession(clientId, pwd, totp)

refreshToken = data['data']['refreshToken']

feedToken = smartApi.getfeedToken()
print(feedToken)

#--------------------------------------------- ------------------------------------------ -----------------------------------------------



# FA152764_U
# abc1234
# 2d12eb0d1c9e768ca5f4e58e65a61d1f


# FORWARD MESSAGS------+++++++++++++++++++++++++++++++++++++
async def send_new_message(destination_chat_id, message_text):
  try:
    await client.send_message(destination_chat_id, message_text)
  except Exception as e:
    print(f"Error sending new message: {e}")


@client.on(events.NewMessage(chats=-1001959827182))
async def handle_message_my_channel(event):
  
  destination_chat_username = -1001959125612

  message_text = event.message.message.upper()
  print("call text:", message_text)
  trade_call_array = message_text.split()
  print(trade_call_array)
  
  
  while True:
      exchange = "NFO"
      searchscrip = "BANKNIFTY30NOV2356000CE"
      searchScripData = smartApi.searchScrip(exchange, searchscrip)
      
      print(searchScripData)
      time.sleep(1)

  await send_new_message(destination_chat_username, message_text)


@client.on(events.NewMessage)
async def handle_new_message(event):
  if event.is_channel and event.chat_id == -1001959125612:
    print(f"New message in channel {event.chat_id}: {event.message.text}")


async def main():
  # channel_id = -1001959125612
  # FETCH LATEST MESSAGES
  # await read_latest_message(channel_id)

  await client.run_until_disconnected()


if __name__ == '__main__':
  client.start()
  client.loop.run_until_complete(main())