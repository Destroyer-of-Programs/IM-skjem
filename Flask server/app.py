from flask import Flask, request, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory("../HTML", "index.html")

if __name__ == "__main__":
    app.run(debug = True)
