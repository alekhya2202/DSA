#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <stdbool.h>

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
        bool isFBST(BST*);
};

bool BST :: isFBST(BST* root){
    if(root == NULL){
        return true;
    }
    if(root -> left == NULL && root -> right == NULL){
        return true;
    }
    else if((root ->left == NULL && root -> right != NULL) || (root -> left != NULL && root -> right == NULL)){
        return false;
    }
    return isFBST(root -> left) && isFBST(root -> right);
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
        if(b.isFBST(root)){
            cout << "True" << endl;
        }
        else{
            cout << "False" << endl;
        }
    }
    return 0;
}
