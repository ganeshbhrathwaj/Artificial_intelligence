ae=af=ag=ah=be=bf=bg=bh=ce=cf=cg=ch=de=df=dg=dh=False
ph=[]
val=[]
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
def change():
    global ae,af,ag,ah,be,bf,bg,bh,ce,cf,cg,ch,de,df,dg,dh
    if(ae):
        af=ag=ah=be=ce=de=Not(ae)
        val[ph.index('af')]=0
        val[ph.index('ag')]=0
        val[ph.index('ah')]=0
        val[ph.index('be')]=0
        val[ph.index('ce')]=0
        val[ph.index('de')]=0
    if(be):
        bf=bg=bh=ae=ce=de=Not(be)
        val[ph.index('bf')]=0
        val[ph.index('bg')]=0
        val[ph.index('bh')]=0
        val[ph.index('ae')]=0
        val[ph.index('ce')]=0
        val[ph.index('de')]=0
    if(ce):
        cf=cg=ch=ae=be=de=Not(ce)
        val[ph.index('cf')]=0
        val[ph.index('cg')]=0
        val[ph.index('ch')]=0
        val[ph.index('ae')]=0
        val[ph.index('be')]=0
        val[ph.index('de')]=0
    if(de):
        df=dg=dh=ae=be=ce=Not(de)
        val[ph.index('df')]=0
        val[ph.index('dg')]=0
        val[ph.index('dh')]=0
        val[ph.index('ae')]=0
        val[ph.index('be')]=0
        val[ph.index('ce')]=0
    if(af):
        ae=ag=ah=bf=cf=df=Not(af)
        val[ph.index('ae')]=0
        val[ph.index('ag')]=0
        val[ph.index('ah')]=0
        val[ph.index('bf')]=0
        val[ph.index('cf')]=0
        val[ph.index('df')]=0
        
    if(bf):
        be=bg=bh=af=cf=df=Not(bf)
        val[ph.index('be')]=0
        val[ph.index('bg')]=0
        val[ph.index('bh')]=0
        val[ph.index('af')]=0
        val[ph.index('cf')]=0
        val[ph.index('df')]=0
        
    if(cf):
        ce=cg=ch=af=bf=df=Not(cf)
        val[ph.index('ce')]=0
        val[ph.index('cg')]=0
        val[ph.index('ch')]=0
        val[ph.index('af')]=0
        val[ph.index('bf')]=0
        val[ph.index('df')]=0
    if(df):
        de=dg=dh=af=bf=cf=Not(df)
        val[ph.index('de')]=0
        val[ph.index('dg')]=0
        val[ph.index('dh')]=0
        val[ph.index('af')]=0
        val[ph.index('bf')]=0
        val[ph.index('cf')]=0
    if(ag):
        ae=af=ah=bg=cg=dg=Not(ag)
        val[ph.index('ae')]=0
        val[ph.index('af')]=0
        val[ph.index('ah')]=0
        val[ph.index('bg')]=0
        val[ph.index('cg')]=0
        val[ph.index('dg')]=0
        
        
    if(bg):
         be=bf=bh=ag=cg=dg=Not(bg)
         val[ph.index('be')]=0
         val[ph.index('bf')]=0
         val[ph.index('bh')]=0
         val[ph.index('ag')]=0
         val[ph.index('cg')]=0
         val[ph.index('dg')]=0
    if(cg):
        cf=ce=ch=ag=bg=dg=Not(cg)
        val[ph.index('cf')]=0
        val[ph.index('ce')]=0
        val[ph.index('ch')]=0
        val[ph.index('ag')]=0
        val[ph.index('bg')]=0
        val[ph.index('dg')]=0
    if(dg):
        de=df=dh=ag=bg=cg=Not(dg)
        val[ph.index('de')]=0
        val[ph.index('df')]=0
        val[ph.index('dh')]=0
        val[ph.index('ag')]=0
        val[ph.index('bg')]=0
        val[ph.index('cg')]=0
    if(ah):
        ae=af=ag=bh=ch=dh=Not(ah)
        val[ph.index('ae')]=0
        val[ph.index('af')]=0
        val[ph.index('ag')]=0
        val[ph.index('bh')]=0
        val[ph.index('ch')]=0
        val[ph.index('dh')]=0
    if(bh):
        be=bf=bg=ah=ch=dh=Not(bh)
        val[ph.index('be')]=0
        val[ph.index('bf')]=0
        val[ph.index('bg')]=0
        val[ph.index('ah')]=0
        val[ph.index('ch')]=0
        val[ph.index('dh')]=0
    if(ch):
        cf=ce=cg=ah=bh=dh=Not(ch)
        val[ph.index('cf')]=0
        val[ph.index('ce')]=0
        val[ph.index('cg')]=0
        val[ph.index('ah')]=0
        val[ph.index('bh')]=0
        val[ph.index('dh')]=0
    if(dh):
        de=df=dg=ah=bh=ch=Not(dh)
        val[ph.index('de')]=0
        val[ph.index('df')]=0
        val[ph.index('dg')]=0
        val[ph.index('ah')]=0
        val[ph.index('bh')]=0
        val[ph.index('ch')]=0
       
person=['a','b','c','d']
house=['e','f','g','h']
print("Persons")
print(person)
print("houses")
print(house)
for m in person:
    for n in house:
        ph.append(m+n)
val=[1]*16
print("person_house_possible_combination")
print(ph)

print("person-house")
for i in range(0,2):
    for j in range(0,2):
        for k in range(0,2):
            for l in range(0,2):
                if(i==0):
                    ae=True
                if(i==1):
                    ae=False
                    val[ph.index('ae')]=0
                if(j==0):
                    ag=True
                   
                if(j==1):
                    ag=False
                    val[ph.index('ag')]=0
                if(k==0):
                    ch=True
                if(k==1):
                    ch=False
                    val[ph.index('ch')]=0
                if(l==0):
                    be=True
                if(l==1):
                    be=False
                    val[ph.index('be')]=0
                change()
                kb=And(Or(ae,ag),Not(ch),be)
                
                if(kb):
                    for q in range(0,16):
                        if(val[q]):
                            if(ph[q]=='ae'):
                                ae=True
                            if(ph[q]=='af'):
                                af=True
                            if(ph[q]=='ag'):
                                ag=True
                            if(ph[q]=='ah'):
                                ah=True
                            if(ph[q]=='be'):
                                be=True
                            if(ph[q]=='bf'):
                                bf=True
                            if(ph[q]=='bg'):
                                bg=True
                            if(ph[q]=='bh'):
                                bh=True
                            if(ph[q]=='ce'):
                                ce=True
                            if(ph[q]=='cf'):
                                cf=True
                            if(ph[q]=='cg'):
                                cg=True
                            if(ph[q]=='ch'):
                                ch=True
                            if(ph[q]=='de'):
                                de=True
                            if(ph[q]=='df'):
                                df=True
                            if(ph[q]=='dg'):
                                dg=True
                            if(ph[q]=='dh'):
                                dh=True
                            change()
                            print(ph[q])
                val=[1]*16
                    
