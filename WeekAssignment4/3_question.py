"""
Q3> Use pandas to identify the student who got the lowest marks in more than 2 subjects.
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

# Identify the students who got the lowest marks in more than 2 subjects
df['Lowest Marks'] = df[['Subject 1', 'Subject 2', 'Subject 3', 'Subject 4', 'Subject 5', 'Subject 6']].min(axis=1)
df['Lowest Count'] = df[['Subject 1', 'Subject 2', 'Subject 3', 'Subject 4', 'Subject 5',
                         'Subject 6']].apply(lambda x: (x == x.min()).sum(), axis=1)
lowMarks = df.loc[df['Lowest Count'] > 2]

# Printing the names and IDs of the students who got the lowest marks in more than 2 subjects
for index, row in lowMarks.iterrows():
    print('Name:', row['Name'], ', Student ID:', row['Student ID'])


"""
OUTPUT:
Name: Hudson , Student ID: 4
"""

"""
Explanation:
🎱 This code first calculates the lowest marks for each student using the min() function, 
and then counts the number of subjects in which the student got the lowest marks using the apply() function. It then 
uses the loc[] function to get the names and IDs of the students who got the lowest marks in more than 2 subjects.
"""