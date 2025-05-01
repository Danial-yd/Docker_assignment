# Docker Assignment: CSV Analyzer

## Objective

This project involves creating a Python data processing script that analyzes CSV files and outputs summary statistics. The Python script is packaged into a Docker container, making it easy to run anywhere. 

### Steps involved:
1. **Write a Python script** to analyze CSV data.
2. **Create a Dockerfile** to build a Docker image.
3. **Build the Docker image** and run the container.
4. **Push the image to Docker Hub**.

---

## Step 1: Python Script - CSV Analyzer

The first step is writing a Python script that processes a CSV file and outputs some basic statistics. This was done using the **Pandas** library.

### Python Script (`csv_analyzer.py`)

```python
import pandas as pd

def analyze_csv(file_path):
    df = pd.read_csv(file_path)
    print(f"Summary Statistics of {file_path}:\n")
    print(df.describe())

# Example usage
if __name__ == "__main__":
    file_path = "data.csv"  # Specify the path to your CSV file here
    analyze_csv(file_path)


