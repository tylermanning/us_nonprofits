import pandas as pd
from us_nonprofits.constants import REGIONS


def extract(region=None):
    if region:
        df = pd.read_csv(REGIONS[region])
        return df
    all_regions = []
    for r in REGIONS:
        all_regions.append(pd.read_csv(REGIONS[r]))
    return pd.concat(all_regions)


def transform(data):
    return transformed_data


def load(data):
    # TO DO: cache data locally or to some data store
    pass
