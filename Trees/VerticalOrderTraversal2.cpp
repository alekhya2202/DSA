#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
using namespace std;

class BST{
    int val;
    BST* left;
    BST* right;
   
    public:
        BST(){
            val = 0;
            left = right = nullptr;}
   
        BST(int data){
            val = data;
            left = right = nullptr;}
       
        BST* insert(BST* root, int data){
           
            if(root == nullptr){
                return new BST(data);}
           
            if(data > root-> val){
                root -> right = insert(root -> right, data);}
           
            else{
                root -> left = insert(root -> left, data);}          
            return root;
        }
   
        void Inorder(BST*);
        void vOrder(BST*, int, std :: map <int, vector <int > > &m);
        void printVerticalOrder(BST*);
};

void BST ::Inorder(BST* root)
{
    if (!root) {
        return;
    }
    Inorder(root->left);
    cout << root->val << " ";
    Inorder(root->right);
}


void BST :: vOrder(BST* root, int v, map<int, vector <int> > &m){
    if(root == NULL){
        return;
    }
    m[v].push_back(root -> val);
    
    vOrder(root -> left, v - 1, m);
    vOrder(root -> right, v + 1, m);
}

void BST :: printVerticalOrder(BST* root)
{
    map < int,vector<int> > m;
    int hd = 0;
    vOrder(root, hd,m);
    
    map< int,vector<int> > :: iterator it;
    
    for (it = m.begin(); it != m.end(); it++)
    {   
        sort(it->second.begin(), it->second.end());
        for (int i = 0; i < it -> second.size(); ++i)
            cout << it->second[i] << " ";
        cout << endl;
    }
}
 

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    int tc;
    cin >> tc;
    while(tc--){
        int n;
        cin >> n;
        int nodes[n];
        BST b, *root = NULL;
        for(int i = 0; i < n; i++){
            cin >> nodes[i];
            if(i == 0){
                root = b.insert(root, nodes[0]);
            }
            else{
                b.insert(root, nodes[i]);
            }
        }
        b.printVerticalOrder(root);
        if(tc >= 1){
            cout << "\n";
        }
    }
    return 0;
}
