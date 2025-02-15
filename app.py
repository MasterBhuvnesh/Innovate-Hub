from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

with open('data.json', 'r', encoding='utf-8') as file:
    platforms = json.load(file)

@app.route('/')
def index():
    return render_template('index.html', platforms=platforms, title="Innovate Hub")

@app.route('/api', methods=['GET'])
def get_platforms():
    return jsonify(platforms)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)