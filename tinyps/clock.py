import sys, time
import sevseg


print(time.localtime().tm_year)


year = sevseg.getSevSegStr(str(time.localtime().tm_year))
month = sevseg.getSevSegStr(str(time.localtime().tm_mon))
day = sevseg.getSevSegStr(str(time.localtime().tm_mday))
hour = sevseg.getSevSegStr(str(time.localtime().tm_hour))
mins = sevseg.getSevSegStr(str(time.localtime().tm_min))
sec = sevseg.getSevSegStr(str(time.localtime().tm_sec))


allGuests = {
    "Alice": {"apples": 5, "pretzels": 12},
    "Bob": {"ham sandwiches": 3, "apples": 2},
    "Carol": {"cups": 3, "apple pies": 1},
}


for guests, items in allGuests.items():
    print(guests, "**", items)
