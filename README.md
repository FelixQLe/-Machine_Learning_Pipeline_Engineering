# Work_Sample_Data_Engineer
Technical Evaluations

- Problem 1: Raw Data Processing  
- Problem 2: Feature Engineering
- Problem 3: Integrate ML Training
- Problem 4: Model Serving
References: 
- https://airflow.apache.org/docs/apache-airflow/stable/tutorial/fundamentals.html#testing
- https://towardsdatascience.com/end-to-end-machine-learning-pipeline-with-docker-and-apache-airflow-from-scratch-35f6a75f57ad
- https://github.com/btphan95/greenr-airflow
- https://betterdatascience.com/apache-airflow-run-tasks-in-parallel/
- https://stackoverflow.com/questions/52741536/running-airflow-tasks-dags-in-parallel
- https://stackoverflow.com/questions/31645466/give-column-name-when-read-csv-file-pandas
- https://www.simplilearn.com/tutorials/python-tutorial/map-in-python
- https://stackoverflow.com/questions/50337843/extract-file-name-from-read-csv-python
- https://sparkbyexamples.com/pandas/pandas-read-multiple-csv-files/?amp=1

#### Directory structure: 
dags/
  ├── ml_pipeline.py
  ├── sql/
  │     └── create_tracking_best_model_table.sql
  └── utils/
        ├── add_symbol_serName.py
        ├── custome_LSTMregressor.py
        ├── data_processing.py
        ├── feature_engineering.py
        ├── features_added.py
        ├── fetch_data.py
      ├── fetching_best_model.py
      ├── grid_search.py
      ├── load_files.py
|     ├── logging_function.py
      ├── postgres_database_conf.py
      ├── preparing_data.py
      ├── rolling_aveage_median.py
      ├── save_model.py
      ├── save_parquet.py
      ├── split_data.py
      ├── storing_metrics_to_database.py
      └── unit_tests_rollings.py
|___model
|   |___ best_lstm_model.SavedModel
    |___ scaler_X.save
    |___ scaler_y.save
    |___training_log
        |__grid_search.csv
|
data/
├── stocks_etfs/
│   ├── A.csv
│   ├── AA.csv
│   ├── AACG.csv
│   ├── AAL.csv
│   ├── HAYN.csv
│   ├── HBAN.csv
│   ├── HBANN.csv
│   ├── HBANO.csv
│   ├── IOO.csv
│   ├── IOSP.csv
│   ├── IOTS.csv
│   ├── IOVA.csv
│   ├── IP.csv
│   ├── IPAC.csv
│   ├── IPAR.csv
│   ├── IPAY.csv
│   ├── VSGX.csv
│   ├── VSL.csv
│   ├── VSMV.csv
│   ├── VSS.csv
│   ├── VTHR.csv
│   ├── VTI.csv
│   └── VTV.csv
└── processed_stocks_etfs/
|
└── featuresAdded_stocks_etfs/


dags: 
- contain all python and sql scripts, ml_pipeline run on Apache Airflow, training_log, training_metrics

Model_API:
- contain flask API app, deploying ml_model to predict trading Volume, and ho_to_run.txt


