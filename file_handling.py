
# PLACEHOLDERRRRR ONLY  

import csv
import pandas as pd

def split_csv(file_path, rows_per_file):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)
        rows = list(reader)

    file_count = 1
    for i in range(0, len(rows), rows_per_file):
        with open(f'sales_data_{file_count}.csv', 'w', newline='') as output_file:
            writer = csv.writer(output_file)
            writer.writerow(headers)
            writer.writerows(rows[i:i+rows_per_file])
        file_count += 1

def column_to_set(filepath, column_name) -> set[str]:
  df = pd.read_csv(filepath)
  return {
      str(val).strip().lower()
      for val in df[column_name].dropna()
      if str(val).strip()
  }

if __name__ == "__main__":
    split_csv('sales_data.csv', 500)