#my own code without gemini
def ret(a):
    k={}
    l=0
    mk=0
    for r in range(0,len(a)):
        if a[r] not in k:
            k[a[r]]=r

        elif a[r] in k:
            del k[a[r]]
            k[a[r]]=r
    return k

print(ret("tmmzuxt"))

''' my own code with help of gemini
def ret(a):
    k={}
    l=0
    mk=0
    for r in range(0,len(a)):
        if a[r] not in k:
            k[a[r]]=r
        elif a[r] in k:
            oi=k[a[r]]
            if k[a[r]]>=l:
                l=oi+1
                k[a[r]]=r
        mk=max(mk,r-l+1)
    return mk,k,l
print(ret("tmmzuxt"))

'''
'''
def ret(a):
    k = {}
    l = 0
    mk = 0
    
    for r in range(0, len(a)):
        # 1. Duplicate character current window kulla irundha, left pointer-ah jump panna vaikrom
        if a[r] in k and k[a[r]]     >= l:
            l = k[a[r]] + 1
            
        # 2. Character puthusa irundhalumசரி, pazhasa irundhalumசரி... fresh index-ah update panrom
        k[a[r]] = r
        
        # 3. Every single time max length tracking scaling pool
        mk = max(mk, r - l + 1)
        
    return mk,k,l

# Testing the code
print(ret("tmmzuxt"))  # Output: 3

'''

