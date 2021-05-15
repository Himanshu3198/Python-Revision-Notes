# Good Bye 2014 A. New Year Transportation
n,t=list(map(int,input().split()))

arr=[]
arr = list(map(int,input().strip().split()))[:n]
t=t-1

c=0
while c<t:
    c=c+arr[c]

if t==c:
    print("YES")
else :
    print("NO")    
   
   















 