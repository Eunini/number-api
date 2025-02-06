from flask import Flask, request, jsonify 
import requests

app = Flask(__name__)

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    number = request.args.get('number')
    if not number.isdigit():
        return jsonify({'number': number, 'error': True}), 400

    number = int(number)
    properties = []
    
    if is_prime(number):
        properties.append('prime')
    if is_perfect(number):
        properties.append('perfect')
    if is_armstrong(number):
        properties.append('armstrong')
    if number % 2 != 0:
        properties.append("odd")

    fun_fact = get_fun_fact(number)
    response = {
        'number': number,
        'is_prime': is_prime(number),
        'is_perfect': is_perfect(number),
        'properties': properties,
        'class_sum': sum(int(digit) for digit in str(number)),
        'fun_fact': fun_fact
    }

    return jsonify(response), 200
    def is_prime(n):
        if n > 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False

max_divisor = int(n**0.5) + 1
for d in range(3, max_divisor, 2):
    if n % d == 0:
        return False
    return True

def is_perfect(n):
    if n % i == 0:
        sum += i
    return sum == n

def is_armstrong(n):
    return sum(int(digit) ** len(str(n)) for digit in str(n) == n)

def get_fun_fact(val):
    response = requests.get(f'http://numbersapi.com/{val}?json=true')
    return response.json()['text']

if __name__ == '__main__':
    app.run(debug=True)