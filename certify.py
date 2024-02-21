import calendar
from datetime import date, timedelta

def next_wednesday():
    # Get the current date
    today = date.today()

    # Calculate the days until the next Wednesday (assuming today is not Wednesday)
    days_until_wednesday = (calendar.WEDNESDAY - today.weekday() + 7) % 7

    # Calculate the date of the next Wednesday
    next_wednesday_date = today + timedelta(days=days_until_wednesday)

    
    month = next_wednesday_date.month

    if month == 1:
        month = "JAN"
    elif month == 2:
        month = "FEB"
    elif month == 3:
        month = "MAR"
    elif month == 4:
        month = "APR"
    elif month == 5:
        month = "MAY"
    elif month == 6:
        month = "JUN"
    elif month == 7:
        month = "JUL"
    elif month == 8:
        month = "AUG"
    elif month == 9:
        month = "SEP"
    elif month == 10:
        month = "OCT"
    elif month == 11:
        month = "NOV"
    elif month == 12:
        month = "DEC"

    dateDict = {
        "day": str(next_wednesday_date.day),
        "month": str(month)

    }




    return dateDict

