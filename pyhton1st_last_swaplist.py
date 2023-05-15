#SWAP LAST AND FIRST ELEMENTS OF THE LIST
n=list(input("enter numbers comma saperated:").split(','))#[1,2,3,4,5]
t=n[0]
n[0]=n[len(n)-1]
n[len(n)-1]=t
print(n)#[5,2,3,4,1]
