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
    
    void reorderList(ListNode* head) {
        ListNode *nhead = head;
        
        if (head == NULL || head->next == NULL)
            return;
       
        while (nhead->next && nhead->next->next) 
            nhead = nhead->next;
        
        ListNode *tail = nhead->next;
        nhead->next = NULL;
        
        ListNode *newhead = head->next;
        
        tail->next = newhead;                 
        head->next = tail;
        
        reorderList(newhead);
        
    }
};
