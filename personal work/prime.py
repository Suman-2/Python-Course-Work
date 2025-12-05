def is_prime(n):
    if n==1:
        print("neither prime or not")
    if n==2:
        print("prime")
    for i in range(3,n,1):
        if n%i==0:
            print("no prime")
    return True
print(is_prime(10))
