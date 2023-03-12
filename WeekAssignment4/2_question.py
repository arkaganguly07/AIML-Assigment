"""
Q2> Use pandas to get the name and ID of the student with the highest percentage of marks.
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

# Calculate the total marks for each subjects
df['Total Marks'] = df['Subject 1'] + df['Subject 2'] + df['Subject 3'] + df['Subject 4'] + df['Subject 5']\
                    + df['Subject 6']

# Calculate the percentage of marks for each student
df['Percentage'] = df['Total Marks'] / 6

# Get the name and ID of the student with the highest percentage of marks
highest_percentage = df.loc[df['Percentage'].idxmax()]

# Printing the name and ID of the student
print("Name: ", highest_percentage['Name'])
print("Student ID: ", highest_percentage['Student ID'])


"""
OUTPUT:
Name:  Mycroft
Student ID:  3
"""

"""
Explanation: This code first calculates the total marks and percentage of marks for each student using the data 
from the previous code. It then uses the `idxmax()` function to get the index of the row with the highest percentage of 
marks, and the `loc[]` function to get the name and ID of the student with that index.
"""