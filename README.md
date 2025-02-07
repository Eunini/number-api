<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Number Classification API</title>
</head>
<body>
    <h1>Number Classification API</h1>
    <p>This API provides mathematical properties of a number, including whether the number is prime, perfect, and Armstrong, as well as its parity (odd/even). It also fetches a fun fact from the Numbers API based on the given number.</p>

    <h2>Features</h2>
    <ul>
        <li>Classifies numbers as prime, perfect, or Armstrong.</li>
        <li>Determines if the number is odd or even.</li>
        <li>Computes the sum of digits of the number.</li>
        <li>Fetches a fun fact about the number from the Numbers API.</li>
    </ul>

    <h2>Technologies</h2>
    <ul>
        <li>Python (Flask Framework)</li>
        <li>Flask-CORS for handling Cross-Origin Requests</li>
        <li>Requests for fetching data from the Numbers API</li>
        <li>JSON for the response format</li>
    </ul>

    <h2>Installation</h2>
    <h3>Prerequisites</h3>
    <p>Ensure you have Python 3.6+ installed. If not, download and install it from the official Python website.</p>

    <h3>Clone the repository</h3>
    <pre><code>git clone https://github.com/Eunini/number-api.git</code></pre>
    <pre><code>cd number-api</code></pre>

    <h3>Create a virtual environment</h3>
    <pre><code>python -m venv venv</code></pre>

    <h3>Activate the virtual environment</h3>
    <p>On Windows:</p>
    <pre><code>venv\Scripts\activate</code></pre>
    <p>On MacOS/Linux:</p>
    <pre><code>source venv/bin/activate</code></pre>

    <h3>Install the required dependencies</h3>
    <pre><code>pip install -r requirements.txt</code></pre>

    <h4>requirements.txt includes:</h4>
    <ul>
        <li>Flask</li>
        <li>Flask-CORS</li>
        <li>Requests</li>
    </ul>

    <h3>If you don't have a requirements.txt file, you can generate it by running:</h3>
    <pre><code>pip freeze > requirements.txt</code></pre>

    <h3>Set environment variables (optional)</h3>
    <p>You can set the PORT environment variable for deployment purposes or leave it as default (5000).</p>

    <h2>Running the API Locally</h2>
    <p>To run the API locally, execute the following command:</p>
    <pre><code>python app.py</code></pre>
    <p>By default, the API will be accessible at:</p>
    <pre><code>http://127.0.0.1:5000</code></pre>

    <h2>API Endpoints</h2>
    <h3>GET /api/classify-number?number={number}~</h3>
    <h4>Request</h4>
    <p>This endpoint accepts a query parameter number (an integer) and returns a JSON response with its properties.</p>
    <p>Example:</p>
    <pre><code>GET /api/classify-number?number=371</code></pre>

    <h4>Response</h4>
    <h5>200 OK</h5>
    <p>If the number is valid, the response will contain the number's properties.</p>
    <pre><code>{
  "number": 371,
  "is_prime": false,
  "is_perfect": false,
  "properties": ["armstrong", "odd"],
  "digit_sum": 11,
  "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}</code></pre>

    <h5>400 Bad Request</h5>
    <p>If the number is not provided or if the input is not a valid integer.</p>
    <pre><code>{
  "number": "alphabet",
  "error": true
}</code></pre>

    <h2>Mathematical Properties Explained</h2>
    <ul>
        <li><strong>Prime Number:</strong> A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.</li>
        <li><strong>Perfect Number:</strong> A perfect number is a positive integer that is equal to the sum of its proper divisors, excluding the number itself.</li>
        <li><strong>Armstrong Number:</strong> An Armstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.</li>
        <li><strong>Odd/Even:</strong> The number is classified as odd or even based on its divisibility by 2.</li>
    </ul>

    <h2>Example Usage</h2>
    <h3>Check for Armstrong number, Prime, Perfect, and Parity (Odd/Even)</h3>
    <pre><code>curl "http://127.0.0.1:5000/api/classify-number?number=371"</code></pre>
    <p>Response:</p>
    <pre><code>{
  "number": 371,
  "is_prime": false,
  "is_perfect": false,
  "properties": ["armstrong", "odd"],
  "digit_sum": 11,
  "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}</code></pre>

    <h3>Invalid Input</h3>
    <pre><code>curl "http://127.0.0.1:5000/api/classify-number?number=abc"</code></pre>
    <p>Response:</p>
    <pre><code>{
  "number": "abc",
  "error": true
}</code></pre>

    <h2>Deployment</h2>
    <p>You can deploy this API to any platform of your choice that supports Python, such as:</p>
    <ul>
        <li>Heroku</li>
        <li>Render</li>
        <li>AWS (EC2 or Lambda)</li>
        <li>Google Cloud Platform (App Engine)</li>
    </ul>

    <h4>For example, to deploy on Render, follow these steps:</h4>
    <ul>
        <li>Create a requirements.txt file by running <code>pip freeze > requirements.txt</code>.</li>
        <li>Link your GitHub repository to Render.</li>
        <li>Deploy and set the environment variable for the port (Render uses PORT by default).</li>
    </ul>

    <h4>Deployment Example on Render:</h4>
    <ul>
        <li>Create a new Web Service on Render, linking your repository.</li>
        <li>Choose the Python environment and specify <code>python app.py</code> as the start command.</li>
        <li>Your API will be available via the URL provided by Render.</li>
    </ul>

    <h2>License</h2>
    <p>This project is licensed by Inioluwa made for HNG DevOps Internship.</p>
</body>
</html>
