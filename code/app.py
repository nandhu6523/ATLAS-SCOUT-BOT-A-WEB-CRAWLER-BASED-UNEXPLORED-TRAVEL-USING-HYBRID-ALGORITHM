from flask import Flask, render_template, request
from recommender import get_recommendations

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    if request.method == "POST":
        city = request.form["city"]
        limit = int(request.form["limit"])
        results = get_recommendations(city, limit)
    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)
