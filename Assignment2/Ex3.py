import pandas as pd
import time


def load_csv(filepath):
    print(f"Loading CSV file from: {filepath}")
    start_time = time.time()

    try:
        df = pd.read_csv(filepath, engine='pyarrow', on_bad_lines='skip')
        end_time = time.time()
        load_time = end_time - start_time
        print(f"CSV file loaded successfully in {load_time:.2f} seconds.")
        print(f"Number of rows: {len(df)}")
        return df

    except Exception as e:
        print(f"Error occurred while reading the CSV file:", e)
        return None


def display_initial_rows(data):
    try:
        row_count = int(input("How many initial rows would you like to see? "))
        if row_count <= 0:
            raise ValueError
    except ValueError:
        print("Invalid input. Please enter a positive whole number.")
        return

    print(data.head(row_count))


def main():
    csv_file = 'https://drive.google.com/uc?id=1Fv_vhoN4sTrUaozFPfzr0NCyHJLIeXEA'
    sales_data = load_csv(csv_file)

    if sales_data is None:
        return

    print("Data types of the dataframe fields:")
    print(sales_data.dtypes)

    while True:
        display_initial_rows(sales_data)


if __name__ == "__main__":
    main()