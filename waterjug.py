from collections import deque

def waterjug(m,n,d):
    queue=deque()
    queue.append((0,0,[]))
    visited=set()
    visited.add((0,0))
    while queue:
        a,b,path=queue.popleft()
        if a==d or b==d:
            path.append((a,b))
            return path       
        states=[(m,b,path+[(m,b)]),
                (a,n,path+[(a,n)]),
                (0,b,path+[(0,b)]),
                (a,0,path+[(a,0)]),
                (min(a+b,m), b-(min(a+b,m)-a),path+[(min(a+b,m),b-(min(a+b,m)-a))]),
                (a-(min(a+b,n)-b),min(a+b,n),path+[(a-(min(a+b,n)-b),min(a+b,n))])            
                ]       
        for st in states:
            st_ab=(st[0],st[1])
            if st_ab not in visited:
                visited.add(st_ab)
                queue.append(st)
    return None

m=int(input("Enter the capacity of 1st Jug : "))
n=int(input("Enter the capacity of 2nd Jug : "))
d=int(input("Enter the Desired Amount : "))
print("\n")

steps=waterjug(m,n,d)
if steps:
    print(f"possible to measure exactly {d} litres in one of the jug, Steps are : ")
    for i, step in enumerate(steps):
        print(f"step {i+1},: jug 1= {step[0]} litres, Jug 2= {step[1]} litres")
else:
    print(f"Not possible to measure exactly {d} litres in one of the jug")
