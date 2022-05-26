import csv
import pandas as pd

files = ['kaggle', 'lowlands', 'plos_one']
try:
    for fn in files:
        df = pd.read_csv(fn+'.csv')
        df.to_csv(fn+'.csv', index=False) 

        csv_file = fn+'.csv'
        txt_file = fn+'.txt'
        with open(txt_file, "w") as my_output_file:
            with open(csv_file, "r") as my_input_file:
                [ my_output_file.write("|"+" | ".join(row)+' |\n') for row in csv.reader(my_input_file)]
            my_output_file.close()

        with open(fn+'.txt', 'r') as f:
            contents = f.readlines()
        contents.insert(1, '|---|---|---|---|---|\n')
        with open(fn+'.txt', 'w') as f:
            contents = "".join(contents)
            f.write(contents)
except:
    print("Error opening files")
    