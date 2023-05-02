# 4. Repeat previous question, but this time print only prime numbers.
# Ans. # creating an empty list

bucket = []
# # to ask the number of items to be stored in list from the user
n= int(input("enter the number of items: "))
#to iterate till the range
for i in range(0,n):
    items= int(input()) #will take the items from the user till the range number
    bucket.append(items) #to add the items to the list
#to print the list
print(bucket)

#to print the prime numbers in the list
for num in bucket:
    if num==0 or num==1: # 0 and 1 are not prime numbers
        continue
    for i  in range(2,num):
        if num%i==0:
            break
        else:
         print(num)


# Isme kuchh issue h is code m dekhne padega