import sys
print(sys.getrecursionlimit()) # Check current limit
sys.setrecursionlimit(3000) # Set a new limit
#by using the above lines we can set the limit of the recursion da
def infinite_recursion(n):
    print(n)
    infinite_recursion(n + 1)
    if n==100000:
        return
a=0
infinite_recursion(a)
'''
....
....
1013
1014
1015
1016
1017
1018
1019Traceback (most recent call last):
  File "C:/Users/dell/AppData/Local/Programs/Python/Python313/dsa probelms/for fun bro.py", line 7, in <module>
    infinite_recursion(a)
  File "C:/Users/dell/AppData/Local/Programs/Python/Python313/dsa probelms/for fun bro.py", line 3, in infinite_recursion
    infinite_recursion(n + 1)
  File "C:/Users/dell/AppData/Local/Programs/Python/Python313/dsa probelms/for fun bro.py", line 3, in infinite_recursion
    infinite_recursion(n + 1)
  File "C:/Users/dell/AppData/Local/Programs/Python/Python313/dsa probelms/for fun bro.py", line 3, in infinite_recursion
    infinite_recursion(n + 1)
  [Previous line repeated 1016 more times]
  File "C:/Users/dell/AppData/Local/Programs/Python/Python313/dsa probelms/for fun bro.py", line 2, in infinite_recursion
    print(n)
RecursionError: maximum recursion depth exceeded'''#which means this is the max_depth of python
