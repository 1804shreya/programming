n=int(input("enter a number"))
count=1
if n>1:
    for i in range (2,n+1):
        if(n%i)==0:
            count+=1
    if count==2:
        print("it is prime",n)


    else:
        print("not a prime")
