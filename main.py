from flask import Flask, render_template, request
from datetime import datetime
from crawler.爬蟲_Yahoo股市 import get_one_page_data
# import json

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/yahoo")
def get_yahoo_data():
    title, datas = get_one_page_data()
    # print(datas)
    price = [i[2] for i in datas]
    return render_template("Yahoo.html", title=title, datas=datas, price=price)


@app.route("/yahoo_charts")
def get_yahoo_charts():
    return render_template("Yahoo_charts.html")


if __name__ == "__main__":
    app.run(debug=True)
