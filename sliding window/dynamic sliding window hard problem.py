from collections import Counter
def ret(s,t):
    tc=Counter(t)
    wc={}
    l=0
    ml=float('inf')
    res=[-1,-1]
    n=len(tc)
    have=0
    for r in range(len(s)):
        c=s[r]
        wc[c]=wc.get(c,0)+1
        if wc[s[r]]==tc[s[r]]:
            have+=1
        while have==n:
            cl=r-l+1
            if cl<ml:
                ml=cl
                res=[l,r]
            wc[s[l]]-=1
            if s[l] in tc and wc[s[l]]<tc[s[l]]:
                have-=1
            l+=1
    start, end = res
    return s[start : end + 1] if ml != float('inf') else ""
print(ret("ADOBECODEBANC","ABC"))
#the above is not my own and it is tougher than i thought like i did dynamic win without duplicates in easy and i thought
#this would be easy but it is way fucker than i thought :(
