import csv
from matplotlib import pyplot as plt
# 411 days

# step 1.1  - class for days with all necessary attributes
category_dict={"food":["DE91700202700015820755", "DE75200907004055624073",
            "DE03200907002535050071", "DE68750200730008472092","DE48300500000001108018","DE61300500000008000119","DE34302201900024938816"],"games":["DE88500700100175526303"], 
            "income":["DE78100500001064858054", "DE77100500000054026601","DE80150505001231063951",
            "DE80100500006012217500","DE04100208900355448533","DE97100700240728665100"], 
            "rent":["DE55100800000324360600","DE34120300001018874717"], "phone" : ["DE49700400410225563601","DE16700202700005713153"],
            "crypto" : ["EE957700771001355096","EE297700771001961370"], "internet":["DE13380700590045335700"]}
game_accounts = ["STEAM GAMES", "G2ACOMLIMIT","UBISOFT","INSTANTGAMI","HUMBLEBUNDL","HRK GAME","SWTOR"]

#food - Rewe, Edeka, Netto, Real  -- aufsplitten in outside essen, alc -- bargeld (auszahlungen) einbauen
# games -- (paypal) in games und anderes unterteilen (achtung auch income)
# income - hermann, mutter, oma, tom, arne, swantje -- paypal einbauen(tiff?)
# rent - hermann, jakob strom
#  





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
        self.sum_games = 0
        self.sum_income = 0
        self.sum_rent = 0
        self.sum_phone = 0
        self.sum_internet = 0
        self.sum_rest = 0
        self.sum_crypto = 0
        self.sum_food_outside = 0
        self.sum_total = 0
        #self.sum_alcohol_and_bars = 0

        

    def __str__(self):
        return f"{self.name}: Food: {self.sum_food}"

    #@property
    def sum_food(self):
        return self.sum_food if self.sum_food else self.calculate_sums("food")

    def find_category(self):
        categories = []
        for x in category_dict.keys():
            categories.append(x)
        for transaction in self.transactions:
            for i in categories:
                for account in category_dict[i]:
                    if account in transaction.recipient_account:
                        transaction.category = i


    def gamecheck(self,transaction):
        for account in game_accounts:
            if account in transaction.usecase[13:]:
                return True
        

    def calculate_sums(self):
        for transaction in self.transactions:
            if transaction.category == "food":
                self.sum_food += float(transaction.amount)*-1
            elif transaction.category == "games":
                if self.gamecheck(transaction):
                    self.sum_games += float(transaction.amount)*-1
                else:
                    self.sum_rest += float(transaction.amount)*-1
            elif transaction.category == "income":
                self.sum_income += float(transaction.amount)
            elif transaction.category == "rent":
                self.sum_rent += float(transaction.amount)*-1
            elif transaction.category == "internet":
                self.sum_internet += float(transaction.amount)*-1
            elif transaction.category == "crypto":
                self.sum_crypto += float(transaction.amount)*-1
            elif transaction.category == "phone":
                self.sum_phone += float(transaction.amount)*-1
            else:
                if "GA NR" in transaction.recipient[0:6]:
                    self.sum_food_outside +=float(transaction.amount)*-1
                else:
                    #print(transaction.amount, transaction.recipient, transaction.usecase)
                    self.sum_rest += float(transaction.amount)*-1



    def calculate_total(self):
        for transaction in self.transactions:
            if transaction.category != "income":
                self.sum_total += float(transaction.amount)


def show_graph(year):
        food = []
        rent = []
        games = []
        phone = []
        internet = []
        food_outside = []
        crypto = []
        rest = []
        expense_titles = ["food", "rent", "games", "phone", "internet","food_outside","crypto","rest"]
        for month in year:
            food.append(month.sum_food)
            rent.append(month.sum_rent)
            games.append(month.sum_games)
            phone.append(month.sum_phone)
            internet.append(month.sum_internet)
            food_outside.append(month.sum_food_outside)
            crypto.append(month.sum_crypto)
            rest.append(month.sum_rest)
        print(food)
        plt.bar(range(len(food)),food)
        plt.bar(range(len(food)),rent, bottom=food)
        plt.bar(range(len(food)),games, bottom=rent)
        plt.bar(range(len(food)),phone, bottom=games)
        plt.bar(range(len(food)),internet, bottom=phone)
        plt.bar(range(len(food)),food_outside, bottom=internet)
        plt.bar(range(len(food)),crypto, bottom=food_outside)
        plt.bar(range(len(food)),rest, bottom=crypto)
        plt.legend(expense_titles)
        plt.show()

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
    for i in range(1, 13):
        months2018.append(Month(months[i], split_into_months(i, year2018)))
    for i in range(1, 13):
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
            y = i.split(";")[-3].strip('"')
            transactions.append(Transaction(i.split(";")[1], i.split(
                ";")[4], i.split(";")[-6], i.split(";")[-5], y))
        transactions.reverse()
        small_recipients, medium_recipients, heavy_recipients=unique_recipients(
            transactions)
        months2018, months2019=call_months(transactions)
        x_values = []

        for i in months2018:
            i.find_category()
            i.calculate_sums()
            i.calculate_total()
            #print(f'''
            #total: {i.sum_total}
            #income:{i.sum_income}, food: {i.sum_food}, games: {i.sum_games}, 
            #rent: {i.sum_rent}, internet: {i.sum_internet}, 
            #crypto: {i.sum_crypto}, phone: {i.sum_phone}, food_outside: {i.sum_food_outside} rest: {i.sum_rest}''' )
            #print("___________")
        show_graph(months2018)

        
        
        
           



# sort recipients in to groups
# compare days in months with groups
# create monthly + yearly statistics
# create charts

# or
