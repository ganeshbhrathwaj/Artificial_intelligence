def inter(l,r):
    if(l== True and r==False):
        return False
    else:
        return True

def And(*argv):
    for i in argv:
        if(i==True):
            f=1
        else:
            f=0
            break
    if(f==1):
        return True
    else:
        return False
def Or(*argv):
    for i in argv:
        if(i==False):
            f=1
        else:
            f=0
            break
    if(f==1):
        return False
    else:
        return True
   
def Not(s):
    if(s==True):
        return False
    return True
rain=False
ganesh=False
print("Rain  Ganesh  kb")
for i in range(0,2):
    for j in range(0,2):
        if(i==0):
            rain=True
        if(i==1):
            rain=False
        if(j==0):
            ganesh=True
        if(j==1):
            ganesh=False
        kb=And(inter(Not(rain),ganesh), Not(ganesh))
        print(rain,ganesh,kb,sep=" ")
