text = """👍👍👍
BANK NIFTY
45000 PE
ABOVE 330
VIEW / EDUCATIONAL PURPOSE
"""


# SLICE PRICE FROM TEXT
price = ""
aboveText = text.find("ABOVE")
for i in range(aboveText+3, aboveText + 12):
    if text[i].isdigit():
        price = price + text[i]



# SLICE POSITION SIDE FROM TEXT
positionSide = ""
findNifty = text.find("NIFTY")
for i in range(findNifty + 10, findNifty + 17):
    if(text[i] == "P"):
        positionSide = "PE"
    if(text[i] == "C"):
        positionSide = "CE"



# SLICE STRIKE PRICE FROM TEXT
strike_price = ""
for i in range(findNifty+ 4, findNifty + 15):
    if text[i].isdigit():
        strike_price = strike_price + text[i]


print(strike_price)


"""
# FIRST ORDER INFORMATION:  {


 'order_name': 'FIRST ORDER', 
 'symbol': 'BANKNIFTY21FEB24C45000', 
 'token': '45811', 
 'buying_price': 301.5, 
 'is_order_executed': False, 
 'order_no': '24021501286644', 
 'target_price': 340.5, 
 'stoploss_price': 260.0, 
 'is_order_cancelled': False, 
 'is_position_squareOff': False, 
 'is_exit_order_placed': False, 
 'exit_order_no': '', 
 'angel_symbol': 'BANKNIFTY21FEB2445000CE'
 
 }

# SECOND ORDER INFORMATION:  {'order_name': 'SECOND ORDER', 'symbol': 'BANKNIFTY21FEB24C45000', 'token': '45811', 'buying_price': 301.5, 'is_order_executed': False, 'order_no': '24021501286645', 'target_price': 340.5, 'stoploss_price': 260.0, 'is_order_cancelled': False, 'is_position_squareOff': False, 'is_exit_order_placed': False, 'exit_order_no': '', 'angel_symbol': ''}








 VIEW/ EDUCATIONAL PURPOSE
300   45000    CE
FIRST ORDER INFORMATION:  {'order_name': 'FIRST ORDER', 'symbol': 'BANKNIFTY21FEB24C45000', 'token': '45811', 
'buying_price': 301.5, 'is_order_executed': False, 'order_no': '24021501286677', 'target_price': 340.5, 'stoploss_price': 260.0, 'is_order_cancelled': False, 
'is_position_squareOff': False, 'is_exit_order_placed': False, 'exit_order_no': '', 'angel_symbol': 'BANKNIFTY21FEB2445000CE'}
THREAD 1 STATE  True
https://api.shoonya.com/NorenWClientTP//SingleOrdHist
BOOK PROFIT, currnet price is:  1445.0    FIRST ORDER
https://api.shoonya.com/NorenWClientTP//ModifyOrder
ORDER MODIFIED TIME:  1
THREAD 1 STATE  True
ORDER MODIFIED TIME:  1




THREAD 1 STATE  True
https://api.shoonya.com/NorenWClientTP//SingleOrdHist
----- AFTER PLACING STOPLOSS ORDER -------- {'order_name': 'FIRST ORDER', 'symbol': 'BANKNIFTY21FEB24C45000', 'token': '45811', 'buying_price': 301.5, 'is_order_executed': True, 'order_no': '24021501286714', 'target_price': 340.5, 'stoploss_price': 260.0, 'is_order_cancelled': False, 'is_position_squareOff': False, 'is_exit_order_placed': True, 'exit_order_no': '24021501286715', 'angel_symbol': 'BANKNIFTY21FEB2445000CE'}
SECOND ORDER INFORMATION:  {'order_name': 'SECOND ORDER', 'symbol': 'BANKNIFTY21FEB24C45000', 'token': '45811', 'buying_price': 301.5, 'is_order_executed': False, 'order_no': '24021501286716', 'target_price': 340.5, 'stoploss_price': 260.0, 'is_order_cancelled': False, 'is_position_squareOff': False, 'is_exit_order_placed': False, 'exit_order_no': '', 'angel_symbol': ''}
BOOK PROFIT, currnet price is:  1445.0    FIRST ORDER
https://api.shoonya.com/NorenWClientTP//ModifyOrder







----- AFTER PLACING STOPLOSS ORDER -------- {'order_name': 'FIRST ORDER', 
'symbol': 'BANKNIFTY21FEB24C45000', 
'token': '45811',
 'buying_price': 301.5, 
 'is_order_executed': True, 
 'order_no': '24021501286723', 
 'target_price': 340.5, 
 'stoploss_price': 260.0, 
 'is_order_cancelled': False, 
 'is_position_squareOff': False, 
 'is_exit_order_placed': True,
 'exit_order_no': '24021501286724', 
 'angel_symbol': 'BANKNIFTY21FEB2445000CE'}
BOOK PROFIT, currnet price is:  1445.0    FIRST ORDER
https://api.shoonya.com/NorenWClientTP//ModifyOrder
ORDER MODIFIED TIME:  1
THREAD 1 STATE  True
ORDER MODIFIED TIME:  1




    # ANGEL SYMBOL HANDLE-----------------------------------------------
    #expiry_date = next_wednesday()
    # day = expiry_date['day']
    # month = expiry_date['month']
    # angel_symbol = "BANKNIFTY" + day + month + "23" + strike + side
    
    # -----------------------------------------------------------------







---------------------------------------------------------------------------------------------------------------------------------------------


hkQ0k2TVRjd09ESTFPVFEwT0N3aWFuUnBJam9pTUROaU5ESmhZell0WWpSak1pMDBZVE5oTFdJelpqa3RNRE5oWkRreU5qUXlZalZpSWl3aWIyMXVaVzFoYm1GblpYSnBaQ0k2TUN3aWRHOXJaVzRpT2lKU1JVWlNSVk5JTFZSUFMwVk9JaXdpZFhObGNsOTBlWEJsSWpvaVkyeHBaVzUwSWl3aWRHOXJaVzVmZEhsd1pTSTZJblJ5WVdSbFgzSmxabkpsYzJoZmRHOXJaVzRpTENKa1pYWnBZMlZmYVdRaU9pSTFOREE1Tm1WbFpTMHpORFkyTFRNd1lUY3RPR1k0WVMxak9XVXhaak01WTJGbU5HUWlMQ0poWTNRaU9udDlmUS5NekpHcWptOVNVRUpuZDVuSHhOUmthY0NQOUdIY0ViaHJTek9sQjVzX1lhNW16UkJtc29BWDc3V0tseV9nUVJaeG9QeGFSc1E1N2tYOF9lcW8zNS1nUSIsImlhdCI6MTcwODI1OTUwOH0.wLpWkQZl5_Aa0DsDEjJMcRPFGH34uJVTprgnvW_Vs1CCu_kA6jov4iXJ7WkSGGzbs1Z6D7pfNjRWzZUvlqI5sQ
🕉📉📈
 
 📉BANK NIFTY📈🕉

 45000 CE

 ABOVE  300

 VIEW/ EDUCATIONAL PURPOSE
300   45000    CE
FIRST ORDER INFORMATION:  {
    'order_name': 'FIRST ORDER', 
    'symbol': 'BANKNIFTY21FEB24C45000', 
    'token': '45811', 
    'buying_price': 301.5, 
    'is_order_executed': False, 
    'order_no': '24021700014088', 
    'target_price': 340.5, 
    'stoploss_price': 260.0, 
    'is_order_cancelled': False, 
    'is_position_squareOff': False, 
    'is_exit_order_placed': False, 
    'exit_order_no': '', 
    'angel_symbol': 'BANKNIFTY21FEB2445000CE'
    }
    
THREAD 1 IS RUNNING:   True
https://api.shoonya.com/NorenWClientTP//SingleOrdHist
----- AFTER PLACING STOPLOSS ORDER -------- {'order_name': 'FIRST ORDER', 'symbol': 'BANKNIFTY21FEB24C45000', 'token': '45811', 'buying_price': 301.5, 'is_order_executed': True, 'order_no': '24021700014088', 'target_price': 340.5, 'stoploss_price': 260.0, 'is_order_cancelled': False, 'is_position_squareOff': False, 'is_exit_order_placed': True, 'exit_order_no': '24021700014089', 'angel_symbol': 'BANKNIFTY21FEB2445000CE'}      
BOOK PROFIT, currnet price is:  1452.0    FIRST ORDER
https://api.shoonya.com/NorenWClientTP//ModifyOrder
ORDER MODIFIED TIME:  1
THREAD 1 IS RUNNING:   True
ORDER MODIFIED TIME:  1
THREAD 1 IS RUNNING:   True
ORDER MODIFIED TIME:  1
THREAD 1 IS RUNNING:   True
ORDER MODIFIED TIME:  1
THREAD 1 IS RUNNING:   True
ORDER MODIFIED TIME:  1
THREAD 1 IS RUNNING:   True











"""