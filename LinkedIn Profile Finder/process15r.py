import pandas as pd
from googlesearch import search
import time
import os

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

# Ask user to specify the starting row number
row_number = int(input("Enter the starting row number to process (starting from 1): "))

# Read the Excel file (assumed to be in the same folder as the script)
excel_file = 'jan1.xlsx'  # Update the file name as needed

# Read the Excel file
df = pd.read_excel(excel_file, header=None)  # No headers, hence header=None

# Create a DataFrame to store new results
new_results_df = pd.DataFrame(columns=['Name', 'Company', 'LinkedIn Profile'])

# Process five rows starting from the specified row number
for i in range(row_number - 1, row_number + 14):  # Adjusting for 0-based index and processing next five rows
    if i < len(df):  # Ensure not to exceed the DataFrame length
        row = df.iloc[i]

        # Extract company and name from the specified row
        company = str(row[0]).strip()  # Convert to string and remove any leading or trailing whitespace from the first column (company)
        name = str(row[1]).strip()  # Convert to string and remove any leading or trailing whitespace from the second column (candidate name)
        print(f"Processing: {name} from {company}")

        # Fetch and print the LinkedIn profile
        if name:
            profile = fetch_linkedin_profile(name, company)
            print(profile)  # Display the result in the console
            # Append the result to the new results DataFrame
            new_results_df = pd.concat([new_results_df, pd.DataFrame({'Name': [name], 'Company': [company], 'LinkedIn Profile': [profile]})], ignore_index=True)
            time.sleep(1)  # Pause for 1 second between searches
    else:
        print(f"Row {i + 1} is out of range.")

# Define the results file path
results_excel_file = 'output.xlsx'

# Check if the results file already exists
if os.path.exists(results_excel_file):
    # Read the existing results file
    existing_results_df = pd.read_excel(results_excel_file)
    # Append the new results to the existing DataFrame
    combined_results_df = pd.concat([existing_results_df, new_results_df], ignore_index=True)
else:
    # If the file does not exist, the new results are the combined results
    combined_results_df = new_results_df

# Save the combined results to the Excel file
combined_results_df.to_excel(results_excel_file, index=False)

print(f"Results saved to {results_excel_file}")
