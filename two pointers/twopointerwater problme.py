'''def maxw(a):
    l=0
    r=len(a)-1
    ar=[]
    while(l<r):
        ar.append((r-l)*(min(a[l],a[r])))
        if a[l]<a[r]:
            l+=1
        else:
            r-=1
    return ar
aa=[1,8,6,2,5,4,8,3,7]
#FROMULA=(right-left)*min(l[a],r[a])
mw=maxw(aa)
print(mw)
print(max(mw))
'''
'''
def mergear(nums1,nums2,n):
    l=len(nums1)-1
    r=0
    while(n!=0):
        if nums1[l]==0 and nums2[r]!=0:
            t=nums2[r]
            nums1[l]=t
            l-=1
            r+=1
            n-=1
        else:
            l-=1
    return(nums1)
aa=[0,0,0,1]
bb=[2,5,6]
w=mergear(aa,bb,3)
ww=sorted(w)
print(ww)'''

'''
def rw(a):
    l = 0
    r = len(a) - 1
    lm = 0 # Left maximum height
    rm = 0 # Right maximum height
    total_water = 0 # To store the sum of water
    while(l < r):
        if a[l] < a[r]:
            if a[l] >= lm:
                lm = a[l] # Update left max height
            else:
                total_water += lm - a[l] # Add trapped water
            l += 1
        else:
            if a[r] >= rm:
                rm = a[r] # Update right max height
            else:
                total_water += rm - a[r] # Add trapped water
            r -= 1
    return total_water
aa = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(rw(aa)) # Output: 6
'''

'''
def tr(a,t):
    l=0
    r=len(a)-1
    while(l<r):
        if a[l]+a[r]==t:
            return l+1,r+1
        elif a[l]+a[r]>t:
            r-=1
        else:
            l+=1

aa=[2,6,10,6]
tar=tr(aa,12)
print(tar)
'''

def trip(a):
    a = sorted(a)
    tot = []    
    # Outer loop to fix one element
    for i in range(len(a) - 2):
        # Skip duplicates for the fixed element
        if i > 0 and a[i] == a[i-1]:
            continue
        left = i + 1
        right = len(a) - 1
        while left < right:
            summ = a[i] + a[left] + a[right]
            if summ == 0:
                tot.append([a[i], a[left], a[right]])
                # Move pointers and skip duplicates
                while left < right and a[left] == a[left+1]:
                    left += 1
                while left < right and a[right] == a[right-1]:
                    right -= 1
                left += 1
                right -= 1
            elif summ < 0:
                left += 1
            else:
                right -= 1
    return tot
aa = [-1, 0, 1, 2, -1, -4]
print(trip(aa)) # Expected: [[-1, -1, 2], [-1, 0, 1]]
















