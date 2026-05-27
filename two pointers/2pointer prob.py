def rem(s1,s2):
    r1=len(s1)-1
    r2=len(s2)-1
    a=[]
    l=0
    while l < len(s2) and s1[l]==s2[l]:
        l+=1
    while r2>=0 and s1[r1]==s2[r2]:
        r1-=1
        r2-=1
    if l >= r1:
        for i in range(r1, l + 1):
            a.append(i)
    else:
        return [-1]
        
    return a
a=rem("abcc","abc")
print(a)

'''
def rem(s1, s2):
    l = 0
    while l < len(s2) and s1[l] == s2[l]:
        l += 1
    r1 = len(s1) - 1
    r2 = len(s2) - 1
    while r2 >= 0 and s1[r1] == s2[r2]:
        r1 -= 1
        r2 -= 1
'''
