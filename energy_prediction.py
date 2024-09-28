from flask import Flask, request, jsonify
from flask_marshmallow import Marshmallow
from prophet.serialize import model_from_json
import pandas as pd
from datetime import timedelta

app = Flask(__name__)
ma = Marshmallow(app)

# Load model as indicated in proophet docs[3] 
with open('model.json', 'r') as fin:
    model = model_from_json(fin.read())
@app.route('/predict_consumption', methods=['GET'])
def predict():
    # Check if the input is for Option A
    if 'N' in request.args:
        try:
            N = int(request.args['N'])
            if N <= 0:
                return jsonify({'error': 'N must be a positive integer.'}), 400
            
            # Get last date from training data 
            last_date = pd.to_datetime('2016-01-01')  
            future_dates = [last_date + timedelta(hours=i) for i in range(1, N + 1)]

            # Create DataFrame for future predictions
            future_df = pd.DataFrame({'ds': future_dates})

            # Make predictions
            forecast = model.predict(future_df)

            # Return predictions as JSON
            return jsonify({'predictions': forecast['yhat'].tolist()}), 200

        except ValueError:
            return jsonify({'error': 'Invalid input for N, must represent the number of next hours for prediction.'}), 400

    return jsonify({'error': 'Invalid request. Please provide either number of hours which you to predict its energy consumption '}), 400

if __name__ == '__main__':
    app.run(debug=True)



