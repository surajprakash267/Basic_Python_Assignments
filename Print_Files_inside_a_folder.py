# 8. Write a program to take input as a folder name, then print out all the file names in that folder.
# Ans.

import os
Direc= input(r"enter the path of the folder: ")
print(f"files in the direct : {Direc}:-")
files= os.listdir(Direc)
print(*files, sep="\n")
