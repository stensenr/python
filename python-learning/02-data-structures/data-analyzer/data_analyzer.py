import pandas as pd
import matplotlib.pyplot as plt

def create_sample_data():
    """Create a sample CSV file with sales data."""
    data = {
        'Date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05',
                 '2024-01-06', '2024-01-07', '2024-01-08', '2024-01-09', '2024-01-10'],
        'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Laptop',
                   'Mouse', 'Keyboard', 'Monitor', 'Laptop', 'Mouse'],
        'Sales': [1200, 25, 75, 300, 1150, 30, 80, 320, 1180, 28],
        'Quantity': [2, 5, 3, 1, 2, 6, 4, 1, 2, 5],
        'Region': ['North', 'South', 'East', 'West', 'North',
                  'South', 'East', 'West', 'North', 'South']
    }
    
    df = pd.DataFrame(data)
    df.to_csv('sales_data.csv', index=False)
    print("✓ Sample data created: sales_data.csv")
    return df


def load_data(filename):
    """Load data from CSV file.
    
    Args:
        filename: Name of the CSV file to load
    
    Returns:
        DataFrame with the loaded data
    """
    try:
        df = pd.read_csv(filename)
        print(f"✓ Loaded {len(df)} rows from {filename}")
        return df
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
        return None
    except Exception as e:
        print(f"Error loading file: {e}")
        return None


def display_basic_info(df):
    """Display basic information about the dataset."""
    print("\n=== DATASET INFORMATION ===")
    print(f"Number of rows: {len(df)}")
    print(f"Number of columns: {len(df.columns)}")
    print(f"\nColumn names: {list(df.columns)}")
    print(f"\nData types:")
    print(df.dtypes)
    print(f"\nFirst 5 rows:")
    print(df.head())


def calculate_statistics(df):
    """Calculate and display statistics for numeric columns."""
    print("\n=== SALES STATISTICS ===")
    
    # Statistics for Sales column
    print(f"\nSales:")
    print(f"  Mean: ${df['Sales'].mean():.2f}")
    print(f"  Median: ${df['Sales'].median():.2f}")
    print(f"  Min: ${df['Sales'].min():.2f}")
    print(f"  Max: ${df['Sales'].max():.2f}")
    print(f"  Total: ${df['Sales'].sum():.2f}")
    
    # Statistics for Quantity column
    print(f"\nQuantity:")
    print(f"  Mean: {df['Quantity'].mean():.2f}")
    print(f"  Median: {df['Quantity'].median():.2f}")
    print(f"  Min: {df['Quantity'].min()}")
    print(f"  Max: {df['Quantity'].max()}")
    print(f"  Total: {df['Quantity'].sum()}")

def filter_data(df):
    """Demonstrate data filtering."""
    print("\n=== DATA FILTERING ===")
    
    # Filter: Sales greater than 100
    high_sales = df[df['Sales'] > 100]
    print(f"\nHigh value sales (>$100): {len(high_sales)} transactions")
    print(high_sales[['Product', 'Sales', 'Region']])
    
    # Filter: Specific product
    laptop_sales = df[df['Product'] == 'Laptop']
    print(f"\nLaptop sales: {len(laptop_sales)} transactions")
    print(f"Total laptop revenue: ${laptop_sales['Sales'].sum():.2f}")
    
    # Filter: Multiple conditions
    north_laptops = df[(df['Product'] == 'Laptop') & (df['Region'] == 'North')]
    print(f"\nLaptops sold in North region: {len(north_laptops)} transactions")
    print(north_laptops[['Date', 'Sales', 'Quantity']])


def group_data(df):
    """Demonstrate data grouping and aggregation."""
    print("\n=== DATA GROUPING ===")
    
    # Group by Product
    print("\nSales by Product:")
    product_sales = df.groupby('Product')['Sales'].agg(['sum', 'mean', 'count'])
    product_sales.columns = ['Total Sales', 'Average Sale', 'Number of Sales']
    print(product_sales)
    
    # Group by Region
    print("\nSales by Region:")
    region_sales = df.groupby('Region')['Sales'].agg(['sum', 'mean'])
    region_sales.columns = ['Total Sales', 'Average Sale']
    print(region_sales)
    
    # Group by multiple columns
    print("\nSales by Product and Region:")
    product_region = df.groupby(['Product', 'Region'])['Sales'].sum()
    print(product_region)


def find_top_products(df, n=3):
    """Find top N products by total sales."""
    print(f"\n=== TOP {n} PRODUCTS ===")
    
    top_products = df.groupby('Product')['Sales'].sum().sort_values(ascending=False).head(n)
    
    for i, (product, sales) in enumerate(top_products.items(), 1):
        print(f"{i}. {product}: ${sales:.2f}")

