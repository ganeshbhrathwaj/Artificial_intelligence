q=[]
ct=[]
n=17
max=0
graph = [[] for i in range(n)]
v=[0]*n
def addedge(s,e,c):
    graph[s].append((e,c))
    
    
def gfs(st,tar,n):
    q.append(st)
    ct.append(0)
    while(q[0]!=tar):
        v[q[0]]=1
        for i in graph[q[0]]:
            #print(i[1])
            q.append(i[0])
            ct.append(i[1])
        print(q[0])
        q.pop(0)
        ct.pop(0)
        for j in range(len(ct)-1):
            for h in range(j+1,len(ct)):
                if (ct[j]>ct[h]):
                    t=ct[j]
                    t1=q[j]
                    ct[j]=ct[h]
                    q[j]=q[h]
                    ct[h]=t
                    q[h]=t1
            
        
        
    
addedge(0, 1, 3)
addedge(0, 2, 6)
addedge(0, 3, 5)
addedge(1, 4, 9)
addedge(1, 5, 8)
addedge(2, 6, 12)
addedge(2, 7, 14)
addedge(3, 8, 7)
addedge(8, 9, 5)
addedge(8, 10, 6)
addedge(9, 11, 1)
addedge(9, 12, 10)
addedge(9, 13, 2)
st=0
tar=9
gfs(st,tar,n)

