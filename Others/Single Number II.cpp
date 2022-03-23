/*Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 */
//Problem link : https://leetcode.com/problems/single-number-ii/

//bit manipulation approach -- runtime: 7ms
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int ones = 0;
        int twos = 0;
        for(auto ele: nums)
        {
            ones = (ones^ele) & (~twos);
            twos = (twos^ele) & (~ones);
        }
        return ones;
    }
};

//Set bits approach -- runtime: 14ms
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        long ans = 0;
        long mask = 1;
        
        for(int i = 0; i <= 31; i++){
            int set = 0;
            for(int num : nums){
                if(num & mask){
                    set++;
                }
            }
            
            if(set % 3 != 0){
                ans += mask;
            } 
            mask = mask * 2;
        }
        return ans;
    }
};
