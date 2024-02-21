from typing import _SpecialForm
from NorenRestApiPy.NorenApi import NorenApi
from threading import Timer
from certify import next_wednesday
# --------------------------
import logging
import pyotp
from telethon import TelegramClient, events
import time
import threading
from SmartApi import SmartConnect #or from SmartApi.smartConnect import SmartConnect



# --------------------- SMART API CREDENTIALS ---------------------
smart_api_key = 'kAELgp1J'
smartClientID = 'N51889834'
smartPWD = 9862
smartToken = "FKVSHLRW7RDNV6YUYAIK7F5D4I"
smartOTP = pyotp.TOTP(smartToken).now()
correlation_id = "abc123"

smartApi = SmartConnect(smart_api_key)
data = smartApi.generateSession(smartClientID, smartPWD, smartOTP)

refreshToken = data['data']['refreshToken']

feedToken = smartApi.getfeedToken()
print(feedToken)





class ShoonyaApiPy(NorenApi):

  def __init__(self):
    NorenApi.__init__(self, host='https://api.shoonya.com/NorenWClientTP/', websocket='wss://api.shoonya.com/NorenWSTP/')
    global api
    api = _SpecialForm

 

#start of our program
api = ShoonyaApiPy()
token = '23IL2KM7VY7D5WUL557W67EG34J75LM3'
otp = pyotp.TOTP(token).now()









# FINVASIA CREDENTIALS

user = 'FA152764'
pwd = '@RadeonF97'
factor2 = otp
vc = 'FA152764_U'
app_key = 'd2ffa5fa99ba35cfce2593eef2714dfa'
imei = 'abc1234'
 
# logging.basicConfig(level=logging.DEBUG)



# FINVASIA API LOGIN
loginResult = api.login(userid=user, password=pwd, twoFA=otp, vendor_code=vc, api_secret=app_key, imei=imei)

 

# print("THE LOGIN RESULT IS: ",loginResult)


# print("THE LOGIN RESULT IS: ",loginResult)
# MY CHANNEL : 1001959827182
# SHIVAY CHANNEL: 1001640142628


senderUserID = -1001959827182
receiverUserID = -1001959125612





# DEFAULT STATE FOR ORDER OBJECT 1
order1_Obj = {
  'symbol': '',
  'token': 0,
  'buying_price' : 0,
  'is_order_executed': False,
  'order_no': '',
  'target_price' : 0,
  'stoploss_price': 0,
  'is_order_cancelled' : False,
  'is_position_squareOff' : False,
  'is_exit_order_placed': False,
  'exit_order_no': '',
  'angel_symbol': '',
  # 'angel_symboltoken' : ''
}

# DEFAULT STATE FOR ORDER OBJECT 2
order2_Obj = {
  'symbol': '',
  'token': 0,
  'buying_price' : 0,
  'is_order_executed': False,
  'order_no': '',
  'target_price': 0,
  'stoploss_price' : 0,
  'is_order_cancelled' : False,
  'is_position_squareOff' : False,
  'is_exit_order_placed' : False,
  'exit_order_no': '',
  'angel_symbol': '',
  # 'angel_symboltoken' : ''
}

# DEFAULT STATE FOR THREAD
thread_1_Active = True
thread_2_Active = True


order_1_history = None
order_2_history = None


def getOrderStauts(orderHistory):
  return orderHistory[0]

api_called = 0

