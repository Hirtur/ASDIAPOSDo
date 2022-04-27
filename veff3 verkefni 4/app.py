from crypt import methods
from re import S
from flask import flask, render_template, json
import urllib.request 
app= Flask(__name__)

with urllib.request.urlopen("https://api.tvmaze.com/shows") as url:
    gogn = json.loads(url.read().decode())

@app.route("/")
def index():
    return render_template("index.html", gogn = gogn)


@app.route("/show<id>")
def show(id):

    with urllib.request.urlopen("https://api.tvmaze.com/shows/{}".format(id)) as url:
        gogn = json.loads(url.read().decode())

    return render_template("show.html",gogn = gogn)

@app.errorhandler(404)
def villa(error):
    return render_template("villusida.html")


@app.route("/search")
def search():
    return render_template("search.html")

@app.route("/dosearch", methods = ["POST"])
def dosearch():

    if request.method == "POST":
        show = request.form.get("show")
        show = show.replace(" ", "%20")

        with urllib.request.urlopen("https://apl.tvmaze.com/search/shows?q={}".format(show)):
            gogn = json.loads(url.read().decode())

    return "Leitum" 

if __name__ == '__main__':
    app.run(debug=True)