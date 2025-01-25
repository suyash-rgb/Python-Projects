# Automating LinkedIn Profile Discovery with Python
![photo](https://github.com/suyash-rgb/Python-Projects/blob/8cc898695c0a2b55cd70ecaa9e5451ed8688c712/LinkedIn%20Profile%20Finder/images/1.png)

## Why We Chose Google Search Over LinkedIn API for Profile Discovery

Initially, we explored using LinkedIn’s official API to programmatically access profile data. This approach required:
1. **Creating a LinkedIn Developer Account**: 
    - Registering an application and obtaining API keys.
2. **OAuth Authentication**: 
    - Setting up secure access to LinkedIn's data with user authorization.
3. **Usage Restrictions**: 
    - Compliance with LinkedIn’s terms of service, limiting access to data only from users who authorize the app.
![process](https://github.com/suyash-rgb/Python-Projects/blob/8cc898695c0a2b55cd70ecaa9e5451ed8688c712/LinkedIn%20Profile%20Finder/images/1.png)

Upon deeper evaluation, we found that this method wouldn’t meet our needs due to restrictions and the necessity of user authorization.

### Why We Chose an Alternative Approach
Given the limitations of LinkedIn’s API, we opted for a solution leveraging Google search. This method allowed us to:
- **Perform Automated Searches**: Using Google to search for LinkedIn profiles based on candidate names and company information.
- **Avoid Authorization Hurdles**: No need for explicit user authorization for accessing public profile data.
- **Maintain Efficiency**: Implement rate limiting to handle large datasets without interruptions.

### Overview
Discovering LinkedIn profiles manually can be a tedious task, especially when dealing with long candidate lists. This Python script automates the process by leveraging Google search, making it easier and faster to find LinkedIn profiles based on candidate names and their company information. <br> <br>
![Demo](https://github.com/suyash-rgb/Python-Projects/blob/1f1e173b908d0d7a4a49cb1b424228b1c44b7fc7/LinkedIn%20Profile%20Finder/gif/google%20search.gif)

### Features
- **Automated Searches**: Input candidate names and company information, and the script will find the most relevant LinkedIn profiles.
- **Rate Limiting Compliance**: Incorporates pauses to comply with Google’s search rate limits, ensuring uninterrupted execution.
- **Efficient Data Handling**: Uses `pandas` for easy manipulation and storage of data in Excel sheets.
- **Time-Saving**: Automates a time-consuming task, allowing users to focus on more strategic activities.

### Getting Started

#### Prerequisites
- Python 3.x
- `pandas` library
- `googlesearch` library

You can install the necessary libraries using pip:

```bash
pip install pandas googlesearch-python
```

#### Installation

1. Clone the repository:
    ```bash
    git clone [Repository Link]
    cd linkedin-profile-discovery
    ```

2. Set up your Excel file with candidate names and company information.

#### Usage

1. Update the script with the path to your Excel file.

2. Run the script:
    ```bash
    python linkedin_profile_discovery.py
    ```

3. The script will search for LinkedIn profiles and save the results in a new Excel file.

### How It Works
- **Input**: Provide an Excel file with columns for candidate names and company names.
- **Search**: The script uses Google to search for LinkedIn profiles based on the input data.
- **Output**: Results are saved in a new Excel file with links to the discovered LinkedIn profiles.

### Limitations
- The script is subject to Google’s search rate limits and may require pauses to avoid errors.
- It relies on the accuracy of Google search results, which may vary.

### Recommendations
- For large-scale professional use, consider tools like LinkedIn Sales Navigator or LinkedIn Recruiter, which comply with LinkedIn’s Terms of Service.
![Sales Navigator](https://github.com/suyash-rgb/Python-Projects/blob/89cd073b2a0e5ef79a4b7c37c49a5a01be4877fe/LinkedIn%20Profile%20Finder/images/nav.webp)
![LinekdIn Recruiter](https://github.com/suyash-rgb/Python-Projects/blob/89cd073b2a0e5ef79a4b7c37c49a5a01be4877fe/LinkedIn%20Profile%20Finder/images/recruiter.jpg)

### Contributing
Feel free to fork this repository, make improvements, and submit pull requests. Your contributions are welcome!

### License
This project is licensed under the MIT License.

### Acknowledgments
Special thanks to my friend for inspiring this project and to all the developers contributing to open-source libraries.
