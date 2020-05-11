# Green Graphs by Bagel Pizza

## Roles:

Alice: Front-end, Bootstrap, JS/D3

Leia: Python, Database/CSV

Pratham: JS/D3

Hilary: Project Manager (prime minister), Flask

## Summary:

Our website’s objective is to display climate change through graphs demonstrating the changes in temperature from 1901 to 2000, as well as CO2 emissions from fossil fuels globally. To use our site, the homepage will have three buttons labeled “Global Temperature Anomaly”, “Carbon Dioxide Emissions” and “Compare Data”. When each button is clicked, the user will be redirected to a page that has graphs displaying the specified data. The graphs are interactive, so the user can adjust the graphs to what they want to view. 

## How to Run this Project

1. Git clone this repo by running:

```
git clone https://github.com/hilaryzen/Bagel_Pizza.git
```

2. Install Flask in the repo folder with:

```
cd Bagel_Pizza
pip3 install flask
```

If the pip3 command did not work for you, create a virtual environment, activate it, and install Flask with the following lines:

```
python3 -m venv myvenv
. myvenv/bin/activate
pip3 install flask
```

3. Move into the app folder.

```
cd app
```

4. Run the website with:

```
python3 __init__.py
```

5. Go to http://localhost:5000/ to view Green Graphs!

6. After you are done looking at the site, if you are running a virtual environment you can close it with:

```
deactivate
```
