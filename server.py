"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return """<!doctype html><html><a href="/hello">Hi! This is the home page.</a></html>"""


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet" method="POST">
          What's your name? <input type="text" name="person"><br />
          Select compliment: <input type="checkbox" name="compliment" value="Good Boy">Good Boy
          <input type="checkbox" name="compliment" value="Good Girl">Good Girl
          <input type="checkbox" name="compliment" value="Good Enby">Good Enby<br />
          <input type="submit" value="Submit">
        </form><br />
        <form action="/diss">
          What's your street name? <input type="text" name="nickname"><br />
          Select insult: <input type="radio" name="diss" value="Big Turd">Big Turd
          <input type="radio" name="diss" value="Bully">Bully
          <input type="radio" name="diss" value="Loser">Loser<br />
          <input type="submit" value="Submit">
      </body>
    </html>
    """


@app.route('/greet', methods=["POST"])
def greet_person():
    """Get user by name."""

    player = request.form.get("person")

    # compliment = choice(AWESOMENESS)
    compliment = request.form.getlist("compliment")
    # returns list so would need another function to loop over list to pull in
    # multiple choices, perhaps to create a string to then pass through as
    # compliment, etc.

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're a {compliment}!
      </body>
    </html>
    """.format(player=player, compliment=compliment)


@app.route('/diss')
def diss_person():
    """Get user by name."""

    player = request.args.get("nickname")

    # compliment = choice(AWESOMENESS)
    diss = request.args.get("diss")

    return """
    <!doctype html>
    <html>
      <head>
        <title>An Insult</title>
      </head>
      <body>
        Hi, {player}! I think you're a {diss}!
      </body>
    </html>
    """.format(player=player, diss=diss)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
