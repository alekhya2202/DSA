//https://www.codechef.com/problems/ALTARAY/

#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int tc;
	cin >> tc;
	while(tc--){
	    int n;
	    cin >> n;
	    long long int arr[n];
	    for(int i = 0; i < n; i++){
	        cin >> arr[i];
	    }
	    
	    long long int out[n] = {1};
	    out[n - 1] = 1;
	    
	    for(int i = n - 2; i >= 0; i--){
	        if(arr[i] * arr[i + 1] < 0){
	            out[i] = 1 + out[i + 1];
	        }
	        else{
	            out[i] = 1;
	        }
	    }
	    
	    for(int i = 0; i < n; i++){
	        cout << out[i] << " ";
	    }
	    cout << endl;
	}
	return 0;
}
