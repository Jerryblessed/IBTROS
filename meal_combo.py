import sqlite3

# Connect to the SQLite database
db_path = "database.sqlite"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Provided institutions data

institutions = [
    {"name": "Access Bank Plc Garki Branch", "category": "Financial", "location": "Garki", "price": 2000},
    {"name": "Fidelity Bank Plc - NNPC Tower Abuja Branch", "category": "Financial", "location": "NNPC Towers", "price": 2000},
    {"name": "LOTUS Bank", "category": "Financial", "location": "Wuse II", "price": 2000},
    {"name": "TAJBank", "category": "Financial", "location": "Abuja", "price": 2000},
    {"name": "Family Homes Funds", "category": "Financial", "location": "Central Business District", "price": 2000},
    {"name": "Institute of Chartered Accountants of Nigeria (ICAN)", "category": "Financial", "location": "Wuse", "price": 2000},
    {"name": "University of Abuja", "category": "Educational", "location": "Gwagwalada", "price": 50000},
    {"name": "African University of Science and Technology", "category": "Educational", "location": "Abuja", "price": 50000},
    {"name": "Baze University", "category": "Educational", "location": "Abuja", "price": 50000},
    {"name": "National Open University", "category": "Educational", "location": "Abuja", "price": 50000},
    {"name": "Nile University of Nigeria", "category": "Educational", "location": "Abuja", "price": 50000},
    {"name": "Veritas University", "category": "Educational", "location": "Abuja", "price": 50000},
    {"name": "Miva Open University", "category": "Educational", "location": "Abuja", "price": 50000},
    {"name": "Federal College of Education, Zuba", "category": "Educational", "location": "Zuba", "price": 30000},
    {"name": "Aspire College of Technology", "category": "Educational", "location": "Abuja", "price": 30000},
    {"name": "Citi Polytechnic", "category": "Educational", "location": "Abuja", "price": 30000},
    {"name": "Dorben Polytechnic", "category": "Educational", "location": "Abuja", "price": 30000},
    {"name": "Federal Capital Territory (FCT) School of Nursing", "category": "Educational", "location": "Abuja", "price": 30000},
    {"name": "School of Nursing, Abuja University Teaching Hospital (AUTH)", "category": "Educational", "location": "Abuja", "price": 30000},
    {"name": "Federal Ministry Of Education Annex", "category": "Educational", "location": "Wuse", "price": 30000},
    {"name": "Abuja Preparatory School", "category": "Educational", "location": "Wuse", "price": 30000},
    {"name": "Digital Bridge Institute", "category": "Educational", "location": "Utako", "price": 30000},
    {"name": "FAMAKS British Schools", "category": "Educational", "location": "Aso", "price": 30000},
    {"name": "Christabel Schools", "category": "Educational", "location": "Wuye", "price": 30000},
    {"name": "Fortreal Real Estate Academy", "category": "Educational", "location": "Wuye", "price": 30000},
    {"name": "National Hospital Abuja", "category": "Health", "location": "Central Business District", "price": 5000},
    {"name": "Garki Hospital", "category": "Health", "location": "Garki", "price": 5000},
    {"name": "Maitama District Hospital", "category": "Health", "location": "Maitama", "price": 5000},
    {"name": "Wuse General Hospital", "category": "Health", "location": "Wuse", "price": 5000},
    {"name": "Nigerian National Mosque", "category": "Religious", "location": "Central Business District", "price": 0},
    {"name": "National Christian Centre", "category": "Religious", "location": "Central Business District", "price": 0},
    {"name": "All Saints Anglican Church", "category": "Religious", "location": "Wuse", "price": 0},
    {"name": "Holy Trinity Catholic Church", "category": "Religious", "location": "Maitama", "price": 0},
    {"name": "ECWA Good News Church", "category": "Religious", "location": "Maitama", "price": 0},
    {"name": "Word of Faith Group of Schools", "category": "Educational", "location": "Abuja", "price": 30000},
    {"name": "Dunamis International Gospel Centre Headquarters (Glory Dome)", "category": "Religious", "location": "Airport Road", "price": 0},
    {"name": "Dunamis International Gospel Centre, Area 1", "category": "Religious", "location": "Area 1", "price": 0},
    {"name": "Dunamis International Gospel Centre, Mararaba", "category": "Religious", "location": "Mararaba", "price": 0},
    {"name": "Mountain of Fire and Miracles Ministries, Utako", "category": "Religious", "location": "Utako", "price": 0},
    {"name": "Mountain of Fire and Miracles Ministries, Gwarinpa", "category": "Religious", "location": "Gwarinpa", "price": 0},
    {"name": "Mountain of Fire and Miracles Ministries, Kubwa", "category": "Religious", "location": "Kubwa", "price": 0},
    {"name": "Mountain of Fire and Miracles Ministries, Law School Assembly", "category": "Religious", "location": "Bwari", "price": 0},
    {"name": "Mountain of Fire and Miracles Ministries, Wuse", "category": "Religious", "location": "Wuse", "price": 0},
    {"name": "Mountain of Fire and Miracles Ministries, Maitama", "category": "Religious", "location": "Maitama", "price": 0},
    {"name": "Mountain of Fire and Miracles Ministries, Asokoro", "category": "Religious", "location": "Asokoro", "price": 0},
    {"name": "Mountain of Fire and Miracles Ministries, Nyanya", "category": "Religious", "location": "Nyanya", "price": 0},
    {"name": "Mountain of Fire and Miracles Ministries, Lugbe", "category": "Religious", "location": "Lugbe", "price": 0},

    
    ]

# Function to generate the name field (full ride details)
def generate_ride_name(from_inst, to_inst, price):
    return f"""From: {from_inst}
To: {to_inst}
Round: True
Wait time: 30 minutes
Price: {price}"""

# Function to generate the description field (short summary)
def generate_ride_description(from_inst, to_inst):
    return f"Ride from {from_inst} to {to_inst}"

def insert_rides():
    # Loop over all unique ordered pairs (i != j)
    for i in range(len(institutions)):
        for j in range(len(institutions)):
            if i != j:
                from_inst = institutions[i]["name"]
                to_inst = institutions[j]["name"]
                ride_price = institutions[i]["price"] + institutions[j]["price"]

                # Swap fields: Full details in `name`, short summary in `description`
                ride_name = generate_ride_name(from_inst, to_inst, ride_price)
                ride_description = generate_ride_description(from_inst, to_inst)

                cursor.execute("""
                    INSERT INTO products (name, description, price, deleted)
                    VALUES (?, ?, ?, ?)
                """, (ride_name, ride_description, ride_price, 0))  # Use 0 for False
    
    conn.commit()
    print("Ride entries added successfully.")

# Run the insertion function
insert_rides()

# Close the database connection
conn.close()
