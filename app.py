from flask import Flask, render_template, request
from helpers import temp_anomaly, calc_emissions, geocode
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
        emissions_1990 = emissions[0]
        emissions_2018 = emissions[1]

        return render_template("index.html", tmp_display=tmp_display, loc_in=loc_in, emissions_2018=emissions_2018, emissions_1990=emissions_1990, country=country)

    else:
        lat_in = request.form.get("lat")
        lon_in = request.form.get("lon")
        if not lat_in or not lon_in:
            tmp_display = temp_anomaly(44,9)
            country = 'Italy'
            loc_in = {'lat' : 44, 'lon' : 9}
            emissions = calc_emissions(country)
            emissions_1990 = emissions[0]
            emissions_2018 = emissions[1]
            return render_template("coord.html", tmp_display=tmp_display, loc_in=loc_in, emissions_2018=emissions_2018, emissions_1990=emissions_1990, country=country)
        loc_in = {'lat' : lat_in, 'lon' : lon_in}

        tmp_display = temp_anomaly(int(lat_in), int(lon_in))
        country = geocode(lat_in,lon_in)
        emissions = calc_emissions(country)
        emissions_1990 = emissions[0]
        emissions_2018 = emissions[1]

        return render_template("coord.html", tmp_display=tmp_display, loc_in=loc_in, emissions_2018=emissions_2018, emissions_1990=emissions_1990, country=country)

@app.route("/explain")
def explain():
        ip_address = "24.48.0.1" #this will need to be: request.headers['X-Real-IP'] currently using test IP address the command is specific for pythoneverywhere
        # Code to get initial user location:
        url = f"http://ip-api.com/json/{ip_address}?fields=country,countryCode,lat,lon"
        response = requests.get(url)
        location = response.json()
        country = location["country"]
        lat_in = int(location["lat"])
        lon_in = int(location["lon"])
        loc_in = {'lat' : lat_in, 'lon' : lon_in}
        
        return render_template("explain.html", loc_in=loc_in)