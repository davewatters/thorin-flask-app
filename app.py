import os
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

# @app.route('/')
# def index():
#     return '<h1>Hello, world</h1> - baby! Oh yeah oh yeah'


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)

    print(os.environ.get("IP"))
    print(os.environ.get("PORT"))
