from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

# Enable CORS for all origins, allow all origins (*), making your API accessible from any domain.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Helper function to check if a number is prime by dividing it by all numbers up to the square root of the number.
def is_prime(num: int) -> bool:
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

"""Helper function to check if a number is perfect. A perfect number is a number that equals the sum of its proper divisors (excluding itself).This function sums the divisors and compares the sum to the original number."""
def is_perfect(num: int) -> bool:
    if num <= 0: 
        return False
    divisors_sum = sum(i for i in range(1, num) if num % i == 0)
    return divisors_sum == num

# Helper function to check if a number is Armstrong: a number equal to the sum of its own digits raised to the power of the number of digits.
def is_armstrong(num: int) -> bool:
    num_str = str(abs(num))  # Ensure only positive number for calculation
    power = len(num_str)
    return num == sum(int(digit) ** power for digit in num_str)

# Function to fetch a fun fact from the Numbers API
def get_fun_fact(num: int) -> str:
    try:
        response = requests.get(f"http://numbersapi.com/{num}/math")
        return response.text if response.status_code == 200 else "No fun fact available."
    except requests.RequestException:
        return "No fun fact available."

# API endpoint to classify the number and get properties
@app.get("/api/classify-number")
async def classify(number: str):
    try:
        # Convert string to integer
        num = int(number)
    except ValueError:
        raise HTTPException(
            status_code=400,
            content={
                "number": "alphabet",
                "error": True
            })

    # Initialize properties
    properties = []
    is_even = "even" if num % 2 == 0 else "odd"

    # Check if the number is prime, perfect, and Armstrong
    prime = is_prime(num)
    perfect = is_perfect(num)
    armstrong = is_armstrong(num)

    if armstrong:
        properties.append("armstrong")
    properties.append(is_even)

    # Get the fun fact for the number
    fun_fact = get_fun_fact(num)

    # Calculate the sum of digits of the number
    digit_sum = sum(int(digit) for digit in str(abs(num)))

    return {
        "number": num,
        "is_prime": prime,
        "is_perfect": perfect,
        "properties": properties,
        "digit_sum": digit_sum,
        "fun_fact": fun_fact
    }