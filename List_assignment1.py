#3.Write a program to :-
# 1. Create an empty python list
# 2. Read 10 values from user and add to python list
# 3. Iterate through the list and print alternate values
# Eg.
# 5 12 8 14 9 3 22
# Output:  5 8 9 22
#Ans.  creating an empty list

bucket = []
# to ask the number of items to be stored in list from the user
n= int(input("enter the number of items: "))
#to iterate till the range
for i in range(0,n):
    items= int(input()) #will take the items from the user till the range number
    bucket.append(items) #to add the items to the list
#to print the list
print(bucket)
#for printing alternate elements of list:-
for i in range(0,n,2):
    print(bucket[i])
