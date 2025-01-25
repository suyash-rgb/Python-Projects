# Automating LinkedIn Profile Discovery with Python

### Overview
Discovering LinkedIn profiles manually can be a tedious task, especially when dealing with long candidate lists. This Python script automates the process by leveraging Google search, making it easier and faster to find LinkedIn profiles based on candidate names and their company information.

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
