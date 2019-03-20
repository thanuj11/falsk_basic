from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Flask inside Docker!!"


if __name__ == "__main__":
    #hello()
    app.run(debug=True)
