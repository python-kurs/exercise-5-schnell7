# Exercise 5
from pathlib import Path
import numpy as np
import pandas as pd
import xarray as xr
# import functions from utils here

output_dir = Path("data")
output_dir = Path("solution")

# 1. Go to http://surfobs.climate.copernicus.eu/dataaccess/access_eobs.php#datafiles and 
#    download the 0.25 deg. file for daily mean temperature. Save the file into the data directory
#    but don't commit it to github. [2P]


# 2. Read the file using xarray. Get to know your data. What's in the file?
#    Calculate monthly means for the reference periode 1981-2010 for Europe (Extent: Lon_min:-13, Lon_max: 25, Lat_min: 30, Lat_max: 72). [2P]


# 3. Calculate monthly anomalies for 2018 for the reference period and extent in #2.
#    Make a quick plot of the anomalies for the region. [2P]


# 4. Calculate the mean anomaly for the year 2018 for Europe and compare it to the anomaly of the element which contains
#    Marburg. Is the anomaly of Marburg lower or higher than the one for Europe? [2P] 


# 5. Write the monthly anomalies from task 3 to a netcdf file with name "europe_anom_2018.nc" to the solution directory.
#    Write the monthly anomalies for Marburg to a csv file with name "marburg_anom_2018.csv" to the solution directory. [2P]
