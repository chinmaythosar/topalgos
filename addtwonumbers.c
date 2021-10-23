#define NULL ((void *)0)
//   Definition for singly-linked list.
struct ListNode {
   int val;
   struct ListNode *next;
};



void add(struct ListNode* l1, struct ListNode* l2,int carry,struct ListNode* prev);

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
    struct ListNode* ret;
    
    add(l1,l2,0,NULL);
    
    return l1;
}

void add(struct ListNode* l1, struct ListNode* l2,int carry,struct ListNode* prev){
    struct ListNode *nextl1,*nextl2;
    
    //If both are true add
    if(l1 && l2){
        int total = l1->val + l2->val + carry;
        carry = total / 10;
        l1->val = total % 10;
        if(l1->next) //If l1 is not empty continue 
            add(l1->next,l2->next,carry,l1);
        else{//otherwise put l2 as NULL and connect L2 to L1
            l1->next = l2->next;
            add(l1->next,NULL,carry,l1);
        }
    }
    else if(l1 && !l2){ //If L2 is empty do same as before but add carry to l1
       int total = l1->val + carry;
        carry = total / 10;
        l1->val = total % 10;
        add(l1->next,NULL,carry,l1);
    }
    else{
        if(carry>0){//If carry is positive add a node with NULL as ending
        struct ListNode *new;
        new = malloc(sizeof(struct ListNode));
        new->val = carry % 10;
        carry = carry/10;
        new->next = NULL;
        prev->next = new;
        }
        if(carry>0)//Continue if carry is positive continue.
            add(l1->next,NULL,carry,l1);
    }
    
}