/*Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.
Input: nums = [1,2,1,3,2,5]
Output: [3,5]

Problem link: https://leetcode.com/problems/single-number-iii/
*/

class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        long xor_val = 0;
        for(int num : nums){
            xor_val ^= num;
        }
        
        long mask = (xor_val & (xor_val - 1)) ^ xor_val;
        
        int num1 = 0;
        for(int num : nums){
            if((mask & num) == 0){
                num1 = num1 ^ num;
            }
        }
        int num2 = xor_val ^ num1;
        
        vector <int> op;
        op.push_back(num1);
        op.push_back(num2);
        
        return op;
    }
};
