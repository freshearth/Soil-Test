def create_document(data, analysis_results, filename='soil_test_report.txt'):
    """
    Function to create a formatted document from the data and analysis results.
    """
    with open(filename, 'w') as file:
        file.write("Soil Test Report\n")
        file.write("================\n\n")
        
        file.write("Soil Test Data:\n")
        for key, value in data.items():
            file.write(f"{key}: {value}\n")
        
        file.write("\nAnalysis Results:\n")
        for key, value in analysis_results.items():
            file.write(f"{key}: {value}\n")

if __name__ == "__main__":
    # Example usage
    sample_data = {
        "pH": 6.5,
        "nitrogen": 15,
        "phosphorus": 30,
        "potassium": 0
    }
    sample_analysis = {
        "pH": "optimal",
        "nitrogen": "optimal",
        "phosphorus": "optimal",
        "potassium": "low"
    }
    create_document(sample_data, sample_analysis)
