import os

from flask import Flask


app = Flask(__name__)


@app.get("/")
def root():
    return "Hello, world!"


if __name__ == "__main__":
    print(os.getenv("API_TOKEN", "No token provided"))
    app.run(host="0.0.0.0", port=8000)
