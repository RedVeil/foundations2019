import csv

#411 days

#step 1.1  - class for days with all necessary attributes
class Day:
    def __init__(self, day, usecase, recipient, recipient_account, amount):
        self.day = day
        self.recipient = recipient
        self.recipient_account = recipient_account
        self.amount = amount


def recipients_per_month():
    pass

#step3.1 - take days and sort them in to years
def break_years(days_list):
    year2019=[]
    year2018=[]
    for day in days_list:
        if day.day[-2] == "9":
            year2019.append(day)
        elif day.day[-2] == "8":
            year2018.append(day)
    return year2019, year2018

#step3.2  - split years in to months compared to table in step 2 
def split_into_months(month_num, year_list):
    temp_lst = []
    for day in year_list:
        if day.day[4:6] == month_num:
            temp_lst.append(day)
    return temp_lst

#step 3 - call functions to split das into years and months
def call_months(day_list):
    months2019=[]
    months2018=[]
    months_list=[["jan","01"], ["feb", "02"], ["mrz", "03"],["apr", "04"],["mai","05"],["jun","06"],["jul","07"],["aug","08"],["sep","09"],["okt", "10"],["nov","11"],["dez","12"]]
    year2019, year2018 = break_years(day_list)
    for month in months_list: 
        months2018.append(split_into_months(month[1],year2018))
        months2019.append(split_into_months(month[1],year2019))
    return months2018, months2019

#step2.1   - check for different "classes" of recipients
def recipient_frequency(recipients):
    small_recipients = {}
    medium_recipients = {}
    heavy_recipients = {}
    for key,value in recipients.items():
        if value <= 2:          #2,5% oder 10.275 orders
            small_recipients[key] = value
        elif value <= 10:
            medium_recipients[key] = value
        else:
            heavy_recipients[key] = value
    return small_recipients, medium_recipients, heavy_recipients

#step 2  -   check for unique recipients for sorting
def unique_recipients(days_list):
    recipients = {}
    for day in days:
        if day.recipient not in recipients:
            recipients[day.recipient] = 1
        elif day.recipient in recipients:
            recipients[day.recipient] += 1
    return recipient_frequency(recipients)

def usecase(month_list):
    essen = ["DE91700202700015820755", "DE75200907004055624073", "DE03200907002535050071", "DE68750200730008472092"]
    rewe = []
    for month in month_list:
        for day in month:
            if "DE91700202700015820755" in day.recipient_account or "DE75200907004055624073"in day.recipient_account or "DE03200907002535050071" in day.recipient_account or "DE68750200730008472092" in day.recipient_account:
                rewe.append(day)
    print(rewe)
    print(len(rewe))
    

#step 1 - open table, sort in to object and than those in to a list (days)
if __name__=="__main__":
    with open("C:/Users/Leon/Desktop/umsatz.csv", "r") as umsatz:
            table = csv.reader(umsatz)
            split_lst = []
            days = []
            for row in table:
                a = ",".join(row)
                split_lst.append(a)
            for i in split_lst:
                days.append(Day(i.split(";")[1], i.split(";")[5],i.split(";")[-6],i.split(";")[-5], i.split(";")[-3] ))
            days.reverse()
            small_recipients, medium_recipients, heavy_recipients = unique_recipients(days)
            months2018, months2019 = call_months(days) 
            usecase(months2018)
            usecase(months2019)


##sort recipients in to groups
## compare days in months with groups
## create monthly + yearly statistics
## create charts