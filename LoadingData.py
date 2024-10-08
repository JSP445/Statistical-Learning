import pandas as pd
import sqlite3

data_csv = pd.read_csv("percent-bachelors-degrees-women-usa.csv")
#print(data_csv)

print(data_csv.info())

# To drop missing values from a database

# print(data_csv.dropna())

# To fill N/A values with a dummy variable

# print(data_csv.fillna("NULL"))

# To drop duplicate entries

# print(data_csv.drop_duplicates())

# To retrieve the data index in the position of a table where the headers aren't integers and are strings

print(data_csv.iloc[10])

# For text files

data_txt = pd.read_csv("StudentSchools.txt", header = 0, sep = ',')
#print(data_txt)



# For Excel files

# data_excel = pd.read_excel("file.xlsx", sheet_name = "ExampleSpreadSheet")

# For JSON files

# data_json = pd.read_json("file.json")

# For SQL databases

#connection_db = sqlite3.connect("database_name.db")
#query = 'SELECT col_1 FROM table_1'
#data_sql = pd.read_sql(query, connection_db)

