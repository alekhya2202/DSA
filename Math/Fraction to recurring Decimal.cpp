//https://leetcode.com/problems/fraction-to-recurring-decimal/

class Solution {
public:
    string fractionToDecimal(int numerator, int denominator) {
        string ans = "";
        
        if((denominator < 0 && numerator > 0) || (denominator > 0 && numerator < 0)){
                ans.append("-");
        }
        numerator = abs(numerator);
        denominator = abs(denominator);
        
        long long quo = abs(numerator / denominator);
        //cout << quo << endl;
        long long rem = numerator % denominator;
        
        ans = ans.append(to_string(quo));
        
        if(rem == 0){
            cout << "yo " << ans << endl;
            return ans;
        }
        else{
            ans.append(".");
            unordered_map <int, int> reminders;
            
            while(rem != 0){
                if(reminders.find(rem) != reminders.end()){
                    ans.insert(reminders[rem], "(");
                    ans.append(")");
                    return ans;
                }
                else{
                    reminders.insert(make_pair(rem, ans.size()));
                    rem *= 10;
                    //cout << " rem = " << rem << endl;
                    quo = abs(rem / denominator);
                    rem = rem % denominator;

                    ans = ans.append(to_string(quo));
                }
            }
            
            return ans;
        }
        
    }
};
