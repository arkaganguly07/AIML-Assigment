"""
Q1> Use pandas to create a student mark-sheet with Student ID, Name, and marks obtained in 6 subjects.
"""

import pandas as pd


# Creating a dictionary with student data
student_data = {
    'Student ID': [1, 2, 3, 4, 5],
    'Name': ['Sherlock', 'John', 'Mycroft', 'Hudson', 'James'],
    'Subject 1': [98, 80, 99, 60, 99],
    'Subject 2': [97, 75, 98, 55, 96],
    'Subject 3': [96, 70, 98, 50, 98],
    'Subject 4': [96, 65, 98, 45, 99],
    'Subject 5': [95, 60, 97, 40, 99],
    'Subject 6': [99, 55, 100, 35, 99]
}

# Creating a pandas DataFrame from the dictionary and then printing it
df = pd.DataFrame(student_data)
print(df)

"""
OUTPUT:

   Student ID      Name  Subject 1  ...  Subject 4  Subject 5  Subject 6
0           1  Sherlock         98  ...         96         95         99
1           2      John         80  ...         65         60         55
2           3   Mycroft         99  ...         98         97        100
3           4    Hudson         60  ...         45         40         35
4           5     James         99  ...         99         99         99
"""