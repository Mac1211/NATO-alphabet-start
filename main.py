
# import pandas
# import csv
# # student_data_frame = pandas.DataFrame(student_dict)

# # #Loop through rows of a data frame
# # for (index, row) in student_data_frame.iterrows():
# #     #Access index and row
# #     #Access row.student or row.score
# #     pass

# # # Keyword Method with iterrows()
# # # {new_key:new_value for (index, row) in df.iterrows()}

# # #TODO 1. Create a dictionary in this format:
# # {"A": "Alfa", "B": "Bravo"}

# # #TODO 2. Create a list of the phonetic code words from a word that the user inputs.


# reader= pandas.read_csv('nato_phonetic_alphabet.csv')

# dict = {row.letter:row.code for (index, row) in reader.iterrows()}

# word = input('Enter your word: ').upper()


# coded_list = [dict[i] for i in word]
# print(coded_list)

import os
print(os.getcwd())

import os
import pandas as pd

file_name = 'nato_phonetic_alphabet.csv'

if os.path.isfile(file_name):
    df = pd.read_csv(file_name)
    # Your code to work with the DataFrame
else:
    print(f"The file '{file_name}' does not exist in the current directory.")
    
    



