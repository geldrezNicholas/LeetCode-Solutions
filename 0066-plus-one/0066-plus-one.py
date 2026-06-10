class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = ""
        for i in digits:
            result += str(i)
        result = int(result)+1
        result = str(result)
        final = [int(x) for x in str(result)]
        return final