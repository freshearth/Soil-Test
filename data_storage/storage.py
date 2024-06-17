import csv
import os

def store_data(data, filename='preprocessed_soil_data.csv'):
    """
    Function to store data in a CSV file.
    """
    file_exists = os.path.isfile(filename)

    with open(filename, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data.keys())

        if not file_exists:
            writer.writeheader()  # File doesn't exist yet, write a header

        writer.writerow(data)

if __name__ == "__main__":
    # Example usage
    sample_data = {
        "pH": 6.5,
        "nitrogen": 15,
        "phosphorus": 30,
        "potassium": 0  # Default value filled
    }
    store_data(sample_data)
