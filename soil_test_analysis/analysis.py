def analyze_soil_data(data):
    """
    Function to analyze preprocessed soil test data.
    """
    analysis_results = {}

    # Define optimal ranges for nutrients (example values)
    optimal_ranges = {
        'pH': (6.0, 7.5),
        'nitrogen': (10, 50),  # Example values
        'phosphorus': (10, 50),  # Example values
        'potassium': (10, 50)  # Example values
    }

    for key, (low, high) in optimal_ranges.items():
        if key in data:
            value = data[key]
            if value < low:
                analysis_results[key] = 'low'
            elif value > high:
                analysis_results[key] = 'high'
            else:
                analysis_results[key] = 'optimal'
        else:
            analysis_results[key] = 'missing'

    return analysis_results

if __name__ == "__main__":
    # Example usage
    sample_data = {
        "pH": 6.5,
        "nitrogen": 15,
        "phosphorus": 30,
        "potassium": 0
    }
    analysis = analyze_soil_data(sample_data)
    print("Analysis Results:", analysis)
