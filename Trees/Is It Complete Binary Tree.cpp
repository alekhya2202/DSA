#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <stdbool.h>
#include <list>

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
        bool isComplete(BST*);
};

bool BST :: isComplete(BST* root)
{
    if (root == nullptr) {
        return true;
    }
    
    list<BST*> queue;
    queue.push_back(root);
 
    BST* front = nullptr;
 
    bool flag = false;
 
    while (queue.size())
    {
        front = queue.front();
        queue.pop_front();
 
        if (flag && (front->left || front->right)) {
            return false;
        }
        
        if (front->left == nullptr && front->right) {
            return false;
        }

        if (front->left) {
            queue.push_back(front->left);
        }
        
        else {
            flag = true;
        }
 
        if (front->right) {
            queue.push_back(front->right);
        }
        
        else {
            flag = true;
        }
    }
 
    return true;
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
        if(b.isComplete(root)){
            cout << "Yes" << endl;
        }
        else{
            cout << "No" << endl;
        }
    }
    return 0;
}
