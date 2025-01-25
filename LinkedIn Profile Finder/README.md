# Automating LinkedIn Profile Discovery with Python
![photo](https://github.com/suyash-rgb/Python-Projects/blob/8cc898695c0a2b55cd70ecaa9e5451ed8688c712/LinkedIn%20Profile%20Finder/images/1.png)
### Overview
Discovering LinkedIn profiles manually can be a tedious task, especially when dealing with long candidate lists. This Python script automates the process by leveraging Google search, making it easier and faster to find LinkedIn profiles based on candidate names and their company information.
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
