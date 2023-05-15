print("The original dictionary is : " + str(D1))#{'Anjali': [1, 2, 3, 4], 'and': [4, 5, 6, 7, 8], 'vivek': [7, 8, 9, 10], 'best': [10, 11], 'friend': [2, 9, 10, 33]}

res = list(sorted({X for val in D1.values() for X in val}))

print("The unique values list is : " + str(res))#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 33]
