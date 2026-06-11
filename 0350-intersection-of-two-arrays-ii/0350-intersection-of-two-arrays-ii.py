class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1 = {}
        final = []

        for i in nums1:
            if i in dict1:
                dict1[i]+=1
            else:
                dict1[i]=1

        for e in nums2:
            if e in dict1 and dict1[e] > 0:
                final.append(e)
                dict1[e]-=1
        
        return final

        


        

