import pandas as pd

# Basic calculations with sales
sales = [200, 150, 250]

total_sales = sum(sales)
average_sales = total_sales / len(sales)
maximum_sales = max(sales)
minimum_sales = min(sales)

print("Total sales:", total_sales)
print("Average sales:", average_sales)
print("Maximum sales:", maximum_sales)
print("Minimum sales:", minimum_sales)

# Basic calculations with containers
containers = [12, 8, 15, 10, 20, 12]

total_containers = sum(containers)
average_containers = total_containers / len(containers)
maximum_containers = max(containers)
minimum_containers = min(containers)

print("Total containers:", total_containers)
print("Average containers:", average_containers)
print("Maximum containers:", maximum_containers)
print("Minimum containers:", minimum_containers)

# Create a pandas DataFrame
data = {
    "day": ["Monday", "Tuesday", "Wednesday"],
    "containers": [10, 15, 8],
}

df = pd.DataFrame(data)

print("\nContainer data:")
print(df)

# Calculate the total and average with pandas
print("\nTotal containers in the table:", df["containers"].sum())
print("Average containers in the table:", df["containers"].mean())

# Show only the days with more than 10 containers
print("\nDays with more than 10 containers:")
print(df[df["containers"] > 10])