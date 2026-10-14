
from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Weather Information</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                background: #eaf4ff;
                padding: 60px;
            }
            .card {
                background: white;
                padding: 30px;
                border-radius: 12px;
                max-width: 550px;
                margin: auto;
                box-shadow: 0 4px 12px #cccccc;
            }
            h1 { color: #1769aa; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Weather Information System</h1>
            <p>Welcome to our Weather Information project!</p>
            <p>Application is running successfully.</p>
            <p>DevOps Pipeline Mini Project</p>
        </div>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return {"status": "healthy", "application": "weather-devops"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
