//without recursion
vector<int> Solution::inorderTraversal(TreeNode* A) {
    vector<int> res;
    TreeNode* pCurrent = A;
    stack<TreeNode* > stack;
    
    while (!stack.empty() || pCurrent)
    {
        if (pCurrent)
        {
            stack.push(pCurrent);
            pCurrent = pCurrent->left;
        }
        else
        {
            TreeNode* pNode = stack.top();
            res.push_back(pNode->val);
            stack.pop();
            pCurrent = pNode->right;
        }
    }
    return res;
}
