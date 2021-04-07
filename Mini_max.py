n=15
g=[[]for i in range(n)]
q=[]
v=[0]*n
score=[[]for i in range(n)]
leaf=[]
#print(v)
ma=[]
mi=[]
w=[]
main_s=[]

def add_edge(u,v,c):
    g[u].append((v,c))


def find_score(st,en):
    q.append(st)
    while(q[0]!=en):
        for i in g[q[0]]:
            q.append(i[0])
            if(i[1]!=0):
                score[q[0]].append(i[1])
                main_s.append(i[1])
                
        q.pop(0)
    for i in score:
        if(len(i)!=0):
            leaf.append(score.index(i))
    
    print("Before performing mini_max algorithm:")
    print(main_s)

def mini_max():
    f=1
    r=0
    while(len(ma)!=1):
        if(f==1):
            for i in score:
                if(len(i)!=0):
                    if(len(i)==1):
                        w.append(i[0])
                        r=1
                    else:    
                        ma.append(max(i))
                        i.clear()
            if(r==1):
                #print(max(w))
                ma.append(max(w))
            
            for j in g:
                if(len(j)!=0):
                    for h in leaf:
                        if(h==j[0][0]):
                            leaf[leaf.index(h)]=g.index(j)
                        if(h==j[1][0]):
                            leaf[leaf.index(h)]=g.index(j)
        
            print("Max turn")
            print(ma)
            f=0 
            #if(len(ma)==1):
                #break
        else:
            for q in range(len(ma)-1):
                for y in range(q+1,len(ma)):
                    if(leaf[q]==leaf[y]):
                        score[leaf[q]].append(min(ma[q],ma[y]))
                        mi.append(min(ma[q],ma[y]))
                        
            ma.clear()
            print("Min turn")
            print(mi)
            mi.clear()
            f=1
        
    
    
add_edge(1,2,0)
add_edge(1,3,0)
add_edge(2,4,0)
add_edge(2,5,0)
add_edge(3,6,0)
add_edge(3,7,0)
add_edge(4,8,-1)
add_edge(4,9,4)
add_edge(5,10,2)
add_edge(5,11,6)
add_edge(6,12,-3)
add_edge(6,13,-5)
add_edge(7,14,-7)
add_edge(7,15,7)

find_score(1,8)
mini_max()
