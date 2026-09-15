import pandas as pd
import sqlite3

# Load CSV dataset
df = pd.read_csv("customer_complaints.csv")

# Connect to SQLite database
connection = sqlite3.connect("complaints.db")

# Store DataFrame in SQL table
df.to_sql(
    "complaints",
    connection,
    if_exists="replace",
    index=False
)

print("Dataset successfully stored in SQLite database")


# Query 1: Display all complaints
query1 = """
SELECT *
FROM complaints;
"""

result1 = pd.read_sql_query(query1, connection)

print("\nAll Complaints:")
print(result1)


# Query 2: Count complaints by category
query2 = """
SELECT category, COUNT(*) AS total_complaints
FROM complaints
GROUP BY category
ORDER BY total_complaints DESC;
"""

result2 = pd.read_sql_query(query2, connection)

print("\nComplaints by Category:")
print(result2)


# Query 3: Count complaints by status
query3 = """
SELECT status, COUNT(*) AS total_complaints
FROM complaints
GROUP BY status;
"""

result3 = pd.read_sql_query(query3, connection)

print("\nComplaints by Status:")
print(result3)


# Query 4: Average resolution time by team
query4 = """
SELECT assigned_team,
       AVG(resolution_time_hours) AS average_resolution_time
FROM complaints
GROUP BY assigned_team;
"""

result4 = pd.read_sql_query(query4, connection)

print("\nAverage Resolution Time by Team:")
print(result4)


# Query 5: High-priority pending complaints
query5 = """
SELECT *
FROM complaints
WHERE priority = 'High'
AND status = 'Pending';
"""

result5 = pd.read_sql_query(query5, connection)

print("\nHigh-Priority Pending Complaints:")
print(result5)


# Close database connection
connection.close()

print("\nDatabase connection closed")