
"""

REF: PLACE SQUARE OFF ORDER:
---------------------------
    
    # 1. IF ORDER ITEM IS NOT EXECUTED THEN CHECK ORDER STATUS.
    # 2. IF ORDER STATUS  = 'COMPLETED' THEN SET ORDER EXECUTED STATUS AS TRUE. IMMEDIATELY PLACE A SQUARE OFF ORDER
    # 3. IF ORDER ITEM EXIT ORDER PLACED STATUS IS FALSE THEN 
        _SET EXIT ORDER STATUS AS TRUE AND 
        _PASS SQUARE OFF ORDER ID AS EXIT ORDER ID AND 
        _SET EXIT ORDER PLACED STATUS AS TRUE. SO, IT DONT PLACE ANOTHER EXIT ORDER

         
REF: CANCEL ALTERNATE ORDER:
---------------------------

    # 1. IF FIRST ORDER IS EXECUTED AND SECOND ORDER IS EXIST THEN SET CANCEL ORDER TARGET = SECOND ORDER ID
    # 2. IF SECOND ORDER IS EXECUTED AND FIRST ORDER IS EXIST THEN SET CANCEL ORDER TARGET = FIRST ORDER ID
    # 3. IF CANCEL ORDER TARGET ID IS NOT EMPTY STRING AND isAlternateOrderCancelled = False THEN CANCEL ORDER BY ORDER ID





REF: MODIFY TARGET:
-------------------

    # RESULT: AFTER MODIFIED TARGET isTargetModified WILL BE TRUE. 
    #        SO THAT IF PRICE STILL STAYS ABOVE BUYING PRICE IT DONT NEED TO MODIFY THE TARGET AGAIN 
    #        AFTER THAT isStoplossModified HAS SET TO FALSE.   MEANS = AFTER MODIFIED TARGET THE CODE WILL ONLY BE ABLE TO MODIFY STOPLOSS



REF: MODIFY STOPLOSS:
---------------------

    # RESULT: AFTER MODIFIED STOPLOSS isStoplossModified WILL BE TRUE
    #         SO THAT IF PRICE STILL CONTINUES BELOW BUYING PRICE IT DONT NEED TO MODIFY THE STOPLOSS AGAIN
    #         AFTER THAT isTargetModified HAS SET TO FALSE.    MEANS = AFTER MODIFIED THE STOPLOSS THE CODE WILL ONLY BE ABLE TO MODIFY TARGET
    

      








"""










