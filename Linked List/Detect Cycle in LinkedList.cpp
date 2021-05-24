/* write algorithm to detect if there is cycle in linked list*/

/* two pointer approach - using slow and fast two pointers
    move fast by two and slow by one - if there is cycle, they will surely meet somewhere
    otherwise we reach the end of list and return false
*/

#include<iostream>
using namespace std;

struct node{
    int data;
    struct node*next;
    node(int val){
        data = val;
        next = NULL;
    }
};

bool detectCycle(struct node *head) {
        struct node*slow = head,*fast = head;
        while(fast&&fast->next){
            fast=fast->next->next;
            slow=slow->next;
            if(fast==slow)
                return true;
        }
        return false;
}

int main(){

    struct node*head = new struct node(12);
    struct node*two = new struct node(9);
    head->next = two;
    struct node*three = new struct node(23);
    two->next = three;
    struct node*four = new struct node(33);
    three->next = four;
    struct node*five = new struct node(1);
    four->next = five;
    five->next = three;

    /*linked list created is  12 -> 9 -> 23 -> 33 ->1
                                         |          |
                                          ----------   */

    cout<<(detectCycle(head)?"There is cycle":"There is no cycle")<<endl;
    return 0;
}
