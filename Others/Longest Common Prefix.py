#Bruteforce

class Solution:
    def longestCommonPrefix(self, arr: List[str]) -> str:
        arr.sort(key = len)
        minlen = len(arr[0])
        
        result =""
        
        for i in range(minlen):
            current = arr[0][i]

            for j in range(1, len(arr)):
                if (arr[j][i] != current):
                    return result
                
            result = result+current

        return result
            
