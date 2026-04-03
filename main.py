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

# Добавили типизацию прямо в URL
@app.route('/calc/<float:a>/<float:b>')
def calculate(a, b):
    try:
        # Теперь a и b уже числа (float)
        return jsonify({"a": a, "b": b, "sum": a + b})
    except ValueError:
        return jsonify({"error": "Invalid input. Please provide numbers."}), 400

if __name__ == '__main__':
    # Оставляем 0.0.0.0 — это залог успеха для Docker + WSL
    app.run(host='0.0.0.0', port=5000)
