import pandas as pd
from utils.rolling_aveage_median import calculate_moving_average, calculate_rolling_median
from utils.save_parquet import save_parquet

#retain features columns
features = ['Symbol', 'Security Name', 'Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume', 'vol_moving_avg', 'adj_close_rolling_med']
#path to save processed dataset

featured_stocks_path = 'dags/data/featuresAdded_stocks_etfs/'

def adding_features(file):
    name = file.stem
    df = pd.read_parquet(file, engine='pyarrow')
    #df.name = name
    # Convert the 'date' column to a datetime format
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    df['vol_moving_avg'] = calculate_moving_average(df, 'Volume', 30)
    df['adj_close_rolling_med'] = calculate_rolling_median(df, 'Volume', 30)
    df.reset_index(inplace=True)
    df.dropna(inplace=True)
    #save as parquet format
    save_parquet(df[features], name, featured_stocks_path)
