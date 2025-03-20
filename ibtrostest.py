import random

# List of institutions in Abuja
institutions = [
    {"name": "Access Bank Plc Garki Branch", "category": "Financial", "location": "Garki"},
    {"name": "Fidelity Bank Plc - NNPC Tower Abuja Branch", "category": "Financial", "location": "NNPC Towers"},
    {"name": "LOTUS Bank", "category": "Financial", "location": "Wuse II"},
    {"name": "TAJBank", "category": "Financial", "location": "Abuja"},
    {"name": "Family Homes Funds", "category": "Financial", "location": "Central Business District"},
    {"name": "Institute of Chartered Accountants of Nigeria (ICAN)", "category": "Financial", "location": "Wuse"},
    {"name": "University of Abuja", "category": "Educational", "location": "Gwagwalada"},
    {"name": "African University of Science and Technology", "category": "Educational", "location": "Abuja"},
    {"name": "Baze University", "category": "Educational", "location": "Abuja"},
    {"name": "National Open University", "category": "Educational", "location": "Abuja"},
    {"name": "Nile University of Nigeria", "category": "Educational", "location": "Abuja"},
    {"name": "Veritas University", "category": "Educational", "location": "Abuja"},
    {"name": "Miva Open University", "category": "Educational", "location": "Abuja"},
    {"name": "Federal College of Education, Zuba", "category": "Educational", "location": "Zuba"},
    {"name": "Aspire College of Technology", "category": "Educational", "location": "Abuja"},
    {"name": "Citi Polytechnic", "category": "Educational", "location": "Abuja"},
    {"name": "Dorben Polytechnic", "category": "Educational", "location": "Abuja"},
    {"name": "Federal Capital Territory (FCT) School of Nursing", "category": "Educational", "location": "Abuja"},
    {"name": "School of Nursing, Abuja University Teaching Hospital (AUTH)", "category": "Educational", "location": "Abuja"},
    {"name": "Federal Ministry Of Education Annex", "category": "Educational", "location": "Wuse"},
    {"name": "Abuja Preparatory School", "category": "Educational", "location": "Wuse"},
    {"name": "Digital Bridge Institute", "category": "Educational", "location": "Utako"},
    {"name": "FAMAKS British Schools", "category": "Educational", "location": "Aso"},
    {"name": "Christabel Schools", "category": "Educational", "location": "Wuye"},
    {"name": "Fortreal Real Estate Academy", "category": "Educational", "location": "Wuye"},
    {"name": "National Hospital Abuja", "category": "Health", "location": "Central Business District"},
    {"name": "Garki Hospital", "category": "Health", "location": "Garki"},
    {"name": "Maitama District Hospital", "category": "Health", "location": "Maitama"},
    {"name": "Wuse General Hospital", "category": "Health", "location": "Wuse"},
    {"name": "Nigerian National Mosque", "category": "Religious", "location": "Central Business District"},
    {"name": "National Christian Centre", "category": "Religious", "location": "Central Business District"},
    {"name": "All Saints Anglican Church", "category": "Religious", "location": "Wuse"},
    {"name": "Holy Trinity Catholic Church", "category": "Religious", "location": "Maitama"},
    {"name": "ECWA Good News Church", "category": "Religious", "location": "Maitama"},
    {"name": "Word of Faith Group of Schools", "category": "Educational", "location": "Abuja"},
    {"name": "Dunamis International Gospel Centre Headquarters (Glory Dome)", "category": "Religious", "location": "Airport Road"},
    {"name": "Dunamis International Gospel Centre, Area 1", "category": "Religious", "location": "Area 1"},
    {"name": "Dunamis International Gospel Centre, Mararaba", "category": "Religious", "location": "Mararaba"},
    {"name": "Mountain of Fire and Miracles Ministries, Utako", "category": "Religious", "location": "Utako"},
    {"name": "Mountain of Fire and Miracles Ministries, Gwarinpa", "category": "Religious", "location": "Gwarinpa"},
    {"name": "Mountain of Fire and Miracles Ministries, Kubwa", "category": "Religious", "location": "Kubwa"},
    {"name": "Mountain of Fire and Miracles Ministries, Law School Assembly", "category": "Religious", "location": "Bwari"},
    {"name": "Mountain of Fire and Miracles Ministries, Wuse", "category": "Religious", "location": "Wuse"},
    {"name": "Mountain of Fire and Miracles Ministries, Maitama", "category": "Religious", "location": "Maitama"},
    {"name": "Mountain of Fire and Miracles Ministries, Asokoro", "category": "Religious", "location": "Asokoro"},
    {"name": "Mountain of Fire and Miracles Ministries, Nyanya", "category": "Religious", "location": "Nyanya"},
    {"name": "Mountain of Fire and Miracles Ministries, Lugbe", "category": "Religious", "location": "Lugbe"},
    {"name": "Mountain of Fire and Miracles Ministries, Karu", "category": "Religious", "location": "Karu"},
    {"name": "Mountain of Fire and Miracles Ministries, Jabi", "category": "Religious", "location": "Jabi"},
    {"name": "Mountain of Fire and Miracles Ministries, Kuje", "category": "Religious", "location": "Kuje"},
    {"name": "Mountain of Fire and Miracles Ministries, Gwagwalada", "category": "Religious", "location": "Gwagwalada"},
    {"name": "Mountain of Fire and Miracles Ministries, Dei-Dei", "category": "Religious", "location": "Dei-Dei"},
    {"name": "Mountain of Fire and Miracles Ministries, Mpape", "category": "Religious", "location": "Mpape"},
    {"name": "Mountain of Fire and Miracles Ministries, Karshi", "category": "Religious", "location": "Karshi"},
    {"name": "Mountain of Fire and Miracles Ministries, Airport Road", "category": "Religious", "location":
        "Airport Road"},
]

# Function to generate transportation schedules
def generate_transportation_schedules(institutions, num_schedules=20):
    schedules = []
    for _ in range(num_schedules):
        from_inst = random.choice(institutions)
        to_inst = random.choice([inst for inst in institutions if inst != from_inst])
        round_trip = random.choice([True, False])
        wait_time = random.choice([15, 30, 45, 60])  # in minutes
        schedule = {
            "From": f"{from_inst['name']} ({from_inst['category']})",
            "To": f"{to_inst['name']} ({to_inst['category']})",
            "Round": round_trip,
            "Wait time": f"{wait_time} minutes"
        }
        schedules.append(schedule)
    return schedules

# Generate and display the schedules
schedules = generate_transportation_schedules(institutions)
for schedule in schedules:
    print(f"From(pickup): {schedule['From']}")
    print(f"To: {schedule['To']}")
    print(f"Round: {schedule['Round']}")
    print(f"Wait time: {schedule['Wait time']}\n")

