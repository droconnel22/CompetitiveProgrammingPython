# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
from datetime import datetime
if __name__ == "__main__": 
    month,day,year = map(int,input().strip().split())
    date = datetime(year=year,day=day, month=month)
    print(str(calendar.day_name[date.weekday()]).upper())
    