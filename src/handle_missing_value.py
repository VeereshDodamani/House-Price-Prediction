import logging
from abc import ABC, abstractmethod

# Setup logging configuration
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


# Abstract Base Class for Missing Value Handling Strategy
class MissingValueHandlingStrategy(ABC):
    @abstractmethod
    def handle(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Abstract method to handle missing values in the DataFrame.

        Parameters:
        df (pd.DataFrame): The input DataFrame containing missing values.

        Returns:
        pd.DataFrame: The DataFrame with missing values handled.
        """
        pass


# Concrete Strategy for Dropping Missing Values
class DropMissingValuesStrategy(MissingValueHandlingStrategy):
    def __init__(self, axis=0, thresh=None):
        """
        Initializes the DropMissingValuesStrategy with specific parameters.

        Parameters:
        axis (int): 0 to drop rows with missing values, 1 to drop columns with missing values.
        thresh (int): The threshold for non-NA values. Rows/Columns with less than thresh non-NA values are dropped.
        """
        self.axis = axis
        self.thresh = thresh

    def handle(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Drops rows or columns with missing values based on the axis and threshold.

        Parameters:
        df (pd.DataFrame): The input DataFrame containing missing values.

        Returns:
        pd.DataFrame: The DataFrame with missing values dropped.
        """
        logging.info(f"Dropping missing values with axis={self.axis} and thresh={self.thresh}")
        df_cleaned = df.dropna(axis=self.axis, thresh=self.thresh)
        logging.info("Missing values dropped.")
        return df_cleaned
