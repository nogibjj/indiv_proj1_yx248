# lib.py

import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path="dataset_sample.csv"):
    """Load data from the given file path."""
    return pd.read_csv(file_path)

def get_descriptive_statistics(data):
    """Return descriptive statistics of the data."""
    return data.describe()

def plot_data_distribution(data, column_name, save=True):
    """Plot and save the distribution of data for a specific column."""
    plt.figure(figsize=(10, 6))
    plt.hist(data[column_name], bins=10, edgecolor="k", alpha=0.7)
    plt.title(f"Distribution of {column_name}")
    plt.xlabel(column_name)
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.tight_layout()
    if save:
        plt.savefig(f"{column_name}_distribution.png")
    plt.show()
