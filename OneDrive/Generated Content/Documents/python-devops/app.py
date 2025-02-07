from flask import Flask, request, jsonify
from flask_cors import CORS  # Handles Cross-Origin Requests
import requests
import os
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    return sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong(n):
    num_str = str(n)
    return sum(int(digit) ** len(num_str) for digit in num_str) == n

def get_fun_fact(n):
    try:
        response = requests.get(f"http://numbersapi.com/{n}/math?json=true")
        return response.json().get("text", "No fun fact available.")
    except:
        return "No fun fact available."

app = Flask(__name__)
CORS(app)  # Enable CORS

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    number = request.args.get('number')
    if not number or not number.isdigit():
        return jsonify({"number": number, "error": True}), 400

    number = int(number)
    properties = []
    
    if is_armstrong(number):
        properties.append("armstrong")
    properties.append("odd" if number % 2 != 0 else "even")
    
    response = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": sum(int(digit) for digit in str(number)),
        "fun_fact": get_fun_fact(number)
    }
    return jsonify(response), 200

import os
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

