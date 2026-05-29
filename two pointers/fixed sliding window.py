'''def ret(a,k):
    ma=[]
    l=0
    su=0
    while(k<=len(a)):
        for s in range(l,k):
            su+=a[s]
        s=su/4
        ma.append(s)
        l+=1
        k+=1
        su=0
    return ma
aa=ret([1,12,-5,-6,50,3],4)
print(max(aa))

 the above code is o(nxk) becoz of the two loops soo my code will work but it is not efficient but the thinking is crt

def ret(a, k):
    su = sum(a[:k])      
    max_su = su
    for i in range(k, len(a)):
        su += a[i] - a[i-k]   
        if su > max_su:
            max_su = su
    return max_su / k

print(ret([1,12,-5,-6,50,3], 4))  
# the above code is the optimal code for the problem

'''


from collections import Counter
def ret(a,k):
    r=len(k)
    tar=Counter(k)
    for i in range(0,len(a)):
        wt=Counter(a[i:i+r])
        if wt==tar:
            return True    
print(ret("eidbaooo","ab"))


