def event_handler_feed_update(tick_data):
  global thread_1_Active
  global thread_2_Active
  global order_1_history
  global order_2_history
  global api_called

  feed_data = tick_data
  latest_price = float(feed_data['lp'])
  print(latest_price, "============================================================================", feed_data)
  api_called= api_called + 1
  feed_token = int(feed_data['tk'])
  # order_1_token = int(order1_Obj['token'])
  # order_1_history = api.single_order_history(orderno=order1_Obj['order_no'])


  # IF ORDER 1 IS NOT EXECUTED-------------------------------------------------------------------------
  # STEP 1
  if order1_Obj['is_order_executed'] == False:
    order_1_history = api.single_order_history(orderno=order1_Obj['order_no'])
    if getOrderStauts(order_1_history)['stat'] == 'Ok' and getOrderStauts(order_1_history)['status'] == "OPEN":
      order1_Obj['is_order_executed'] = True
      thread_2_Active = False

      # PLACE EXIT ORDER FOR ORDER 1
      square_off_order_response = api.place_order(
        buy_or_sell='S', 
        product_type='I', 
        exchange='NFO', 
        tradingsymbol=order1_Obj['symbol'], 
        quantity=15, 
        discloseqty=0, 
        price_type='SL-LMT', 
        price=order1_Obj['stoploss_price'], 
        trigger_price=order1_Obj['stoploss_price']+1, 
        retention='DAY', 
        remarks='Option order placed...'
      )
      
      # IF THERE IS NO STOPLOSS ORDER FOR ORDER 1 THEN PLACE A STOPLOSS ORDER
      if order1_Obj['is_exit_order_placed'] == False:
        order1_Obj['exit_order_no'] = square_off_order_response['norenordno']
        order1_Obj['is_exit_order_placed'] = True

      # IF ORDER 2 ORDER_NO != '' THEN CANCEL ORDER 2
      if order2_Obj['order_no'] != '':
        api.cancel_order(orderno=order2_Obj['order_no'])
      
      


  # # --- HANDLE SQUARE OFF AND ORDER CANCELLATION ON ORDER 1 EXECUTED
  # # STEP 2
  if order1_Obj['is_order_executed'] == True:
    if int(order1_Obj['token']) == feed_token:
      print(feed_data['lp'], " LATEST PRICE OF ORDER 1 AND TOKEN: ", order1_Obj['token'] )
      if float(feed_data['lp']) > float(order1_Obj['buying_price']): # BOOK PROFIT
        print("BOOK PROFIT OF ORDER 1")
        api.modify_order(
          exchange='NFO', 
          tradingsymbol=order1_Obj['symbol'], 
          orderno=order1_Obj['exit_order_no'],
          newquantity=15, 
          newprice_type='SL-LMT', 
          newprice=order1_Obj['target_price'], 
          newtrigger_price=order1_Obj['target_price'] - 1)
      else:
        print("BOOK LOSS OF ORDER 1")
        api.modify_order(
          exchange='NFO', 
          tradingsymbol=order1_Obj['symbol'], 
          orderno=order1_Obj['exit_order_no'],
          newquantity=15, 
          newprice_type='SL-LMT', 
          newprice=order1_Obj['stoploss_price'], 
          newtrigger_price=order1_Obj['stoploss_price'] + 1)
  # -------------------------------- ORDER 1 CLOSE --------------------------------------------------



  #====================================== HANDLE ORDER 2 ============================================



  # IF ORDER 2 IS NOT EXECUTED---------------------------------------------------------------------------
  # LOGIC FOR STEP 1: 
  # 1. IF ORDER 2 IS NOT EXECUTED THEN CHECK FOR ORDER STATUS
  # 2. IF ORDER 2 IS EXECUTED THEN SET EXECUTED STATUS AS -TRUE
  # CLOSE THREAD 1 WHILE LOOP AND PLACE A STOPLOSS ORDER

  # 3. IF ORDER 2 EXIT OR STOPLOSS ORDER STATUS IS -FALSE THEN 
  # MAKE IT -TRUE AND SET STOPLOSS ORDER NO AND SET EXIT 
  # ORDER STATUS TRUE SO THAT IT WILL NOT PLACE STOPLOSS 
  # ORDER REPEATEDLY 
  
  # 4. AFTER PLACING A STOPLOSS ORDER CHECK IS SECOND ORDER
  # EXISTS. IF SECOND ORDER EXISTS THEN CANCEL SECOND ORDER
  # STEP 1
  if order2_Obj['is_order_executed'] == False:
    order_2_history = api.single_order_history(orderno=order2_Obj['order_no'])
    if getOrderStauts(order_2_history)['stat'] == 'Ok' and getOrderStauts(order_2_history)['status'] == 'COMPLETED':
      order2_Obj['is_order_executed'] = True # IF ORDER EXECUTED THEN SET EXECUTION STATUS = TRUE
      thread_1_Active = False

      # PLACE EXIT ORDER FOR ORDER 1
      square_off_order_response = api.place_order(
        buy_or_sell='S', 
        product_type='I', 
        exchange='NFO', 
        tradingsymbol=order2_Obj['symbol'], 
        quantity=15, 
        discloseqty=0, 
        price_type='SL-LMT', 
        price=order2_Obj['stoploss_price'], 
        trigger_price=order2_Obj['stoploss_price']+1, 
        retention='DAY', 
        remarks='Option order placed...'
      )

      # IF THERE IS NO STOPLOSS ORDER FOR ORDER 2 THEN PLACE A STOPLOSS ORDER
      if order2_Obj['is_exit_order_placed'] == False:
        order2_Obj['exit_order_no'] = square_off_order_response['norenordno']
        order2_Obj['is_exit_order_placed'] = True

      # IF ORDER 1 ORDER NO != '' THEN CANCEL ORDER 1
      if order1_Obj['order_no'] != '':
        api.cancel_order(orderno=order1_Obj['order_no'])

  

  # # ---HANDLE SQUARE OFF AND ORDER CANCELLATION ON ORDER 2 EXECUTED
  # # STEP 2
  if order2_Obj['is_order_executed'] == True:
    if int(order2_Obj['token']) == feed_token:
      print(feed_data['lp'], " LATEST PRICE OF ORDER 2 AND TOKEN: ", order2_Obj['token'] )
      if float(feed_data['lp']) > float(order2_Obj['buying_price']):
        print("BOOK PROFT OF ORDER 2")
        api.modify_order(
          exchange='NFO', 
          tradingsymbol=order2_Obj['symbol'], 
          orderno=order2_Obj['exit_order_no'],
          newquantity=15, 
          newprice_type='SL-LMT', 
          newprice=order2_Obj['target_price'], 
          newtrigger_price=order2_Obj['target_price'] - 1)
      else:
        print("BOOK LOSS OF ORDER 2")
        api.modify_order(
          exchange='NFO', 
          tradingsymbol=order2_Obj['symbol'], 
          orderno=order2_Obj['exit_order_no'],
          newquantity=15, 
          newprice_type='SL-LMT', 
          newprice=order2_Obj['stoploss_price'], 
          newtrigger_price=order2_Obj['stoploss_price'] + 1)
  # -------------------------------- ORDER 2 CLOSE --------------------------------------------------




