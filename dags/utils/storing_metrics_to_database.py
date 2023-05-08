import pandas as pd
from sqlalchemy import create_engine

import utils.postgres_database_conf as config

db_engine = config.params["db_engine"]
db_schema = config.params["db_schema"]
table_name = config.params["db_tracking_model_table"]

path_to_metrics_df = 'dags/model/training_log/grid_search.csv'

def track_experiments_info():
    df = pd.read_csv(path_to_metrics_df).iloc[-2:-1,:]
    engine = create_engine(db_engine)
    df.to_sql(table_name, engine, schema=db_schema, if_exists='append', index=False)