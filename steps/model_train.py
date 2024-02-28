import logging
import pandas as pd
from zenml import step

@step
def train_model(df: pd.DataFrame) -> None:
    """
    Train the model on the ingested and cleaned data

    Args:
        df: the cleaned data
    """
    pass