import os
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
import numpy as np
import time
import sys
import time
import pickle

data_folders = [
    "Data_For_Ben/June_2019"
]

output_files = [
    "plains/test.plain"
]

# f = open("plains/April_2019.plain","w")

directory = data_folders[0]
print(directory)

f = open(output_files[0],"w")

for filename in os.listdir(directory):
    data_str = os.path.join(directory, filename)
    if os.path.isfile(data_str):
        print(data_str)

        data = pd.read_csv(data_str)

        for index, row in data.iterrows():
            f.write("fen ")
            f.write(row["fen"])
            f.write("\n")
            f.write("move ")
            f.write(row["move"])
            f.write("\n")
            f.write("score ")
            f.write(str(row["voc"]*1000))
            f.write("\n")
            f.write("ply ")
            f.write(str(row["ply"]))
            f.write("\n")
            f.write("result ")
            f.write(str(row["rt"]))
            f.write("\n")
            f.write("e\n")