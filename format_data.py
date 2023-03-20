import pandas as pd
import numpy as np
import os

directory = "temp"

f = open("data.plain","w")

for filename in os.listdir(directory):
    sub_dir = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(sub_dir):
        print(sub_dir)
    
    if os.path.isdir(sub_dir):
        for filename in os.listdir(sub_dir):
            data_str = os.path.join(sub_dir, filename)
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
                    f.write(str(row["voc"]))
                    f.write("\n")
                    f.write("ply ")
                    f.write(str(row["ply"]))
                    f.write("\n")
                    f.write("result ")
                    f.write(str(row["result"]))
                    f.write("\n")
                    f.write("e\n")