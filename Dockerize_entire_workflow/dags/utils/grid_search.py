from sklearn.model_selection import GridSearchCV
from utils.custome_LSTMregressor import LSTMRegressor

def grid_search(param_grid, X_train, y_train, validation_data, cv_fold):
    """
    function take param_grid, X_train, y_train
    """
    # Define grid search object
    grid_search = GridSearchCV(estimator=LSTMRegressor(), param_grid=param_grid, 
                               cv=cv_fold, scoring='neg_mean_squared_error', verbose=2, n_jobs=-1
                              )
    # Fit grid search on training data
    grid_search.fit(X_train, y_train, validation_data=validation_data)
    return grid_search