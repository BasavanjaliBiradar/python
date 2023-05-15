# Python program to get all combinations of 2 tuples
test_tuple1 = (7,2)
test_tuple2 = (7, 8)
  
# generating all pair combinations of 2 tuples using list comprehension
res = [(a, b) for a in test_tuple1 for b in test_tuple2] + [(a, b) for a in test_tuple2 for b in test_tuple1]
print("output : " + str(res))#[(7, 7), (7, 8), (2, 7), (2, 8), (7, 7), (7, 2), (8, 7), (8, 2)]
