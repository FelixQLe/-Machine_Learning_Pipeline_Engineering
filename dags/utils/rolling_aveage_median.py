def calculate_moving_average(dataframe, column, window_size):
    """
    Calculates the rolling average of a column in a pandas DataFrame
    """
    rolling_average = dataframe[column].rolling(window=window_size).mean()
    return rolling_average

def calculate_rolling_median(dataframe, column, window_size):
    """
    Calculates the rolling median of a column in a pandas DataFrame
    """
    rolling_median = dataframe[column].rolling(window=window_size).median()
    return rolling_median
