from sklearn.preprocessing import MinMaxScaler
import joblib
import datetime
import pandas as pd

from utils.fetch_data import fetch_data
from utils.logging_function import logging_grid_search
from utils.preparing_data import preparing_data
from utils.split_data import split_data
from utils.grid_search import grid_search
from utils.load_files import load_file


# params for Grid_search
param_grid = {
    'num_units': [32],
    'dropout': [0.4],
    'batch_size': [128],
    'epochs': [50],
    'learning_rate': [0.0001]}


def best_model_search():
    df = load_file(1, 'dags/data/featuresAdded_stocks_etfs/', "IP.parquet", press="")

    #fetch data
    features, target = fetch_data(df[0])

    # scale data
    scaler_X = MinMaxScaler()
    sclaer_y = MinMaxScaler()
    # scale feature and target
    scaled_features = scaler_X.fit_transform(features)
    scaled_target = sclaer_y.fit_transform(target.reshape(-1,1))

    # save scaler to file
    saving_ml_path = 'dags/model/'
    joblib.dump(scaler_X, saving_ml_path+'scaler_X.save')
    joblib.dump(sclaer_y, saving_ml_path+'scaler_y.save')

    #prepare data
    X, y = preparing_data(scaled_features, scaled_target)

    # split data
    X_train, X_test, X_val, y_train, y_test, y_val = split_data(X,y)
    cv_fold = 3

    # Fit grid search on training data
    grid = grid_search(param_grid, X_train, y_train, cv_fold=cv_fold, validation_data=(X_val, y_val))

    #training time
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H:%M')

    # Save best model to file
    best_model = grid.best_estimator_
    best_model.model.save(saving_ml_path+'best_lstm_model.SavedModel')
    
    #gather metrics
    experiment_datetime = timestamp
    cv_folds = cv_fold
    batch_size = grid.best_params_['batch_size']
    dropout = grid.best_params_['dropout']
    epochs = grid.best_params_['epochs']
    learning_rate = grid.best_params_['learning_rate']
    num_units = grid.best_params_['num_units']
    mean_test_score = grid.cv_results_['mean_test_score'][0]
    std_test_score = grid.cv_results_['std_test_score'][0]

    #create df tempt
    tempt = pd.DataFrame([[experiment_datetime,
                    cv_folds,
                    batch_size,
                    dropout,
                    epochs,
                    learning_rate,
                    num_units,
                    mean_test_score,
                    std_test_score]],
             columns=['experiment_datetime', 
                      'cv_folds', 
                      'batch_size', 
                      'dropout',
                      'epochs', 
                      'learning_rate', 
                      'num_units', 
                      'mean_test_score', 
                      'std_test_score'
                    ])
    log_name = 'grid_search.csv'
    #call logging function to save model metrics
    logging_grid_search(tempt, log_name)
