from _datetime import datetime, timedelta
import re
import calendar

name = "sukanya"
def calculator(year):
            date = datetime.now()
            current_date = date.year
            age = current_date-year
            print("hellooooo %s your age is: %d"%(name, age))

loop="f"
while (loop=="f"):
        dob = input("enter date in mm/dd/yyyy")
        date=dob
        pattern = re.match('[0-9]{1,2}/?[0-9]{1,2}/?[0-9]{2,4}',dob)
        if pattern is not None:
            month, day, year = map(int,dob.split('/'))
            if (day<= 31 and month<=12 and year <=2015):
                d=datetime.strptime(date,"%m/%d/%y")
                print(d)


                calculator(year)
                loop = "t"
            else:
                print("enter the date in correct format  mm/dd/yyyy")
                loop = "f"
        else:
                print("enter the date in correct format")
                loop = "f"





