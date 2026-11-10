import pandas as pd
import time
import sys
from pathlib import Path


def load_csv(filepath):
    print(f"Loading CSV file from: {filepath}")
    start_time = time.time()

    try:
        df = pd.read_csv(filepath, engine='pyarrow', on_bad_lines='skip')
        end_time = time.time()
        load_time = end_time - start_time
        print(f"Time taken to load CSV file: {load_time} seconds")
        print("Number of rows loaded:", len(df))
        return df

    except Exception as e:
        print(f"An error occurred while reading the CSV file: {e}")
        return None


def display_data_summary(data):
    """Display available sales-data metrics, identifying missing source columns."""
    print("\nSales data summary:")

    def show_metric(label, required_columns, calculate):
        missing_columns = [
            column for column in required_columns if column not in data.columns
        ]
        if missing_columns:
            print(
                f"{label}: Unavailable (missing columns: "
                f"{', '.join(missing_columns)})"
            )
        else:
            print(f"{label}: {calculate(data)}")

    show_metric(
        "Total orders",
        ("order_number",),
        lambda frame: f"{frame['order_number'].nunique():,}",
    )
    employee_column = next(
        (
            column
            for column in ("employee_id", "employee_name")
            if column in data.columns
        ),
        None,
    )
    if employee_column:
        print(f"Number of employees: {data[employee_column].nunique():,}")
    else:
        print("Number of employees: Unavailable (missing employee_id or employee_name)")

    show_metric(
        "Sales regions",
        ("sales_region",),
        lambda frame: f"{frame['sales_region'].nunique():,}",
    )

    def order_date_range(frame):
        raw_dates = frame["order_date"]
        if pd.api.types.is_datetime64_any_dtype(raw_dates):
            dates = pd.to_datetime(raw_dates, errors="coerce").dropna()
        else:
            date_strings = raw_dates.astype("string").str.strip()
            short_year_dates = date_strings.str.fullmatch(
                r"\d{1,2}/\d{1,2}/\d{2}", na=False
            )
            long_year_dates = date_strings.str.fullmatch(
                r"\d{1,2}/\d{1,2}/\d{4}", na=False
            )
            parsed_dates = []
            if short_year_dates.any():
                parsed_dates.append(
                    pd.to_datetime(
                        date_strings[short_year_dates],
                        format="%m/%d/%y",
                        errors="coerce",
                    )
                )
            if long_year_dates.any():
                parsed_dates.append(
                    pd.to_datetime(
                        date_strings[long_year_dates],
                        format="%d/%m/%Y",
                        errors="coerce",
                    )
                )
            other_dates = ~(short_year_dates | long_year_dates)
            if other_dates.any():
                parsed_dates.append(
                    pd.to_datetime(
                        date_strings[other_dates],
                        format="mixed",
                        dayfirst=True,
                        errors="coerce",
                    )
                )
            dates = (
                pd.concat(parsed_dates).dropna()
                if parsed_dates
                else pd.Series(dtype="datetime64[ns]")
            )
        if dates.empty:
            return "No valid dates"
        return f"{dates.min():%Y-%m-%d} to {dates.max():%Y-%m-%d}"

    show_metric("Order date range", ("order_date",), order_date_range)

    customer_column = next(
        (
            column
            for column in ("customer_id", "customer_name")
            if column in data.columns
        ),
        None,
    )
    if customer_column:
        print(f"Unique customers: {data[customer_column].nunique():,}")
    else:
        print("Unique customers: Unavailable (missing customer_id or customer_name)")

    show_metric(
        "Product categories",
        ("product_category",),
        lambda frame: f"{frame['product_category'].nunique():,}",
    )
    show_metric(
        "Unique states",
        ("customer_state",),
        lambda frame: f"{frame['customer_state'].nunique():,}",
    )

    def total_sales_amount(frame):
        sales = (
            pd.to_numeric(frame["unit_price"], errors="coerce")
            * pd.to_numeric(frame["quantity"], errors="coerce")
        ).sum(min_count=1)
        if pd.isna(sales):
            return "No numeric sales data"
        return f"${sales:,.2f}"

    show_metric(
        "Total sales amount",
        ("unit_price", "quantity"),
        total_sales_amount,
    )

    def total_quantity(frame):
        quantity = pd.to_numeric(frame["quantity"], errors="coerce").sum(
            min_count=1
        )
        if pd.isna(quantity):
            return "No numeric quantity data"
        return f"{quantity:,.2f}".rstrip("0").rstrip(".")

    show_metric("Total quantities sold", ("quantity",), total_quantity)


def display_initial_rows(data):
    """Prompt for and display a requested number of initial DataFrame rows."""
    try:
        row_count = int(input("How many initial rows would you like to see? "))
        if row_count < 0:
            print("Please enter a non-negative whole number.")
            return
    except ValueError:
        print("Invalid input. Please enter a non-negative whole number.")
        return

    result = data.head(row_count)
    print(result)
    offer_csv_export(result)


