/*write an algorithm to check if linked list is palindrome

    approach - first we go to middle of list.
               then we reverse the list after midpoint.
               from start and from last we compare the values (increasing the start and decreasing the last)
               if at any nodes, values are not equal, we return false
               otherwise return true if "last" reaches middle; and then we restore the half reversed list back
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

struct node* reverseList(struct node* head) {
        struct node* prev= NULL;
        struct node*curr = head;
        while(curr){
            struct node* temp = curr->next;
            curr->next = prev;
            prev=curr;
            curr=temp;
        }
        return prev;

}

 bool isPalindrome(struct node* head) {
        struct node*slow=head;
        struct node*fast=head;

        while(fast->next!=NULL && fast->next->next!=NULL){
            slow=slow->next;
            fast=fast->next->next;
        }

        //slow is at mid now, we reverse the list after slow

        struct node* last  = reverseList(slow->next);
        struct node* last_ = last;
        struct node* first = head;

        while(last){
            if(last->data!=first->data)
                return false;
            first=first->next;
            last=last->next;
        }

        slow->next = reverseList(last_);  // restore the list back
        return true;
    }

  int main(){

    struct node*head = new struct node(12);
    struct node*two = new struct node(9);
    head->next = two;
    struct node*three = new struct node(23);
    two->next = three;
    struct node*four = new struct node(9);
    three->next = four;
    struct node*five = new struct node(12);
    four->next = five;

    // linked list created is  12 -> 9 -> 23 -> 9 -> 12 which is a palindrome

    cout<<(isPalindrome(head)?"Yes, palindrome":"Not palindrome")<<endl;
    return 0;
}
