def binpow(a,b):
    res=1
    while(b>0):
        if(b&1):
            res=res*a
        a=a*a
        b >>=1
    return res


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print(binpow(num1,num2))
