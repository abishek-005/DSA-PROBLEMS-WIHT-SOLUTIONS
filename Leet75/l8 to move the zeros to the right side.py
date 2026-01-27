def move(nums):
    l=0
    for r in range(0,len(nums)):
        if nums[r]!=0:
            t=nums[l]
            nums[l]=nums[r]
            nums[r]=t
            l+=1
    return nums
a=[0,1,23,0,5]
ab=move(a)
print(ab)
