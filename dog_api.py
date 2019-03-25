import json
import urllib.request as request

content = request.urlopen("https://dog.ceo/api/breeds/image/random").read()
img = json.loads(content)["message"]


html_file = open("dog_api.html", "w")

message = """
<html>
<head></head>
<body>
<img src={} alt="Good Boy">
</body>
</html>""".format(img)

html_file.write(message)
html_file.close