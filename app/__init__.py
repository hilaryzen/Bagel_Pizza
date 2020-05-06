from flask import Flask, render_template, request
import csv
import json
app = Flask(__name__)

globalco2 = {}

# year: anomaly
# {1901: -0.15, 1902: -0.25, etc}
globalTemp = {}

# year: value
# {1901: 51.87, 1902: 51.59, etc}
usTempValue = {}
# year: anomaly
# {1901: -0.15, 1902: -0.43, etc}
usTempAnomaly = {}

def importUsTemp(fileName):
    with open(fileName, 'r') as file:
        data = json.loads(file.read())['data']
        date = 1901
        for i in data:
            if int(i) / 100 >= 1901 and int(i) / 100 <= 2001:
                usTempValue[date] = float(data[i]['value'])
                usTempAnomaly[date] = float(data[i]['anomaly'])
                date += 1

def importGlobalTemp(fileName):
    with open(fileName, 'r') as file:
        data = json.loads(file.read())['data']
        date = 1901
        for i in data:
            if int(i) >= 1901 and int(i) <= 2000:
                globalTemp[date] = float(data[i])
                date += 1

globalco2beta = []
def importGlobalCO2(filename):
    with open(filename, 'r') as file:
        data = csv.reader(file)
        year = 1901
        for row in data:
            globalco2beta.append(row)
        globalco2beta.pop(0)
        for row in globalco2beta:
            if int(row[0]) >= 1901 and int(row[0]) <= 2000:
                globalco2[year] = float(row[2])
                year += 1

@app.route("/")
def hello_world():
    return render_template("home.html")

@app.route("/temperature")
def temperature():
    return render_template("temp.html", usTempValue = usTempValue, usTempAnomaly = usTempAnomaly, globalTemp = globalTemp)

@app.route("/emissions")
def emissions():
    importGlobalCO2("static/co2-global.csv")
    return render_template("carbon.html", globalEmissions = globalco2)

@app.route("/compare")
def compare():
    return render_template("alldata.html")

if __name__ == "__main__":
    app.debug = True
    importUsTemp('static/us_temp.json')
    #print(usTempValue)
    #print(usTempAnomaly)
    importGlobalTemp('static/global_temp.json')
    app.run()
