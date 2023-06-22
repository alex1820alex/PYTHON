chislo=input()
def recurs(chislo,lens):
    if lens>=0:
        return int(chislo[lens])+int(recurs(chislo,lens-1))
    else:
        return 0

print(recurs(chislo,len(chislo)-1))