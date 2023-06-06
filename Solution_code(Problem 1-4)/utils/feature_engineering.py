from utils.features_added import adding_features
from utils.load_files import load_file
from multiprocessing import cpu_count


processed_stocks_path = 'dags/data/processed_stocks_etfs/'

#list of loaded csv files will split into n_processor, for parralezation process
n_processor = cpu_count()



def feature_engineering(batch_number:int):
    '''
    Takes stocks list batches as input
    Map function adding_features for every dataframe in batch
    '''
    #get batches of data
    prefeaturing_list = load_file(n_processor, processed_stocks_path, 'parquet')
    temp = list(map(adding_features,prefeaturing_list[batch_number]))