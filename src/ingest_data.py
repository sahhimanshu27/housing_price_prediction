from abc import ABC, abstractmethod
import zipfile
import os

import pandas as pd

# Define an abstract base class for data ingestion
class DataIngestor(ABC):
    @abstractmethod
    def ingest(self, file_path: str) -> pd.DataFrame:
        pass

# Implement a concrete class for zip ingestion
class ZipDataIngestor(DataIngestor):
    def ingest(self, file_path: str) -> pd.DataFrame:
        '''Extracts a .zip file and reads the contained CSV into a DataFrame.'''
        # Ensure the file is a .zip file
        if not file_path.endswith('.zip'):
            raise ValueError("File must be a .zip archive")
        
        # Extract the zip file
        with zipfile.ZipFile(file_path, 'r') as zip_file:
            zip_file.extractall('extracted_data')

        # Assuming the zip contains a single CSV file
        extracted_files = os.listdir('extracted_data')
        csv_files = [f for f in extracted_files if f.endswith('.csv')]

        if len(csv_files) == 0:
            raise ValueError("No CSV file found in the zip archive")
        if len(csv_files) > 1:
            raise ValueError("Multiple CSV files found in the zip archive")
        
        # Read the CSV file into a DataFrame
        csv_file_path = os.path.join("extracted_data", csv_files[0])
        df = pd.read_csv(csv_file_path)

        return df
    
# Implement a factory to create data ingestors
class DataIngestorFactory:
    @staticmethod
    def get_ingestor(file_extension: str) -> DataIngestor:
        if file_extension == '.zip':
            return ZipDataIngestor()
        else:
            raise ValueError(f"Unsupported file type: {file_extension}")
        
# Example usage
if __name__ == "__main__":
    file_path = '/Users/himanshusah/Downloads/AI-Learning-Projects/aiMlops/house_price/data/archive.zip'  # Example zip file path
    file_extension = os.path.splitext(file_path)[1]

    ingestor = DataIngestorFactory.get_ingestor(file_extension)
    data_frame = ingestor.ingest(file_path)

    print(data_frame.head())
