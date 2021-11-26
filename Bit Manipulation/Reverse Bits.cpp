/*
Given a number, reverse the bits in the binary representation (consider 32-bit unsigned data) of the number, and print the new number formed.

Input Format

First line of input contains T - number of test cases. Each of the next T lines contains a number integer N.

Constraints

1 <= T <= 100000
0 <= N <= 109

Output Format

For each test case, print the new number formed after reversing the bits, separated by new line.

Sample Input

4
4
15
6
1000000000

Sample Output

536870912
4026531840
1610612736
5462492
"""

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

*/
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    int tc;
    cin >> tc;
    for(int i = 0; i < tc; i++){
        int num;
        cin >> num;
        unsigned int rev = 0;
        
        for(int i = 31; i >= 0; i--){
            rev |= (num & 1) << i;
            num >>= 1;
        }
        
        cout << rev << endl;
    }
    return 0;
}
