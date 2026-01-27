'''
Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
#my code but one small error thooo
def check(s,t):
    l=0
    r=0
    tar=0
    for i in range(0,len(t)):
        if s[i]==t[i]:
            l+=1
            r+=1
            tar=0
        else:
            r+=1
    return tar
s = "abc"
t = "ahbgdc"
a=check(s,t)
if a==len(s):
    print(True)
else:
    print(False)
 '''
#by cahtgpt after finding my error
def check(s, t):
    i = 0  # pointer for s
    j = 0  # pointer for t

    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1

    return i == len(s)
s = "ace"
t = "abcde"
a=check(s,t)
print(a)
