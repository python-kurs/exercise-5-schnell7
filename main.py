# Exercise 5
from pathlib import Path
import numpy as np
import pandas as pd
import xarray as xr
import matplotlib.pyplot as plt
#%%
input_dir  = Path("data")
output_dir = Path("solution")

# 1. Go to http://surfobs.climate.copernicus.eu/dataaccess/access_eobs.php#datafiles
#    and download the 0.25 deg. file for daily mean temperature.
#    Save the file into the data directory but don't commit it to github!!! [2P]

#%%
# 2. Read the file using xarray. Get to know your data. What's in the file?
#    Calculate monthly means for the reference periode 1981-2010 for Europe (Extent: Lon_min:-13, Lon_max: 25, Lat_min: 30, Lat_max: 72). [2P]
data = xr.open_dataset(input_dir / "tg_ens_mean_0.25deg_reg_v19.0e.nc")

data = data.sel(latitude  = slice(30, 72), longitude = slice(-13, 25))
month_means = data.sel(time = slice("1981-01-01", "2010-12-31")).groupby("time.month").mean("time")
#%%
# 3. Calculate monthly anomalies from the reference period for the year 2018 (use the same extent as in #2).
#    Make a quick plot of the anomalies for the region. [2P]
month_annom = data.sel(time = "2018").groupby("time.month").mean("time") - month_means
month_annom["tg"].plot(x="longitude", y="latitude", col="month", col_wrap=3)
#%%
# 4. Calculate the mean anomaly for the year 2018 for Europe (over all pixels of the extent from #2) 
#    Compare this overall mean anomaly to the anomaly of the pixel which contains Marburg. 
#    Is the anomaly of Marburg lower or higher than the one for Europe? [2P] 
total_annom = month_annom.mean(["month", "latitude", "longitude"])

mr_annom = month_annom.sel(longitude=8.77069, latitude=50.80904, method="nearest").mean("month")

mr = mr_annom["tg"].values
tot = total_annom["tg"].values

if mr > tot:
    print("Ja, Annomalie ist groesser in MR")
else:
    print("Nein, annomalie ist nicht groesser in MR")
#%%

# 5. Write the monthly anomalies from task 3 to a netcdf file with name "europe_anom_2018.nc" to the solution directory.
#    Write the monthly anomalies for Marburg to a csv file with name "marburg_anom_2018.csv" to the solution directory. [2P]
month_annom.to_netcdf(output_dir / "europe_anom_2018.nc")

mr_month_annom = month_annom["tg"].sel(longitude=8.77069, latitude=50.80904, method="nearest").to_dataframe()
mr_month_annom["tg"].to_csv(output_dir / "marburg_anom_2018.csv",header=True)
#%%