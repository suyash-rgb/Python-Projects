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
            return profiles
        else: 
            return f"No LinkedIn profiles found for {name} at {company}."
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Example usage
name = "Sample Name"
company = "ABC Foods Ltd"
result = fetch_linkedin_profile(name, company)

if isinstance(result, list):
    print("LinkedIn profiles found: ")
    for profile in result: 
        print(profile)
else: 
    print(result)
