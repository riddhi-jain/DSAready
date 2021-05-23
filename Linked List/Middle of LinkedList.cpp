/* write an efficient algorithm to find middle of linked list*/

/* reference to head node of linked list is provided as input*/

/*two pointer approach: using two pointers slow and fast
  1. move fast pointer by two and slow pointer by one
  2. when fast pointer reaches end, slow reaches the middle of list*/

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

int findMiddle(struct node* head){

    if(head == NULL)
        return -1;

    struct node*slow = head;
    struct node*fast = head;

    while(fast->next!=NULL && fast->next->next!=NULL){
        fast = fast->next->next;
        slow = slow->next;
    }
    return slow->data;

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

    // linked list created is  12 -> 9 -> 23 -> 33 ->1

    cout<<findMiddle(head)<<endl;
    return 0;
}
