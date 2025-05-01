import sys
import pandas as pd
from tabulate import tabulate


def analyze_csv(file_path):
    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    numeric_df = df.select_dtypes(include='number')
    if numeric_df.empty:
        print("No numeric columns found in the CSV.")
        return

    summary = numeric_df.agg(['mean', 'median', 'min', 'max']).transpose()
    summary.reset_index(inplace=True)
    summary.columns = ['Column', 'Mean', 'Median', 'Min', 'Max']

    print(tabulate(summary, headers='keys', tablefmt='grid'))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python analyze.py <csv_file>")
        sys.exit(1)

    analyze_csv(sys.argv[1])
