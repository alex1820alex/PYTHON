x=int(input())
y=int(input())
def recurs(x,y):
    if y>0:
        return x*recurs(x,y-1)
    else:
        return 1
print(recurs(x,y))