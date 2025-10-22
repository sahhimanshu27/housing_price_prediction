from abc import ABC, abstractmethod
import pandas as pd

# Define an abstract base class for data analysis
'''This class provides a blueprint for data analysis tasks.'''
# Subclasses must implement the analyze method.
class DataInspectionStrategy(ABC):
    @abstractmethod
    def analyze(self, data: pd.DataFrame) -> None:
        '''

        Perform a specific type of data analysis on the provided DataFrame.
        Args:
            data (pd.DataFrame): The DataFrame to analyze.
        Returns:
            None

        '''
        pass

class DataTypeInspectionStrategy(DataInspectionStrategy):
    def analyze(self, data: pd.DataFrame) -> None:
        '''
        Prints the data types and non-null values of each column in the DataFrame.
        Args:
            data (pd.DataFrame): The DataFrame to analyze.
        Returns:
            None
        '''
        print("\nData Types and Non-Null Values:")
        print(data.info())

class SummaryStatisticsInspectionStrategy(DataInspectionStrategy):
    def analyze(self, data: pd.DataFrame) -> None:
        '''
        Prints summary statistics for numerical columns in the DataFrame.
        Args:
            data (pd.DataFrame): The DataFrame to analyze.
        Returns:
            None
        '''
        print("\nSummary Statistics (Numerical Features):")
        print(data.describe())
        print("\nSummary Statistics (Categorical Features):")
        print(data.describe(include=["O"]))

# Context class to use the inspection strategies
class DataInspector:
    def __init__(self, strategy: DataInspectionStrategy):
        '''
        Initializes with a specific data inspection strategy.
        Args:
            strategy (DataInspectionStrategy): The strategy to use for data inspection.
        '''
        self.strategy = strategy

    def execute_inspection(self, data: pd.DataFrame) -> None:
        '''
        Executes the data inspection using the selected strategy.
        Args:
            data (pd.DataFrame): The DataFrame to analyze.
        Returns:
            None
        '''
        self.strategy.analyze(data)

# Example usage
if __name__ == "__main__":
    # Sample DataFrame for demonstration
    data = pd.DataFrame({
        'A': [1, 2, 3, 4, 5],
        'B': [5.5, 6.5, 7.5, 8.5, 9.5],
        'C': ['foo', 'bar', 'baz', 'qux', 'quux']
    })

    # Inspect data types
    type_inspector = DataInspector(DataTypeInspectionStrategy())
    type_inspector.execute_inspection(data)

    # Inspect summary statistics
    stats_inspector = DataInspector(SummaryStatisticsInspectionStrategy())
    stats_inspector.execute_inspection(data)