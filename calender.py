day=int(input("Enter Day in Date :"))
month=str(input("Enter Month :"))
year=str(input("Enter Year in Date :"))

last=int(year[2:4])#For Last two Digits

#ForLeapYear
year=int(year)
Leap=int(last/4)

#Month Codes   
mC={"1":0,"2":3,"3":3,"4":6,"5":1,"6":4,"7":6,"8":2,"9":5,"10":0,"11":3,"12":5}
monthCode=mC[month]

#year Codes
if (year>=1600 and year<1700) or (year>=2000 and year<2100):
    Sum=6+last+day+monthCode+Leap
elif (year>=1700 and year<1800) or (year>=2100 and year<2200):#yearCode=4
    Sum=4+last+day+monthCode+Leap
elif (year>=1800 and year<1900) or (year>=2200 and year<2300):#yearCode=2
    Sum=2+last+day+monthCode+Leap
elif (year>=1900 and year<2000) or (year>=2200 and year<2300):#yearCode=0
    Sum=0+last+day+monthCode+Leap


#dayCalculation With Day Codes
remimderResult=Sum%7

dayDict={"0":"Sunday",
         "1":"Monday",
         "2":"Tuesday",
         "3":"WednesDay",
         "4":"Thursday",
         "5":"Friday",
         "6":"Saturday"}
print("Are You For ",dayDict[str(remimderResult)])





