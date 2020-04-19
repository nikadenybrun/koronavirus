from flask import Flask, render_template, request, redirect, url_for

from datetime import datetime

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def start_page():
    return render_template('kvest1.html')

@app.route('/mmm_soap')
def kvest2():
    return render_template("kvest2.html")

@app.route('/black_boomer')
def kvest3():
    return render_template("kvest3.html")


@app.route('/isolation')
def kvest4():
    return render_template("kvest4.html")

@app.route('/oxxxymiron')
def kvest5():
    return render_template("kvest5.html")

@app.route('/cube_game')
def kvest6():
    return render_template("kvest6.html")

@app.route('/interesting_story')
def kvest7():
    return render_template("kvest7.html")

@app.route('/yt_is_what_i_love')
def kvest8():
    return render_template("kvest8.html")

@app.route('/easier_then_you_think')
def kvest9():
    return render_template("kvest9.html")

@app.route('/end_of_the_line')
def kvest10():
    return render_template("kvest10.html")

@app.route('/home')
def description():
    return render_template("home.html")






if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)
