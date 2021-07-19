import numpy as np
import xarray as xr
import matplotlib.pyplot as plt

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

# Not currenly used --------- NEEDS WORK TO DISPLAY A GRAPH ----------
def temp_graph(lat_in, lon_in):
    tmps = xr.open_dataset("Data/Raw_TAVG_LatLong1.nc")
    lat = lat_in + 90
    lon = lon_in + 180
    graph = tmps.temperature.values[3230:3253, lat, lon]
    
    return plt.plot(graph)