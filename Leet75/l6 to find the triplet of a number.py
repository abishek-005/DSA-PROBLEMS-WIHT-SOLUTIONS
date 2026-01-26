def check(a):
    for i in range(0,len(a)):
        for j in range(i+1,len(a)):
            for k in range(j+1,len(a)):
                if nums[i]<nums[j]<nums[k]:
                    return True
                else:
                    continue
    return False
nums = [5,4,3,2,1]
b=check(nums)
print(b)
    
'''
def check(nums):
    first = float('inf')
    second = float('inf')

    for num in nums:
        if num <= first:
            first = num
        elif num <= second:
            second = num
        else:
            return True

    return False
'''
