import json
import urllib.request as request

content = request.urlopen("https://dog.ceo/api/breeds/image/random").read()
content = content.decode("UTF-8")
img = content[content.find("https"):-2]
print(img)


