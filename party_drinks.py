#list of your friends and their favorite drink
favorite_drinks = { "David": "Beer","Elias":"Water", "Katya":"Whisky Sour", "Behnaz": "Gin Tonic", "Winston":"Ginger Beer", "Tilli":"Whisky Coke","Leon":"Moscow Mule", "Viktoria":"Gin Tonic"}

favorite_drinks2 = { "David": "Beer","Elias":"Water", "Katya":"Whisky Sour", "Behnaz": "Gin Tonic", "Winston":"Ginger Beer", "Tilli":"Whisky Coke","Leon":"Moscow Mule", "Viktoria":"Gin Tonic",'Adam':'Gin Tonic','Angela':'Mate Vodka','Sven':'Whiskey','Alexandra':'Whiskey',
'Michael':'White Wine','Ariana':'Gin Tonic','Thomas':'beer','Eduardo':'White Wine', 'Leanne':'Red Wine', 'Karla':'Whiskey', 'Taylor': 'Mate Vodka','Jonathan':'Water', 'Katja':'Whiskey Sour', 'Behnaz':'Gin Tonic', 'Leon':'Moscow Mule', 'Viktoria':'Gin Basil', 'Winston':'Ginger Beer', 'Tilli':'Whiskey Coke', 'David':'Beer', 'Elias':'Water'}

drinks= {"cocktails":['gin tonic', 'mate vodka', 'whisky coke',"moscow mule", "whisky sour"],"wines":['red wine', 'white wine'],"liquors":['whiskey', 'gin', 'vokda'],"nonalcoholic":['tea', 'water', 'orange juice',"ginger beer"],"beer":["beer",]}

number_of_drinks_per_hour_per_type = {'cocktails':1, 'beer':3,'wines':2,'liquors':2,'nonalcoholic':3}
total_drinks = {"cocktails":0, 'beer':0,'wines':0,'liquors':0,'nonalcoholic':0}

def append_drink(value):
    pass





def drinks_needed(favorite_drinks, drinks, number_of_drinks_per_hour_per_type):
    for key, value in favorite_drinks.items():
        for x,y in drinks.items():
            if value.lower() in y:
                total_drinks[x] += number_of_drinks_per_hour_per_type[x]*6
            #else:
                #append_drink(value)
                print(total_drinks)
        return total_drinks

print(drinks_needed(favorite_drinks2, drinks, number_of_drinks_per_hour_per_type))