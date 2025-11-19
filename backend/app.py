from flask import Flask, send_from_directory, jsonify
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='static', static_url_path='')
CORS(app)

@app.route("/ping")
def ping():
    return jsonify({"message": "pong"})

def find_index_html(directory):
    """Recursively find index.html in directory and return relative path"""
    for root, dirs, files in os.walk(directory):
        if 'index.html' in files:
            # Return the relative path from the game directory
            rel_path = os.path.relpath(root, directory)
            if rel_path == '.':
                return 'index.html'
            return os.path.join(rel_path, 'index.html').replace('\\', '/')
    return None

@app.route("/api/games")
def get_games():
    """Dynamically fetch all games from static/games folder"""
    games_path = os.path.join('static', 'games')
    games = []
    game_id = 1
    
    if os.path.exists(games_path):
        for game_dir in sorted(os.listdir(games_path)):
            game_full_path = os.path.join(games_path, game_dir)
            if os.path.isdir(game_full_path):
                # Recursively find index.html
                index_path = find_index_html(game_full_path)
                
                if index_path:
                    # Clean up game name for display
                    game_name = game_dir.replace('-', ' ').replace('---', ' - ').title()
                    game_url = f'http://localhost:5000/games/{game_dir}/{index_path}'
                    
                    print(f"Found game: {game_name} -> {game_url}")  # Debug log
                    
                    games.append({
                        'id': game_id,
                        'title': game_name,
                        'description': f'Play {game_name} now!',
                        'url': game_url,
                        'instructions': 'Use your keyboard or mouse to play.',
                        'rating': '4.5',
                        'players': '1,000+'
                    })
                    game_id += 1
    
    return jsonify(games)

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/games/<path:filename>')
def games(filename):
    return send_from_directory('static/games', filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
