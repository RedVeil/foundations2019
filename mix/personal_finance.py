import csv

day = []
usecase = []
recipient = []
recipient_account = []
amount = []
heavy_recipients = {}
unique_recipients = {}
small_recipients = {}
medium_recipients = {}

with open("C:/Users/Leon/Desktop/umsatz1.csv", "r") as umsatz:
        table = csv.reader(umsatz)
        split_lst = []
        for row in table:
            a = ",".join(row)
            split_lst.append(a)
        for i in split_lst:
            day.append(i.split(";")[1])
            usecase.append(i.split(";")[5])
            recipient.append(i.split(";")[-6])
            recipient_account.append(i.split(";")[-5])
            amount.append(i.split(";")[-3])

#411 days

for i in recipient:
    if i not in unique_recipients:
        unique_recipients[i] = 1
    elif i in unique_recipients:
        unique_recipients[i] += 1

for key,value in unique_recipients.items():
    if value <= 2:          #2,5% oder 10.275 orders
        small_recipients[key] = value
    elif value <= 10:
        medium_recipients[key] = value
    else:
        heavy_recipients[key] = value 

print(medium_recipients)
