from utils.add_symbol_serName import add_name
from utils.load_files import load_file
from multiprocessing import cpu_count

stocks_path = 'dags/data/stocks_etfs/'

#list of loaded csv files will split into n_processor, for parralezation process
n_processor = cpu_count()
#get batches of data, list of list
preprocessing_list = load_file(n_processor, stocks_path, 'csv')


def data_processing(batch_number:int):
    '''
    Takes batch number as input
    Map function add_name for every dataframe in batch number in preprocessing_list
    '''
    temp = list(map(add_name, preprocessing_list[batch_number]))
