from transformers import pipeline

def generate_text(prompt, max_length=150):
    """
    Generate text using Hugging Face's Transformers.
    """
    generator = pipeline('text-generation', model='gpt-2')
    response = generator(prompt, max_length=max_length, num_return_sequences=1)
    
    return response[0]['generated_text']

if __name__ == "__main__":
    # Example usage
    prompt = "Generate a soil test report based on the following data: pH: 6.5, Nitrogen: 15, Phosphorus: 30, Potassium: 0"
    text = generate_text(prompt)
    print("Generated Text:", text)
