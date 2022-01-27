//https://leetcode.com/problems/palindrome-linked-list/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* FindMid(ListNode* head){
        ListNode *slowPtr = head, *FastPtr = head;
        while(FastPtr -> next != NULL && FastPtr -> next -> next != NULL){
            slowPtr = slowPtr -> next;
            FastPtr = FastPtr -> next -> next;
        }
        return slowPtr;
    }
    
    ListNode* reverseList(ListNode* head){
        ListNode *prev = NULL;
        while(head != NULL){
            ListNode* next = head -> next;
            head -> next = prev;
            prev = head;
            head = next;
        }
        return prev;
    }
    
    bool isPalindrome(ListNode* head) {
        if(head == NULL){
            return true;
        }
        ListNode* mid = FindMid(head);
        ListNode *second = reverseList(mid -> next);
       
        ListNode *p1 = head, *p2 = second;
        while(p2 != NULL){
            if(p1 -> val != p2 -> val){
                return false;
            }
            p1 = p1 -> next;
            p2 = p2 -> next;
        }
        return true;
    }
};
