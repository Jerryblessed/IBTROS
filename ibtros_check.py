import re
from fuzzywuzzy import process

# List of institutions in Abuja
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


def fuzzy_match_institution(input_name):
    """Return the best matching institution dictionary based on fuzzy matching."""
    best_match, score = process.extractOne(input_name, [inst['name'] for inst in institutions])
    
    # If confidence is low, return None
    if score < 50:
        return None
    
    # Find the matching institution and return the full dictionary
    for inst in institutions:
        if inst["name"] == best_match:
            return inst
    return None

def process_query(query):
    """
    Process the user's query:
      - Corrects 'From:' and 'To:' fields using fuzzy matching.
      - Supplies default values for missing fields:
          Round: True
          Wait time: 30 minutes
          Price: Sum of institution prices
    """
    # Split the query into lines
    lines = query.strip().split('\n')
    result_dict = {}
    
    # Set default values
    result_dict["Round"] = "True"
    result_dict["Wait time"] = "30 minutes"

    from_inst, to_inst = None, None
    
    for line in lines:
        line = line.strip()
        if line.startswith("From:"):
            inst_input = line[len("From:"):].strip()
            from_inst = fuzzy_match_institution(inst_input)
            result_dict["From"] = from_inst["name"] if from_inst else inst_input
        elif line.startswith("To:"):
            inst_input = line[len("To:"):].strip()
            inst_clean = re.sub(r'\bAldenco\b', '', inst_input, flags=re.IGNORECASE).strip()
            to_inst = fuzzy_match_institution(inst_clean)
            result_dict["To"] = to_inst["name"] if to_inst else inst_input

    # Calculate price as the sum of the 'From' and 'To' institution prices
    result_dict["Price"] = (from_inst["price"] if from_inst else 0) + (to_inst["price"] if to_inst else 0)

    # Build final output string
    output = f"From: {result_dict.get('From', '')}\n"
    output += f"To: {result_dict.get('To', '')}\n"
    output += f"Round: {result_dict.get('Round', '')}\n"
    output += f"Wait time: {result_dict.get('Wait time', '')}\n"
    output += f"Price: {result_dict.get('Price', '')}"
    return output

# Example user input
# user_input = """\
# From: Digital Bridge Institution 
# To: Azzess bank blc Garki Branch
# """

# final_output = process_query(user_input)
# print(final_output)
