from flask import Flask, app, render_template
app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/about")
def deep():
    name = "deepratan"
    return render_template("about.html", name=name)


app.run(debug=True)
