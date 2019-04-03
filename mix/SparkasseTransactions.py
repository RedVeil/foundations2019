import csv

# 411 days

# step 1.1  - class for days with all necessary attributes


class Transaction:
    def __init__(self, day, usecase, recipient, recipient_account, amount, category=None):
        self.day = day
        self.usecase = usecase
        self.recipient = recipient
        self.recipient_account = recipient_account
        self.amount = amount
        self.category = category


class Month:

    def __init__(self, name, transactions):
        self.name = name
        self.transactions = transactions
        self.sum_food = 0
        

    def __str__(self):
        return f"{self.name}: Food: {self.sum_food}"

    #@property
    def sum_food(self):
        return self.sum_food if self.sum_food else self.calculate_sums("food")

    def find_category(self, category):
        food=["DE91700202700015820755", "DE75200907004055624073",
            "DE03200907002535050071", "DE68750200730008472092"]
        for transaction in self.transactions:
            for i in food:
                if i in transaction.recipient_account:
            #if "DE91700202700015820755" in transaction.recipient_account:
                    transaction.category = "food"
        # check if any transaction_account amtches items in list matching to passed category

    def calculate_sums(self, category):
        for transaction in self.transactions:
            self.find_category(category)
            if transaction.category == "food":
                str(transaction.amount).strip()
                self.sum_food += float(transaction.amount)
        return self.sum_food


    

# step3.1 - take days and sort them in to years
def break_years(transactions_list):
    year2019 = []
    year2018 = []
    for transaction in transactions_list:
        if transaction.day[-2] == "9":
            year2019.append(transaction)
        elif transaction.day[-2] == "8":
            year2018.append(transaction)
    return year2019, year2018

# step3.2  - split years in to months compared to table in step 2
def split_into_months(month_num, year_list):
    temp_lst = []
    for transaction in year_list:
        if int(transaction.day[4:6]) == month_num:
            temp_lst.append(transaction)
    return temp_lst

# step 3 - call functions to split das into years and months
def call_months(transactions_list):
    months2019 = []
    months2018 = []
    year2019, year2018 = break_years(transactions_list)
    months = ["", "jan", "feb", "mrz", "apr", "mai",
              "jun", "jul", "aug", "sep", "okt", "nov", "dez"]
    for i in range(1, 12):
        months2018.append(Month(months[i], split_into_months(i, year2018)))
    for i in range(1, 12):
        months2019.append(Month(months[i], split_into_months(i, year2019)))
    return months2018, months2019

# step2.1   - check for different "classes" of recipients
def recipient_frequency(recipients):
    small_recipients={}
    medium_recipients={}
    heavy_recipients={}
    for key, value in recipients.items():
        if value <= 2:  # 2,5% oder 10.275 orders
            small_recipients[key]=value
        elif value <= 10:
            medium_recipients[key]=value
        else:
            heavy_recipients[key]=value
    return small_recipients, medium_recipients, heavy_recipients

# step 2  -   check for unique recipients for sorting
def unique_recipients(transactions_list):
    recipients={}
    for transaction in transactions_list:
        if transaction.recipient not in recipients:
            recipients[transaction.recipient]=1
        elif transaction.recipient in recipients:
            recipients[transaction.recipient] += 1
    return recipient_frequency(recipients)


def categorie(month_list):
    essen_account=["DE91700202700015820755", "DE75200907004055624073",
                     "DE03200907002535050071", "DE68750200730008472092"]
    essen=[]
    paypal=[]
    for month in month_list:
        for transaction in month:
            if "DE91700202700015820755" in transaction.recipient_account or "DE75200907004055624073"in transaction.recipient_account or "DE03200907002535050071" in transaction.recipient_account or "DE68750200730008472092" in transaction.recipient_account:
                essen.append(transaction)
            elif "DE88500700100175526303" in transaction.recipient_account:
                paypal.append(transaction)

    return essen, paypal


# step 1 - open table, sort in to object and than those in to a list (days)
if __name__ == "__main__":
    with open("C:/Users/Leon/Desktop/umsatz.csv", "r") as umsatz:
        table=csv.reader(umsatz)
        split_lst=[]
        transactions=[]
        for row in table:
            a=",".join(row)
            b = a.replace(",",".")
            split_lst.append(b)
        for i in split_lst:
            transactions.append(Transaction(i.split(";")[1], i.split(
                ";")[4], i.split(";")[-6], i.split(";")[-5], i.split(";")[-3]))
        transactions.reverse()
        small_recipients, medium_recipients, heavy_recipients=unique_recipients(
            transactions)
        months2018, months2019=call_months(transactions)
        for i in months2018:
            i.calculate_sums("food")
            print(i.sum_food)



# sort recipients in to groups
# compare days in months with groups
# create monthly + yearly statistics
# create charts

# or
