#https://leetcode.com/problems/counting-bits/

class Solution:

    def countBits(self, n: int) -> List[int]:
        hamming_weights = [0] * (n + 1)
        offset = 1
        pow_2 = 1
        
        for index in range(1, n + 1):
            
            # offset changes only at power of 2
            # also increment pow_2 for next check 
            if pow(2, pow_2) == index:
                offset = index
                pow_2 += 1
            
            # using previous calculated hamming weight
            # 0000 - 0 => 0
            # 0001 - 1 => 1 + hamming_weight[1 - 1] 
            # 0010 - 2 => 1 + hamming_weight[2 - 2] # offset updated to 2 since it a power of 2
            # 0011 - 3 => 1 + hamming_weight[3 - 2]
            # 0100 - 4 => 1 + hamming_weight[4 - 4] # first operand 1 is for 4, second operand is caculated 
            # from hamming_weight[0] since 0 is previous offset for 4
            # 0101 - 5 => 1 + hamming_weight[5 - 4]
            # 0110 - 6 => 1 + hamming_weight[6 - 4]
            # 0111 - 7 => 1 + hamming_weight[7 - 4]
            # 1000 - 8 => 1 + hamming_weight[8 - 8] # offset is updated to next power of 2 
            # since current index == next power of 2
            hamming_weights[index] = 1 + hamming_weights[index  - offset]
        
        return hamming_weights