def create_sales_chart(df):
    """Create a bar chart of total sales by product."""
    print("\n=== CREATING SALES CHART ===")
    
    # Calculate total sales by product
    product_sales = df.groupby('Product')['Sales'].sum().sort_values(ascending=False)
    
    # Create the bar chart
    plt.figure(figsize=(10, 6))
    product_sales.plot(kind='bar', color='steelblue')
    plt.title('Total Sales by Product', fontsize=16, fontweight='bold')
    plt.xlabel('Product', fontsize=12)
    plt.ylabel('Total Sales ($)', fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    
    # Save the chart
    plt.savefig('sales_by_product.png')
    print("✓ Chart saved: sales_by_product.png")
    plt.close()


def create_region_chart(df):
    """Create a pie chart of sales by region."""
    print("\n=== CREATING REGION CHART ===")
    
    # Calculate total sales by region
    region_sales = df.groupby('Region')['Sales'].sum()
    
    # Create the pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(region_sales, labels=region_sales.index, autopct='%1.1f%%', 
            startangle=90, colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99'])
    plt.title('Sales Distribution by Region', fontsize=16, fontweight='bold')
    plt.tight_layout()
    
    # Save the chart
    plt.savefig('sales_by_region.png')
    print("✓ Chart saved: sales_by_region.png")
    plt.close()


def create_time_series(df):
    """Create a line chart showing sales over time."""
    print("\n=== CREATING TIME SERIES CHART ===")
    
    # Convert Date to datetime and set as index
    df_copy = df.copy()
    df_copy['Date'] = pd.to_datetime(df_copy['Date'])
    df_copy = df_copy.sort_values('Date')
    
    # Create the line chart
    plt.figure(figsize=(12, 6))
    plt.plot(df_copy['Date'], df_copy['Sales'], marker='o', linewidth=2, markersize=8)
    plt.title('Sales Over Time', fontsize=16, fontweight='bold')
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Sales ($)', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Save the chart
    plt.savefig('sales_over_time.png')
    print("✓ Chart saved: sales_over_time.png")
    plt.close()


def create_comparison_chart(df):
    """Create a grouped bar chart comparing products across regions."""
    print("\n=== CREATING COMPARISON CHART ===")
    
    # Pivot data for comparison
    pivot_data = df.pivot_table(values='Sales', index='Product', columns='Region', aggfunc='sum', fill_value=0)
    
    # Create the grouped bar chart
    pivot_data.plot(kind='bar', figsize=(12, 6), width=0.8)
    plt.title('Sales Comparison: Products by Region', fontsize=16, fontweight='bold')
    plt.xlabel('Product', fontsize=12)
    plt.ylabel('Sales ($)', fontsize=12)
    plt.legend(title='Region', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.xticks(rotation=45)
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    
    # Save the chart
    plt.savefig('sales_comparison.png')
    print("✓ Chart saved: sales_comparison.png")
    plt.close()

def display_menu():
    """Display the main menu."""
    print("\n" + "="*50)
    print("           DATA ANALYZER MENU")
    print("="*50)
    print("1. Display dataset information")
    print("2. Calculate statistics")
    print("3. Filter data")
    print("4. Group and aggregate data")
    print("5. Find top products")
    print("6. Create all visualizations")
    print("7. Create sales by product chart")
    print("8. Create sales by region chart")
    print("9. Create time series chart")
    print("10. Create comparison chart")
    print("11. Export filtered data")
    print("12. Exit")
    print("="*50)

def export_filtered_data(df):
    """Allow user to filter and export data."""
    print("\n=== EXPORT FILTERED DATA ===")
    print("1. Export high-value sales (>$100)")
    print("2. Export specific product")
    print("3. Export specific region")
    print("4. Export all data")
    
    choice = input("\nEnter your choice (1-4): ").strip()
    
    if choice == "1":
        filtered = df[df['Sales'] > 100]
        filename = 'high_value_sales.csv'
    elif choice == "2":
        product = input("Enter product name: ").strip()
        filtered = df[df['Product'] == product]
        filename = f'{product.lower()}_sales.csv'
    elif choice == "3":
        region = input("Enter region name: ").strip()
        filtered = df[df['Region'] == region]
        filename = f'{region.lower()}_sales.csv'
    elif choice == "4":
        filtered = df
        filename = 'all_sales_export.csv'
    else:
        print("Invalid choice!")
        return
    
    filtered.to_csv(filename, index=False)
    print(f"✓ Exported {len(filtered)} rows to {filename}")


def main():
    """Main function to run the data analyzer."""
    print("=== DATA ANALYZER ===\n")
    
    # Create sample data if it doesn't exist
    import os
    if not os.path.exists('sales_data.csv'):
        print("Creating sample data...")
        create_sample_data()
    
    # Load the data
    print("Loading data...")
    df = load_data('sales_data.csv')
    
    if df is None:
        print("Failed to load data. Exiting.")
        return
    
    print(f"✓ Dataset loaded: {len(df)} rows, {len(df.columns)} columns")
    
    # Main loop
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-12): ").strip()
        
        if choice == "1":
            display_basic_info(df)
        
        elif choice == "2":
            calculate_statistics(df)
        
        elif choice == "3":
            filter_data(df)
        
        elif choice == "4":
            group_data(df)
        
        elif choice == "5":
            try:
                n = int(input("How many top products to show? (default 3): ").strip() or 3)
                find_top_products(df, n=n)
            except ValueError:
                print("Invalid number, showing top 3")
                find_top_products(df, n=3)
        
        elif choice == "6":
            print("\nCreating all visualizations...")
            create_sales_chart(df)
            create_region_chart(df)
            create_time_series(df)
            create_comparison_chart(df)
            print("\n✓ All visualizations created!")
        
        elif choice == "7":
            create_sales_chart(df)
        
        elif choice == "8":
            create_region_chart(df)
        
        elif choice == "9":
            create_time_series(df)
        
        elif choice == "10":
            create_comparison_chart(df)
        
        elif choice == "11":
            export_filtered_data(df)
        
        elif choice == "12":
            print("\nThank you for using Data Analyzer!")
            print("Goodbye! 📊")
            break
        
        else:
            print("Invalid choice. Please enter 1-12.")


if __name__ == "__main__":
    main()