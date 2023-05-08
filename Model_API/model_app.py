from flask import Flask, jsonify, request
import pandas as pd
import joblib
from tensorflow.keras.models import load_model

app = Flask(__name__)

# load the model and scaler
loaded_model = load_model('best_lstm_model.SavedModel', compile=False)

with open('scaler_X.save', 'rb') as fX:
    scaler_X = joblib.load(fX)

with open('scaler_y.save', 'rb') as fy:
    scaler_y = joblib.load(fy)

@app.route('/predict')
def predict():
    # get query parameters from request
    vol_moving_avg = float(request.args.get('vol_moving_avg'))
    adj_close_rolling_med = float(request.args.get('adj_close_rolling_med'))
    
    # create input dataframe
    data = {
        'Volume_Moving_Average': [vol_moving_avg],
        'Adj_Close_Rolling_Median': [adj_close_rolling_med]
    }
    input_df = pd.DataFrame(data)
    
    # scale input data
    input_scaled = scaler_X.transform(input_df.values)
    
    # make prediction
    pred = loaded_model.predict(input_scaled.reshape(1,1,2))

    #inverse scaled transform
    pred = scaler_y.inverse_transform(pred)[0][0]
    
    # return predicted trading volume as json
    result = round(float(pred), 2)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)