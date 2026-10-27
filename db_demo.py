import sqlite3

# Create/connect to database
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''
CREATE TABLE IF NOT EXISTS leads (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    score INTEGER,
    source TEXT
)
''')

# Insert sample data
lead_data = [
    ("Hope", "hope@email.com", 90, "website"),
    ("Alice", "alice@email.com", 75, "social"),
    ("John", "john@email.com", 95, "referral")
]

cursor.executemany(
    "INSERT INTO leads (name, email, score, source) VALUES (?, ?, ?, ?)",
    lead_data
)

# Save changes
conn.commit()

# Read back the data
print("All leads:")
for row in cursor.execute("SELECT * FROM leads"):
    print(row)

print("\nHigh-scoring leads:")
for row in cursor.execute("SELECT name, email, score FROM leads WHERE score >= 80"):
    print(row)

# Close the database connection
conn.close()
print("\nSQLite database created and data inserted successfully.")
