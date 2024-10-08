import pandas as pd

# Create a DataFrame with sample data
data = pd.DataFrame({'Name': ["Anna", "Karen", "John", "Alice", "Kevin", "Sanna", "Bob", "Emily"],
                     'Age': [35, 30, 57, 65, 25, 19, 20, 65],
                     'Salary': [2, 6, 14, 17, 30, 100, 220, 120],
                     'Department': ["Tech", "Tech", "Tech", "Healthcare", "Operations", "Operations", "Tech", "Tech"]})

print(data.sort_values(by = "Salary"))

print("1. \n", data.sort_values(by = "Age", ascending=False))

print("2. \n", data.groupby("Department")["Name"].count())

print("3. \n", data.groupby("Department")["Salary"].mean())

print("4. \n", data.groupby("Department")["Age"].min())

print("5. \n", data.groupby("Department")["Age"].max())

print("6. \n", data[(data["Salary"] >= 100) & (data["Salary"] < 220)])

print("7. \n", data[data["Age"].isin([35, 30])])

# Read a CSV file
data_csv = pd.read_csv("percent-bachelors-degrees-women-usa.csv")
