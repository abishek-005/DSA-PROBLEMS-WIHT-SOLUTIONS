class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        '''res=[]
        for i in candies:
            res.append(i+extraCandies)
        res.sort()
        fin=[]
        maxi=max(res)
        for i in res:
            if i <= maxi-4:
                fin.append(False)
            else:
                fin.append(True)
        return fin'''
        max_candies = max(candies)
        
        result = []
        
        for candy in candies:
            if candy + extraCandies >= max_candies:
                result.append(True)
            else:
                result.append(False)
        
        return result
        

        
