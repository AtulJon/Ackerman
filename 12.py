a=int(input())
t=a
r=0
while(a>0):
    digit=a%10
    r=r*10+digit
    a=a//10
if(r==t):   
    print("yes")
else:
    print("no")
