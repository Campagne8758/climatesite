import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import json

def temp_anomaly(lat_in, lon_in):
    radius = 5
    # SOURCE: http://berkeleyearth.org/data/ 
    tmps = xr.open_dataset("Data/Raw_TAVG_LatLong1.nc")
    lat = lat_in + 90
    lon = lon_in + 180
    # Data points collected from a radius of 5x5 degrees on latitude and longitude in 1 degrees increments for the previous 24 months.
    tmp_values = tmps.temperature.values[3242:3253, lat - radius:lat + radius , lon - radius: lon + radius]
    total_temp = 0
    avg_temp = 0
    data_points = 0
    #  sum of every valid data point (only land measurements considered)
    for year in tmp_values:
        for month in year:
            for j in month:
                if str(j) != "nan":
                    total_temp += float(j)
                    data_points += 1
    #  calculate average and return
    avg_temp = total_temp / data_points
    return round(avg_temp,3)

def calc_emissions(country):
    year_box2 = '1990'
    year_box3 = '2018'
    emissions1990 = '0'
    emissions2018 = '0'
    emissions = []

    with open('Data/co2.json') as co2:
        data = json.load(co2)
        for i in data[1]:
            if i['country']['value'] == country:
                if i['date'] == year_box2:
                    emissions1990 = i['value']
                elif i['date'] == year_box3:
                    emissions2018 = i['value']
    
    emissions.append(emissions1990)
    emissions.append(emissions2018)
    return emissions
                
                
            

# Not currenly used --------- NEEDS WORK TO DISPLAY A GRAPH ----------
def temp_graph(lat_in, lon_in):
    tmps = xr.open_dataset("Data/Raw_TAVG_LatLong1.nc")
    lat = lat_in + 90
    lon = lon_in + 180
    graph = tmps.temperature.values[3230:3253, lat, lon]
    
    return plt.plot(graph)