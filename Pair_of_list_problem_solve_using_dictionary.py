# 7.Make the same problem simper. Read about pairs and reimplement it as a list of pairs.
#Note- This is a very good problem for learning purpose.
# Ans.

pairs = {}
for i in range(10):
    string, number = input("Enter pair (string number): ").split()
    pairs[string] = int(number)
search_string = input("Enter string to search for: ")
if search_string in pairs:
    print("Number is", pairs[search_string])
else:
    print("String not found in pairs")