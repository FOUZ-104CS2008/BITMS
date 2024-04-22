#home work
#zellers according march is first month
# formula: f=k+[(13*m-1)/5] + D + [D/4] + [c/4] -2*C.
#zeller according 0 is sunday
date=int(input("enter the date:"))
month=int(input("enter the month:"))
year=int(input("enter the year:"))
month=month-2
'''if month<3:
    month +=10
else:
    month -=10'''

c=year//100
d=year%100
f=date+((13*month-1)/5) + d + (d/4) + (c/4) -2*c
test=int(f%7)
day={0:"Sunday",1:"Monday",2:"Tuesday",3:"wednesday",4:"thursday",5:"friday",6:"saturday"}
print(day[test])

def CheckLeap(year):
    if((year%400==0)or(year%100!=0)and(year%4==0)):
        print("it is leaper")
    else:
        print("not leaper")
CheckLeap(year)