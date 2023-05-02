# 6.Ask user to enter a pair of string and number. Say 10 pairs.  Then used will in one of the strings. You have to find the number corresponding to it.
# Eg.
# Enter pairs
# Abc 1
# Cwf 23
# Jus 6
# HS 9
# Enter string :
# Jus
# Output : number is 6
# Ans.

l1=[]
l2=[]
for i in range(5):
    a=input("enter the string:")
    l1.append(a)
    b=int(input("enter the number:"))
    l2.append(b)
print(l1)
print(l2)
p=input("enter the string:")
output=l2[l1.index(p)]
print("the number corresponding to the string is:",output)

# Note:- This problem needs to make some more Correction(i.e., what will happen in the case when one string is entered