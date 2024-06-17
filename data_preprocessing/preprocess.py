def preprocess_data(data):
    """
    Function to preprocess soil test data. This example function will normalize
    pH values, convert units for nutrient concentrations, and handle missing values.
    """
    preprocessed_data = {}

    # Normalize pH values (assuming pH should be between 0 and 14)
    if 'pH' in data:
        preprocessed_data['pH'] = max(0, min(14, data['pH']))

    # Convert nutrient concentrations from ppm to mg/kg if necessary
    nutrients = ['nitrogen', 'phosphorus', 'potassium']
    for nutrient in nutrients:
        if nutrient in data:
            preprocessed_data[nutrient] = data[nutrient]  # Assuming data is already in the desired unit

    # Handle missing values (fill with default values)
    default_values = {
        'pH': 7.0,  # Neutral pH
        'nitrogen': 0,  # Default nutrient concentration
        'phosphorus': 0,
        'potassium': 0
    }
    for key, default in default_values.items():
        if key not in preprocessed_data:
            preprocessed_data[key] = default

    return preprocessed_data

if __name__ == "__main__":
    # Example usage
    sample_data = {
        "pH": 6.5,
        "nitrogen": 15,
        "phosphorus": 30
        # 'potassium' is missing and should be filled with default
    }
    print("Original Data:", sample_data)
    preprocessed = preprocess_data(sample_data)
    print("Preprocessed Data:", preprocessed)
