from datetime import time, timedelta
from datetime import date
from datetime import datetime

def main():
    today = date.today()
    print("Today is : ",today)
    print("Year component : ",today.year)
    print("month component : ",today.month)
    print("Day component : ",today.day)
    print("Today's weekDay : ",today.weekday())
    days = ["mon","tues","wed","thus","fri","sat","sun"]
    print("today's weekday is : ",days[today.weekday()])

    # DateTime Objects
    current = datetime.now()
    print("Current DateTime is : ",current)
    timme = datetime.time(datetime.now())
    print("Local Time : ",timme)

# Date Funtioning
    print(current.strftime("%A, %D %B,%Y"))
    print(current.strftime("%a, %d %b,%y"))
    print("Local Date and Time :",current.strftime("%c"))
    print("Local Date : ",current.strftime("%x"))
    print("Local time ",current.strftime("%X"))


    print("Local current time ",current.strftime("%I:%M:%S %p"))
    print("Local time-24 Hour  ",current.strftime("%H:%M %p"))

    # TimeDelta Object-it's a span of time
    noww = datetime.now()
    print("One year from now will be : ",str(noww + timedelta(days=365)))
    print("from today,after 2 weeks & 2 days it will be : ",noww + timedelta(weeks=2,days=2))
    print("from today,Before 2 weeks it was : ",noww - timedelta(weeks=1))












if __name__ == '__main__':
    main()






