# Q10. Write a program to download google website, through python..(use wget or curl command).
# Ans.

import os
i=input("enter the website:")
cmd= 'curl ' + i + ' >Google_website.html'
print(cmd)
output=os.system(cmd)
print(output)
