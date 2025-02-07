**Number Classification API**
This API provides mathematical properties of a number, including whether the number is prime, perfect, and Armstrong, as well as its parity (odd/even). It also fetches a fun fact from the Numbers API based on the given number.

Features
Classifies numbers as prime, perfect, or Armstrong.
Determines if the number is odd or even.
Computes the sum of digits of the number.
Fetches a fun fact about the number from the Numbers API.
Technologies
Python (Flask Framework)
Flask-CORS for handling Cross-Origin Requests
Requests for fetching data from the Numbers API
JSON for the response format
Installation
Prerequisites
Ensure you have Python 3.6+ installed. If not, download and install it from the official Python website.

Clone the repository

git clone https://github.com/Eunini/number-api.git
cd number-api
Create a virtual environment

python -m venv venv
Activate the virtual environment
On Windows:


venv\Scripts\activate
On MacOS/Linux:


source venv/bin/activate
Install the required dependencies

pip install -r requirements.txt
requirements.txt includes:

Flask
Flask-CORS
Requests
If you don't have a requirements.txt file, you can generate it by running:


`pip freeze > requirements.txt`
Set environment variables (optional)
You can set the PORT environment variable for deployment purposes or leave it as default (5000).

Running the API Locally
To run the API locally, execute the following command:

python app.py
By default, the API will be accessible at:

http://127.0.0.1:5000
API Endpoints
GET /api/classify-number?number={number}~
Request
This endpoint accepts a query parameter number (an integer) and returns a JSON response with its properties.

Example:
**GET /api/classify-number?number=371**
Response
200 OK: If the number is valid, the response will contain the number's properties.

`{
  "number": 371,
  "is_prime": false,
  "is_perfect": false,
  "properties": ["armstrong", "odd"],
  "digit_sum": 11,
  "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}`
400 Bad Request: If the number is not provided or if the input is not a valid integer.

`{
  "number": "alphabet",
  "error": true
}`
Mathematical Properties Explained
Prime Number: A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
Perfect Number: A perfect number is a positive integer that is equal to the sum of its proper divisors, excluding the number itself.
Armstrong Number: An Armstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.
Odd/Even: The number is classified as odd or even based on its divisibility by 2.
Example Usage
Check for Armstrong number, Prime, Perfect, and Parity (Odd/Even)

`curl "http://127.0.0.1:5000/api/classify-number?number=371"`
Response:
`{
  "number": 371,
  "is_prime": false,
  "is_perfect": false,
  "properties": ["armstrong", "odd"],
  "digit_sum": 11,
  "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}`
Invalid Input
`curl "http://127.0.0.1:5000/api/classify-number?number=abc"`
Response:

`{
  "number": "abc",
  "error": true
}`
Deployment
You can deploy this API to any platform of your choice that supports Python, such as:

Heroku
Render
AWS (EC2 or Lambda)
Google Cloud Platform (App Engine)
For example, to deploy on Render, follow these steps:

Create a requirements.txt file by running pip freeze > requirements.txt.
Link your GitHub repository to Render.
Deploy and set the environment variable for the port (Render uses PORT by default).
Deployment Example on Render:
Create a new Web Service on Render, linking your repository.
Choose the Python environment and specify python app.py as the start command.
Your API will be available via the URL provided by Render.
License


This project is licensed by Inioluwa made for HNG DevOps Internship.

