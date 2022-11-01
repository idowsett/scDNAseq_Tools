
# Writing this short script to compile all LOH results into a single txt file for easy import into table format
import glob, os
samples = []

os.chdir("G:\My Drive\LOH and HR\LOH wildtype")

for file in glob.glob("*LOH.txt"):
    with open(file, 'r') as f:
        print(f"writing file: {file.split('.')[0]}")
        lines=[i for i in f]
        if len(lines) > 0:
            writing_list = []
            lines = [i.split('\t') for i in lines]
            print(lines)
            with open('LOHresults_compiled.txt', 'a+') as w:
                for i in lines:
                    file_name = file.split('.')[0]
                    last_seg = i[8].split('\n')[0]
                    w.write(f"{file_name}   \t  {i[0]}  \t  {i[1]}  \t  {i[2]}  \t  {i[3]}\t{i[4]}\t{i[5]}\t{i[6]}\t{i[7]}\t    {last_seg}   \n")


for file in glob.glob("*LOH_fy.txt"):
    with open(file, 'r') as f:
        print(f"writing file: {file.split('.')[0]}")
        lines=[i for i in f]
        if len(lines) > 0:
            writing_list = []
            lines = [i.split('\t') for i in lines]
            print(lines)
            with open('LOHresults_compiled.txt', 'a+') as w:
                for i in lines:
                    file_name = file.split('.')[0]
                    last_seg = i[8].split('\n')[0]
                    w.write(f"{file_name}   \t  {i[0]}  \t  {i[1]}  \t  {i[2]}  \t  {i[3]}\t{i[4]}\t{i[5]}\t{i[6]}\t{i[7]}\t    {last_seg}   \n")
