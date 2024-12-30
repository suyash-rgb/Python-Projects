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
            print(f"Found profile for {name} at {company}: {profiles[0]}")
            return profiles[0]  # Return the first profile found
        else: 
            print(f"No LinkedIn profiles found for {name} at {company}.")
            return f"No LinkedIn profiles found for {name} at {company}."
    except Exception as e:
        print(f"An error occurred while searching for {name} at {company}: {str(e)}")
        return f"An error occurred: {str(e)}"

# Function to extract name from HYPERLINK
def extract_name(hyperlink):
    match = re.search(r'","(.*?)"\)$', hyperlink)
    if match:
        return match.group(1)
    return hyperlink  # Return the entire string if no match, assuming it might be the name directly

# Read the Excel file
df = pd.read_excel(r'input.xlsx')

# Print column names to verify
print(df.columns)

# Create a new column for LinkedIn profiles
df['LinkedIn Profile'] = None

# Loop through the DataFrame starting from the second row
for index, row in df.iloc[1:].iterrows():  # iloc[1:] skips the header
    name = extract_name(row.iloc[0])  # First column
    company = row.iloc[1]  # Second column
    print(f"Processing: {name} from {company}")
    if name:
        profile = fetch_linkedin_profile(name, company)
        df.at[index, 'LinkedIn Profile'] = profile
        time.sleep(5)  # Fixed pause of 5 seconds between searches
        #I also tried implementing a random pause of a period between 2-5 seconds, but to no avail. You should try maybe 10 seconds

# Write the updated DataFrame to a new Excel file
df.to_excel('output.xlsx', index=False)
