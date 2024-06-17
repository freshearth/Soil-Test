import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import pickle

def train_model(data_path):
    """
    Train a machine learning model to predict soil nutrient levels.
    """
    # Load the data
    data = pd.read_csv(data_path)
    
    # Define features and target variables
    X = data.drop(columns=['nutrient_level'])
    y = data['nutrient_level']
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train a RandomForest model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Evaluate the model
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Model Mean Squared Error: {mse}")
    
    # Save the model to a file
    with open('soil_nutrient_model.pkl', 'wb') as file:
        pickle.dump(model, file)
        
def predict_nutrient_level(features):
    """
    Predict soil nutrient level using the trained machine learning model.
    """
    with open('soil_nutrient_model.pkl', 'rb') as file:
        model = pickle.load(file)
    
    return model.predict([features])[0]

if __name__ == "__main__":
    # Example usage: Train the model
    train_model('historical_soil_data.csv')
    
    # Example usage: Predict using the trained model
    sample_features = [6.5, 15, 30, 0]
    prediction = predict_nutrient_level(sample_features)
    print("Predicted Nutrient Level:", prediction)