def offer_csv_export(result):
    """Ask whether to save a displayed result as an Excel-readable CSV file."""
    while True:
        choice = input(
            "Would you like to export this result to a CSV file that opens in Excel? (y/n): "
        ).strip().lower()
        if choice in ("y", "yes"):
            break
        if choice in ("n", "no"):
            return
        print("Please enter y or n.")

    while True:
        filename = input("What filename would you like to use? ").strip()
        if filename:
            break
        print("Please enter a filename.")

    output_path = Path(filename)
    if output_path.suffix.lower() != ".csv":
        output_path = output_path.with_suffix(".csv")

    try:
        result.to_csv(output_path)
    except (OSError, ValueError) as error:
        print(f"Could not export the result to {output_path}: {error}")
        return

    print(f"Result exported to {output_path}")


def exit_program(data):
    """Exit the application."""
    print("Exiting the program.")
    sys.exit(0)


def sales_by_region_order_type(data):
    """Display the number of unique employees in each sales region."""
    result = pd.pivot_table(
        data,
        values='employee_id',
        index='sales_region',
        aggfunc='nunique',
    )
    print(result)
    offer_csv_export(result)


def show_employees_by_region(data):
    sales_by_region_order_type(data)


def get_user_selection(options, prompt):
    """Return selected options, accepting comma-separated option numbers."""
    while True:
        print(prompt)
        for i, option in enumerate(options):
            print(f"{i + 1}. {option}")

        choice = input(
            "Enter the number(s) of your choice(s), separated by commas: "
        ).strip()
        if not choice:
            return []

        try:
            indices = [int(item.strip()) for item in choice.split(",")]
        except ValueError:
            print("Invalid selection. Enter option numbers separated by commas.")
            continue

        if any(index < 1 or index > len(options) for index in indices):
            print(f"Invalid selection. Enter numbers from 1 to {len(options)}.")
            continue

        return list(dict.fromkeys(options[index - 1] for index in indices))


def generate_custom_pivot_table(data):
    """Collect pivot-table dimensions and display the resulting table."""
    row_options = list(data.columns)
    rows = get_user_selection(row_options, "Select rows:")
    while not rows:
        print("At least one row selection is required.")
        rows = get_user_selection(row_options, "Select rows:")

    col_options = row_options
    col_options = [col for col in col_options if col not in rows]
    cols = get_user_selection(col_options, "Select columns (optional; press Enter to skip):")

    value_options = list(data.select_dtypes(include=['number']).columns)
    if not value_options:
        print("No numeric columns are available to aggregate.")
        return

    values = get_user_selection(value_options, "Select values:")
    while not values:
        print("At least one value selection is required.")
        values = get_user_selection(value_options, "Select values:")

    agg_options = ['sum', 'mean', 'count']
    agg_func = get_user_selection(agg_options, "Select aggregation function(s):")
    while not agg_func:
        print("At least one aggregation function is required.")
        agg_func = get_user_selection(agg_options, "Select aggregation function(s):")

    result = pd.pivot_table(
        data,
        index=rows,
        columns=cols if cols else None,
        values=values,
        aggfunc=agg_func,
    )
    print(result)
    offer_csv_export(result)


menu_options = (
    ("Show the first n rows of sales data", display_initial_rows, ()),
    (
        "Show the number of employees by region",
        show_employees_by_region,
        ("employee_id", "sales_region"),
    ),
    ("Generate a custom pivot table", generate_custom_pivot_table, ()),
    ("Exit the program", exit_program, ()),
)


def get_available_menu_options(data):
    """Exclude predefined actions whose required columns are unavailable."""
    return tuple(
        (description, action)
        for description, action, required_columns in menu_options
        if all(column in data.columns for column in required_columns)
    )


def display_menu(options):
    """Display available actions and return the user's selection."""
    print("\nMenu:")
    for number, (description, _) in enumerate(options, start=1):
        print(f"{number}. {description}")
    return input("Select an option: ").strip()


def main():
    csv_file = 'https://drive.google.com/uc?id=1Fv_vhoN4sTrUaozFPfzr0NCyHJLIeXEA'
    sales_data = load_csv(csv_file)

    if sales_data is None:
        return

    display_data_summary(sales_data)
    available_options = get_available_menu_options(sales_data)

    while True:
        selection = display_menu(available_options)
        try:
            option_number = int(selection)
        except ValueError:
            print(
                f"Invalid selection. Enter a number from 1 to "
                f"{len(available_options)}."
            )
            continue

        if not 1 <= option_number <= len(available_options):
            print(
                f"Invalid selection. Enter a number from 1 to "
                f"{len(available_options)}."
            )
            continue

        _, action = available_options[option_number - 1]
        action(sales_data)


if __name__ == "__main__":
    main()