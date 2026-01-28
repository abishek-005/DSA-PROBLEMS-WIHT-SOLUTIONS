def maxi(lst,k):
    l=0
    r=len(lst)-1
    maxm=[]
    while l<r:
        if lst[l]+lst[r]==k:
            r-=1
            maxm.append(l)
        elif lst[l]+lst[r]<k:
            l+=1
        else:
            r-=1
    return len(maxm)
nums = [1,2,3,4]
k = 5
a=maxi(nums,k)
print(a)
