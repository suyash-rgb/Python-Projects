import pandas as pd
from googlesearch import search
import re
import time

def fetch_linkedin_profile(name, company):
    query = f"{name} {company} site:linkedin.com/in/" 
    profiles = []

    try: 
        for url in search(query, num_results=5):
            if "linkedin.com/in/" in url:
                profiles.append(url)
        if profiles:
            return profiles[0]  # Return the first profile found
        else: 
            return f"No LinkedIn profiles found for {name} at {company}."
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Function to extract name from HYPERLINK
def extract_name(hyperlink):
    match = re.search(r'","(.*?)"\)$', hyperlink)
    if match:
        return match.group(1)
    return hyperlink  # Return the entire string if no match, assuming it might be the name directly

# Ask user to specify the row number
row_number = int(input("Enter the row number to process (starting from 1): "))

# Read the Excel file (assumed to be in the same folder as the script)
excel_file = 'input.xlsx'  # Update the file name as needed

# Read the Excel file
df = pd.read_excel(excel_file)

# Print column names to verify
print("Available columns:", df.columns)

# Specify the correct column names for name and company
name_column = "Client name "  # Update the column name for 'Client name'
company_column = "Company name"  # Update the column name for 'Company name'

# Get the specified row
row = df.iloc[row_number - 1]  # Subtract 1 because DataFrame index starts from 0

# Extract name and company from the specified row
name = extract_name(row[name_column].strip())  # Remove any leading or trailing whitespace
company = row[company_column].strip()  # Remove any leading or trailing whitespace
print(f"Processing: {name} from {company}")

# Fetch and print the LinkedIn profile
if name:
    profile = fetch_linkedin_profile(name, company)
    print(profile)  # Display the result in the console
    time.sleep(1)  # Pause for 1 second between searches
