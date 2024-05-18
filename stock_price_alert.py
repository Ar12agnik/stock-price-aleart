from typing import Optional
from nselib import capital_market as cm
from nselib import trading_holiday_calendar
import mysql.connector as connector
from  sendmail_app import send_mail_msg
import time
from datetime import datetime
#Universal stuff(this needs to run to connect to database)
connection = connector.connect(
        host="localhost",  # Your host name
        user="root",   # Your MySQL username
        password="",  # Your MySQL password
        database="investment_app"  # Your MySQL database name
    )
cursor=connection.cursor()
def save_investments(symbol:str,price:int,no_of_shares:int)->bool:
    Total=price*no_of_shares
    try:
        queay=f"INSERT INTO `shares_owned` (`Symbol`, `Price`, `No_of_shares`, `Total`) VALUES (NULL, '{symbol}', '{price}', '{no_of_shares}', '{Total}');"
        cursor.execute(queay)
        connection.commit()
        return True
    except:
        return False
def view_investments(symbols:Optional[str]=None)->list:
    if not symbols:
        cursor.execute("SELECT * FROM `shares_owned`;")
        all_details = cursor.fetchall()
    else:
        queary = f"SELECT * FROM `shares_owned` WHERE Symbol LIKE '{symbols}';"
        cursor.execute(queary)
        all_details=cursor.fetchall()
    return all_details
def check_investment(symbol:str,price:int)->int:
    data=cm.price_volume_and_deliverable_position_data(symbol,period='1D')
    #print(data)
    Last_price=data.iloc[-1]['LastPrice']
    #print(Last_price)
    if price<Last_price:
        return f"Congracs! you are running in profit for {symbol} for ₹{Last_price-price} rounded off to 0 decimal places"
    else:
        send_mail_msg(f"You are Running on loss on {symbol} for ₹{price-Last_price} pre stock!! please do the nesessory things!!")
def view_overall_performance():
    queary="SELECT * FROM shares_owned; "
    cursor.execute(queary)
    total=cursor.fetchall()
    return total
from datetime import datetime, time

def is_current_time_in_range():
    # Get the current time
    current_time = datetime.now().time()

    # Define the start and end time
    start_time = time(9, 15)  # 9:15 AM
    end_time = time(15, 30)   # 3:30 PM

    # Check if the current time is within the range
    return start_time <= current_time <= end_time

# Check if the current time is in range and print the result

#print(trading_holiday_calendar())
def holiday_or_not():
    
    trading_holiday=trading_holiday_calendar()
    a=trading_holiday['tradingDate']
    holiday_list=[]
    for i in a:
        holiday_list.append(i)
    today_date = datetime.today()
    formatted_date = today_date.strftime('%d-%b-%Y')
    return formatted_date in holiday_list or (today_date.weekday() in [5,6])



while True:
    if holiday_or_not():
        print("today is trading hollyday!")
        print("BYE!")
        input("press enter to exit....")
        break
    else:
        is_in_range = is_current_time_in_range()
        if is_in_range:
            
            total=view_overall_performance()
            symbols={}
            for i in total:
                symbols[i[1]]=i[2]
            for key in symbols:
                x=check_investment(key,int(symbols[key]))
            time.sleep(7200)
        else:
            pass






      
# a=view_investments()
# print(a)



##'kctg tgwo cuii ggqg'
    
    
    
    






# print(trading_holiday_calendar())
# x=input("enter the symbol of the stock you want to check last price:")
# a=cm.price_volume_and_deliverable_position_data(symbol=x,period="1D")
# print(a.iloc[1]['LastPrice'])
# def save_investments(Symbol,price_per_share,no_of_shares):