import pandas as pd
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

def train_model():
    # Example dataset; you'll replace this with real data
    df = pd.read_csv('flight_data.csv')
    
    X = df[['day_of_week', 'is_event_day', 'temperature']]
    y = df['price']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = XGBRegressor()
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    print(f"Mean Squared Error: {mean_squared_error(y_test, y_pred)}")
    
    return model

def predict_price(model, input_data):
    prediction = model.predict([input_data])  # Input should be formatted as feature vector
    return prediction[0]
