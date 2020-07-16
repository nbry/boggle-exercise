from boggle import Boggle
from flask import Flask, render_template

app = Flask(__name__)

boggle_game = Boggle()

@app.route('/')
def home_page():
    board = boggle_game.make_board()
    return render_template('board.html', board=board)