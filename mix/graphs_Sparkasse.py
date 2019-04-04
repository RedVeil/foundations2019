import numpy as np
from matplotlib import pyplot as plt


def show_graph(year):
    food, rent, games, phone, internet, food_outside, crypto, rest, expense_titles = prepare_lists(year)
    months = ["jan", "feb", "mrz", "apr", "mai",
              "jun", "jul", "aug", "sep", "okt", "nov", "dez"]

    food = np.array(food)  
    rent = np.array(rent)
    games = np.array(games)
    phone = np.array(phone)
    internet = np.array(internet)
    food_outside = np.array(food_outside)
    crypto = np.array(crypto)
    rest = np.array(rest)

    x = len(months)
    z = np.arange(x)


    p1 = plt.bar(z, rent)
    p2 = plt.bar(z, internet, bottom=rent)
    p3 = plt.bar(z, phone, bottom= rent+internet)
    p4 = plt.bar(z, food, bottom= rent+internet+phone)
    p5 = plt.bar(z, games, bottom= rent+internet+phone+food)
    p6 = plt.bar(z,food_outside, bottom=rent+internet+phone+food+games)
    p7 = plt.bar(z,rest, bottom=rent+internet+phone+food+games+food_outside)
    p8 = plt.bar(z,crypto, bottom=rent+internet+phone+food+games+food_outside+rest)

    plt.xticks(z,months,rotation=90)

    plt.show()



def prepare_lists(year):
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
        return food, rent, games, phone, internet, food_outside, crypto, rest, expense_titles