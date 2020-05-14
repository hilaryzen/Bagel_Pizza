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
            if int(i) / 100 >= 1901 and int(i) / 100 <= 2011:
                usTempValue[date] = float(data[i]['value'])
                usTempAnomaly[date] = float(data[i]['anomaly'])
                date += 1

def importGlobalTemp(fileName):
    with open(fileName, 'r') as file:
        data = json.loads(file.read())['data']
        date = 1901
        for i in data:
            if int(i) >= 1901 and int(i) <= 2010:
                globalTemp[date] = float(data[i])
                date += 1

globalco2beta = []
def importGlobalCO2(filename):
    with open(filename, 'r') as file:
        data = csv.reader(file)
        year = 1901
        x = 0
        for row in data:
            if x == 0: x += 1
            else: globalco2beta.append(row)
            #globalco2beta.pop(0)
        for row in globalco2beta:
            if int(row[0]) >= 1901 and int(row[0]) <= 2010:
                globalco2[year] = float(row[1])
                year += 1

countryco2 = {} # the dictionary
oneCountry = {}
# gives dictionary of country's co2 emissions by year
# ex. {"UNITED STATES" : {1901: ####, ...}}
def importCO2(country):
    with open("static/co2-emissions.csv", 'r') as file:
        data = csv.reader(file)
        for row in data:
            if row[1] == country and int(row[0]) >= 1901 and int(row[0]) <= 2010:
                oneCountry[int(row[0])] = float(row[2])
        countryco2[country] = oneCountry


importCO2("UNITED KINGDOM")
oneCountry = {}
importCO2("CANADA")
oneCountry = {}
importCO2("GERMANY")
oneCountry = {}
importCO2("UNITED STATES OF AMERICA")
oneCountry = {}
importCO2("POLAND")
oneCountry = {}
importCO2("SPAIN")
oneCountry = {}
importCO2("NORWAY")
oneCountry = {}
importCO2("INDIA")
oneCountry = {}
importCO2("PORTUGAL")
oneCountry = {}
importCO2("VIET NAM")
oneCountry = {}
importCO2("HUNGARY")
oneCountry = {}
importCO2("CHINA (MAINLAND)")
oneCountry = {}
importCO2("SWEDEN")
oneCountry = {}
importCO2("PERU")
oneCountry= {}
importCO2("JAPAN (EXCLUDING THE RUYUKU ISLANDS)")
oneCountry = {}
importCO2("FRANCE (INCLUDING MONACO)")
oneCountry = {}
importCO2("ITALY (INCLUDING SAN MARINO)")
oneCountry = {}
importCO2("AUSTRALIA")
oneCountry = {}
importCO2("BELGIUM")
oneCountry = {}

yearlyCountryCO2 = {} # the dictionary
oneYear = {}
keys = ["UNITED KINGDOM", "CANADA", "GERMANY", "UNITED STATES", "POLAND", "SPAIN", "NORWAY", "INDIA", "PORTUGAL", "VIET NAM", "HUNGARY", "GREECE", "SWEDEN", "PERU"]
# gives dictionary of year's co2 emissions by country
# ex. {1901 : {"UNITED STATES" : #####, ...}
def importYearCO2(filename):
    with open(filename, 'r') as file:
        data = csv.reader(file)
        year = "1901"
        while int(year) <= 2010:
            for row in data:
               if year == row[0] and row[1] in keys:
                    oneYear[row[1]] = float(row[2])
            yearlyCountryCO2[int(year)] = oneYear
            year = str(int(year) + 1)

@app.route("/")
def hello_world():
    return render_template("home.html")

@app.route("/temperature")
def temperature():
    return render_template("temp.html", usTempValue = usTempValue, usTempAnomaly = usTempAnomaly, globalTemp = globalTemp)

@app.route("/emissions")
def emissions():
    importGlobalCO2("static/co2-global.csv")
    return render_template("carbon.html", globalEmissions = globalco2, countryCO2 = countryco2)

@app.route("/compare")
def compare():
    importGlobalCO2("static/co2-global.csv")
    return render_template("alldata.html", globalEmissions = globalco2, globalTemp = globalTemp, usTemp = usTempValue, usAnomaly = usTempAnomaly, countryEmissions = yearlyCountryCO2, countryCO2 = countryco2)

if __name__ == "__main__":
    app.debug = True
    importUsTemp('static/us_temp.json')
    #print(usTempValue)
    #print(usTempAnomaly)
    importGlobalTemp('static/global_temp.json')
    importYearCO2('static/co2-emissions.csv')
    app.run()
