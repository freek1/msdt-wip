import csv

files = ['kaggle', 'lowlands', 'plos_one']
try:
    for fn in files:
        csv_file = fn+'.csv'
        txt_file = fn+'.txt'
        with open(txt_file, "w") as my_output_file:
            with open(csv_file, "r") as my_input_file:
                [ my_output_file.write(" ".join(row)+'\n') for row in csv.reader(my_input_file)]
            my_output_file.close()
except:
    print("Error opening files")
    