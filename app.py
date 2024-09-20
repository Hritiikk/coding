from flask import Flask, request, jsonify
from model import train_model, predict_price
from data_collection import get_flight_prices, get_facebook_events, get_weather

app = Flask(__name__)

# Load your trained model at the start of the app
model = train_model()

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json  # Input data (origin, destination, date)
    prediction = predict_price(model, data)
    return jsonify({'predicted_price': prediction})

if __name__ == '__main__':
    app.run(debug=True)


