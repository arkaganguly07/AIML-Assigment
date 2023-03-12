"""
Q4> Save the dataFrame as a csv file called marksheet.csv.
"""

import pandas as pd


# Creating a dictionary with student data
studentData = {
    'Student ID': [1, 2, 3, 4, 5],
    'Name': ['Sherlock', 'John', 'Mycroft', 'Hudson', 'James'],
    'Subject 1': [98, 80, 99, 60, 99],
    'Subject 2': [97, 75, 98, 55, 96],
    'Subject 3': [96, 70, 98, 50, 98],
    'Subject 4': [96, 65, 98, 45, 99],
    'Subject 5': [95, 60, 97, 40, 99],
    'Subject 6': [99, 55, 100, 35, 99]
}

# Creating a pandas DataFrame from the dictionary
df = pd.DataFrame(studentData)

# Saving the DataFrame as a CSV file
df.to_csv('marksheet.csv', index=False)


"""
OUTPUT:
Saved as .csv file.
"""

"""
Explanation:
✔ A Comma Separated Values (CSV) file is a plain text file that stores data by delimiting (setting 
boundaries) data entries with commas. CSV files are often used when data needs to be compatible with many different 
programs. CSVs can be opened in text editors, spreadsheet programs like Excel, or other specialized applications. 
It's a way to exchange structured information, similar to a spreadsheet, between programs that wouldn't normally be 
able to talk to each other2.

✔ We use the `to_csv()` method to save the dataframe as a CSV file called marksheet.csv. The `index=False` parameter is 
used to exclude the row index from the CSV file.
"""