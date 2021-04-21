def eval(b):
    r=0
    c=0
    for i in range(3):
        if(b[r][i]==b[r+1][i] and b[r][i]==b[r+2][i] and b[r][i]=='x'):
            return 1
        if(b[r][i]==b[r+1][i] and b[r][i]==b[r+2][i] and b[r][i]=='o'):
            return -1
           
           
    for j in range(3):
        if(b[j][c]==b[j][c+1] and b[j][c]==b[j][c+2] and b[j][c]=='x'):
            return 1
        if(b[j][c]==b[j][c+1] and b[j][c]==b[j][c+2] and b[j][c]=='o'):
            return -1
   
    if(b[0][0]==b[1][1] and b[0][0]==b[2][2] and b[0][0]=='x'):
        return 1
               
    if(b[0][0]==b[1][1] and b[0][0]==b[2][2] and b[0][0]=='o'):
        return -1
   
    if(b[0][2]==b[1][1] and b[0][2]==b[2][0] and b[0][0]=='x'):
        return 1
   
    if(b[0][2]==b[1][1] and b[0][2]==b[2][0] and b[0][0]=='o'):
        return -1
   
    return 0  
   
def left(b):
    for i in range(3):
        for j in range(3):
            if(b[i][j]=='_'):
                return True
    return False
def minimax(b,w):
    s=eval(b)
   
    if(s==1 or s==-1):
       
        return s
    if(left(b)==False):
        return 0
    if(w):
        best=-1000
        for i in range(3):
            for j in range(3):
                if(b[i][j]=='_'):
                    b[i][j]='x'
                   
                    best=max(best,minimax(b,not w))
                    b[i][j]='_'
                   
        return best
    else:
        best=1000
        for i in range(3):
            for j in range(3):
                if(b[i][j]=='_'):
                    b[i][j]='o'
                   
                    best=min(best,minimax(b,not w))
                    b[i][j]='_'
        return best
                       
               
               
def best_val(b):
    bestval=-1000
    for i in range(3):
        for j in range(3):
            if(b[i][j]=='_'):
                b[i][j]='x'
                h=minimax(b,False)
                b[i][j]='_'
                if(h<bestval):
                    bestval=h
                    best_pos=(i,j)
    return best_pos


b = [
    [ 'x', 'o', 'x' ],
    [ '_', 'o', 'x' ],
    [ '_', '_', 'o' ]
]
print("next best position is....")
print(best_val(b))
