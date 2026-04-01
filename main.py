from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"status": "vibe_check_passed", "msg": "Docker is running!"})

@app.route('/info')
def info():
    return jsonify({
        "developer": "Vostryakov-Vibe",
        "env": "Windows + WSL 2 + Docker",
        "task": "Endpoints & Containerization"
    })

@app.route('/calc/<a>/<b>')
def calculate(a, b):
    try:
        return jsonify({"a": a, "b": b, "sum": float(a) + float(b)})
    except:
        return jsonify({"error": "Please use numbers in URL"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
