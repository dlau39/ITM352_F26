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


def exit_program(data):
    print("Exiting program.")
    raise SystemExit(0)


def sales_by_region_order_type(data):
    required_columns = {"sales_region", "order_type", "employee_id"}
    missing_columns = required_columns.difference(data.columns)
    if missing_columns:
        raise ValueError(
            "Cannot create employee pivot table; missing columns: "
            + ", ".join(sorted(missing_columns))
        )

    pivot_table = pd.pivot_table(
        data,
        values="employee_id",
        index="sales_region",
        columns="order_type",
        aggfunc=pd.Series.nunique,
        fill_value=0,
        margins=True,
        margins_name="Total",
    )
    print(pivot_table)


def show_employees_by_region(data):
    sales_by_region_order_type(data)


menu_options = (
    ("Show the first n rows of sales data", display_initial_rows),
    ("Show the number of employees by region", show_employees_by_region),
    ("Exit the program", exit_program),
)


def display_menu():
    print("\nSales Data Menu")
    for number, (description, _) in enumerate(menu_options, start=1):
        print(f"{number}. {description}")
    return input("Select an option: ")


def main():
    csv_file = 'https://drive.google.com/uc?id=1Fv_vhoN4sTrUaozFPfzr0NCyHJLIeXEA'
    sales_data = load_csv(csv_file)

    if sales_data is None:
        return

    print("Data types of the dataframe fields:")
    print(sales_data.dtypes)

    while True:
        selection = display_menu()
        try:
            option_number = int(selection)
            if option_number < 1 or option_number > len(menu_options):
                raise ValueError
        except ValueError:
            print(f"Invalid selection. Enter a number from 1 to {len(menu_options)}.")
            continue

        _, action = menu_options[option_number - 1]
        action(sales_data)


if __name__ == "__main__":
    main()