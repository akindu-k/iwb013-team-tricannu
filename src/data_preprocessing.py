import pandas as pd

def load_data(file_path):
    """Load data from a CSV file."""
    return pd.read_csv(file_path)

def preprocess_data(df):
    """Preprocess the dataset to make it suitable for training."""
    # Example preprocessing steps:
    df['skills'] = df['skills'].apply(lambda x: x.split(','))
    return df
