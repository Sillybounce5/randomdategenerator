import os
import sys
import random
from time import sleep as wait
import text
from text import sprintpro
import datetime
from datetime import date
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
today = date.today()

def past():
    finmonths = random.choice(months)
    if finmonths == "Jan":
        finmo = 1
        long="january"
    elif finmonths == "Feb":
        finmo=2
        long="february"
    elif finmonths == "Mar":
        finmo=3
        long="march"
    elif finmonths == "Apr":
        finmo=4
        long="april"
    elif finmonths =="May":
        finmo=5
        long="may"
    elif finmonths == "Jun":
        finmo=6
        long="june"
    elif finmonths == "Jul":
        finmo=7
        long="july"
    elif finmonths == "Aug":
        finmo=8
        long="august"
    elif finmonths == "Sep":
        finmo=9
        long = "september"
    elif finmonths == "Oct":
        finmo=10
        long = "october"
    elif finmonths == "Nov":
        finmo=11
        long = "november"
    elif finmonths == "Dec":
        finmo=12
        long = "december"
    finmo=int(finmo)
    findat = str(random.randint(1,29))
    if int(findat) < 10:
        findat = str(0+int(findat))
    finyear = str(random.randint(1800,2021))
    finall= finmonths +" "+ findat +" "+ finyear + " Find more at https://todayago.com/days/"+long+"-"+findat
    if int(finyear) > int(today.strftime("%Y")):
        past()
    else:
        return finall
def future():
    finmonths = random.choice(months)
    if finmonths == "Jan":
        finmo = 1
    elif finmonths == "Feb":
        finmo=2
    elif finmonths == "Mar":
        finmo=3
    elif finmonths == "Apr":
        finmo=4
    elif finmonths =="May":
        finmo=5
    elif finmonths == "Jun":
        finmo=6
    elif finmonths == "Jul":
        finmo=7
    elif finmonths == "Aug":
        finmo=8
    elif finmonths == "Sep":
        finmo=9
    elif finmonths == "Oct":
        finmo=10
    elif finmonths == "Nov":
        finmo=11
    elif finmonths == "Dec":
        finmo=12
    finmo=int(finmo)
    findat = str(random.randint(1,29))
    finyear = str(random.randint(2020,2100))
    finall= finmonths +" "+ findat +" "+ finyear 
    if int(finyear) < int(today.strftime("%Y")):
        future()
    else:
        return finall
def custom():
    finmonths = random.choice(months)
    if finmonths == "Jan":
        finmo = 1
    elif finmonths == "Feb":
        finmo=2
    elif finmonths == "Mar":
        finmo=3
    elif finmonths == "Apr":
        finmo=4
    elif finmonths =="May":
        finmo=5
    elif finmonths == "Jun":
        finmo=6
    elif finmonths == "Jul":
        finmo=7
    elif finmonths == "Aug":
        finmo=8
    elif finmonths == "Sep":
        finmo=9
    elif finmonths == "Oct":
        finmo=10
    elif finmonths == "Nov":
        finmo=11
    elif finmonths == "Dec":
        finmo=12
    finmo=int(finmo)
    findat = str(random.randint(1,29))
    start = int(input("Start Year:"))
    end = int(input("End Year:"))
    finyear = str(random.randint(start,end))
    finall= finmonths +" "+ findat +" "+ finyear 
    return finall
