def assoc(a,b,c):
    left=a+(b+c)
    right=(a+b)+c
    if(left==right):
        print("a+(b+c)=(a+b)+c")
        print("Associative Law proved for addition")
    else:
        print("Associative Law Not proved for addition")
    print("\n")
    l=a*(b*c)
    r=(a*b)*c
    if(l==r):
        print("a*(b*c)=(a*b)*c")
        print("Associative Law proved for multiplication")
    else:
        print("Associative Law Not proved for multiplication")

a=int(input("Enter a : "))
b=int(input("Enter b : "))
c=int(input("Enter c : "))
assoc(a,b,c)

"""
def distri(a,b,c):
    left= a*(b + c)
    right= (a*b)+(a*c)
    if(left==right):
        print("a(b+c)=ab+ac")
        print("Distributive law proved(for Addition)")
    else:
        print("Distributive law Not proved")

    print("\n")
    
    le= a*(b-c)
    ri= (a*b)-(a*c)
    if(le==ri):
        print("a(b-c)=ab-ac")
        print("Distributive law proved(for Subtraction)")
    else:
        print("Distributive law Not proved")
a=int(input("Enter a : "))
b=int(input("Enter b : "))
c=int(input("Enter c : "))
distri(a,b,c)
"""
