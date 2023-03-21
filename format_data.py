# import pandas as pd
# import numpy as np
# import os

# directory = "Data_For_Ben"

# f = open("data.plain","w")

# for filename in os.listdir(directory):
#     sub_dir = os.path.join(directory, filename)
#     # checking if it is a file
#     if os.path.isfile(sub_dir):
#         print(sub_dir)
    
#     if os.path.isdir(sub_dir):
#         for filename in os.listdir(sub_dir):
#             data_str = os.path.join(sub_dir, filename)
#             if os.path.isfile(data_str):
#                 print(data_str)

#                 data = pd.read_csv(data_str)

#                 for index, row in data.iterrows():
#                     f.write("fen ")
#                     f.write(row["fen"])
#                     f.write("\n")
#                     f.write("move ")
#                     f.write(row["move"])
#                     f.write("\n")
#                     f.write("score ")
#                     f.write(str(row["voc"]))
#                     f.write("\n")
#                     f.write("ply ")
#                     f.write(str(row["ply"]))
#                     f.write("\n")
#                     f.write("result ")
#                     f.write(str(row["result"]))
#                     f.write("\n")
#                     f.write("e\n")

import os
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
import numpy as np
import time
import sys
import time
import pickle

job_idx = int(os.environ["SLURM_ARRAY_TASK_ID"]) - 1

data_folders = [
    "Data_For_Ben/April_2019",
    "Data_For_Ben/February_2019",
    "Data_For_Ben/Jan_2019_300",
    "Data_For_Ben/Jan_2019_600",
    "Data_For_Ben/June_2019",
    "Data_For_Ben/May_2019",
    "Data_For_Ben/August_2019",
    "Data_For_Ben/Jan_2019_180",
    "Data_For_Ben/Jan_2019_60",
    "Data_For_Ben/July_2019",
    "Data_For_Ben/March_2019"
]

output_files = [
    "plains/April_2019.plain",
    "plains/February_2019.plain",
    "plains/Jan_2019_300.plain",
    "plains/Jan_2019_600.plain",
    "plains/June_2019.plain",
    "plains/May_2019.plain",
    "plains/August_2019.plain",
    "plains/Jan_2019_180.plain",
    "plains/Jan_2019_60.plain",
    "plains/July_2019.plain",
    "plains/March_2019.plain"
]

# f = open("plains/April_2019.plain","w")

directory = data_folders[job_idx]
print(directory)

f = open(output_files[job_idx],"w")

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
            f.write(str(row["voc"]))
            f.write("\n")
            f.write("ply ")
            f.write(str(row["ply"]))
            f.write("\n")
            f.write("result ")
            f.write(str(row["result"]))
            f.write("\n")
            f.write("e\n")