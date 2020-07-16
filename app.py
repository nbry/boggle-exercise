from boggle import Boggle
from flask import Flask, render_template, session

app = Flask(__name__)
app.config['SECRET_KEY'] = "aw9rg87ar98ga7r896a9reh"

boggle_game = Boggle()

def check_for_active_board():
    if session['board']:
        active_board = session['board']
    return active_board

@app.route('/')
def home_page():
    if session['board']:
        active_board = session['board']
    new_board    = boggle_game.make_board()
    session['board'] = new_board
    active_board = session['board']
    return render_template('board.html', board=active_board)