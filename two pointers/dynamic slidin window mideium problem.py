'''from collections import Counter
def ret(s,k):
    l=0
    t={}
    ms=0
    for r in range(len(s)):
        t[s[r]] = t.get(s[r], 0) + 1
        print(max(t.values()))
        if r-l+1 - max(t.values())>k:
            t[s[l]]-=1
            l+=1
        ms=max(ms,r-l+1)
        
    return ms
                   
print(ret("AABABBA",1))
'''


'''def ret(n,t):
    l=0
    s=0
    ms=float('inf')
    for r in range(len(n)):
        s=s+n[r]
        while s>=t:
            ms=min(ms,r-l+1)
            s-=n[l]
            l+=1
    return ms if ms != float('inf') else 0
print(ret([2,3,1,2,4,3],7))
#the above code is my own code but i got 1 help from gemini to add while s>=t but other than
#that this is my logic
'''

from collections import Counter

def ret(s, p):
    pc = Counter(p)       
    sc = Counter()
    k = []
    for r in range(len(s)):
        sc[s[r]] += 1        
        if r >= len(p):
            left_char = s[r - len(p)]
            sc[left_char] -= 1
            if sc[left_char] == 0:
                del sc[left_char]      
        if sc == pc:
            k.append(r - len(p) + 1)
            
    return k

print(ret("cbaebabacd", "abc"))






























