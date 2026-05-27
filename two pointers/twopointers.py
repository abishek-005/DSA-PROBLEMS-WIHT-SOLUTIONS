'''def poin(a):
    l=0
    rr=len(a)-1
    while(l<rr):
        if a[l]==0 and a[rr]!=0:
            t=a[l]
            a[l]=a[rr]
            a[rr]=t
            l+=1
            rr-=1
        if a[l]!=0 and a[rr]!=0:
            l+=1
    return a
a1=[4,5,0,0]
print("original arr:",a1)
print("changed arr:",poin(a1))'''

def poin_analysis(a):
    l = 0
    rr = len(a) - 1
    steps = 0 # Intha variable thaan time complexity-ah analyze panna pothu
    
    while(l < rr):
        steps += 1 # Ovvoru loop run aagum pothum step count eharum
        
        if a[l] == 0 and a[rr] != 0:
            a[l], a[rr] = a[rr], a[l]
            l += 1
            rr -= 1
        elif a[l] != 0:
            l += 1
        else:
            rr -= 1
            
    return steps

# Check with different input sizes (n)
for n in [10, 100, 1000]:
    import random
    test_arr = [random.choice([0, 1]) for _ in range(n)]
    
    total_steps = poin_analysis(test_arr)
    print(f"Input Size (n): {n} | Total Steps Taken: {total_steps}")