token1 = 0
token2 = 0

def open_callback():
  global feed_opened
  feed_opened = True




# LOOP FOR ORDER 1-------------------------------------------------------------------
def loopForOrder1():
  global thread_1_Active
  while thread_1_Active:
    if token1 != 0 and order1_Obj['order_no'] != '':
      print("THREAD 1 STATE ", thread_1_Active)
      print("API CALLED: ", api_called)
      
      handleSquareOff(order1_Obj['angel_symbol'], order1_Obj['token'], order1_Obj)

    time.sleep(1)      
# -----------------------------------------------------------------------------------





# LOOP FOR ORDER 2-------------------------------------------------------------------
def loofForOrder2():
  global thread_2_Active
  while thread_2_Active:
    if token2 != 0 and order2_Obj['order_no'] != '':
      try:
        print(" THREAD 2 STATE ", thread_2_Active)
      except Exception as e:
        print(f"Error in loopForOrder2:{e}")
    time.sleep(1) 
# -----------------------------------------------------------------------------------







# RUN DIFFERENT THREAD TO GET BOTH LATEST DATA---------------------------------------
threadOrder1 = threading.Thread(target=loopForOrder1)
threadOrder2 = threading.Thread(target=loofForOrder2)

threadOrder1.start()
threadOrder2.start()
# -----------------------------------------------------------------------------------






# #------------------------------------------------------------------------------- IMPLEMENTING TELEGRAM FUNCTIONALITY-------------------------------------------------------
api_id = 29395559
api_hash = 'd3f70d97f92a979dc5578168c14fa117'
client = TelegramClient('s1', api_id, api_hash)




# ON MESSAGE RECEIVE -------------
async def placeOrder(messageText):
    global token1
    global token2

    # EXTRACT MESSAGE CONTENT
    message_content = messageText.split();
    strike = message_content[3][:-2]
    side = message_content[3][-2:]
    optionName = "BANKNIFTY " + strike + " " + side

    # ANGEL SYMBOL HANDLE-----------------------------------------------
    expiry_date = next_wednesday()
    day = expiry_date['day']
    month = expiry_date['month']
    angel_symbol = "BANKNIFTY" + day + month + "23" + strike + side
    
    # -----------------------------------------------------------------


    # EXTRACT PRICES FROM MESSAGE
    order_price = float(message_content[4][5:8])
    stoploss_price = float(message_content[5][2:5])

    # MODIFY ORDER PRICE
    order_price = order_price + 5
    target_price = order_price + 25


    # SEARCH INSTRUMENT IN FINVASIA
    searchInstruements = api.searchscrip(exchange="NFO", searchtext=optionName)['values']

    myInstrument = searchInstruements[0]
    tSymbol = myInstrument['tsym']
    token = myInstrument['token']

    # PLACE ORDER
    order_response = api.place_order(
    buy_or_sell='B', 
    product_type='I', 
    exchange='NFO', 
    tradingsymbol=tSymbol, 
    quantity=15, 
    discloseqty=0, 
    price_type='SL-LMT', 
    price=order_price, 
    trigger_price=order_price - 1, 
    retention='DAY', 
    remarks='Option order placed...')

    orderNo = order_response['norenordno']



    # IF ORDER 1 IS EMPTY------------
    if token1 == 0:
       token1 = token
       order1_Obj['symbol'] = tSymbol
       order1_Obj['token'] = token
       order1_Obj['buying_price'] = order_price
       order1_Obj['order_no'] = orderNo
       order1_Obj['target_price'] = target_price
       order1_Obj['stoploss_price'] = stoploss_price
       order1_Obj['angel_symbol'] = angel_symbol
       

       #  SEND ORDER NOTIFICATION
       msg = f'''BUY ORDER PLACED:
                   AT PRICE: {order_price}
                   TARGET PRICE: {target_price}
                   STOPLOSS PRICE: {stoploss_price}
                   ORDER NO: {orderNo}
                   ANGEL SYMBOL: {angel_symbol}
                   ANGEL TOKEN: {token}'''
       
       await forwardMessage(receiverUserID, msg)
    
    # IF ORDER 1 IS NOT EMPTY THEN FILL ORDER 2
    else:
       token2 = token
       order2_Obj['symbol'] = tSymbol
       order2_Obj['token'] = token
       order2_Obj['buying_price'] = order_price
       order2_Obj['order_no'] = orderNo
       order2_Obj['target_price'] = target_price
       order2_Obj['stoploss_price'] = stoploss_price
       order1_Obj['angel_symbol'] = angel_symbol
       

       # SEND ORDER NOTIFICATION 
       msg = f'''BUY ORDER PLACED:
                   AT PRICE: {order_price}
                   TARGET PRICE: {target_price}
                   STOPLOSS PRICE: {stoploss_price}
                   ORDER NO: {orderNo}
                   ANGEL SYMBOL: {angel_symbol}
                   ANGEL TOKEN: {token}'''
       
       await forwardMessage(receiverUserID, msg)
