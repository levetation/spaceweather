import urllib, json
import pandas as pd

jsonURL = "https://services.swpc.noaa.gov/json/solar-cycle/observed-solar-cycle-indices.json"

with urllib.request.urlopen(jsonURL) as url:
    dataJSON = json.load(url)

data = pd.DataFrame.from_dict(dataJSON)