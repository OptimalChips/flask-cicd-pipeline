from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    # Running on all available interfaces on port 5000 with debug mode enabled
    app.run(host='0.0.0.0', port=5001, debug=True)

