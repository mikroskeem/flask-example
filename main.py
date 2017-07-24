#!/usr/bin/env python3

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def main_page():
    """The home page renderer"""
    return render_template("home.html")

app.debug = True
app.run()
