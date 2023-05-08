import pandas as pd
import numpy as np
import unittest
from utils.rolling_aveage_median import calculate_moving_average, calculate_rolling_median


class TestMovingAverage(unittest.TestCase):

    def setUp(self):
        '''
        calling two rollings functions and test results
        '''
        # Create a sample DataFrame with some test data
        data = {'date': ['2021-01-01', '2021-01-02', '2021-01-03', '2021-01-04', '2021-01-05'],
                'volume': [10, 20, 30, 40, 50]}
        self.df = pd.DataFrame(data)
        self.df['date'] = pd.to_datetime(self.df['date'])
        self.df.set_index('date', inplace=True)


    def test_calculate_moving_average(self):
        # Test the calculate_moving_average function with a window size of 2
        result = calculate_moving_average(self.df, 'volume', 2)
        result = pd.Series(result.values)
        expected = pd.Series([float('nan'), 15.0, 25.0, 35.0, 45.0])
        pd.testing.assert_series_equal(result, expected)
        # Test the calculate_moving_average function with a window size of 3
        result = calculate_moving_average(self.df, 'volume', 3)
        result = pd.Series(result.values)
        expected = pd.Series([float('nan'), float('nan'), 20.0, 30.0, 40.0])
        pd.testing.assert_series_equal(result, expected)

     
    def test_rolling_median(self):
        # Test rolling median with window size 2
        expected = pd.Series([np.nan, 15.0, 25.0, 35.0, 45.0])
        result = calculate_rolling_median(self.df, 'volume', 2)
        result = pd.Series(result.values)
        pd.testing.assert_series_equal(expected, result)

        # Test rolling median with window size 3
        expected = pd.Series([np.nan, np.nan, 20.0, 30.0, 40.0])
        result = calculate_rolling_median(self.df, 'volume' , 3)
        result = pd.Series(result.values)
        pd.testing.assert_series_equal(expected, result)

    
if __name__ == '__main__':
    unittest.main()

