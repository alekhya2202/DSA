//https://leetcode.com/problems/maximum-subarray/

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int meh = 0;
        int msf = INT_MIN;
        
        for(int num : nums){
            meh += num;
            if(meh < num){
                meh = num;
            }
            if(msf < meh){
                msf = meh;
            }
        }
        return msf;
    }
};
