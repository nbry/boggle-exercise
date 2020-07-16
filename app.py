from boggle import Boggle
from flask import Flask, render_template, session, redirect, request, jsonify

app = Flask(__name__)
app.config['SECRET_KEY'] = "aw9rg87ar98ga7r896a9reh"

boggle_game = Boggle()

# def check_for_active_board():
#     if session['board']:
#         active_board = session['board']
#     return active_board


@app.route('/')
def home_page():
    # if session['board']:
    #     active_board = session['board']
    new_board = boggle_game.make_board()
    session['board'] = new_board
    session['words'] = []
    active_board = session['board']
    return render_template('board.html', board=active_board)


@app.route('/<guess>')
def check_guess_json(guess):
    result = boggle_game.check_valid_word(session['board'], guess)
    if guess in session['words'] and result == "valid word!":
        data_dict = {"result": "word already submitted", "word": guess}
    elif guess not in session['words'] and result == "valid word!":
        current_list = session['words']
        current_list.append(guess)
        session['words'] = current_list
        data_dict = {"result": result, "word": guess} 
    else:
        data_dict = {"result": result, "word": guess}
         
    return jsonify(data_dict)

