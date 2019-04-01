from flask import Flask, render_template
import urllib.request as request
app = Flask(__name__)

def get_pokemon():
    content = request.urlopen(" ").read()
    content = content.decode("UTF-8")
    #img = content[content.find("https"):-2]
    return content

print(get_pokemon())
'''@app.route('/')
def clickingAround():
    content = get_pokemon()
    return render_template("index.html", content = content)

if __name__ == "__main__":
    app.run(port="3000")'''
