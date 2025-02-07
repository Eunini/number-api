from flask import Flask, request, jsonify
from flask_cors import CORS  # Handles Cross-Origin Requests
import requests

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    return sum(i for i in range(1, abs(n)) if n % i == 0) == abs(n)  # Handle negative numbers correctly

def is_armstrong(n):
    num_str = str(abs(n))  # Use absolute value for digit calculations
    return sum(int(digit) ** len(num_str) for digit in num_str) == abs(n)

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
    number_str = request.args.get('number')

    try:
        # Allow both integers and floats
        number = float(number_str)
    except (TypeError, ValueError):
        return jsonify({"number": "alphabet", "error": True}), 400

    properties = []
    
    if number.is_integer():
        number = int(number)  # Convert to integer for further checks

        if is_armstrong(number):
            properties.append("armstrong")
        properties.append("odd" if number % 2 != 0 else "even")

    response = {
        "number": number,
        "is_prime": is_prime(int(number)) if number.is_integer() and number > 0 else False,
        "is_perfect": is_perfect(int(number)) if number.is_integer() and number > 0 else False,
        "properties": properties,
        "digit_sum": sum(int(digit) for digit in str(abs(int(number)))),
        "fun_fact": get_fun_fact(int(number)) if number.is_integer() else get_fun_fact(number)
    }
    return jsonify(response), 200

if __name__ == "__main__":
    app.run(debug=True)