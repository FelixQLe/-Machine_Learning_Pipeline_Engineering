#logging functions
import pandas as pd

def logging_grid_search(df, log_name, level='INFO'):
    '''
    accepts dataframe list as input
    keep csv file updated with each new dataframe
    '''
    path_file = 'dags/model/training_log/'
    try:
        with open(path_file+log_name) as f:
            pass
    except FileNotFoundError:
        # If the file does not exist, write the new DataFrame to it
        df.to_csv(path_file+log_name, sep=',', index=False)
    
     # If the file exists, read its contents into a DataFrame
    existing_df = pd.read_csv(path_file+log_name)
    
    #concatenate the existing dataframe
    conc_df = pd.concat([existing_df, df], ignore_index=True)
    
    #write to csv file
    conc_df.to_csv(path_file+log_name, index=False)