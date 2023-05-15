# Python program to create a list of tuples from given list having number and its cube in each tuple.

# Input: list = [9, 5, 6]
# Output: [(9, 729), (5, 125), (6, 216)]
list=[9,5,6]
output=[(val,pow(val,3)) for val in list]
print("output:",output)
