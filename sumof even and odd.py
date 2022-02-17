n=int(input("enter n"))
evensum=0 
oddsum=0
for i in range (1,n+1):
    if i%2==0:
        evensum=i+evensum
        i=i+2
    else :
        oddsum=i+oddsum
        i=i+2
print("evennumbers sum=",evensum)
print("oddnumbers sum=",oddsum)
