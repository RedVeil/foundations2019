destinations = ["Paris, France",
"Shanghai, China",
"Los Angeles, USA",
"So Paulo, Brazil",
"Cairo, Egypt"]

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]


def get_destination_index(destination):
    destination_index = -1
    for i in destinations:
        destination_index += 1
        if i == destination:
            return destination_index

def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  return get_destination_index(traveler_destination)

test_destination_index = get_traveler_location(test_traveler)
print(test_destination_index)


attractions = [[] for things in destinations]
print(attractions)

def add_attractions(destination, attraction):
  try:
  	destination_index = get_destination_index(destination)
  except ValueError:
    return
  attractions_for_destination = attractions[destination_index]
  attractions_for_destination.append(attraction)
  return attractions_for_destination



add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])
