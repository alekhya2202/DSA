#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int tc;
    cin >> tc;
    for(int i = 0; i < tc; i ++){
        int num;
        cin >> num;
        
        for(int i = 0; i < 32; i += 2){
            int ith = (num >> i) & 1;
            int i_plus_1th = (num >> (i + 1)) & 1;
            num = num - (ith << i)
                    - (i_plus_1th << (i + 1))
                    + (ith << (i + 1))
                    + ((i_plus_1th) << i);}
        cout << num << endl;
        }
    return 0;
}
