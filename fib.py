n=int(input("enter  n value "))
a=0
b=1
c=1
count=0
if n<0:
print("not possible")
elif n==1:
print(a)
else:
while count<n:
print(a,end=" ")
c=a+b
a=b
b=c
count=count+1
