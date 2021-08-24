import yaml
import fsspec
from datetime import datetime, timedelta

# Configs
CLIENT_KWARGS = {'endpoint_url': 'https://s3.wasabisys.com',
                 'region_name': 'us-east-1'}
CONFIG_KWARGS = {'max_pool_connections': 100}
PROFILE = 'default'
STORAGE_OPTIONS = {'anon': True,
                   'client_kwargs': CLIENT_KWARGS,
                   'config_kwargs': CONFIG_KWARGS}
fs = fsspec.filesystem('s3', **STORAGE_OPTIONS)

fname = "./catalogs/atmosphere.yaml"

# Get last available zarr
count = 0
max_guesses_allowed = 20
day = datetime.now() #
store_exists = False
while not store_exists and count < max_guesses_allowed:
    urlpath = f"s3://era5/world/reanalysis/single-levels/zarr-time-cache/{day.strftime('%Y-%m-%d')}"
    store_exists = fs.exists(urlpath)
    day = day - timedelta(days=1)
    count += 1

# Change urlpath in yaml and update
stream = open(fname, 'r')
data = yaml.load(stream, Loader=yaml.FullLoader)
urlpaths = ['s3://era5/world/reanalysis/single-levels/zarr-time-cache/2021-08-14',
            urlpath]
data['sources']['era5_hourly_reanalysis_single_levels_ts']['args']['urlpath']= urlpaths
with open(fname, 'w') as yaml_file:
    yaml_file.write( yaml.dump(data, default_flow_style=False))
