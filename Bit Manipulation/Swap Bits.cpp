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
        unsigned int even = num & 0xAAAAAAAA;
        unsigned int odd = num & 0x55555555;
        
        even >>= 1;
        odd <<= 1;
        
        cout << (even | odd) << endl;}
    return 0;
}
