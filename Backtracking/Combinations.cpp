//https://www.interviewbit.com/problems/combinations/

void combinations(vector<vector<int>> &ans, vector<int> comb, int n, int k, int idx, int A){
    if(k == 0){
        ans.push_back(comb);
        return;
    }
    if(n == A + 1){
        return;
    }
    comb[idx] = n;
    combinations(ans, comb, n + 1, k - 1, idx + 1, A);
    combinations(ans, comb, n + 1, k, idx, A);
}

vector<vector<int> > Solution::combine(int A, int B) {
    vector <vector<int>> ans;
    vector <int> comb(B);
    combinations(ans, comb, 1, B, 0, A);
    return ans;
}
