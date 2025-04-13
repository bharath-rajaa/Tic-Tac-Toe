from flask import Flask, request, jsonify
from tic_tac_toe import TicTacToe  # your existing class

app = Flask(__name__)

game = TicTacToe()

@app.route('/move', methods=['POST'])
def move():
    data = request.get_json()
    position = data['position']
    result = game.make_move(position)

    response = {
        'board': game.board,
        'message': result['message'],
        'game_over': result['game_over']
    }
    return jsonify(response)

@app.route('/reset', methods=['POST'])
def reset():
    game.reset()
    return jsonify({'board': game.board})

if __name__ == '__main__':
    app.run(debug=True)
