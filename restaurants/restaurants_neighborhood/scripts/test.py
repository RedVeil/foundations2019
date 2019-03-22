import database as d



def list_restaurants(name,area):
    list_restaurants = """"""
    for name in d.name:
        index = d.name.index(name)
        if d.area[index] == area:
            list_restaurants += "<li>{}</li>\n".format(name)
    return list_restaurants


v_area = int(input(""))
print(type(v_area))
message = "{}".format(list_restaurants(d.name, v_area))
print(message)