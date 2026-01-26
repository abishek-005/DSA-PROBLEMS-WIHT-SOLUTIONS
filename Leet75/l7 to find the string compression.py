#method to convert the dictonary  also into a list wiht the dictonary values into string"
'''
my_dict = {'a': 1, 'b': 2, 'c': 3}

flat_list = [str(item) if isinstance(item, int) else item for pair in my_dict.items() for item in pair]
print(flat_list)  # ['a', '1', 'b', '2', 'c', '3']'''

#method to create a dict key from reading a list elemet
'''
lst = ["a"]
d = {}

for ch in lst:
    d[ch] = 1

print(d)
'''


def compress(chars):
    memo={}
    for i in chars:
        if i not in memo:
            memo[i]=1
        elif i in memo:
            memo[i]+=1
    
    flat_list = [str(item) if isinstance(item, int) else item for pair in memo.items() for item in pair]
    return flat_list
a=["a","a","b","b"]
ab=compress(a)
print(ab)
'''but in leet code shit they want like
class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        read = 0

        while read < len(chars):
            ch = chars[read]
            count = 0

            while read < len(chars) and chars[read] == ch:
                read += 1
                count += 1

            chars[write] = ch
            write += 1

            if count > 1:
                for d in str(count):
                    chars[write] = d
                    write += 1

        return write
'''
