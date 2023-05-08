import pandas as pd

def fetch_data(path_to_stock):
    '''
    function retain vol_moving_avg', 'adj_close_rolling_med', 'Volume' features
    and return df values
    '''
    df = pd.read_parquet(path_to_stock)
    df = df[['vol_moving_avg', 'adj_close_rolling_med', 'Volume']].values
    features = df[:,0:2]
    target = df[:, 2]
    return features, target