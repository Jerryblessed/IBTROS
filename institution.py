
import sqlite3

# Dictionary of institute locations (Abuja, Nigeria) with an associated shuttle fare.
institute_fares = {
    "Zenith Bank Court of Appeal - MFM Dawko": 1500,
    "Powa International School - MFM Dawko": 1200,
    "St. Mary's Hospital - JRJ Academy, Aldenco": 2000,
    "Dunamis Church Airport road - JRJ Academy": 1000,
    "Abuja University - Powa Internation School": 1800,
    "National Hospital Abuja - MFM Uya": 2200,
    "Federal Secretariat - Abuja University": 1700,
    "Mitama Hopital - Dunamis Church": 1300,
}

db_path = "database.sqlite"

# Prepare a list of single institute records.
institute_records = []
for institute, fare in institute_fares.items():
    name = institute
    description = f"A shuttle trip to {institute}."
    price = fare  # Use the individual institute fare.
    image = None  # Placeholder for a future image (e.g., generated map or location preview)
    deleted = 0
    institute_records.append((name, description, price, image, deleted))

# Insert the institute records into the SQLite database.
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Assumes that there's a table named 'products' with columns 
# (name, description, price, image, deleted)
cursor.executemany(
    "INSERT INTO products (name, description, price, image, deleted) VALUES (?, ?, ?, ?, ?)",
    institute_records
)

conn.commit()
conn.close()

print(f"Inserted {len(institute_records)} records into the database.")




# import sqlite3

# # Path to your SQLite database file
# db_path = "database.sqlite"

# # Connect to the database
# conn = sqlite3.connect(db_path)
# cursor = conn.cursor()

# # Execute the query to clear the table
# cursor.execute("DELETE FROM products;")

# # Optionally, reclaim disk space if needed
# # cursor.execute("VACUUM;")

# # Commit the changes and close the connection
# conn.commit()
# conn.close()

# print("The 'products' table has been cleared.")
