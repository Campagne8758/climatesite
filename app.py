from flask import Flask, flash, redirect, render_template, request, session
from helpers import temp_anomaly, calc_emissions
import requests

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        #  get ip address to get user's location
        ip_address = "24.48.0.1" #this will need to be: request.headers['X-Real-IP'] currently using test IP address the command is specific for pythoneverywhere
        # Test code to get initial user location:
        url = f"http://ip-api.com/json/{ip_address}?fields=country,countryCode,lat,lon"
        response = requests.get(url)
        location = response.json()
        country = location["country"]
        lat_in = int(location["lat"])
        lon_in = int(location["lon"])
        loc_in = {'lat' : lat_in, 'lon' : lon_in}

        tmp_display = temp_anomaly(lat_in, lon_in)
        emissions = calc_emissions(country)

        return render_template("index.html", tmp_display=tmp_display, loc_in=loc_in, emissions=emissions)

    else:
        return render_template("index.html")
