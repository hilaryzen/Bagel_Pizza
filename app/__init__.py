from flask import Flask, render_template, request
app = Flask(__name__)

co2Emissions = {}
globalTemp = {}
usTemp = {}

def importCSV(fileName):
    return 5

def importJSON(fileName):
    return 5

@app.route("/")
def hello_world():
    return render_template("home.html")

@app.route("/temperature")
def temperature():
    return render_template("temp.html")

@app.route("/emissions")
def emissions():
    return render_template("carbon.html")

@app.route("/compare")
def compare():
    return render_template("alldata.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
