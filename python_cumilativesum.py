# cumulative sum=list elemengts add to one their previous elements and form a new list.
lst=list(input("enter the values comma saperated:").split(","))#10,20,30,40,50
sum=0

result=[]
for num in lst:
    sum=sum+int(num)
    result.append(sum)
print(result)#[10, 30, 60, 100, 150]
