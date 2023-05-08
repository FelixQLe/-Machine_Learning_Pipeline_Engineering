def save_parquet(df_stock, stock_name, path):
    '''
    accepts dataframe, name, path as in put
    save dataframe in the path folder with name stock_name
    '''
    #save df to parquet, memmory efficiency with engine pyarrow, optizing space storage wit compression gzip
    df_stock.to_parquet(path+stock_name+'.parquet', engine = 'pyarrow', compression = 'gzip')