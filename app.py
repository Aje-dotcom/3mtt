import os
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains

API_KEY = os.environ.get("OPENWEATHERMAP_API_KEY", "YOUR_API_KEY_HERE")  # Replace with your real API key

@app.route('/weather')
def get_weather():
    city = request.args.get('city', 'London')
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    resp = requests.get(url)
    if resp.status_code == 200:
        return jsonify(resp.json())
    else:
        return jsonify({'error': 'City not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)