from boggle import Boggle
from flask import Flask, render_template, session, redirect, request, jsonify

app = Flask(__name__)
app.config['SECRET_KEY'] = "aw9rg87ar98ga7r896a9reh"

boggle_game = Boggle()

@app.route('/')
def home_page():
    new_board = boggle_game.make_board()
    session['board'] = new_board
    session['words'] = []

    try:
        session['top_score']
    except:
        session['top_score'] = 0
    
    try:
        session['game_attempts']
    except:
        session['game_attempts'] = 0

    active_board = session['board']
    return render_template('board.html', board=active_board, top_score=session['top_score'], attempts=session['game_attempts'])


@app.route('/<guess>')
def check_guess_json(guess):
    result = boggle_game.check_valid_word(session['board'], guess.lower())
    if guess.lower() in session['words'] and result == "valid word!":
        data_dict = {"result": "word already submitted", "word": guess}
    elif guess not in session['words'] and result == "valid word!":
        current_list = session['words']
        current_list.append(guess.lower())
        session['words'] = current_list
        data_dict = {"result": result, "word": guess} 
    else:
        data_dict = {"result": result, "word": guess}
         
    return jsonify(data_dict)

@app.route('/submit-score/<score>')
def update_session(score):
    if int(score) > int(session['top_score']):
        session['top_score'] = int(score)
    
    session['game_attempts'] += 1
        
    data_dict = {"top_score": session['top_score'], "attempts": session['game_attempts']}
    return jsonify(data_dict)