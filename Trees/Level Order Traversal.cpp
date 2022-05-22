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
        void levelOrder(BST*);
};

void BST :: levelOrder(BST* root){
    if(root == NULL){
        return;
    }
    
    list<BST*> queue;
    queue.push_back(root);
    queue.push_back(NULL);
    BST* front = NULL;
    int i = 0;
    while(queue.size()){
        i++;
        front = queue.front();
        if(front == NULL){
            queue.pop_front();
            cout << "\n";
            if(queue.front() == NULL){
                break;
            }
            queue.push_back(NULL);
        }
        else{
            cout << front -> val << " ";
    
            if(front -> left){
                queue.push_back(front -> left);
            }
            if(front -> right){
                queue.push_back(front -> right);
            }
            
            queue.pop_front();
        }
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
        b.levelOrder(root);
        if(tc >= 1){
            cout << endl;
        }
    }
    return 0;
}
