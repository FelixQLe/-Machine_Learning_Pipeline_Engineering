from sklearn.base import BaseEstimator, RegressorMixin
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import tensorflow as tf

class LSTMRegressor(BaseEstimator, RegressorMixin):
    """
    custome LSTM to take params_grid and try all params on LTSM by using GridSerchCV
    example how to use: GridSearchCV(estimator=LSTMRegressor(), param_grid=param_grid, cv=3, scoring='neg_mean_squared_error', verbose=2, n_jobs=-1)
    """
    def __init__(self, num_units=32, dropout=0.2, batch_size=32, epochs=50, learning_rate=0.05):
        self.num_units = num_units
        self.dropout = dropout
        self.batch_size = batch_size
        self.epochs = epochs
        self.learning_rate = learning_rate
        self.model = None
    
    def fit(self, X, y, validation_data=None):
        self.model = Sequential()
        self.model.add(LSTM(self.num_units, input_shape=(X.shape[1], X.shape[2]), dropout=self.dropout, return_sequences=False))
        self.model.add(Dense(1, activation='linear'))
        optimizer = tf.keras.optimizers.Adam(learning_rate=self.learning_rate)
        self.model.compile(loss='mse', optimizer=optimizer)
        if validation_data is not None:
            X_val, y_val = validation_data
            self.model.fit(X, y, epochs=self.epochs, batch_size=self.batch_size, verbose=0, validation_data=(X_val, y_val))
        else:
            self.model.fit(X, y, epochs=self.epochs, batch_size=self.batch_size, verbose=0)
        return self
    
    def predict(self, X):
        return self.model.predict(X).flatten()