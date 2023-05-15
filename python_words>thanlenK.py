S1 =  input('Enter the string : ')#Anjali chandrashekar meenakshi lavanyakumar kalyani
k = int(input('Enter k  (value for accepting string) : '))#9
largerStr = []
words = S1.split(" ")
for word in words:
	if len(word) > k:
		largerStr.append(word)
print("All words which are greater than given length ", k, "are ", largerStr)#All words which are greater than given length  9 are  ['chandrashekar', 'lavanyakumar']
