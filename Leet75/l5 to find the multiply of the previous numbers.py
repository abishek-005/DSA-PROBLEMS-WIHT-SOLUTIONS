'''
ab=[1,2,3,4]

def mul(a):
    ans=[]
    for i in range(0,len(a)):
        if i==0:
            ans.append(a[i]*mul(a[i+1:len(a)+1]))
        else:
            break
    return ans
b=mul(ab)
print(b)


'''
'''
ab=[1,2,3,4]
def mul(a,memo={}):
    if len(a)==1:
        return a[0]
    return a[0]*mul(a[1:])
    if a in memo:
        return memo[a]
    if n==0:
        return memo[
b=mul(ab)
print(b)'''
# for multiplyting the front numbers
'''
a = [1, 2, 3, 4]

front_product = 1
result = []

for i in range(len(a)):
    result.append(front_product * a[i])
    front_product *= a[i]

print(result)
'''

def productExceptSelf(nums):
    n = len(nums)

    prefix = [1] * n   # memoization
    suffix = [1] * n   # memoization
    answer = [1] * n

    # prefix product
    for i in range(1, n):
        prefix[i] = prefix[i-1] * nums[i-1]

    # suffix product
    for i in range(n-2, -1, -1):
        suffix[i] = suffix[i+1] * nums[i+1]

    # final answer
    for i in range(n):
        answer[i] = prefix[i] * suffix[i]

    return answer


























