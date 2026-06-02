'''def ret(s):
    t={}
    ml=0
    l=0
    for r in range(len(s)):
        if s[r] in t and t[s[r]]>=l:
            l=t[s[r]]+1
        t[s[r]]=r
        ml=max(ml,r-l+1)
    return t,l,ml
    
print(ret("tmmzuxt"))
'''



def ret(s,k):
    t=s[0]
    l=0
    for r in range(len(s)):
        
    return t

print(ret("ABAB",2))

