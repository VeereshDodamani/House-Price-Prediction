from abc import ABC, abstractmethod

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


class BivariateAnalysisStrategy(ABC):
    @abstractmethod
    def analyze(df: pd.DataFrame, feature1: str, feature2: str):
        """
        Perform bivariate analysis on two features of the dataframe.

        Parameters:
        df (pd.DataFrame): The dataframe containing the data.
        feature1 (str): The name of the first feature/column to be analyzed.
        feature2 (str): The name of the second feature/column to be analyzed.

        Returns:
        None: This method visualizes the relationship between the two features.
        """
        pass
