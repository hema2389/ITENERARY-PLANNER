from flask import Flask, jsonify
from flask_cors import CORS
from blueprints.crowd import crowd_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(crowd_bp)

@app.errorhandler(Exception)
def handle_exception(e):
    """Global exception handler."""
    return jsonify({
        "error": "An unexpected error occurred",
        "message": str(e)
    }), 500

@app.route('/')
def index():
    return "Welcome to the Anti-Overtourism Planning Agent Backend!"

if __name__ == '__main__':
    app.run(debug=True)
