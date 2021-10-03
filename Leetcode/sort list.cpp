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
    
    ListNode* merge(ListNode* link1, ListNode* link2) {
        if(link1 == NULL)
        return link2;
        
        if(link2 == NULL)
        return link1;

        if(link1->val < link2->val) {
            link1->next = merge(link1->next, link2);
            return link1;
        }
        else {
             link2->next = merge(link1,link2->next);
             return link2;
        }
    }
    
    ListNode* sortList(ListNode* head) {
        
        if(head == NULL || head->next == NULL)
            return head;

            ListNode* first = head->next;
            ListNode* second = head;
        
            while(first && first->next) {
                second = second->next;
                first = first->next->next;
            }

            ListNode* newhead = second->next;
            second->next = NULL;

        return merge(sortList(head), sortList(newhead));
    }
};
