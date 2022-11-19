from cProfile import run
from re import A
from app import app
from flask import render_template
from datetime import date, datetime as dt

@app.route('/')
@app.route('/index')
def index():
    #return "Hello World"
    a = "My name is VISHV"
    return a + """
    <html>
        <head>
            <title> Home </title>
        </head>
        <body>
            <div><a href ="/about"> About Me </a></div>
            <div><a href ="/test"> Test Page <a></div>
            <div><a href ="/test2"> Test2 Page <a></div>
            <div><a href ="/pokemon"> Pokemon Info </a></div>
        </body>
    </html>
    """

@app.route('/about')
def about():
    title = "This is my ABOUT ME page"
    return render_template('about.html', title=title)

@app.route('/test')
def test():
    user = {'username': 'Vishv'}
    age = dt.today() - dt(2020, 1, 11, 7, 44)
    return render_template('test.html', user=user, age=age)

@app.route('/test2')
def test2():
    user = {'username': 'V_Tornadus'}
    sample_data = [
        {'author': {'username': 'V_Tornadus'}, 'body': 'Hello!'},
        {'author' : {'username': 'Vishv'}, 'body': 'Welcome to Flask!'}]
    return render_template('test2.html', user=user, sample_data=sample_data)

@app.route('/pokemon')
def pokemon():
    pokeNews = {
        "Nov 18: ": [{"!!!Game Release!!!": "https://scarletviolet.pokemon.com/"}], 
        "Nov 15: ": [{"Nintendo Final Overview Trailer": "https://www.youtube.com/watch?v=dAQBo9BGRdA"}],
        "Nov 10 - Present: ": [{"Game Datamine + Leaking": "https://docs.google.com/spreadsheets/d/1Ox3SwLFTP0ZfOj-O-1ijn8Im8kU0QnjNyi3AJ6a5feM/htmlview?pru=AAABhIdzvv8*mEw-p-HlUvJ3pJrlJtpjmw#"}],
        "Nov 8: ": [{"A New Chapter in the Pokemon Series Trailer (final trailer)": "https://www.youtube.com/watch?v=ZWFiD5-hhFU"}, 
        {"Gimmighoul Gameplay": "https://www.youtube.com/watch?v=-nzi0S3NGzg"}],
        "Nov 6: ": [{"Gimmighoul Reveal": "https://www.youtube.com/watch?v=HYH1cpAtjEE"}],
        "Oct 25: ": [{"Meet Greavard Gameplay": "https://www.youtube.com/watch?v=TOKBC11D0eI"}, 
        {"A new Ghost-type in Paldea": "https://www.youtube.com/watch?v=PF5UzdmOzPs"}],
        "Oct 20: ": [{"Selected few get to play SV for 1 hr (AustinJohnPlays)": "https://www.youtube.com/watch?v=B7id9nqCLQs"}],
        "Oct 14: ": [{"Iono & Bellibolt Gameplay": "https://www.youtube.com/watch?v=2rABZFQmWII"},
        {"Meet Bellibolt": "https://www.youtube.com/watch?v=PF5UzdmOzPs"}],
        "Oct 12: ": [{"Guess Gym Leader Iono's Partner Pokemon": "https://youtu.be/U9HAaHc3wnc"}],
        "Oct 3: ": [{"Scarlet Violet Overview Trailer": "ttps://www.youtube.com/watch?v=4YEEDqke-D0"}]}
    timeLeft = dt(2022, 11, 18, 21, 0) - dt.today()
    links = {
        "Go back to the Index page": "/",
        "View the Official Pokemon Scarlet Violet Website": "https://scarletviolet.pokemon.com/",
        "View the Official Pokemon Website": "https://www.pokemon.com/"
        }
    return render_template('pokemon.html', pokeNews=pokeNews, timeLeft=timeLeft, links=links)
        