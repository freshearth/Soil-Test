import json
from data_collection.collect import fetch_soil_test_data, fetch_land_management_data, aggregate_data
from data_preprocessing.preprocess import preprocess_data
from data_storage.storage import store_data
from soil_test_analysis.analysis import analyze_soil_data
from document_template.template import create_template
from document_generation.generate import generate_document
from ai_models.nlp import generate_text
from ai_models.ml_model import train_model, predict_nutrient_level

def handle_request(data):
    """
    Handle a data preprocessing, analysis, and document generation request.
    """
    try:
        # Preprocess the data
        preprocessed_data = preprocess_data(data)
        
        # Analyze the preprocessed data
        analysis_results = analyze_soil_data(preprocessed_data)
        
        # Predict nutrient levels
        features = [preprocessed_data.get('pH', 7.0), preprocessed_data.get('nitrogen', 0),
                    preprocessed_data.get('phosphorus', 0), preprocessed_data.get('potassium', 0)]
        nutrient_prediction = predict_nutrient_level(features)
        preprocessed_data['predicted_nutrient_level'] = nutrient_prediction
        
        # Store the preprocessed data
        store_data(preprocessed_data)
        
        # Create a document template
        template = create_template(preprocessed_data, analysis_results)
        
        # Generate a document using NLP
        prompt = f"Generate a soil test report based on the following data: {preprocessed_data}, Analysis Results: {analysis_results}"
        generated_text = generate_text(prompt)
        
        # Generate a document
        generate_document(generated_text)
        
        # Create a response
        response = {
            'status': 'success',
            'message': 'Data preprocessed, analyzed, stored, and document generated successfully',
            'preprocessed_data': preprocessed_data,
            'analysis_results': analysis_results,
            'generated_text': generated_text
        }
        return response
    except Exception as e:
        response = {
            'status': 'error',
            'message': str(e)
        }
        return response

def main():
    # Fetch data from APIs
    soil_test_api_url = "https://api.example.com/soil-tests"
    land_management_api_url = "https://api.example.com/land-management"
    
    soil_test_data = fetch_soil_test_data(soil_test_api_url)
    land_management_data = fetch_land_management_data(land_management_api_url)
    
    if soil_test_data and land_management_data:
        aggregated_data = aggregate_data(soil_test_data, land_management_data)
        print("Aggregated Data:", json.dumps(aggregated_data, indent=4))
        
        # Handle the request with aggregated data
        response = handle_request(aggregated_data)
        print("Response:", json.dumps(response, indent=4))
    else:
        print("Failed to fetch data from one or more APIs.")

if __name__ == "__main__":
    main()