# ----------------------------------------------------------------------------------------------------------------------------------------------------










# HANDLE SQUARE OFF ORDER------------------------------------------------------------------------------------------------------------------------------
def handleSquareOff(angel_token_symbol, token, orderItem):

  # IF ORDER NOT EXECUTED THEN CHECK EXECUTION STATUS
  if orderItem['is_order_executed'] == False:
    orderItem_history = api.single_order_history(orderno=orderItem['order_no'])

    # IF ORDER EXECUTED THEN
    if getOrderStauts(orderItem_history)['stat'] == 'Ok' and getOrderStauts(orderItem_history)['status'] == "REJECTED":
      orderItem['is_order_executed'] = True                                       
      
      # PLACE SQUARE OFF ORDER
      square_off_order_response = api.place_order(
        buy_or_sell='S', 
        product_type='I', 
        exchange='NFO', 
        tradingsymbol=orderItem['symbol'], 
        quantity=15, 
        discloseqty=0, 
        price_type='SL-LMT', 
        price=orderItem['stoploss_price'], 
        trigger_price=orderItem['stoploss_price']+1, 
        retention='DAY', 
        remarks='stoploss order placed...'
      )

      # IF SQUARE OFF ORDER NO IS NULL THEN SET SET SQUARE OFF ORDER NO
      if orderItem['is_exit_order_placed'] == False:
        orderItem['exit_order_no'] = square_off_order_response['norenordno']
        orderItem['is_exit_order_placed'] = True
        
        # CANCEL ALTERNATE ORDER


        # ----------------------

  # IF ORDER EXECUTED THEN HANDLE SQUARE OFF BASED ON CURRENT PRICE
  if orderItem['is_order_executed'] == True:
    current_price_data = smartApi.ltpData("NFO", angel_token_symbol, str(token))
    current_price = current_price_data['data']['ltp']
    
    if current_price > orderItem['buying_price']:
      # MODIFY TARGET
      api.modify_order(
        exchange='NFO', 
        tradingsymbol=orderItem['symbol'], 
        orderno=orderItem['exit_order_no'],
        newquantity=15, 
        newprice_type='SL-LMT', 
        newprice=orderItem['target_price'], 
        newtrigger_price=orderItem['target_price'] - 1)
    else:
      # MODIFY STOPLOSS
      api.modify_order(
        exchange='NFO', 
        tradingsymbol=orderItem['symbol'], 
        orderno=orderItem['exit_order_no'],
        newquantity=15, 
        newprice_type='SL-LMT', 
        newprice=orderItem['stoploss_price'], 
        newtrigger_price=orderItem['stoploss_price'] + 1)

# ------------------------------------------------------------------------------------------------------------------------------------------------------

















# FUNCTION FOR FORWARDING MESSAGE
async def forwardMessage(receiver, message):
    try:
        await client.send_message(receiver, message)
    except Exception as err:
        print("Failed to forward messages: ", err)




# FUNCTION WHEN NEW MESSAGE ARRIVE
@client.on(events.NewMessage(chats=senderUserID))
async def whenSenderSendMessage(event):
    msg_text = event.message.message.upper()
    print(msg_text)
    await placeOrder(msg_text)



# api.start_websocket(order_update_callback=event_handler_feed_update, subscribe_callback=event_handler_feed_update, socket_open_callback=open_callback)


# START TELETHON API-----------
async def main():
  await client.run_until_disconnected()

if __name__ == '__main__':
  client.start()
  client.loop.run_until_complete(main())
# #------------------------------------------------------------------------------- IMPLEMENTING TELEGRAM FUNCTIONALITY-------------------------------------------------------