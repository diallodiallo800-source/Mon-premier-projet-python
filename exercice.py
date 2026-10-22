Sales = [200, 150, 250]

total = sum(Sales)
moyenne = total / len(Sales)

print("Total :", total)
print("Moyenne :", moyenne)
containers = [12,8,15,10,20]
total_containers = sum(containers)
moyenne_containers = total_containers / len(containers)

print("Total des conteneurs :", total_containers)
print("Moyenne des conteneurs :", moyenne_containers)

sales = [200, 150, 250]

total = sum(sales)
average = total / len(sales)
sales_max = max(sales)
sales_min = min(sales)

print("Total:", total)
print("Average:", average)
print("Max sales:", sales_max)
print("Min sales:", sales_min)

containers = [12, 8, 15, 10, 20,12]

total_containers = sum(containers)
average_containers = total_containers / len(containers)
containers_max = max(containers)
containers_min = min(containers)

print("Total containers:", total_containers)
print("Average containers:", average_containers)
print("Max containers:", containers_max)
print("Min containers:", containers_min)
import pandas as pd
df = pd.DataFrame({
    "jour": ["lundi", "mardi", "mercredi"],
    "conteneurs": [10, 15, 8]
})

print(df)   
df['conteneurs'].sum()
print(df['conteneurs'].sum())
df['conteneurs'].mean()
print(df['conteneurs'].mean())
df['conteneurs']>10
print(df[df["conteneurs"] > 10])
